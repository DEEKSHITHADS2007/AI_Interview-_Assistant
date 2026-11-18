import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice", layout = "centered")
st.title('AI Interview Assistant')
st.caption('Practice and Prepare for your Placements here')
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing.Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title' , ['machine learning Engineer', 'Senior Software Engineer','DevOps Engineer', 'Other' ])
if role == "Other":
  st.text_input("Enter your Job Title" , "XXXXXXX")
  model = st.selectbox('Model',['openai/gpt-oss-safeguard-20b', 'qwen/qwen3.8-27b'])
