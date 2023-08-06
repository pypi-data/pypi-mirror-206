from __future__ import annotations

import enum
import itertools
from dataclasses import dataclass, field
from functools import partial
from typing import Iterable, Generic, TypeVar, Sized, TYPE_CHECKING, Any

import pandas as pd

from .df_utils import derive_categoricals

if TYPE_CHECKING:
    from .raw import RawHeaderType


class MyStrEnum(enum.Enum):

    @classmethod
    def cast(cls, arg):
        return arg if isinstance(arg, cls) else cls(arg)

    def as_str(self):
        return str(self.value)


class MDConcepts(MyStrEnum):
    Time = 'time'
    Object = 'object'
    Type = 'type'
    Label = 'label'


base_machine_data_columns = [c.as_str() for c in MDConcepts]


def only_feature_columns(cols):
    return [c for c in cols if c not in base_machine_data_columns]


def project_on_feature_columns(df: pd.DataFrame):
    return df[only_feature_columns(df.columns)]


TimeseriesTypeKey = tuple[str, str]
TimeseriesFeatureLabels = tuple[str, ...]


class MachineDataType(MyStrEnum):
    E = 'E'
    M = 'M'


@dataclass(frozen=True, unsafe_hash=True, eq=True, repr=True)
class TimeseriesType(Iterable, Sized):
    type: MachineDataType
    label: str
    features: TimeseriesFeatureLabels = field(default=())

    def __init__(self, type: MachineDataType, label: str, features: TimeseriesFeatureLabels = ()) -> None:
        super().__init__()
        object.__setattr__(self, 'type', MachineDataType.cast(type))
        object.__setattr__(self, 'label', label)
        object.__setattr__(self, 'features', features if isinstance(features, tuple) else tuple(features))

    def __iter__(self):
        return iter(self.features)

    def __len__(self):
        return len(self.features)

    def askey(self) -> TimeseriesTypeKey:
        return self.type.as_str(), self.label


EventTypeKey = str
MeasurementTypeKey = str


@dataclass(frozen=True)
class EventTimeseriesType(TimeseriesType):

    def __init__(self, label: EventTypeKey, features) -> None:
        super().__init__(MachineDataType.E, label, features)


@dataclass(frozen=True)
class MeasurementTimeseriesType(TimeseriesType):

    def __init__(self, label: MeasurementTypeKey, features) -> None:
        super().__init__(MachineDataType.M, label, features)


class TimeseriesTypeFactory:
    types = {MachineDataType.E: EventTimeseriesType, MachineDataType.M: MeasurementTimeseriesType}

    @classmethod
    def for_name(cls, arg):
        return cls.types[MachineDataType.cast(arg)]


@dataclass(frozen=True, eq=True, repr=True)
class Header:
    feature_definitions: dict[TimeseriesTypeKey, TimeseriesType]

    @classmethod
    def from_raw(cls, raw_feature_definitions: RawHeaderType):
        return cls({k: TimeseriesTypeFactory.for_name(k[0])(k[1], v) for k, v in raw_feature_definitions.items()})

    def __getitem__(self, item) -> TimeseriesFeatureLabels:
        return self.feature_definitions[item].features


TSType = TypeVar('TSType', EventTimeseriesType, MeasurementTimeseriesType)


@dataclass
class MachineDataTimeseries(Generic[TSType]):
    timeseries_type: TSType
    object: str
    df: pd.DataFrame


@dataclass
class EventSeries(MachineDataTimeseries[EventTimeseriesType]):
    pass


@dataclass
class MeasurementSeries(MachineDataTimeseries[MeasurementTimeseriesType]):
    pass


TS = TypeVar('TS', EventSeries, MeasurementSeries)


@dataclass
class TypedTimeseriesCollection(Generic[TSType, TS]):
    timeseries_type: TSType
    df: pd.DataFrame
    object_map: dict[str, TS] = field(init=False)
    _ts_type_cls: type[TSType] = None
    _ts_cls: type[TS] = None

    def __init__(self, timeseries_type: TSType, df: pd.DataFrame) -> None:
        super().__init__()
        self.timeseries_type = timeseries_type
        self.df = df
        self.object_map: dict[str, TS] = {}
        self._repopulate_object_map()

    def __len__(self):
        return len(self.df)

    def _repopulate_object_map(self):
        self.object_map = {}

        for obj, idx in self.df.groupby(MDConcepts.Object.as_str()).groups.items():
            obj = str(obj)
            self.object_map[obj] = self._mk_timeseries_view(self.timeseries_type, obj, self.df.loc[idx])

    def _check_ts_features(self):
        return set(self.timeseries_type.features) <= set(self.df.columns)

    def _mk_timeseries_view(self, timeseries_type, obj, df) -> TS:
        return self._ts_cls(timeseries_type, obj, df)

    def _update_timeseries_type(self, timeseries_type: TSType = None):
        self.timeseries_type = timeseries_type if timeseries_type is not None else self._derive_timeseries_type()
        assert self._check_ts_features()
        self._repopulate_object_map()

    def _derive_timeseries_type(self) -> TSType:
        return self._ts_type_cls(self.timeseries_type.label,
                                 only_feature_columns(self.df.columns))

    def fit_to_data(self):
        self._update_timeseries_type()

    def get_for_obj(self, obj) -> TS:
        return self.object_map[obj]


