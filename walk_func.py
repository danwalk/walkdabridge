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


