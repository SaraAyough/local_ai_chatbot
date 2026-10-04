import utils
import streamlit as st 

st.title('CHATBOT project')

if 'message' not in st.session_state:
    st.session_state['message'] = [{'role':'ai', 'content':'How can i help you?'}]

for msg in st.session_state['message']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input()
model = 'qwen:0.5b'

if prompt:
    st.session_state['message'].append({
        'role': 'user',
        'content': prompt
    })

    with st.chat_message('user'):
        st.write(prompt)

    with st.spinner('Generating response....'):
        new_prompt = 'give me answer with example and emoji and shapes and description ' + prompt
        response = utils.call_ollama_model(model, new_prompt)

    with st.chat_message('assistant'):
        st.write(response)

    st.session_state['message'].append({
        'role': 'assistant',
        'content': response
    })
