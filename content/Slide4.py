import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

st.header("Project:")
st.subheader("Exploration Data Analysis:")
st.image("content/images/titanic.png")

data=pd.read_csv('content/figures/train.csv')
Pclass_filter = st.selectbox("Select the Class:",  ["all",1,2,3] )
filter_text=st.text_input("Enter a name:")

if Pclass_filter!="all":
    data=data[data['Pclass']==Pclass_filter]

if filter_text:
    data=data[data["Name"].str.contains(filter_text)]
    
col1, col2 = st.columns(2)
with col1:
    genre_range=st.slider("Age Range",value=[0,100])
    data=data[(data['Age']>= genre_range[0]) & (data['Age']<=genre_range[1])]

with col2:
    Gender_select= st.radio("Gender",("Both", "male", "female"))
    
if Gender_select!="Both":
    data=data[data['Sex']==Gender_select]

    
if data.shape[0]!=0:
    st.dataframe(data)
    st.subheader("How many Survived??")

    fig,ax=plt.subplots(1,2,figsize=(18,8))
    data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
    ax[0].set_title('Survived')
    ax[0].set_ylabel('')
    sns.countplot(y='Survived',data=data,ax=ax[1])
    ax[1].set_title('Survived')

    st.pyplot(fig)


    f,ax=plt.subplots(1,2,figsize=(18,8))
    data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax=ax[0])
    ax[0].set_title('Survived vs Sex')
    sns.countplot(y='Sex',hue='Survived',data=data,ax=ax[1])
    ax[1].set_title('Sex:Survived vs Dead')
    st.pyplot(f)

st.subheader("Prediction:")
Pclass=st.selectbox('Pclass', [1,2,3])
Gender = st.radio('Gender:', ["female", "male"])
SibSp=st.slider('nbre of siblings / spouses aboard the Titanic', 0, 10)
parch = st.slider('nbre of parents / children aboard the Titanic', 0, 10)
Age_band = st.number_input('Age in years', 0, 100)

if Age_band<=16:
    Age_band=0
elif Age_band>16 and Age_band<=32:
    Age_band=1
elif Age_band>32 and Age_band<=48:
    Age_band=2
elif Age_band>48 and Age_band<=64:
    Age_band=3
elif Age_band>64:
    Age_band=4


fare = st.number_input('Passenger fare', 0, 513)

if fare<=7.91:
    Age_band=0
elif fare>7.91 and fare<=14.454:
    fare=1
elif fare>14.454 and fare<=31:
    fare=2
elif fare>31 and fare<=513:
    fare=3


loaded_model = pickle.load(open("content/figures/titanic_model.pkl", 'rb'))

if Gender=="female":
    Gender=1
else:
    Gender=0

prediction=st.button("predict")

if prediction:
    result=loaded_model.predict([[Pclass,Gender,SibSp,parch,Age_band,fare]])
    if(result==1):
        st.success("This passenger probably survived")
    else:
        st.warning("This passenger probably didn't survive")

    result=loaded_model.predict_proba([[Pclass,Gender,SibSp,parch,Age_band,fare]])
    st.write(pd.DataFrame({"survival":["No","Yes"],"probably":result[0]}))



st.header("Exercice:")
a=st.number_input("Insert a number(a):",value=10)
b=st.number_input("Insert a number(b):",value=5)
result={"Operation":["a+b","a-b","a*b","a/b","a**b"],"Result":[a+b,a-b,a*b,a/b,a**b]}
df=pd.DataFrame(result)
st.dataframe(df)
