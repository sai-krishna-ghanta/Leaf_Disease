import streamlit as st

def app():
    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Any Leaf Infection Detection</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("In Progress")

