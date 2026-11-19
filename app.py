import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice", layout = "centered")
st.title('AI Interview Assistant')
st.caption('Practice and Prepare for your Placements here')
st.caption("Launched by DEEKSHITHA DS")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing.Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title' , ['machine learning Engineer', 'Senior Software Engineer','DevOps Engineer', 'Other' ])
if role == "Other":
  st.text_input("Enter your Job Title" , "XXXXXXX")
  model = st.selectbox('Model',['openai/gpt-oss-safeguard-20b', 'qwen/qwen3.8-27b'])
  Level = st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])
  mode = st.radio('Activity',['Generate Questions','Generate Code Question','Evaluate Answer','Improve Answer'])
  if mode == 'Generate Questions' :
    count = st.slider("Number of Questions",1,10,5)
  elif mode == 'Generate Code Question' :
    topic = st.selectbox('Topics', ['SQL','AIML','Python','DSA','C++/C','JAVA','ADA'])
    count = st.slider("Number of Questions",1,10,5)
  else:
    question = st.text_area('Enter Interview Qestion here')
    answer = st.text_area('Enter your answer', height=160)
  if st.button("Generate AI Response", type = "primary"):
    if mode in  ['Evaluate Answers', 'Improve Answers'] and (not question.strip()) or (not answer.strip()):
       st.warning("Please enter a valid Questions and Answer")
       st.stop()
    topics = "Topics is" +  topic  + "Difficulty is" +  Level
    if mode ==  "Generate Question":
       task = "Generate " + str(count) + "Frequently asked Interview Questions 3 theory and 2 conceptual Question. Do not give answers give hint"
    elif mode == "Generate Code Question":
       task = "Generate " + str(count) + "Frequently asked Coding Questions on topic " + topic + "and give hints to solve them. Be accurate"
    elif mode == "Evaluate Answers":
       task = "Question : " + question + "My Answer : " + answer +"Evaluate this answer basd on concepts,relevence, communication length of answer.Give each rating out of 5"
    elif mode == "Improve Answers":
       task = "Question : " + question + "My Answer : " + answer + "improve the answer based on coding ,communication,apptitude ,preparation on interview."
