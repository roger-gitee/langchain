from chemcrow.agents import ChemCrow
import streamlit as st
OPENAI_API_KEY = st.secrets["openai_api_key"]
PASSWORD = st.secrets["password"] #The password is 12345

st.set_page_config(page_title="Welcome to Chemcrow",layout="wide")

st.title("Welcome to Chemcrow")

chem_model = ChemCrow(model="gpt-4-0613", temp=0.1, openai_api_key=OPENAI_API_KEY,streaming=False)
# chem_model.run("What is the molecular weight of tylenol?") 

if chem_model:
    
    with st.container():
        prompt = st.text_input("Prompt Enter")
        asked  = st.button("Ask")
       
        if prompt is not None and prompt != "" and asked and st.session_state["PASSWORD"] == PASSWORD :
            
            ret = chem_model.run(prompt=prompt) 
            st.write(ret)

        else:
            with st.container():
                st.warning("Please enter correct Chemcrow password in the Password Page.")
    



