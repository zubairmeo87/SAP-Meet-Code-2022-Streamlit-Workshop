st.subheader("Quick introduction:")
st.text("Streamlit, an app framework built for ML engineers and its main purpose is to turn Python Scripts into Beautiful ML Tools.")
st.subheader("Quick history:")
st.text("The framework was designed and implemented by two Google Engineers in order to simplify the process of building and maintaining UI applications (ex: ML dashboards) where original process (figure below) seemed unmaintainable and unefficient.")
image = Image.open('content/images/slide 2_first_image.png')
st.image(image)
st.subheader("General simple idea from streamlit:")
st.text("What if we could make building tools as easy as writing Python scripts?")
st.subheader("Read more:")
st.markdown("""
-	Article from streamlit founders: https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace 
- Interesting article from DataCamp: https://www.datacamp.com/tutorial/streamlit 
""")
st.subheader("Getting started with streamlit")
st.markdown("""
- Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. 
- Founded in 2018 by ex Google engineers(Adrien Treuille, Amanda Kelly and Thiago Teixeira
- To install streamlit, you can use the following pip command on the console
""")
st.code("pip install streamlit", language='powershell')
st.markdown("""
- To get started, just create an empty python file as main.py and paste the below code:
""")

code = '''import streamlit as st :
st.write("Hello! Streamlit")'''
st.code(code, language='python')

st.markdown(""" - Finally, run the below command:""")
st.code("streamlit run main.py", language='powershell')

st.header("Core principles of Streamlit")
st.markdown("- #1: Embrace Python scripting:  run from top to bottom(no hidden state). If you know how to write Python scripts, you can write Streamlit apps.")
st.markdown("- #2: no callbacks! Every interaction simply reruns the script from top to bottom. This approach leads to really clean code:")
code = '''x = st.slider('x')
st.write(x, 'squared is', x * x)'''
st.code(code, language='python')
x = st.slider('x')
st.write(x, 'squared is', x * x)
st.markdown("- #3: Reuse data and computation:Streamlit introduces a cache primitive that behaves like a persistent, immutable-by-default, data store that lets Streamlit apps safely and effortlessly reuse information")
code='''data=pd.read_csv("https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz",nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label])'''
st.code(code, language='python')
data=pd.read_csv("https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz",nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label])
st.markdown("In short, Streamlit works like this:")
st.markdown("1-The entire script is run from scratch for each user interaction.")
st.markdown("2- Streamlit assigns each variable an up-to-date value given widget states.")
st.markdown("3- Caching allows Streamlit to skip redundant data fetches and computation.")
image = Image.open('content/images/workflow3.png')
st.image(image)
