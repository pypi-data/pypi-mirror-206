from __future__ import annotations

import pandas as pd

from .df_utils import derive_categoricals
from .machine_data_def import MDConcepts, base_machine_data_columns, TimeseriesTypeKey, TimeseriesFeatureLabels, Header, \
    EventTimeseriesCollection, MeasurementTimeseriesCollection, MachineData, TimeseriesCollectionFactory, \
    MachineDataType

COLUMN_NAME_DICT = {
    # internal to external label mapping
    MDConcepts.Time: 'time',
    MDConcepts.Object: 'object',
    MDConcepts.Type: 'type',
    MDConcepts.Label: 'label'
}
base_raw_machine_data_columns = list(map(COLUMN_NAME_DICT.get, MDConcepts))

MACHINE_DATA_TYPES_DICT = {
    MachineDataType.E: 'E',
    MachineDataType.M: 'M'
}
raw_machine_data_types = set(map(MACHINE_DATA_TYPES_DICT.get, MachineDataType))


def gen_feature_column_names(n):
    return [f'f_{i}' for i in range(1, n + 1)]



RawHeaderType = dict[TimeseriesTypeKey, TimeseriesFeatureLabels]
RawDataType = pd.DataFrame


def convert_to_raw_header(md: MachineData) -> RawHeaderType:
    header = {}
    for typed_timeseries in md.iter_all_timeseries():
        tt = typed_timeseries.timeseries_type
        header[tt.askey()] = tuple(tt.features)
    return header


def convert_to_raw_data(md: MachineData) -> RawDataType:
    max_features = max(map(lambda md_timeseries: len(md_timeseries.timeseries_type), md.iter_all_timeseries()))
    rows = []
    for typed_timeseries in md.iter_all_timeseries():
        tt = typed_timeseries.timeseries_type
        df = typed_timeseries.df
        for tup in df.itertuples(index=True):
            rows.append(
                [getattr(tup, MDConcepts.Time.as_str()), getattr(tup, MDConcepts.Object.as_str()), tt.type.as_str(),
                 tt.label] + [getattr(tup, f)
                              for f in
                              tt.features if
                              f in df.columns])
    res = pd.DataFrame(rows, columns=(base_raw_machine_data_columns + gen_feature_column_names(max_features)),
                       copy=False)
    res.sort_values(COLUMN_NAME_DICT[MDConcepts.Time], inplace=True)
    return res


def create_header_from_raw(feature_definitions: RawHeaderType) -> Header:
    return Header.from_raw(feature_definitions)


def create_machine_data_from_raw(raw_data: RawDataType, raw_header: RawHeaderType):
    header = create_header_from_raw(raw_header)

    mdes, mdms = [], []

    categories = derive_categoricals(raw_data,
                                     map(COLUMN_NAME_DICT.get, [MDConcepts.Object, MDConcepts.Label, MDConcepts.Type]))

    base_colum_mapping = {old: new.as_str() for new, old in COLUMN_NAME_DICT.items()}

    overall = pd.DataFrame(raw_data, columns=base_raw_machine_data_columns, copy=True)
    overall.rename(columns=base_colum_mapping, inplace=True)
    overall = overall.astype(categories, copy=False)

    for group, idx in overall.groupby(['type', 'label']).groups.items():
        tpy, label = group
        timeseries_type = header.feature_definitions[tpy, label]
        actual_feature_labels = timeseries_type.features
        feature_count = len(actual_feature_labels)
        placeholder_feature_labels = gen_feature_column_names(feature_count)
        df = pd.concat([overall.loc[idx, base_machine_data_columns], raw_data.loc[idx, placeholder_feature_labels]],
                       copy=True, axis=1).set_index(idx)
        # relevant_cols = list(base_machine_data_columns) + placeholder_feature_labels
        # df = pd.DataFrame(raw_data.loc[idx, relevant_cols], copy=True)
        # not a good idea in case of duplicates
        # df.set_index('time', inplace=True, verify_integrity=True, drop=False)
        # df = df.astype(categories, copy=False)
        renaming_dict = {old: new for old, new in zip(placeholder_feature_labels, actual_feature_labels)}
        # renaming_dict.update(base_colum_mapping)
        df.rename(columns=renaming_dict, inplace=True)
        ts_collection = TimeseriesCollectionFactory.for_type(timeseries_type)(df)
        if isinstance(ts_collection, EventTimeseriesCollection):
            mdes.append(ts_collection)
        elif isinstance(ts_collection, MeasurementTimeseriesCollection):
            mdms.append(ts_collection)

    placeholder_cols = list(set(overall.columns).difference(base_machine_data_columns))
    overall.drop(columns=placeholder_cols, inplace=True)

    return MachineData(mdes, mdms, overall)
