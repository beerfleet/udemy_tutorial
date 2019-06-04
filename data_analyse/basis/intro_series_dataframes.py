import numpy as np
import pandas as pd
import matplotlib as plt
plt.use('TkAgg')
import pylab


df = pd.read_csv('C:/DEV/Python3/Oefenen/data_analyse/basis/docs/train.csv')
# print(df.head(10))      # print first rows
# print(df.describe())    # print data summaries, like min, max, mean + standard deviation, ..
# print(df['Property_Area'].value_counts())
# pylab.show(df['ApplicantIncome'].hist(bins=50))

# pylab.show(df.boxplot)
# pylab.show(df.boxplot(column='ApplicantIncome'))
# pylab.show(df.boxplot(column='ApplicantIncome', by='Education'))
# pylab.show(df['LoanAmount'].hist(bins=50))
