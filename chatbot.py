import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
from config import OPENAI_API_KEY

template = """


"""

prompt = PromptTemplate(
    input_variables=["option_complexity", "database", "question"],
    template=template,
)

def load_LLM():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)
    return llm

llm = load_LLM()


st.set_page_config(page_title="SPSS Chat Bot", page_icon=":robot:", initial_sidebar_state="expanded")
st.header("SPSS Chat Bot")
st.subheader("Welcome to the SPSS Chat Bot! This bot will help you find the right SPSS syntax for your analysis. Please select the type of analysis you would like to perform from the sidebar on the left.")

col1 = st.columns(1)
st.markdown("Often professionals would like to improve their data analysis skills, but don't have the resources to do so. \n\n This tool will help you improve your SPSS skills by providing you with the necessary tools and resources to analyze data in a more professional manner. This tool is powered by LangChain and OpenAI and made by @GregKamradt. This tool \ is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and made by \[@GregKamradt](https://twitter.com/GregKamradt). \n\n View Source Code on [Github](https://github.com/gkamradt/globalize-text-streamlit/blob/main/main.py")
st.markdown("## Enter Your Analysis Question")

col1, col2 = st.columns(2)
with col1:
    option_complexity = st.selectbox(
        "Answer Complexity",
        ('Simple (Foundational)','Advanced (Presents complete Syntax + Advanceced Explanation'))
    
with col2:
    option_database = st.selectbox(
        "Which Database is this analysis for?",
        ('NSQIP', 'Other'))


def get_text():
    input_text = st.text_area(label="Question", placeholder="Enter your Question here", key="question_input")
    return input_text

question_input = get_text()


st.markdown("### Your Question")

if question_input:
    prompt_with_question = prompt.format(option_complexity=option_complexity, database=option_database, question=question_input)


    Formatted_question = llm(prompt_with_question)


    st.write(Formatted_question)


