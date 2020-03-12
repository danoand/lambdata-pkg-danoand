import pandas as pd 

from lambdata_pkg_danoand.dano_mod_helpers import list2column, date2year_month_day

df = pd.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
lst = [True, False, True, True]

df_new = list2column(lst, df, new_col_name='col_bool')

print(df_new)

df_dts = pd.DataFrame({"my_date": ['2010-01-01', '2010-01-02', '2010-01-03']})

df_dts_new = date2year_month_day(df_dts, 'my_date')

print(f'\n\n{df_dts_new}')