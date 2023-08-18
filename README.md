# Assembly AI + StreamLit App

This is a multi-page Streamlit app that was built to demo how to leverage an AI solution (specifically, the AssemblyAI LeMUR framework) in order to analyze call recordings.

## Pre-requisite

Ensure an AssemblyAI API Key is included in the ~/. streamlit/secrets.toml file (Streamlit docs on secrets.toml [here](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management#develop-locally-with-secrets))

## Components

This is a multi-page streamlit app:
- Home.py : This is the entrypoint file
- pages/Account_Detail.py: This is the page that displays the account detail
- pages/Call_Analysis.py: This page displays the call analyis (Summary and Action Item)
- pages/JAC_Notetaker_QA.py: This page displays the chat app
  
## Installation and Running the App
- `pip install -r requirements.txt`
- `streamlit run Home.py`
