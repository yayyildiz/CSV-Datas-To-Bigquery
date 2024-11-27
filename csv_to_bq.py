# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:20:49 2024

@author: DTYYILDIZ
"""
import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account
import datetime as dt

def func(): 
    csv_yolu = 'C:/Users/DTYYILDIZ/Desktop/employees_output.csv'
    df = pd.read_csv(csv_yolu)

    df['FIRST_NAME'] = df['FIRST_NAME'].str.upper()
    df['LAST_NAME'] = df['LAST_NAME'].str.upper()
    df['EMAIL'] = df['EMAIL'].str.lower()
    df.info()
    
    df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])
    df['HIRE_DATE'] = df['HIRE_DATE'].dt.strftime('%Y/%m/%d')

    df['PHONE_NUMBER'] = df['PHONE_NUMBER'].astype(str)
    df['PHONE_NUMBER'] = df['PHONE_NUMBER'].str.replace('.', '')
    df['PHONE_NUMBER'] = df['PHONE_NUMBER'].fillna('0')
    df['PHONE_NUMBER'] = df['PHONE_NUMBER'].apply(lambda x: int(x) if x.isdigit() else 0)
    
    df['MANAGER_ID']=df['MANAGER_ID'].astype(str)
    df['MANAGER_ID']=df['MANAGER_ID'].str.replace('.','')
    
    df['DEPARTMENT_ID']=df['DEPARTMENT_ID'].astype(str)
    df['DEPARTMENT_ID']=df['DEPARTMENT_ID'].str.replace('.','')
    
    return df

def bq_create_table(df):
    credentials = service_account.Credentials.from_service_account_file("C:/Users/DTYYILDIZ/Desktop/XXXXX.json")
    project_id = 'XXXXXX'
    dataset_id = 'XXXXXX'
    table_id = 'XXXXXX'  
    pandas_gbq.to_gbq(df, table_id, project_id=project_id, credentials=credentials, if_exists='replace')

def main():
    df = func()
    bq_create_table(df)

main()


   



