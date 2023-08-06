import csv

from mdata.core.raw import raw_machine_data_types
from .importing import read_raw_data, read_machine_data, read_machine_data_from_canonical_basename, read_raw_header
from .. import io_utils
from ..validity_checking_utils import *


def is_valid_canonical_file_pair(base_path):
    try:
        read_machine_data_from_canonical_basename(base_path, validity_checking=True)
    except ValidityCheckingException:
        return False
    return True


def is_valid_file_pair(header_path, data_path):
    try:
        read_machine_data(header_path, data_path, validity_checking=True)
    except ValidityCheckingException:
        return False
    return True


def check_if_valid_header_definition_file(path):
    seen_labels = set()
    for row in io_utils.read_csv_lines_from(path):
        if len(row) < 2:
            raise MalformedHeaderFileException('Incomplete timeseries type specification.')
        if row[0] not in raw_machine_data_types:
            raise MalformedHeaderFileException('Unrecognized observation type.')
        key = row[0], row[1]
        if key in seen_labels:
            raise MalformedHeaderFileException('Duplicate timeseries type specification.')
        seen_labels.add(key)
    raw = read_raw_header(path)
    check_if_valid_raw_header(raw)
    return True


def check_if_valid_raw_header(raw_header):
    if any(v is None for v in raw_header.values()):
        raise MalformedHeaderFileException('Empty timeseries type specification.')
    return True


def check_if_valid_data_file(path):
    df = read_raw_data(path)
    check_if_valid_raw_data(df)
    return True


def check_if_valid_raw_data(df):
    if any(c not in df.columns for c in base_raw_machine_data_columns):
        raise MalformedDataFileException(f'Data is missing base column(s): {set(base_raw_machine_data_columns) - set(df.columns)}.')
    check_time_column(df)
    placeholder_cols = get_placeholder_cols(df)
    to_be_cols = gen_feature_column_names(len(placeholder_cols))
    if any(a != b for a, b in zip(placeholder_cols, to_be_cols)):
        raise MalformedDataFileException('Placeholder feature columns have unexpected labels.')
    return True
