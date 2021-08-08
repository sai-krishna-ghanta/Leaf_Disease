import streamlit as st
def app():
    st.image(
            "https://hmp.me/dovo",
            width=500, # Manually Adjust the width of the image as per requirement
        )
    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:Teal ;padding:10px">
    <h2 style="color:white;text-align:center;">IoT Based Farm survillance</h2>
    </div>
    </body>
    """    
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("This is a minor service added to the farm with app")
    st.success("Only disease detection available in website")
    st.text("For more services contact us")
    if st.button("Architecture"):
        st.success("This was made by SVM(sklearn),Opencv-Python,Streamlit and Heroku")
        st.text("The service consits additionlly YOLOV3 leaf detector and Disease detection with openCV")
    if st.button("Github Repository"):
        link1 = '[GithubRepo](https://github.com/sai-krishna-ghanta/Leaf_disease_Detection)'
        st.markdown(link1, unsafe_allow_html=True)
    if st.button("About Developer and Contact Us"):
        link2 = '[Linkedin Profile](https://www.linkedin.com/in/ghanta-sai-krishna-320ab0211/)'
        st.markdown(link2, unsafe_allow_html=True)

    
