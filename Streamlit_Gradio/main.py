import streamlit as st
import time
import random

st.header("A quick Survey when learning Streamlit")
st.subheader("Entry level")
    
## User verification
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("Enter your name: ", value="")
    age = st.slider("What is your age?", 13, 60, 17)
    if age < 18:
        st.write("You are not old enough to submit this form.")
    else:
        st.write("You may continue!")
with col2:
    email = st.text_input("Enter your email: ", value="")
    if st.button("Submit"):
        if "@" not in email and "." not in email:
            st.error("Please enter a valid email address.")
        else:
            st.success("Submitted.")
with col3:
    ## Option for which AIO
    option = st.selectbox(
        "Which of these AI/ML tools do you use?",
        ("TensorFlow", "Keras", "PyTorch", "PySpark"),
        placeholder="Select one tool..."
    )
    
## Model loading
st.header("Model Loading")

def load_model():
    with st.spinner('Model is being loadded...'):
        time.sleep(3)
    is_loaded = random.choice([True, False])
    return is_loaded

if st.button("Load Model"):
    model = load_model()
    if model:
        st.success("Model is loaded!")
    else:
        st.error("Model failed to load.")