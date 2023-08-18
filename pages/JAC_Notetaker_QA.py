import streamlit as st
import assemblyai as aai

#Assembly AI
aai.settings.api_key = aai.settings.api_key = st.secrets.assemblyai.api_key


#Get Question Answer via AssemblyAI LeMUR
#We are caching this data so as long as the input params of this function is the same, it will return the result from the cache instead of running again
@st.cache_data
def get_question_answer(call_transcript_id, user_question, call_context):
    questions = [
        aai.LemurQuestion(
            question=user_question,
            answer_format="short sentences",
            context=call_context)
    ]

    transcript_from_id = aai.Transcript.get_by_id(call_transcript_id)

    result = transcript_from_id.lemur.question(questions)

    return result.response[0].answer

#adding call context
call_context = "A early stage sales discovery call where an Assembly AI sales rep understands the use case of their customer and pithces AssemblyAI's product"
call_transcript_id = "6tx8k1jrfz-3c30-49f9-9f28-2ad58a90aefc"

st.title("JAC Notetaker")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if user_question := st.chat_input("Please ask any questions about this call here!"):
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_question})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_question)
    # Display assistant response in chat message container

    prompt_response = get_question_answer(call_transcript_id, user_question, call_context)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown(prompt_response)
        st.session_state.messages.append({"role": "assistant", "content": prompt_response})

