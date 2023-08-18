import streamlit as st
import app_utils as au 

#This is the module which has the account class
from account import get_account


#This is the Account Detail page where we will display the account data for the Account selected in the home page


selected_account = get_account() 

calls = [ f"{selected_account.name}: AssemblyAI Discovery Call - 17 Aug, 2023",
          f"{selected_account.name}: AssemblyAI Follow Up - 16 Aug, 2023", 
          f"{selected_account.name}: AssemblyAI Intro - 15 Aug, 2023"
        ]


# Dropdown to select an account


# Display Account Details
st.title(selected_account.name)

left, right = st.columns(2)

#Display Account Overview section with the populated account details
with left:
    st.header("Overview")
    tab1, tab2, tab3 = st.tabs(["Details", "Related", "News"])
    with tab1:
        col1, col2 = st.columns(2)

        with col1:     
            st.subheader("Account Owner")
            st.text(selected_account.owner)
            st.subheader("Industry")
            st.text(selected_account.industry)
            st.subheader("Account ID")
            st.text(selected_account.accountID)
            st.subheader("Annual Revenue")
            st.text(selected_account.annualRevenue)
            st.subheader("Billing Address")
            st.text("888 Airport Road, Burlingamge, CA")
            

        with col2:
            st.subheader("Customer Segment")
            st.text(selected_account.customerSegment)
            st.subheader("Phone")
            st.text(selected_account.phone)
            st.subheader("Headcount")
            st.text(selected_account.headcount)
            st.subheader("Website")
            st.text(selected_account.website)
            
    with tab2:
        st.header("Related")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("News")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

#Display Account Activity with the populated call details
with right:
    st.header("Activity")
    tab1, tab2, tab3, tab4 = st.tabs(["Past Calls", "Emails", "Log a Call", "New Event"])
    with tab1:
    # Display the list of calls using Streamlit buttons
        for index, call_title in enumerate(calls):
            # Create a container for each call
            call_container = st.container()

            with call_container:
                if st.button(call_title, key=f"analyze_call_{index}"):
                    st.session_state['call_title'] = call_title
                    au.switch_page('Call_Analysis')     

    with tab2:
        st.header("List of Emails")

    with tab3:
        st.header("Log a Call")

