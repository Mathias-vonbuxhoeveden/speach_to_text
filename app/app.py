import streamlit as st
import pandas as pd
from openai import OpenAI
import os
import yaml

def main():
    st.title("Speach to text app")
    open_ai_key = os.environ['open_api_key']

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file", type=None)

    if uploaded_file is not None:
        client = OpenAI(api_key = open_ai_key)
        transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=uploaded_file
        )
        text_file = open("transcription.txt", "w")
        text_file.write(transcription.text)
        text_file.close()


        # Download button
        st.download_button(
            label="Download file",
            data=transcription.text

        )

if __name__ == "__main__":
    main()