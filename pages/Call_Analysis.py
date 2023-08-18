import streamlit as st
import assemblyai as aai
#This is the module that allows switching between various streamlit pages. Streamlit seems pretty limited in terms of building a multi-page app
import app_utils as au 
#This is the module which has the account class
from account import get_account

#This is the call analysis page where we will display the 1. Call Summary 2. Call Action Items and 3. Display a button to navigate to the JAC Notetaker QA page

#Read the secrets from the .streamlit/secrets.toml file 
#https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management#develop-locally-with-secrets
aai.settings.api_key = st.secrets.assemblyai.api_key


#Transcribe the Video Call
@st.cache_data(show_spinner=False)
def get_call_transcription(file_url):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_url)
    return transcript.id

#Get Call Summary via AssemblyAI LeMUR
#We are caching this data so as long as the input params of this function is the same, it will return the result from the cache instead of running again
@st.cache_data(show_spinner=False)
def get_call_transcript_summary(call_transcript_id, call_context):
    transcript_from_id = aai.Transcript.get_by_id(call_transcript_id)

    answer_format = "3 line summary of the call"

    result = transcript_from_id.lemur.summarize(
        context=call_context,
        answer_format=answer_format,
    )
    return result.response

#Get Call Action Items via AssemblyAI LeMUR
#We are caching this data so as long as the input params of this function is the same, it will return the result from the cache instead of running again
@st.cache_data(show_spinner=False)
def get_call_transcript_action_items(call_transcript_id, call_context):
    transcript_from_id = aai.Transcript.get_by_id(call_transcript_id)
    
    answer_format='''**<topic owner>**:
    \n   <relevant action items>
    '''
    result = transcript_from_id.lemur.action_items(
        context=call_context,
        answer_format=answer_format,
    )

    return result.response

#Transcribe File
file_url = "https://gtusieyatzvotohzvlfy.supabase.co/storage/v1/object/public/take-home/video1982379628.mp4?t=2023-05-01T16%3A31%3A40.958Z"

#Hardcoding the transcript id so that I don't need to transcribe it every time
#transcript_id = get_call_transcription(file_url)
transcript_id = "6tx8k1jrfz-3c30-49f9-9f28-2ad58a90aefc"
call_context = "A early stage sales discovery call where an Assembly AI sales rep understands the use case of their customer and pithces AssemblyAI's product"

selected_account = get_account() 

if 'call_title' not in st.session_state:
    st.session_state['call_title'] = ''

call_title = st.session_state.call_title

st.title(call_title)

#Generate the call summary. The get_call_transcript_summary function is cached using @st.cache_data so that we only need to generate this summary once
st.subheader("Summary")
with st.spinner('Gathering Summary of the call...'):
    call_summary = get_call_transcript_summary(transcript_id, call_context)
st.write(call_summary)

#Generate the call action items. The get_call_transcript_action_items function is cached using @st.cache_data so that we only need to generate this action items once
st.subheader("Action Items")
with st.spinner('Gathering Actions Items from the call...'):
    call_action_items = get_call_transcript_action_items(transcript_id, call_context)
st.write(call_action_items)

#If user choses to ask the JAC Notetaker, swithc to the JAC Notetake QA Page
st.subheader("Additional Questions?")
if (st.button('Ask JAC Notetaker')):
    au.switch_page('JAC_Notetaker_QA')
    
