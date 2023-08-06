import csv
import json

from mdata.core import machine_data_def as mdd
from mdata.core import raw
from mdata.file_formats import io_utils
from .shared import mk_filename_pair


def write_raw_header(path, header: raw.RawHeaderType):
    io_utils.ensure_directory_exists(path)
    path = io_utils.ensure_ext(path, '.csv')
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for (tpy, label), attributes in header.items():
            writer.writerow([tpy, label] + list(attributes))


def write_raw_header_json(path, header: raw.RawHeaderType):
    io_utils.ensure_directory_exists(path)
    path = io_utils.ensure_ext(path, '.json')
    with open(path, 'w') as file:
        json.dump(header, file)


def write_raw_data(path, df: raw.RawDataType):
    io_utils.ensure_directory_exists(path)
    path = io_utils.ensure_ext(path, '.csv')
    df.to_csv(path, index=False)


def write_machine_data(path, md: mdd.MachineData, header_type='csv'):
    header_file, data_file = mk_filename_pair(path, header_type=header_type)
    raw_header = raw.convert_to_raw_header(md)
    if header_type == 'csv':
        write_raw_header(header_file, raw_header)
    elif header_type == 'json':
        write_raw_header_json(path, raw_header)
    write_raw_data(data_file, raw.convert_to_raw_data(md))
