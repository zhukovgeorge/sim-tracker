import streamlit as st
import pandas as pd
import datetime

# Initialize or load data
data_file = 'sim_activations.csv'
try:
    df = pd.read_csv(data_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['SIM ID', 'Activation Date', 'Status'])

# Title
st.title('SIM Card Activation Tracker')

# Sidebar menu
st.sidebar.header('Menu')
option = st.sidebar.selectbox("Choose Action", ["Dashboard", "New Activation"])

if option == "Dashboard":
    st.header('Dashboard')
    # Displaying current status
    st.write('### SIM Activation Data')
    st.dataframe(df)

    # Metrics
    total_sims = len(df)
    active_sims = len(df[df['Status'] == 'Activated'])
    deactivated_sims = total_sims - active_sims

    st.write("### Metrics")
    st.metric("Total SIMs", total_sims)
    st.metric("Activated SIMs", active_sims)
    st.metric("Deactivated SIMs", deactivated_sims)

elif option == "New Activation":
    st.header('New SIM Activation')
    # Form to add new activation
    with st.form(key='activation_form'):
        sim_id = st.text_input("SIM ID")
        activation_date = st.date_input("Activation Date", datetime.date.today())
        status = st.selectbox("Status", ["Activated", "Deactivated"])
        submit_button = st.form_submit_button(label='Activate SIM')

    if submit_button:
        if sim_id:
            new_data = pd.DataFrame({
                'SIM ID': [sim_id],
                'Activation Date': [activation_date],
                'Status': [status]
            })
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(data_file, index=False)
            st.success(f"SIM {sim_id} has been successfully added.")
        else:
            st.error("Please enter a valid SIM ID.")
