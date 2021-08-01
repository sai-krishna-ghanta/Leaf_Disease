import streamlit as st
from PIL import Image
from numpy import asarray
import numpy as np
import pickle
import os 



def app():

    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:Teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Leaf Disease Detection</h2>
    </div>
    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.image(our_image)
    if st.button("Detect"):   
        filename = 'Pickle_RL_Model.pkl'
        with open(filename, 'rb') as f:
            svm_classifier = pickle.load(f) 
        input_data = []
        img = our_image.resize((32,32))
        data = asarray(img)
        input_data.append(data)
        input_data = np.array(input_data, dtype='float32')/255.0
        M = input_data.shape[0]
        input_data = input_data.reshape(M,-1)
        for i in range(0,1) :
            prediction = svm_classifier.predict([input_data[i]])
        if prediction == 0:
            var = "It might be bacterial spot or septoria spot"
            pre = " Use certified disease free seeds and plants."
            a = "Avoid areas that were planted with peppers or tomatoes during previous year. "
            b = "Spraying with a copper  fungicide. "
            c = "Prune plants to promote air circulation."
            d = "Do not use overhead irrigation."
        if prediction == 1:
            var = "It might be late Blight or Early Blight"
            pre = "Allow extra room between the plants, and avoid overhead watering."
            a = "Plant resistant cultivars"
            b = "maintain a sufficient level of potassium,"
            c = " use one of the following fungicides: chlorothalonil , copper fungicide, or mancozeb "
            d = ""

        if prediction == 2:
            var = "It is Healthy"
            pre = "Leaf is healthy maintain the health "
        st.text(var)
        st.markdown("""Preventions and Precautions : :""")
        st.text(pre)
        st.text(a)
        st.text(b)
        st.text(c)
        st.text(d)



