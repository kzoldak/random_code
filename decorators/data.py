#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 20:12:31 2019

@author: kimzoldak
"""


import numpy as np
import pandas as pd
import datetime 



def get_pge_data():
    #direc = '/Users/kimzoldak/Github/PGEbills/'
    filename =   '/Users/kimzoldak/Github/PGEbills/data/' \
                +'pge_electric_interval_data__2018-10-04_to_2019-02-11.csv'
    df = pd.read_csv(filename, skiprows=5)
    # FIX COLUMN NAMES - REPLACE WHITESPACE
    df.columns = df.columns.str.replace(' ', '_')
    # CONVERT DATA TYPES TO DATETIME
    df['DATE'] = pd.to_datetime(df.DATE)
    df['START_TIME'] = pd.to_datetime(df.START_TIME)
    df['END_TIME'] = pd.to_datetime(df.END_TIME)
    # CONVERT COST DTYPE INTO A FLOAT
    df['COST'] = df.COST.str.replace('$','').astype(float)
    # PRICE CHARGED PER KWH. THIS RATE GOES UP WHEN USE MORE ENERGY.
    df['PRICEPERKWH'] = df.COST/df.USAGE
    # MONTH NAME COLUMN
    df['MONTH'] = [date.month_name() for date in df.DATE]
    return df