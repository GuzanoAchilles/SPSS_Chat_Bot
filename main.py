import streamlit as st


st.set_page_config(page_title="SPSS Chat Bot", page_icon=":robot:", initial_sidebar_state="expanded")
st.header("SPSS Chat Bot")
st.subheader("Welcome to the SPSS Chat Bot! This bot will help you find the right SPSS syntax for your analysis. Please select the type of analysis you would like to perform from the sidebar on the left.")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("col1")

with col2:  
    st.markdown("Yes")
    st.write("col2")

with col3:  
    st.write("col3")
    st.markdown("Often Professional")


st.write(2+2)

input_text = st.text_area(label="Email", placeholder="Enter your text here", key="email_input")

if input_text:
    st.write("Now there is text")
    st.write(input_text)