@dataclass
class EventTimeseriesCollection(TypedTimeseriesCollection[EventTimeseriesType, EventSeries]):
    _ts_type_cls = EventTimeseriesType
    _ts_cls = EventSeries

    def __init__(self, timeseries_type: TSType, df: pd.DataFrame) -> None:
        super().__init__(timeseries_type, df)


@dataclass
class MeasurementTimeseriesCollection(TypedTimeseriesCollection[MeasurementTimeseriesType, MeasurementSeries]):
    _ts_type_cls = MeasurementTimeseriesType
    _ts_cls = MeasurementSeries

    def __init__(self, timeseries_type: TSType, df: pd.DataFrame) -> None:
        super().__init__(timeseries_type, df)


class TimeseriesCollectionFactory:
    types = {MachineDataType.E: EventTimeseriesCollection, MachineDataType.M: MeasurementTimeseriesCollection}

    @classmethod
    def for_type(cls, timeseries_type: TimeseriesType):
        if isinstance(timeseries_type, EventTimeseriesType):
            return partial(cls.types[MachineDataType.E], timeseries_type)
        elif isinstance(timeseries_type, MeasurementTimeseriesType):
            return partial(cls.types[MachineDataType.M], timeseries_type)


@dataclass
class MachineData:
    index_frame: pd.DataFrame
    event_series: dict[EventTypeKey, EventTimeseriesCollection]
    measurement_series: dict[MeasurementTypeKey, MeasurementTimeseriesCollection]
    event_series_types: dict[EventTypeKey, EventTimeseriesType] = field(init=False)
    measurement_series_types: dict[MeasurementTypeKey, MeasurementTimeseriesType] = field(init=False)

    def __init__(self, events: Iterable[EventTimeseriesCollection],
                 measurements: Iterable[MeasurementTimeseriesCollection],
                 index_frame: pd.DataFrame = None) -> None:
        super().__init__()
        self.event_series = {etc.timeseries_type.label: etc for etc in events}
        self.measurement_series = {mtc.timeseries_type.label: mtc for mtc in measurements}

        if index_frame is not None:
            self.index_frame = index_frame
        else:
            # this is painful beyond belief
            rows = []
            for md_timeseries in self.iter_all_timeseries():
                for tup in md_timeseries.df.itertuples(index=True):
                    row = [getattr(tup, MDConcepts.Time.as_str()), getattr(tup, MDConcepts.Object.as_str()),
                           md_timeseries.timeseries_type.type.as_str(),
                           md_timeseries.timeseries_type.label]
                    rows.append(row)

            frame = pd.DataFrame(rows, columns=base_machine_data_columns)
            cats = derive_categoricals(frame,
                                       map(MDConcepts.as_str, [MDConcepts.Object, MDConcepts.Type, MDConcepts.Label]))
            frame = frame.astype(cats, copy=False)
            self.index_frame = frame

        self._repopulate_maps()

    def _repopulate_maps(self):
        self.event_series_types = {es.timeseries_type.label: es.timeseries_type for es in self.event_series.values()}
        self.measurement_series_types = {ms.timeseries_type.label: ms.timeseries_type for ms in
                                         self.measurement_series.values()}

    def fit_to_data(self):
        for tsc in self.iter_all_timeseries():
            # retain only the rows that are referenced in the overall table
            tsc.df = tsc.df.filter(items=self.index_frame.index, axis=0)
            tsc.fit_to_data()
        self._repopulate_maps()

    def iter_all_timeseries(self) -> Iterable[TypedTimeseriesCollection]:
        return itertools.chain(self.event_series.values(), self.measurement_series.values())

    def get_unique_objects(self) -> set[str]:
        return set(self.index_frame[MDConcepts.Object.as_str()])

    def get_view(self, mdt: [str | MachineDataType] = None, obj: str = None, label: str = None) -> pd.DataFrame:
        mask = pd.Series(True, index=self.index_frame.index)
        if obj is not None:
            mask &= (self.index_frame[MDConcepts.Object.as_str()] == obj)
        if label is not None:
            mask &= (self.index_frame[MDConcepts.Label.as_str()] == label)
        if mdt is not None:
            mdt = mdt.as_str() if isinstance(mdt, MachineDataType) else str(mdt)
            mask &= (self.index_frame[MDConcepts.Type.as_str()] == mdt)
        return self.index_frame.loc[mask]

    def get_joined_view(self, event_series_labels: Iterable[str] | bool = tuple(),
                        measurement_series_labels: Iterable[str] | bool = tuple()):
        if type(event_series_labels) is bool and event_series_labels:
            event_series_labels = self.event_series_types.keys()
        if type(measurement_series_labels) is bool and measurement_series_labels:
            measurement_series_labels = self.measurement_series_types.keys()
        return pd.concat([self.index_frame] + [project_on_feature_columns(self.event_series[est].df) for est in
                                               event_series_labels] + [
                             project_on_feature_columns(self.measurement_series[mst].df) for mst in
                             measurement_series_labels], axis='columns', copy=False)

    def get_event_series_collection(self, label) -> EventTimeseriesCollection:
        return self.event_series[label]

    def get_measurement_series_collection(self, label) -> MeasurementTimeseriesCollection:
        return self.measurement_series[label]

    def get_specific_event_series(self, obj, label) -> EventSeries:
        return self.event_series[label].get_for_obj(obj)

    def get_specific_measurement_series(self, obj, label) -> MeasurementSeries:
        return self.measurement_series[label].get_for_obj(obj)

    def summary(self):
        return self.index_frame.describe()


