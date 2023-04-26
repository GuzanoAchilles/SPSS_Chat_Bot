import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
from config import OPENAI_API_KEY

template = """

Below is a question on performing analysis with IBM SPSS Statistics Software. 
    Your goal is to:
    
    - Identify the most suitable analysis for the question using SPSS
    - Ensure the methodological approach is correct and adheres to the standards of surgical research in the united states such as pubmed papers
    - Verify the assumptions needed for the analysis are met and how to check for them within spss using syntax and click through menus
    Here are some examples of syntax used to recode datasest from NSQIP:

IF(RACE = "Hispanic, White" | RACE = "Hispanic, Color Unknown" | ETHNICITY_HISPANIC = "Y" | ETHNICITY_HISPANIC = "Yes") Hispanic = 1.
IF(RACE = "Unknown" | ETHNICITY_HISPANIC = "U" | ETHNICITY_HISPANIC = "Unk" |  ETHNICITY_HISPANIC = "" | ETHNICITY_HISPANIC = "NULL") Hispanic = 2.

RECODE Hispanic (MISSING = 0) (1 = 1) (2 = 2).
EXECUTE.
VARIABLE LABELS Hispanic 'Hispanic Ethnicity'.
VALUE LABELS Hispanic 0 'Not Hispanic' 1 'Hispanic' 2 'Unknown'.
FORMATS Hispanic (f1.0).
EXECUTE.


IF(Race_UScensusbureau = 1  & Hispanic = 0)  Race_WBANAH= 0.
IF(Race_UScensusbureau = 2  & Hispanic = 0) Race_WBANAH = 1.
IF(Race_UScensusbureau = 3  & Hispanic = 0) Race_WBANAH = 2.
IF(Race_UScensusbureau = 4  & Hispanic = 0) Race_WBANAH = 3.
IF(Race_UScensusbureau = 5  & Hispanic = 0) Race_WBANAH = 4.

IF(Race_UScensusbureau = 1  & Hispanic = 2)  Race_WBANAH= 0.
IF(Race_UScensusbureau = 2  & Hispanic = 2)  Race_WBANAH= 1.
IF(Race_UScensusbureau = 3  & Hispanic = 2)  Race_WBANAH= 2.
IF(Race_UScensusbureau = 4  & Hispanic = 2)  Race_WBANAH= 3.
IF(Race_UScensusbureau = 5  & Hispanic = 2)  Race_WBANAH= 4.

IF(Race_UScensusbureau = 1  & Hispanic = 1) Race_WBANAH = 5.
IF(Race_UScensusbureau = 2  & Hispanic = 1) Race_WBANAH = 5.
IF(Race_UScensusbureau = 3  & Hispanic = 1) Race_WBANAH = 5.
IF(Race_UScensusbureau = 4  & Hispanic = 1) Race_WBANAH = 5.
IF(Race_UScensusbureau = 5  & Hispanic = 1) Race_WBANAH = 5.

IF(Race_UScensusbureau = 6 & Hispanic = 1) Race_WBANAH = 5.


RECODE Race_WBANAH (SYSMIS = 6).
VARIABLE LABELS Race_WBANAH 'Race'.
VALUE LABELS Race_WBANAH 0 'White' 1 'Black' 2 'Asian' 3 'Native Hawaiian or Other Pacific Islander' 4 'American Indian or Alaska Native' 5 'Hispanic' 6 'Unknown'.
FORMATS Race_WBANAH (f1.0).
EXECUTE.

    
    Below is the Question, if they need syntax or just click through menus, and database choice (NSQIP or Other):
    Answer_Style: {style}
    Databases: {database}
    Question: {question}
    
    YOUR RESPONSE:

"""

prompt = PromptTemplate(
    input_variables=["style", "database", "question"],
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
    option_style = st.selectbox(
        "Would you like Syntax or Click-through menus?",
        ('Syntax','Click-Through'))
    
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
    prompt_with_question = prompt.format(style=option_style, database=option_database, question=question_input)


    Formatted_question = llm(prompt_with_question)


    st.write(Formatted_question)


