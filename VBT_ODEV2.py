# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:33:53 2022

@author: tuncc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import researchpy as rp

import warnings
warnings.filterwarnings("ignore")


df = pd.read_excel('hitters.fixed.xlsx')
df.drop(columns="Unnamed: 0", inplace=True)
df.head()


# # Betimsel İstatistikler

dfCont = df.select_dtypes(include="number")
dfCat = df.select_dtypes(exclude="number")


df.describe().T


rp.summary_cont(dfCont)


rp.summary_cat(df[['League','Division','NewLeague','NEW_YEARS_Cat']])

# # Güven Aralıkları

df['Salary'].mean()


import statsmodels.stats.api as sms


sms.DescrStatsW(df['Salary']).tconfint_mean()

# # Binom

from scipy.stats import binom

p = 0.5
n = len(df['League'])
binom = binom(n, p)

print(binom.pmf(1))


# # Poisson

from scipy.stats import poisson


lamb=df['League'].mean()

poisson=poisson(mu=lamb)

print(poisson.pmf(0))


# # Hipotez Testleri

import scipy.stats as stats

stats.describe(df['Salary'])


# # Normallik Testi

from scipy.stats import shapiro


col_names = dfCont.columns

for i in col_names:
    print(i,"Değişkeni Normal Dağılır mı?", shapiro(dfCont[i])[1] > 0.05)


#H0: Örnek normal dağılım göstermektedir

#H1: Örnek normal dağılım göstermemektedir



shapiro(df['Salary'])



print("T Hesap İstatistiği: " + str(shapiro(df['Salary'])[0]))
print("Hesaplanan P-value: " + str(shapiro(df['Salary'])[1]))



from statsmodels.stats.descriptivestats import sign_test


df['Salary'].median()

sign_test(df['Salary'], 400)


print("T Hesap İstatistiği: " + str(sign_test(df['Salary'], 400)[0]))
print("Hesaplanan P-value: " + str(sign_test(df['Salary'], 400)[1]))




if sign_test(df['Salary'], 400)[1] < 0.5:
    print("H0 reddedilir.")
else:
    print("H0 reddedilemez.")