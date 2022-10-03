st.header("Getting Started with streamlit")

st.markdown("""
- Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. 
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
