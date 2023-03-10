import openai 
import streamlit as st

from cryptography.fernet import Fernet
key = b'vPY3RIw5uiT3n9D4jAJV784sKucjy2TqV43_tvNLwq8='
fernet = Fernet(key)
decMessage = fernet.decrypt(b'gAAAAABkC2KGGRz5S5k2HrDhgvgpro5j_PR5885Ax-KXyS5UHT4-lKv2qS3J6ribOEhYAJvunHjTJ-25TnBQIXz-Ja8IDKPG6kX4dIkjPaSORmjPkVvr7SEfQr8cE7_UD8iyuEWg0210WmbdJR1HxbvXBPiTXLOO2g==').decode()

# pip install streamlit-chat  
from streamlit_chat import message
openai.api_key = decMessage
def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message
st.title("chatBot : Streamlit + openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

