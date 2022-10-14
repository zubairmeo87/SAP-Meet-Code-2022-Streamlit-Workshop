st.header("Streamlit Elements:")

st.header("st.text")
st.text("Write fixed-width and preformatted text.")
code = '''st.text("Hello World!")'''
st.code(code, language='python')

st.text("Hello World!")
st.header("st.write")
st.text("""Write arguments to the app.
This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique properties:
- You can pass in multiple arguments, all of which will be written.
- Its behavior depends on the input types as follows.""")

code = '''st.write("Hello World!")'''
st.code(code, language='python')
st.write("Hello World!")
code = '''import pandas as pd 
df=pd.DataFrame({"a":[1,2,3],"b":["A","B","C"]})
st.write(df)'''
st.code(code, language='python')

import pandas as pd 
df=pd.DataFrame({"a":[1,2,3],"b":["A","B","C"]})
st.write(df)

code = '''st.write({"a":[1,2,3],"b":["A","B","C"]})'''
st.code(code, language='python')

st.write({"a":[1,2,3],"b":["A","B","C"]})


st.header("st.header")
st.text("Display text in header formatting.")

code = '''st.header(Header)'''
st.code(code, language='python')
st.header("Header")

st.header("st.subheader")
st.text("Display text in subheader formatting.")
code = '''st.subheader(Subheader)'''
st.code(code, language='python')
st.subheader("Subheader")


st.header("st.dataframe")
st.text("Display a dataframe as an interactive table.")
code = '''st.dataframe(df)'''
st.code(code, language='python')
st.dataframe(df)




st.header("st.table")
st.text("Display a static table.")
code = '''st.table(df)'''
st.code(code, language='python')
st.table(df)


st.header("st.image")
st.text("Display an image or list of images.")
code = '''st.image("Logo_Tunup.PNG")'''
st.code(code, language='python')
st.image("Logo_Tunup.png")


st.header("st.video")
st.text("Display a video player.")
code = '''st.video("content/images/tunupvideo.mp4")'''
st.code(code, language='python')
st.video("content/images/tunupvideo.mp4")




st.header("st.radio")
st.text("Display a radio button widget.")
code = '''a = st.radio('Select one:', ["dogs", "cats"])
st.markdown(a)'''
st.code(code, language='python')
a = st.radio('Select one:', ["dogs", "cats"])
st.markdown(a)
st.header("st.selectbox")
st.text("Display a select widget.")
code = '''b=st.selectbox('Pick one', ['cats', 'dogs'])
st.markdown(b)
'''
st.code(code, language='python')
b=st.selectbox('Pick one', ['cats', 'dogs'])
st.markdown(b)


st.header("st.button")
st.text("Display a button widget.")
code = '''clicked=st.button('Click me')
if clicked:
    st.markdown("you clicked on the button")'''
st.code(code, language='python')
clicked=st.button('Click me')
if clicked:
    st.markdown("you clicked on the button")

st.header("st.checkbox")
st.text("Display a checkbox widget.")
code = '''checked=st.checkbox('I agree')
if checked:
    st.markdown("i agree to the terms and conditions and the privacy policy")
'''
st.code(code, language='python')
checked=st.checkbox('I agree')
if checked:
    st.markdown("I agree to the terms and conditions and the privacy policy")

st.header("st.multiselect")
st.text("Display a multiselect widget.")
code = '''selected_list=st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
if selected_list:
    st.markdown(selected_list)'''
st.code(code, language='python')
selected_list=st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
if selected_list:
    st.markdown(selected_list)

st.header("st.slider")
st.text("Display a slider widget.")
code = '''st.slider('Pick a number', 0, 100)'''
st.code(code, language='python')
st.slider('Pick a number', 0, 100)

st.header("st.select_slider")
st.text("Display a slider widget to select items from a list.")
code = '''shirt_size=st.select_slider('Pick a size', ['S', 'M', 'L'])
st.markdown("you choose:"+shirt_size)'''
st.code(code, language='python')
shirt_size=st.select_slider('Pick a size', ['S', 'M', 'L'])
st.markdown("you choose:"+shirt_size)

st.header("st.text_input")
st.text("Display a single-line text input widget.")
code = '''name=st.text_input('First name')
st.markdown("Your name is:" + name)'''
st.code(code, language='python')
name=st.text_input('First name')
st.markdown("Your name is:" + name)

st.header("st.number_input")
st.text("Display a numeric input widget.")
code = '''st.number_input('Pick a number', 0, 10)'''
st.code(code, language='python')
st.number_input('Pick a number', 0, 10)

st.header("st.text_area")
st.text("Display a multi-line text input widget.")
code = '''st.text_area('Text to translate')'''
st.code(code, language='python')
st.text_area('Text to translate')

st.header("st.date_input")
st.text("Display a date input widget.")
code = '''st.date_input('Your birthday')'''
st.code(code, language='python')
st.date_input('Your birthday')

st.header("st.time_input")
st.text("Display a time input widget.")
code = '''st.time_input('Meeting time')'''
st.code(code, language='python')
st.time_input('Meeting time')

st.header("st.file_uploader")
st.text("Display a file uploader widget.")
code = '''st.file_uploader('Upload a CSV')'''
st.code(code, language='python')
st.file_uploader('Upload a CSV')


st.header("st.camera_input")
st.text("Display a widget that returns pictures from the user's webcam.")
code = '''st.camera_input("Take a picture")'''
st.code(code, language='python')
st.camera_input("Take a picture")


st.header("st.color_picker")
st.text("Display a color picker widget.")
code = '''a=st.color_picker('Pick a color')
st.markdown(a)'''
st.code(code, language='python')
a=st.color_picker('Pick a color')
st.markdown(a)


