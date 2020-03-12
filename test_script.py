import pandas as pd 

from lambdata_pkg_danoand.dano_mod_helpers import list2column

df = pd.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
lst = [True, False, True, True]

df_new = list2column(lst, df, new_col_name='col_bool')

print(df_new)