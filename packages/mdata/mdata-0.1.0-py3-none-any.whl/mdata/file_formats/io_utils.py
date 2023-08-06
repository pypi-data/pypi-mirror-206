import io
import os

def ensure_directory_exists(path):
    dirname = os.path.dirname(path)
    if dirname != '' and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)


def ensure_ext(path, desired_ext, override_ext=True):
    p, e = os.path.splitext(path)
    if e is None or e == '' or (override_ext and (e != desired_ext)):
        return path + desired_ext
    else:
        return path


def read_csv_lines_from(arg: str | os.PathLike[str] | io.BytesIO | io.StringIO) -> list[list[str]]:
    res: list[list[str]] = []
    source = None
    locally_opened = False
    try:
        if isinstance(arg, str | os.PathLike):
            arg = ensure_ext(arg, '.csv', override_ext=False)
            source = open(arg, 'r', newline='')
            locally_opened = True
        elif isinstance(arg, io.BytesIO):
            source = io.TextIOWrapper(arg, encoding='utf-8', newline='')
        elif isinstance(arg, io.StringIO):
            source = arg
        import csv
        reader = csv.reader(source, dialect='excel')
        res = [r for r in reader]
    finally:
        if locally_opened:
            source.close()
    return res
