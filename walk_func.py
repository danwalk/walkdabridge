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

# for webscraping, the url sometimes has a date at the end, that each day changes for up to date scores e.g https://masseyratings.com/nba/games?dt=20201222
def dateurlchanger(url, adddays, maxdate):
    dateofpage = url[-8:]
    date_time_obj = datetime.strptime(dateofpage, '%Y%m%d')
    maxd = datetime.strptime(maxdate, '%Y%m%d')
    if date_time_obj >= maxd:
        return 'UP TO DATE'
    else:
        date_time_obj1 = date_time_obj + timedelta(days=adddays) 
        date_time_obj1 = date_time_obj1.strftime('%Y%m%d')
        return url.replace(dateofpage, date_time_obj1)

#for webscraping, the url sometimes has a page number at the end  e.g https://www.oddsportal.com/basketball/usa/nba/results/#/page/1
def pageurlchanger(url, adddays, maxpage): #works up to 9
    page = int(url[-1:])
    if page >= maxpage:
        return 'UP TO DATE'
    else:
        return url.replace(url[-1:], str(page+adddays))

def pageadderurl(url, counter):
    return url + str(counter)

#pd.options.display.float_format = "{:,.2%}".format ------ modifiy column format, decimal places


#df3.sort_values(by=['Ratio M'], ascending=False, inplace=True) ------- sort column df

#result = users.groupby('occupation').agg({'age': ['min', 'max']}) ------- select results displayed in info function

#bygender = users.groupby(['occupation', 'gender']).agg({'age': ['mean']})
#pd.options.display.float_format = "{:,.1f}".format

#fhh = users.groupby(['occupation', 'gender']).size().unstack(fill_value=0) ------ group by two columns df

# pd.read_csv('tips.csv', index_col=0) ------ import and use first column as index

# pd.read_csv("data\\cars1.csv") ------ use \\ to move backwards and forwards in file path

# https://www.opentechguides.com/how-to/article/pandas/193/index-slice-subset.html slicing help

#https://www.marsja.se/six-ways-to-reverse-pandas-dataframe/