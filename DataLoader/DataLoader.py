import pandas as pd
from typing import List, Iterable
from openpyxl import load_workbook, Workbook

DATA_PATH = r"G:\My Drive\Deutsch\Wortschatz.xlsx"

""" LOADING SECTION """
_workbook: Workbook = None
sheet_names: tuple = None
__data_cache: dict = None

# TODO Order words by stats


def _reload_data():
    global _workbook, __data_cache, sheet_names

    print("Reloading the data")
    _workbook = load_workbook(DATA_PATH)
    sheet_names = _workbook.sheetnames
    __data_cache = dict()


if _workbook is None or __data_cache is None or sheet_names is None:
    from WordRecorder import load_stats
    _reload_data()
    load_stats()

""" LOADING SECTION """


def _row_to_list(row) -> List[str]:
    from openpyxl.cell import Cell

    return list(map(Cell.value.fget, row))


def _df_to_iter(df: pd.DataFrame) -> Iterable:
    df.reset_index()
    df = df.sample(frac=1).iterrows()
    return df


def _sheet_to_table(sheet_name: str) -> pd.DataFrame:
    if sheet_name in __data_cache:
        return __data_cache[sheet_name]

    sheet = _workbook[sheet_name]
    rows = iter(sheet.rows)
    columns = _row_to_list(next(rows))

    print(f"Loaded sheet: {sheet.title} (columns: {columns})")

    rows_list = []
    for row in rows:
        data = _row_to_list(row)
        if not any(data):
            break
        rows_list.append(data)

    df = pd.DataFrame(rows_list, columns=list(map(str.lower, columns)), dtype=str)
    __data_cache[sheet_name] = df

    return df


def __parse_irregular_verb(rows):
    for row in rows:
        verb = []
        row = _row_to_list(row)
        if not any(row):
            return
        verb.append(row[0])
        verb.append(row[1])
        verb.append(row[3])
        verb.append(row[4])
        row = _row_to_list(next(rows))
        verb.insert(2, row[1])
        row = _row_to_list(next(rows))
        verb.insert(3, row[1])
        verb.insert(4, row[2])
        yield verb


def _load_irregular_verbs() -> pd.DataFrame:
    sheet_name = _workbook.sheetnames[2]

    if sheet_name in __data_cache:
        return __data_cache[sheet_name]

    sheet = _workbook[sheet_name]
    rows = iter(__parse_irregular_verb(sheet.rows))
    columns = next(rows)
    print(f"Loaded sheet: {sheet.title} (columns: {columns})")

    df = pd.DataFrame(list(rows), columns=list(map(str.lower, columns)), dtype=str)
    __data_cache[sheet_name] = df

    return df


def get_nouns() -> Iterable:
    df = _sheet_to_table(_workbook.sheetnames[0])
    return _df_to_iter(df)


def get_verbs() -> Iterable:
    regular = _sheet_to_table(_workbook.sheetnames[1])
    irregular = _load_irregular_verbs()
    irregular = irregular.drop(columns=['präsens', 'präteritum', 'haben/sein', 'partizip ii'])
    df = pd.concat((regular, irregular))
    return _df_to_iter(df)


def get_regular_verbs() -> Iterable:
    df = _sheet_to_table(_workbook.sheetnames[1])
    return _df_to_iter(df)


def get_irregular_verbs() -> Iterable:
    df = _load_irregular_verbs()
    return _df_to_iter(df)


def get_adjectives() -> Iterable:
    df = _sheet_to_table(_workbook.sheetnames[3])
    return _df_to_iter(df)


def get_adverbs() -> Iterable:
    df = _sheet_to_table(_workbook.sheetnames[4])
    return _df_to_iter(df)
