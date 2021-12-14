import streamlit as st
import pandas

#create a dictionary
data = {
    'Series_1':[1,3,4,5,7],
    'Series 2':[10,30,40,100,250]
}

#create a dataframe
df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python ')
st.write('''This is our first Web App.
Enjoy it!
''')

#writing dataframe
st.write(df)
#line graph
st.line_chart(df)
