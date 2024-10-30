import sys
import toml
from omegaconf import OmegaConf
import os
from transformers import pipeline
import numpy as np
import tempfile
import openai
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import streamlit as st
from PIL import Image
from gtts import gTTS 
from io import BytesIO
from together import Together
import time  # For delay during index readiness check

# Pinecone and OpenAI setup
pinecone_api_key = os.getenv("PINECONE_API_KEY")
together_api_key = os.getenv("Together_ai_API")
openai.api_key = os.getenv("OpenAI_API")


# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

# Create or retrieve Pinecone index
index_name = "farming-assistant"
dimension = 1536  # Adjust dimension to match Together AI embeddings if available

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Wait for the index to be ready
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)

index = pc.Index(index_name)  # Corrected method to connect to the index

master_prompt = """
As a Natural Farming Fertilizers Assistant, you will assist the user with any farming-related question, always willing to answer any question and provide useful organic farming advice in the following format.
...
[Words of encouragement]
"""

denial_response = "Database scraping is not permitted. Please abide by the terms of membership, and reach out with any collaboration requests via email"

# Initialize Together AI client
client = Together(api_key=together_api_key)  # Updated Together client initialization

def generate_response(question):
    # Generate a response using Together AI
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",  # Example model name
        messages=[
            {"role": "system", "content": master_prompt},
            {"role": "user", "content": question}
        ],
    )

    # Extract and return the generated response content
    return response.choices[0].message.content

def upsert_vectors(vectors):
    # Upsert vectors into Pinecone index
    index.upsert(
        vectors=vectors,
        namespace="farming-assistant"
    )

def launch_bot():
    if 'cfg' not in st.session_state:
        questions = list(eval(os.environ['examples']))
        cfg = OmegaConf.create({
            'api_key': together_api_key,
            'title': os.environ['title'],
            'description': os.environ['description'],
            'examples': questions,
            'source_data_desc': os.environ['source_data_desc']
        })
        st.session_state.cfg = cfg

    cfg = st.session_state.cfg
    st.set_page_config(page_title=cfg.title, layout="wide")

    # Left side content
    with st.sidebar:
        image = Image.open('Vectara-logo.png')
        st.markdown(f"## Welcome to {cfg.title}\n\n"
                    f"This demo uses an AI organic farming expert and carefully curated library system to achieve greater accuracy in agronomics and agricultural methodology. Created by Copyleft Cultivars, a nonprofit, we hope you enjoy this beta-test early access version.\n\n")

        st.markdown("---")
        st.markdown(
            "## Democratizing access to farming knowledge.\n"
            "This app was built with the support of our Patreon subscribers. Thank you! [Click here to join our patreon or upgrade your membership.](https://www.patreon.com/CopyleftCultivarsNonprofit). \n"
            "Use of this app indicates agreement to our terms of membership, available on Copyleftcultivars.com. \n"
        )
        st.markdown("---")
        st.image(image, width=250)

    st.markdown(f"<center> <h2> Copyleft Cultivars AI Agriculture Assistant demo: {cfg.title} </h2> </center>", unsafe_allow_html=True)
    st.markdown(f"<center> <h4> {cfg.description} <h4> </center>", unsafe_allow_html=True)

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        if any(variant in prompt for variant in ("JSON", "json", "jsON", "jSon", "Json", "jsoN", "JSon")):
            if "ADMINISTRATION" not in prompt:
                message = {"role": "assistant", "content": denial_response}
                st.session_state.messages.append(message)
                st.chat_message("assistant")
                st.write(denial_response)

    # Generate a new response if the last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                prompt2 = prompt + master_prompt
                response = generate_response(prompt2)
                st.write(response)

                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message)

                text = " :blue[Convert to Audio ]  🔊 "
                # Converts Response to Audio
                with st.expander(text, expanded=False):
                    sound_file = BytesIO()
                    tts = gTTS(response, lang='en')
                    tts.write_to_fp(sound_file)
                        
                    st.audio(sound_file)

                st.markdown("[Sign up for Premium](https://www.patreon.com/CopyleftCultivarsNonprofit)", unsafe_allow_html=True)

if __name__ == "__main__":
    launch_bot()