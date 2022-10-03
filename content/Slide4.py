import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Project:")
st.subheader("Exploration Data Analysis:")

df=pd.read_csv('content/figures/train.csv')
Pclass_filter = st.selectbox("Select the Class:",  ["all",1,2,3] )
data=df
if Pclass_filter!="all":
    data=df[df['Pclass']==Pclass_filter]


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
Pclass=st.selectbox('Pclass', [0,1,2,3])
Sex = st.radio('Gender:', ["female", "male"])
SibSp = st.number_input('nbre of siblings / spouses aboard the Titanic', 0, 10)
parch = st.number_input('nbre of parents / children aboard the Titanic', 0, 10)
Age_band = st.number_input('Age in years', 0, 100)
fare = st.number_input('Passenger fare', 0, 1000)

loaded_model = pickle.load(open("titanic_model", 'rb'))

#loaded_model.predict(np.array([0,1,2,3,4,5]))




st.header("Exercice:")
a=st.number_input("Insert a number(a):",value=10)
b=st.number_input("Insert a number(b):",value=5)
result={"Operation":["a+b","a-b","a*b","a/b","a**b"],"Result":[a+b,a-b,a*b,a/b,a**b]}
df=pd.DataFrame(result)
st.dataframe(df)
