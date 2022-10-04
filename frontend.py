from backend import Backend
import streamlit as st


class Fronted:
    """Frontend class of my simple streamlit app."""

    be = None
    data = None

    def __init__(self):
        """Constructor"""
        print('FRONTEND:\tinit()')
        self.be = Backend()
        self.data = self.be.load_data()
        print('FRONTEND:\tData loaded!')

    def show(self):
        """Show stuff on the main page"""

        st.set_page_config(page_title="Hello world of streamlit",
                           page_icon=":fireworks:",
                           layout="centered")

        st.write('# Hello world.')
        st.write('## This is a blank project of streamlit app.')
        st.write(f"Data from DB: {self.data}")
        st.write('This app should be deployable on heroku and streamlit cloud',
                 'without any additional files and settings')
