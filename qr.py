# import qrcode
# url = input("enter the url:").strip()
# file_path ="C:\\Users\\Welcome\\Desktop\\qrcode.png"
# qr = qrcode.qrcode()
# qr.add_data(url)

# img = qr.make_image()
# img.save(file_path)

# import streamlit as st
# import google.generativeai as genai

# # Yahan apni copy ki hui API Key daal dena
# API_KEY = "AIzaSyAoEdcIuP0dtBOM5BvO_NYS-WK3mECxt1g"
# genai.configure(api_key=API_KEY)

# # Gemini AI Model setup
# model = genai.GenerativeModel('gemini-1.5-flash')

# # App ka UI aur Design
# st.set_page_config(page_title="AI Mock Interviewer", page_icon="🎓")
# st.title("🎓 AI Interview & Communication Coach")
# st.markdown("Yeh AI tumhara live interview lega aur Hinglish mein feedback dega ki tumhari English kahan galat thi.")
# st.divider()

# # Job Role Select karne ka option
# role = st.selectbox("Kaunsi Job Profile ke liye Interview dena hai?", 
#                     ["Software Engineer", "Data Analyst", "Python Developer", "BCA Fresher"])

# # Chat history ko save rakhne ke liye
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Pehla sawal AI khud puche
# if len(st.session_state.chat_history) == 0:
#     st.session_state.chat_history.append({"role": "AI", "text": f"Hello! Main apka interviewer hoon. Kya aap {role} role ke interview ke liye taiyar hain? Please introduce yourself."})

# # Puraani chat screen par dikhane ke liye
# for msg in st.session_state.chat_history:
#     if msg["role"] == "User":
#         st.chat_message("user").write(msg["text"])
#     else:
#         st.chat_message("assistant").write(msg["text"])

# # User ka answer input lene ke liye
# user_answer = st.chat_input("Apna answer yahan type karein...")

# if user_answer:
#     # User ka message screen par dikhao
#     st.chat_message("user").write(user_answer)
#     st.session_state.chat_history.append({"role": "User", "text": user_answer})

#     # AI ko strict instruction (Prompt) dena
#     system_prompt = f"""
#     You are a strict but helpful HR interviewer for a {role} role. 
#     The user just answered: "{user_answer}".
    
#     Do two things:
#     1. Ask the NEXT logical technical or HR question based on their answer.
#     2. Analyze their English grammar and confidence. Give them a short, friendly feedback strictly in 'Hinglish' (Hindi written in English alphabet) at the end of your response.
#     Keep the whole response under 100 words.
#     """

#     # AI se response mangwana
#     with st.spinner("AI soch raha hai..."):
#         response = model.generate_content(system_prompt)
#         ai_reply = response.text

#     # AI ka reply screen par dikhao
#     st.chat_message("assistant").write(ai_reply)
#     st.session_state.chat_history.append({"role": "AI", "text": ai_reply})

import streamlit as st
import google.generativeai as genai

# ==========================================
# APNI API KEY YAHAN DAALNA MAT BHOOLNA
# ==========================================
API_KEY = "AIzaSyAoEdcIuP0dtBOM5BvO_NYS-WK3mECxt1g"
genai.configure(api_key=API_KEY)

# Gemini ka sabse stable model use kar rahe hain
model = genai.GenerativeModel('gemini-3-flash-preview')

# App ka UI aur Design
st.set_page_config(page_title="AI Mock Interviewer", page_icon="🎓")
st.title("🎓 AI Interview & Communication Coach")
st.markdown("Yeh AI tumhara live interview lega aur Hinglish mein feedback dega.")
st.divider()

# Job Role Select karne ka option
role = st.selectbox("Kaunsi Job Profile ke liye Interview dena hai?", 
                    ["Software Engineer", "BCA Fresher", "Data Analyst"])

# Chat history ko save rakhne ke liye
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Pehla sawal AI khud puche
if len(st.session_state.chat_history) == 0:
    st.session_state.chat_history.append({"role": "AI", "text": f"Hello! Main apka interviewer hoon. Kya aap {role} role ke interview ke liye taiyar hain? Please introduce yourself."})

# Puraani chat screen par dikhane ke liye
for msg in st.session_state.chat_history:
    if msg["role"] == "User":
        st.chat_message("user").write(msg["text"])
    else:
        st.chat_message("assistant").write(msg["text"])

# User ka answer input lene ke liye
user_answer = st.chat_input("Apna answer yahan type karein...")

if user_answer:
    # User ka message screen par dikhao
    st.chat_message("user").write(user_answer)
    st.session_state.chat_history.append({"role": "User", "text": user_answer})

    # AI ko strict instruction (Prompt) dena
    system_prompt = f"""
    You are a strict but helpful HR interviewer for a {role} role. 
    The user just answered: "{user_answer}".
    Ask the NEXT logical technical or HR question. Analyze their English grammar and confidence. Give them a short, friendly feedback strictly in 'Hinglish' (Hindi written in English alphabet) at the end. Keep it under 100 words.
    """

    # AI se response mangwana
    with st.spinner("AI apka answer check kar raha hai..."):
        try:
            response = model.generate_content(system_prompt)
            ai_reply = response.text
        except Exception as e:
            ai_reply = f"Bhai, thoda technical error aagaya: {e}"

    # AI ka reply screen par dikhao
    st.chat_message("assistant").write(ai_reply)
    st.session_state.chat_history.append({"role": "AI", "text": ai_reply})