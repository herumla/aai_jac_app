import streamlit as st
#This is the module that allows switching between various streamlit pages. Streamlit seems pretty limited in terms of building a multi-page app
import app_utils as au 

#This is the module which has the account class
from account import set_account

#This is a very simply (and ugly) homepage - JAC seems to be stuck in the 90s and has outdated UI :)
st.set_page_config(
    page_title="JAC - Your Cloud CRM",
    layout = "wide"
)

st.title("Just Another CRM")
st.image('assets/logo.png', use_column_width=False, width=400)



# List of Accounts for the selectbox dropdown
accounts = [
    {'Name': ''},
    {'Name': 'TechCorp Inc.', 'AccountID': '1020123', 'Owner': 'John Doe', 'AnnualRevenue': '30M', 'Website':'techcorp.com', 'Headcount': '500','Industry': 'Technology', 'Phone': '555-456-7890', 'CustomerSegment': 'Enterprise'},
    {'Name': 'HealthCare Plus', 'AccountID': '279012', 'Owner': 'Mary Smith', 'AnnualRevenue': '50M', 'Website':'healthcareplus.com', 'Headcount': '100','Industry': 'HealthCare', 'Phone': '551-221-0912', 'CustomerSegment': 'Commercial'},
    {'Name': 'EduTech Innovations', 'AccountID': '981231', 'Owner': 'Jim Doe', 'AnnualRevenue': '300M', 'Website':'edutech.com', 'Headcount': '200','Industry': 'Education', 'Phone': '441-756-1252', 'CustomerSegment': 'Strategic'},
    {'Name': 'GreenEnergy Solutions', 'AccountID': '330123', 'Owner': 'Gary Smith', 'AnnualRevenue': '10M', 'Website':'greenenergy.com', 'Headcount': '5000','Industry': 'Energy', 'Phone': '775-496-123', 'CustomerSegment': 'Mid Market'},
]



st.subheader("Select Account Below:")
selected_account_name = st.selectbox('Choose an option:',[account['Name'] for account in accounts], index=0, label_visibility="collapsed", placeholder="Select...")

#Once the user selects a valid account, we want to instantiate the account object with the details of the selected account and switch to the Account Detail page
#We will be referring to that account object across the different pages of this streamlit app
if selected_account_name != "":
    selected_account = {}
    for account in accounts:
        if account['Name'] == selected_account_name:
            selected_account = account
            break
    
    account = set_account(selected_account['Name'], selected_account['AccountID'] , selected_account['Owner'], selected_account['AnnualRevenue'],selected_account['Website'], selected_account['Headcount'], selected_account['Industry'], selected_account['Phone'], selected_account['CustomerSegment'])
    au.switch_page("Account_Detail")