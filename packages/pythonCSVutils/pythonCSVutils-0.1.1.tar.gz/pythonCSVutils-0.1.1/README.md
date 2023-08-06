# PythonCSVUtils
`pythonCSVutils` is a lightweight Python library that provides utility functions for working with CSV files. It allows you to read, write, filter, sort, update, select, group, aggregate, merge, and manipulate CSV data with ease.

## Installation
You can install pythonCSVutils via pip:
```bash
pip install pythonCSVutils
```
## Usage
Import the necessary functions from the library:

```python
from pythonCSVutils import read_csv, write_csv, filter_rows, sort_rows, update_rows, select_columns, read_csv_header, append_rows, group_by, aggregate, merge, drop_columns

#Reading and Writing CSV Files

data = read_csv('data.csv')

#Write data to a CSV file

write_csv('output.csv', data)

#Filter rows based on a condition

filtered_data = filter_rows(data, lambda row: row['age'] > 30)

#Sort rows based on a key

sorted_data = sort_rows(data, 'age', reverse=True)

#Update rows by modifying a specific column

updated_data = update_rows(data, 'age', lambda row: row['age'] + 1)

#Select specific columns from the data

selected_data = select_columns(data, ['name', 'age'])

#Read the header of a CSV file

header = read_csv_header('data.csv')

#Append rows to an existing CSV file

append_rows('data.csv', new_rows)

#Group data by a specific key

grouped_data = group_by(data, 'gender')

#Aggregate data based on a grouping key, an aggregation key, and an aggregation function

aggregated_data = aggregate(data, 'gender', 'age', sum)

#Merge two datasets based on a common key

merged_data = merge(data1, data2, 'id')

#Drop specific columns from the data

dropped_data = drop_columns(data, ['email', 'phone'])
```

## License
This project is licensed under the MIT License.
