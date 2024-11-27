# CSV-Datas-To-Bigquery

# Employee Data Transformation and BigQuery Integration

This project reads employee data from a CSV file, performs various data transformations, and uploads the processed data to a BigQuery table.

## Features

- Reads employee data from a CSV file.
- Performs data transformations:
  - Converts `FIRST_NAME` and `LAST_NAME` to uppercase.
  - Converts `EMAIL` to lowercase.
  - Formats `HIRE_DATE` to `YYYY/MM/DD`.
  - Cleans and converts `PHONE_NUMBER` to an integer, replacing non-numeric values with `0`.
  - Removes periods from `MANAGER_ID` and `DEPARTMENT_ID`.
- Uploads the transformed data to a specified BigQuery table.
