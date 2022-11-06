"""Dictionary related utility functions."""

__author__ = "730563759"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all the values from the column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    
    return result


def head(column_table: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """Produce a column based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n_rows > len(column_table):
        return column_table
    for column in column_table:
        i: int = 0
        n_values: list[str] = []
        while i < n_rows:
            n_values.append(column_table[column][i])
            i += 1
        result[column] = n_values
    return result


def select(column_table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for key in column:
        result[key] = column_table[key]
    return result


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    
    for key in column_table_one:
        result[key] = column_table_one[key]
    
    for key in column_table_two:
        if key in result:
            result[key] += column_table_two[key]
        else:
            result[key] = column_table_two[key]
    
    return result


def count(count_list: list[str]) -> dict[str, int]:
    """Produces a dictionary with a value and its frequency."""
    result: dict[str, int] = {}
    for i in count_list:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result