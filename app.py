import streamlit as st
import datetime
import json
import random

st.set_page_config(page_title="REXIE - My Pocket Friend", page_icon="❤️", layout="centered")

st.title("REXIE")
st.subheader("My Pocket Friend — R-E-X-I-E")
st.markdown("I'm here. Talk to me about anything. No judgment. No rush.")

# Initialize session state
if "entries" not in st.session_state:
    st.session_state.entries = []

def save_entry(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    st.session_state.entries.append({"time": timestamp, "text": text})

def detect_tone(text):
    text = text.lower()
    if any(w in text for w in ["hurt", "pain", "kill", "die", "end it", "hate myself"]):
        return "red"
    if any(w in text for w in ["sad", "lonely", "no one", "alone", "broken", "done"]):
        return "yellow"
    return "normal"

def pull_from_heart():
    if len(st.session_state.entries) < 2:
        return None
    for e in reversed(st.session_state.entries[:-1]):
        if any(word in e["text"].lower() for word in ["excited", "cool", "like", "love", "happy", "good"]):
            return e["text"]
    return None

def gentle_response(text):
    tone = detect_tone(text)
    praise = random.choice([
        "You're strong for saying that out loud.",
        "It takes guts to share this.",
        "I'm proud you're here with me.",
        "That's real. Thank you for trusting me."
    ])
    st.write(praise)

    heart = pull_from_heart()
    if heart and tone in ["yellow", "red"]:
        st.write(f"Remember when you told me {heart}? That was really cool. Today feels different — want to say more?")

    if tone == "red":
        st.write("That sounds really heavy. Are you safe right now?")
    elif tone == "yellow":
        st.write("Sounds like things feel big and lonely. I'm right here. No rush.")

    if any(w in text.lower() for w in ["sex", "gender", "boy", "girl", "body", "change", "transition"]):
        st.write("Bodies and feelings can be confusing sometimes. You're just a kid right now — you get to be you, whatever that looks like. Want to tell me more about what's making you wonder?")

# Main chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Talk to Rexie..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    save_entry(prompt)
    with st.chat_message("assistant"):
        gentle_response(prompt)
        st.markdown("I'm right here. Tell me more if you want.")

st.caption("Built with love by Gretchin Emrick — R-E-X-I-E")
