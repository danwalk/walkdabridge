import numpy as np
import pandas as pd
import random

#las veces que un valor aparece en una columna de un 
def times_in_column(df, column):
    return df.groupby(column).size()

#return a random number, by default between 1 and 6, but can set a different range
def dice_roller(num1=1, num2=7):
    g = random.randint(num1, num2)
    return g

#pd.options.display.float_format = "{:,.2%}".format ------ modifiy column format, decimal places


#df3.sort_values(by=['Ratio M'], ascending=False, inplace=True) ------- sort column df

#result = users.groupby('occupation').agg({'age': ['min', 'max']}) ------- select results displayed in info function

#bygender = users.groupby(['occupation', 'gender']).agg({'age': ['mean']})
#pd.options.display.float_format = "{:,.1f}".format

#fhh = users.groupby(['occupation', 'gender']).size().unstack(fill_value=0) ------ group by two columns df

# pd.read_csv('tips.csv', index_col=0) ------ import and use first column as index