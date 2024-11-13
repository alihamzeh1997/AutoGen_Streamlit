import streamlit as st
from autogen import GroupChatManager, ConversableAgent, GroupChat


st.set_page_config(page_title="Multi AI Agent App", page_icon="🤖")
st.title("🤖 Multi AI Agent App test")

st.write(
    "In this web application you can create mutiple conversable AI agents to speak with each other in a chat."
)