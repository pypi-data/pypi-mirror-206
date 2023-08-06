import json

import pandas as pd

from mdata.core import machine_data_def as mdd, raw
from mdata.core import raw
from mdata.file_formats import io_utils
from mdata.file_formats.csv.shared import mk_filename_pair


def read_raw_data(path) -> raw.RawDataType:
    # path = ensure_ext(path, '.csv', override_ext=False)
    df = pd.read_csv(path)
    df[raw.COLUMN_NAME_DICT[raw.MDConcepts.Time]] = pd.to_datetime(
        df[raw.COLUMN_NAME_DICT[raw.MDConcepts.Time]])
    return df


def read_machine_data(header_path, data_path, validity_checking=True, header_type='csv') -> mdd.MachineData:
    if validity_checking:
        if header_type == 'csv':
            from .checking import check_if_valid_header_definition_file
            check_if_valid_header_definition_file(header_path)

    raw_header: raw.RawHeaderType = None
    if header_type == 'csv':
        raw_header = read_raw_header(header_path)
    elif header_type == 'json':
        raw_header = read_raw_header_json(header_path)
    raw_data = read_raw_data(data_path)

    if validity_checking:
        from .checking import check_if_valid_raw_header, check_if_valid_raw_data
        from mdata.file_formats.validity_checking_utils import check_header_data_compatibility
        check_if_valid_raw_header(raw_header)
        check_if_valid_raw_data(raw_data)
        check_header_data_compatibility(raw_header, raw_data)

    return raw.create_machine_data_from_raw(raw_data, raw_header)


def read_machine_data_from_canonical_basename(basepath, validity_checking=True, header_type='csv') -> mdd.MachineData:
    header_file, data_file = mk_filename_pair(basepath, header_type=header_type)
    return read_machine_data(header_file, data_file, validity_checking=validity_checking, header_type=header_type)


def read_raw_header_json(path) -> raw.RawHeaderType:
    return json.load(path)


def read_raw_header(path) -> raw.RawHeaderType:
    metadata = {}
    for row in io_utils.read_csv_lines_from(path):
        metadata[row[0], row[1]] = tuple(row[2:]) if len(row) > 2 else []
    return metadata
