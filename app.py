import streamlit as st
from multiapp import MultiApp
from apps import svm_,percentages # import your app modules here
import warnings
warnings.filterwarnings("ignore")

app = MultiApp()

# Add all your application here
app.add_app("Disease", svm_.app)
app.add_app("Infect", percentages.app)


# The main app
app.run()