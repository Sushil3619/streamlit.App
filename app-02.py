import streamlit as st

st.title("My Name is Sushil")

st.write('here is simple text')
number=st.slider('pick number',0,100)

st.write(f'yor selected:{number}')

# adding a button

if st.button('say Hello'):
  st.write('Hi, hello there')
else:
  st.write('Goodbye...!')

#add radio button

genre=st.radio(
  "what's your favorite movie genre",
  ('comedy','Drama','Documentary','Action'))

#add a drop down list 

option=st.selectbox(
  'How would you like to be contacted?'
  ('Email','Home phone','Mobile phone','off-line'))


# add list on the left sidebar


option=st.sidebar(
  'Information'
  ('Home','Extra','Setting ','Help','off-line'))

st.text_input('enter your whatapp no.')


# file upland
uploaded_file=st.sidebar.file_uploder('choosse a CSV file',type='csv')



  




