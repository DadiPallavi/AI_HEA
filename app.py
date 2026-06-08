import streamlit as st
import requests as rq
s_url=st.secrets("s_url")
st.title("AI Healthcare Assistant")

symptom_tab,medicine_tab,hospital_tab=st.tabs(["Symptom","Medicine","Hospital"])
#6d4296ff4698e596556852c128a3c5e1e37b2713217d1172af21a0bb52cba23b 
with symptom_tab:
    st.title("Symptom Tab")
    symptom=st.text_input("Enter the Symptom")
    question=st.text_input("ask question")
    if st.button("Check Symptom"):
        res=rq.post(f"{s_url}/symptom_tool_calling",params={
            "symptom":symptom,
            "question":question
        })
        obj=res.json()
        st.success(obj["messages"][-1]["content"])


with medicine_tab:
    st.title("Medicine Tab")
    problem=st.text_input("enter your health condition problem")
    question=st.text_input("Enter the question")
    if st.button("Get Meds"):
        res=rq.post(f"{s_url}/medicine_tool_calling",params={
            "problem":problem,
            "question":question
        })
        obj=res.json()
        st.success(obj["messages"][-1]["content"])

with hospital_tab:
    st.title("Search Hospitals")
    problem=st.text_input("Enter Your Problem")
    city=st.text_input("enter the City")
    question=st.text_input("Enter which type of hospital you want ")
    if st.button("Find Hospitals"):
        res=rq.post(
            f"{s_url}/hospital_tool_calling",
            params={
                "problem":problem,
                "city":city,
                "question":question
            }
        )
        obj=res.json()
        st.success(obj["messages"][-1]["content"])