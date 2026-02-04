from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from agents.planner import planner
from agents.executor import executor
from agents.verifier import verifier

st.title("AI Operations Assistant")

task = st.text_input("Enter your task")

if st.button("Run"):
    plan = planner(task)
    result = executor(plan)
    final = verifier(result)
    st.json(final)
