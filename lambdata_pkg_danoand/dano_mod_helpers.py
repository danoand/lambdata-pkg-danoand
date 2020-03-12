# lambdata_pkg_danoand/dano_mod_tmp.py
import pandas as pd
import datetime

# list2column takes a list and appends it to a passed dataframe as a column 
def list2column(lst, df, new_col_name='new_col_name'):
    # Validate the passed parameters
    if not type(lst) is list:
        # lst is not a list - error
        print(f'passed "list" parameter is not a Python list')
        return

    if not isinstance(df, pd.DataFrame):
        # df is not a pandas dataframe - error
        print(f'passed "list" parameter is not a Python list')
        return

    # Ensure we have a non-empty list and dataframe
    if len(lst) == 0:
        # passed list is empty
        print(f'passed "list" is empty')
        return

    if len(df) == 0:
        # passed dataframe is empty
        print(f'passed "dataframe" is empty')
        return

    # Ensure the list and dataframe have the same length
    if len(lst) != len(df):
        # length of the list and dataframe are not equal
        print(f'passed "list" parameter is not a Python list')
        return

    # Is there a column name of 'new_column' in the passed dataframe
    if new_col_name in df.columns:
        ts = datetime.datetime.now().timestamp().isoformat()
        new_col_name = new_col_name + "_" + ts

    df_tmp = pd.DataFrame({new_col_name: pd.Series(lst)})

    return pd.concat([df, df_tmp], axis=1)

# date2year_month_day takes a dataframe column and appends
def date2year_month_day(df, col_name):
    # Validate the passed parameters
    if not isinstance(df, pd.DataFrame):
        # df is not a pandas dataframe - error
        print(f'passed "list" parameter is not a Python list')
        return

    if len(df) == 0:
        # passed dataframe is empty
        print(f'passed "dataframe" is empty')
        return

    if len(col_name) == 0:
        # missing column name
        print(f'passed "dataframe" is empty')
        return

    if not col_name in df.columns:
        # column name not found in the passed dataframe
        print(f'passed "dataframe" is empty')
        return

    # Create a series of data time objects
    tmp_dt_tm_srs = pd.to_datetime(df[col_name], infer_datetime_format=True)

    # Is there a column name of 'day' in the passed dataframe
    col_name_day = 'day'
    if col_name_day in df.columns:
        ts = datetime.datetime.now().timestamp().isoformat()
        col_name_day = col_name_day + "_" + ts

    # Is there a column name of 'month' in the passed dataframe
    col_name_month = 'month'
    if col_name_month in df.columns:
        ts = datetime.datetime.now().timestamp().isoformat()
        col_name_month = col_name_month + "_" + ts

    # Is there a column name of 'year' in the passed dataframe
    col_name_year = 'year'
    if col_name_year in df.columns:
        ts = datetime.datetime.now().timestamp().isoformat()
        col_name_year = col_name_year + "_" + ts



    