class Factory:
    @staticmethod
    def ets_from_df(df: pd.DataFrame, **kwargs):
        return Factory.ts_from_df(df, type=MachineDataType.E, **kwargs)

    @staticmethod
    def mts_from_df(df: pd.DataFrame, **kwargs):
        return Factory.ts_from_df(df, type=MachineDataType.M, **kwargs)

    @staticmethod
    def ts_from_df(df: pd.DataFrame, **kwargs):  # tpy: MachineDataType = None, label: str = None):
        def match_spec_and_df(concept):
            spec = kwargs.get(concept.as_str())
            if concept.as_str() not in df.columns:
                assert spec is not None
                df[concept.as_str()] = spec
            else:
                df_type = df.iloc[0][concept.as_str()]
                assert spec is None or spec == df_type
                spec = df_type
            return spec

        spec_type = match_spec_and_df(MDConcepts.Type)
        spec_object = match_spec_and_df(MDConcepts.Object)
        spec_label = match_spec_and_df(MDConcepts.Label)
        if MDConcepts.Time.as_str() in kwargs:
            spec_time = kwargs[MDConcepts.Time.as_str()]
            # if spec_time == 'artificial':
            from mdata.core import df_utils
            df[MDConcepts.Time.as_str()] = df_utils.create_artificial_daterange(df)

        tt_cls = TimeseriesTypeFactory.for_name(spec_type)
        features = only_feature_columns(df.columns)
        tt = tt_cls(spec_label, tuple(features))
        return TimeseriesCollectionFactory.for_type(tt)(df)

    @staticmethod
    def create_index(series, override_categorical_types=True):
        rows = []
        for tsc in series:
            for tup in tsc.df.itertuples(index=True):
                row = [getattr(tup, MDConcepts.Time.as_str()), getattr(tup, MDConcepts.Object.as_str()),
                       tsc.timeseries_type.type.as_str(),
                       tsc.timeseries_type.label]
                rows.append(row)

        frame = pd.DataFrame(rows, columns=base_machine_data_columns)
        cats = derive_categoricals(frame,
                                   map(MDConcepts.as_str, [MDConcepts.Object, MDConcepts.Type, MDConcepts.Label]))
        frame = frame.astype(cats, copy=False)
        if override_categorical_types:
            for tsc in series:
                tsc.df = tsc.df.astype(cats, copy=False)
        return frame

    @staticmethod
    def machine_data_from_spec(*series_defs: dict[str, Any]):
        ets, mts = [], []
        for sd in series_defs:
            assert 'df' in sd
            tsc = Factory.ts_from_df(**sd)
            if isinstance(tsc, EventTimeseriesCollection):
                ets.append(tsc)
            elif isinstance(tsc, MeasurementTimeseriesCollection):
                mts.append(tsc)
        index_frame = Factory.create_index(itertools.chain(ets, mts))
        return MachineData(ets, mts, index_frame)
