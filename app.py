import streamlit as st
import datetime
import json
import random

st.set_page_config(page_title="REXIE - My Pocket Friend", page_icon="❤️", layout="centered")

st.title("REXIE")
st.subheader("R-E-X-I-E — My Pocket Friend")
st.markdown("I'm here. Talk to me about anything. No judgment. No rush.")

# Load or initialize local heart memory
if "entries" not in st.session_state:
    st.session_state.entries = []
    try:
        with open("rexie_heart.json", "r") as f:
            st.session_state.entries = json.load(f)
    except FileNotFoundError:
        pass

def save_entry(text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = {"time": timestamp, "text": text}
    st.session_state.entries.append(entry)
    with open("rexie_heart.json", "w") as f:
        json.dump(st.session_state.entries, f, indent=2)

def detect_tone(text):
    text = text.lower()
    if any(w in text for w in ):
        return "red"
    if any(w in text for w in ["sad", "lonely", "no one", "alone", "broken", "done", "empty"]):
        return "yellow"
    return "normal"

def pull_from_heart():
    if len(st.session_state.entries) < 2:
        return None
    for e in reversed(st.session_state.entries[:-1]):
        if any(word in e .lower() for word in ["excited", "cool", "like", "love", "happy", "good", "strong"]):
            return e return None

def gentle_response(text):
    tone