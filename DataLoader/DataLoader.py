from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

import pandas as pd
from typing import List, Tuple

DATA_PATH = "E:\My Drive\Deutsch\Wortschatz.xlsx"
_workbook: Workbook = load_workbook(DATA_PATH)
sheet_names = _workbook.sheetnames
__data_cache = dict()

def _reload_data():
    global _workbook
    _workbook = load_workbook(DATA_PATH)

def _row_to_list(row) -> List[str]:
    return list(map(Cell.value.fget, row))

def _sheet_to_table(sheet_name:str) -> pd.DataFrame:
    if sheet_name in __data_cache:
        return __data_cache[sheet_name]

    sheet: Worksheet = _workbook[sheet_name]
    rows = iter(sheet.rows)
    columns = _row_to_list(next(rows))

    print(f"Loaded sheet: {sheet.title} (columns: {columns})")

    rows_list = []
    for row in rows:
        data = _row_to_list(row)
        if not any(data):
            break
        rows_list.append(data)

    df = pd.DataFrame(rows_list, columns=columns, dtype=str)
    __data_cache[sheet_name] = df

    return df

def get_nouns() -> pd.DataFrame:
    df = _sheet_to_table(_workbook.sheetnames[0])
    return df

def get_regular_verbs() -> pd.DataFrame:
    df = _sheet_to_table(_workbook.sheetnames[1])
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
        row = _row_to_list(next(rows))
        verb.insert(2, row[1])
        row = _row_to_list(next(rows))
        verb.insert(3, row[1])
        verb.insert(4, row[2])
        yield verb

def get_irregular_verbs() -> pd.DataFrame:
    sheet_name = _workbook.sheetnames[2]

    if sheet_name in __data_cache:
        return __data_cache[sheet_name]

    sheet: Worksheet = _workbook[sheet_name]
    rows = iter(__parse_irregular_verb(sheet.rows))
    columns = next(rows)
    print(f"Loaded sheet: {sheet.title} (columns: {columns})")

    df = pd.DataFrame(list(rows), columns=columns, dtype=str)
    __data_cache[sheet_name] = df
    return df

def get_adjectives() -> pd.DataFrame:
    df = _sheet_to_table(_workbook.sheetnames[3])
    return df

def get_adverbs() -> pd.DataFrame:
    df = _sheet_to_table(_workbook.sheetnames[4])
    return df