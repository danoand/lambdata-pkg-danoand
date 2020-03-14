# lambdata_pkg_danoand/dano_mod_tmp.py
import pandas as pd
import datetime

def list2column(lst, df, new_col_name='new_col_name'):
    """
    list2column takes a list and appends it to a passed dataframe as a column

    Arguments:
    lst          -- a list to be added as a column to a passed dataframe
    df           -- the dataframe to which the column is to added
    new_col_name -- name of the new column

    Returns:
    pandas.DataFrame
    """
    # Validate the passed parameters
    if not isinstance(lst, list):
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
        ts = datetime.datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
        new_col_name = new_col_name + "_" + ts

    df_tmp = pd.DataFrame({new_col_name: pd.Series(lst)})

    return pd.concat([df, df_tmp], axis=1)

def date2year_month_day(df, col_name):
    """
    date2year_month_day takes a dataframe column and appends a year, month, and day column
    of column cell's date value

    Arguments:
    df           -- dataframe containing a column housing a date like value
    new_col_name -- name of the date column

    Returns:
    pandas.DataFrame
    """

    def get_date_day(obj):
        return obj.day

    def get_date_month(obj):
        return obj.month

    def get_date_year(obj):
        return obj.year

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
        print(f'"column name" is missing')
        return

    if not col_name in df.columns:
        # column name not found in the passed dataframe
        print(f'column name "{col_name}" not found in dataframe')
        return

    # Create a series of data time objects
    tmp_dt_tm_srs = pd.to_datetime(df[col_name], infer_datetime_format=True)

    # Is there a column name of 'day' in the passed dataframe
    ts = datetime.datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
    col_name_day = 'day'
    if col_name_day in df.columns:
        col_name_day = col_name_day + "_" + ts

    # Is there a column name of 'month' in the passed dataframe
    col_name_month = 'month'
    if col_name_month in df.columns:
        col_name_month = col_name_month + "_" + ts

    # Is there a column name of 'year' in the passed dataframe
    col_name_year = 'year'
    if col_name_year in df.columns:
        col_name_year = col_name_year + "_" + ts

    # Create dataframe comprised
    df_tmp = pd.DataFrame({
        col_name_day: pd.to_datetime(tmp_dt_tm_srs, infer_datetime_format=True).apply(get_date_day),
        col_name_month: pd.to_datetime(tmp_dt_tm_srs, infer_datetime_format=True).apply(get_date_month),
        col_name_year: pd.to_datetime(tmp_dt_tm_srs, infer_datetime_format=True).apply(get_date_year)})

    return pd.concat([df, df_tmp], axis=1)
