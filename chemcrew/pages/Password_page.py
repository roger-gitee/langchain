import streamlit as st 

if "PASSWORD" not in st.session_state:
    st.session_state["PASSWORD"] = ""

st.set_page_config(page_title="OpenAI Setting",layout="wide")

st.title("OpenAI Settings")

Openai_Password = st.text_input("Password Input", value= st.session_state["PASSWORD"],max_chars= None , key=None,type='password')

saved = st.button("Save")

if saved:
    
    st.session_state["PASSWORD"] = Openai_Password
    