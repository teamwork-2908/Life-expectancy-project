import pandas as pd
import pickle
df=pd.read_csv('E:/Life Expectancy project/Expectancy.csv')
df.shape
cleaneddf=df.dropna()
cleaneddf
cleaneddf.columns=[['Country','Year','Status','Expectancy','Adult Mortality',
       'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
       'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
       'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
       ' thinness  1-19 years', ' thinness 5-9 years',
       'Income composition of resources', 'Schooling']]
cleaneddf


x=cleaneddf[['Adult Mortality',
       'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
       'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
       'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
       ' thinness  1-19 years', ' thinness 5-9 years',
       'Income composition of resources', 'Schooling']].values
x    
y=cleaneddf[['Expectancy']].values
y
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
x_train,x_test,y_train,y_test
from sklearn.linear_model import LinearRegression
lg=LinearRegression()
lg.fit(x_train,y_train)

pickle.dump(lg,open('lg.pkl','wb'))

