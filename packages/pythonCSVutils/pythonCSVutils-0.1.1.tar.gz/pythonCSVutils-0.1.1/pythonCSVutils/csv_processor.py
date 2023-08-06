import csv
from typing import List, Dict, Any, Callable
from collections import defaultdict

def read_csv(file_path: str, delimiter: str = ',') -> List[Dict[str, Any]]:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = [row for row in reader]
    return data

def write_csv(file_path: str, data: List[Dict[str, Any]], delimiter: str = ',') -> None:
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        if data:
            writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)

def filter_rows(data: List[Dict[str, Any]], condition: callable) -> List[Dict[str, Any]]:
    return [row for row in data if condition(row)]

def sort_rows(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    return sorted(data, key=lambda row: row[key], reverse=reverse)

def update_rows(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    for row in data:
        row[key] = value(row)
    return data

def select_columns(data: List[Dict[str, Any]], columns: List[str]) -> List[Dict[str, Any]]:
    return [{k: row[k] for k in columns} for row in data]

def read_csv_header(file_path: str, delimiter: str = ',') -> List[str]:
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        header = next(reader)
    return header

def append_rows(file_path: str, data: List[Dict[str, Any]], delimiter: str = ',') -> None:
    with open(file_path, mode='a', encoding='utf-8', newline='') as file:
        if data:
            writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=delimiter)
            writer.writerows(data)

def group_by(data: List[Dict[str, Any]], key: str or callable) -> Dict[Any, List[Dict[str, Any]]]:
    grouped_data = defaultdict(list)
    for row in data:
        group_key = row[key] if isinstance(key, str) else key(row)
        grouped_data[group_key].append(row)
    return grouped_data

def aggregate(data: List[Dict[str, Any]], group_by_key: str, agg_key: str, agg_func: Callable) -> Dict[Any, Any]:
    groups = group_by(data, group_by_key)
    return {group_key: agg_func([row[agg_key] for row in group_rows]) for group_key, group_rows in groups.items()}

def merge(data1: List[Dict[str, Any]], data2: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    data2_dict = {row[key]: row for row in data2}
    merged_data = []

    for row in data1:
        if row[key] in data2_dict:
            merged_row = {**row, **data2_dict[row[key]]}
            merged_data.append(merged_row)

    return merged_data

def drop_columns(data: List[Dict[str, Any]], columns: List[str]) -> List[Dict[str, Any]]:
    return [{k: v for k, v in row.items() if k not in columns} for row in data]
