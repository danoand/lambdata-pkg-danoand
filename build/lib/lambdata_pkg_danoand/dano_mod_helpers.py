# lambdata_pkg_danoand/dano_mod_tmp.py
import pandas as pd
import datetime


class UpdatedDataFrame(pd.DataFrame):

    # list2column is a method on the class that adds a list to the dataframe as a column
    def list2column(self, lst, new_col_name='new_col_name'):
        """
        list2column accepts a list and adds it as a column to the dataframe

        Arguments:
        self         -- class data
        lst          -- list to be added
        new_col_name -- name of the new column
        """

        # Validate the passed parameters
        if not isinstance(lst, list):
            # lst is not a list - error
            print(f'passed "list" parameter is not a Python list')
            return

        # Ensure we have a non-empty list and dataframe
        if len(lst) == 0:
            # passed list is empty
            print(f'passed "list" is empty')
            return

        # Ensure the list and dataframe have the same length
        if len(lst) != len(self):
            # length of the list and dataframe are not equal
            print(f'passed "list" parameter is not a Python list')
            return

        # Is there a column name of 'new_column' in the passed dataframe
        if new_col_name in self.columns:
            # avoid a name collision with the existing 'new_column' column
            ts = datetime.datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
            new_col_name = new_col_name + "_" + ts

        self[new_col_name] = pd.Series(lst)

    # date2year_month_day takes a dataframe column and appends a year, month, and day column associate with that date
    def date2year_month_day(self, col_name):
        """
        date2year_month_day takes a date like column in the the dataframe object and appends a year, month, and day column

        Arguments:
        self         -- the object's dataframe object
        new_col_name -- name of the date column
        """

        def get_date_day(obj):
            return obj.day

        def get_date_month(obj):
            return obj.month

        def get_date_year(obj):
            return obj.year

        if len(self) == 0:
            # passed dataframe is empty
            print(f'passed "dataframe" is empty')
            return

        if len(col_name) == 0:
            # missing column name
            print(f'"column name" is missing')
            return

        if not col_name in self.columns:
            # column name not found in the passed dataframe
            print(f'column name "{col_name}" not found in dataframe')
            return

        # Create a series of data time objects
        tmp_dt_tm_srs = pd.to_datetime(
            self[col_name], infer_datetime_format=True)

        # Generate column names
        col_name_day = col_name + '_day'
        col_name_month = col_name + '_month'
        col_name_year = col_name + '_year'

        # Assign new day, month, year columns to the dataframe
        self[col_name_day] = pd.to_datetime(
            tmp_dt_tm_srs, infer_datetime_format=True).apply(get_date_day)
        self[col_name_month] = pd.to_datetime(
            tmp_dt_tm_srs, infer_datetime_format=True).apply(get_date_month)
        self[col_name_year] = pd.to_datetime(
            tmp_dt_tm_srs, infer_datetime_format=True).apply(get_date_year)


if __name__ == "__main__":
    # Exercise method 'list2column'

    # Create a updated dataframe class

    df_class = UpdatedDataFrame(pd.DataFrame(
        {"my_date": ['2010-01-01', '2010-02-01', '2010-03-01']}))

    df_class.date2year_month_day('my_date')

    df_class.date2year_month_day('my_date')

    print(df_class)
