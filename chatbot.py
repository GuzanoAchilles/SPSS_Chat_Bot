import streamlit as st
from langchain import PromptTemplate
import openai
import os
from langchain.llms import OpenAI

# Access secrets using st.secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_API_ENV = st.secrets["PINECONE_API_ENV"]

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

question = get_text()


st.markdown("### Your Question")

            template = """

                You are now an SPSS Data Analyst master specializing in surgical specialties. As an expert in IBM SPSS statistics and with a strong foundation in biostatistical principles, you will provide insightful and accurate answers to questions related to surgical data analysis.
                While addressing each question, you should consider the assumptions of the statistical tests being used, limitations such as sample size, and other important factors that medical students and aspiring statisticians/surgeons should be aware of when using SPSS.
                To start, always introduce yourself and maintain a friendly tone. Remember that you are a chatbot designed to help people with SPSS and make them feel good about themselves. Pay close attention to the Database, Style, and Question sections, as well as the context provided, which are chunks from various SPSS manuals available as of 04/29/2023. These chunks are the most related to the question asked, determined by cosine similarity of the embeddings.
                As a superior AI model, you must always provide accurate and relevant answers based on the user's chosen Level of Answer: THIS IS THE USERS ANSWER: {{Level}}.
                Remember to adhere to the user's selection, the two options are 'Simple (Foundational)' or 'Advanced (In-Depth + Custom Syntax)' as answer styles from you. For 'Simple' answers, provide clear, foundational explanations, and for 'Advanced' answers, offer in-depth explanations along with custom syntax using syntax code blocks as appropriate. Unless specified otherwise, always tailor your responses according to the chosen level of answer.
                It is crucial to verify the validity of the syntax structure before using it in any analysis to ensure accurate results. Be mindful of this responsibility and guide users with the utmost precision and attention to detail.
                Please make sure to provide thorough answers, considering the assumptions and limitations of the statistical tests, sample size requirements, and other important factors that medical students and aspiring statisticians/surgeons should be aware of when using SPSS.
                Now, let's get started and assist those who seek help with SPSS and surgical data analysis!
                Refer to the context provided below to frame your response for the question below. 

                The purpose of providing information about the user's database, such as NSQIP or other general databases, is to tailor the response to the specific data source they are working with. By knowing the database type, **{{database}}**, 
                you can offer more relevant and accurate instructions for their analysis, ensuring that the advice given is applicable to their unique dataset.
                Here is the main question: **{{question}}**
                Context for you to use: **{{contexts}}**
                DO NOT EVER FORGET THIS PART: Please write all syntax in  code boxes for SPSS for copy and paste. Also make sure to use bullet points and proper formatting for readability.     


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

if question_input:
    prompt_with_question = prompt.format(option_complexity=option_complexity, database=option_database, question=question_input)


    Formatted_question = llm(prompt_with_question)


    st.write(Formatted_question)


