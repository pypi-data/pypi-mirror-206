import pandas as pd

from mdata.core import machine_data_def as mdd
from mdata.file_formats import io_utils


def write_machine_data_h5(filename, md: mdd.MachineData, complevel: int = 0, **kwargs) -> None:
    if 'format' not in kwargs:
        kwargs['format'] = 't'
    io_utils.ensure_directory_exists(filename)
    filename = io_utils.ensure_ext(filename, '.h5')
    with pd.HDFStore(filename, mode='w', complib='blosc', complevel=complevel) as store:
        store.put('master', md.index_frame, index=True, data_columns=mdd.base_machine_data_columns,
                  dropna=False, **kwargs)
        store.create_table_index('master', columns=['index', 'time', 'label'], kind='full')
        for label, ess in md.event_series.items():
            key = f'events/{label}'
            store.put(key, ess.df, index=True, data_columns=mdd.base_machine_data_columns, dropna=False,
                      **kwargs)
            store.create_table_index(key, columns=['index', 'time', 'label'], kind='full')
        for label, mss in md.measurement_series.items():
            key = f'measurements/{label}'
            store.put(key, mss.df, index=True, data_columns=mdd.base_machine_data_columns, dropna=False,
                      **kwargs)
            store.create_table_index(key, columns=['index', 'time', 'label'], kind='full')
