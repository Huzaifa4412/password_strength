import streamlit as st
import re
import random
import string


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    return score, suggestions


def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(length))
    return password


st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.title("🔐 Password Strength Meter")

check_tab, generate_tab = st.tabs(["🔍 Check Password Strength", "🔑 Generate Strong Password"])

with check_tab:
    st.header("🔍 Check Your Password Strength")
    password = st.text_input("Enter your password", type="password")

    if st.button("Check Password Strength"):
        if password:
            score, suggestions = check_password_strength(password)

            if score == 4:
                st.success("✅ Strong Password!")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions below.")

            if suggestions:
                st.subheader("🔧 Suggestions:")
                for suggestion in suggestions:
                    st.write(f"- {suggestion}")
        else:
            st.warning("Please enter a password to check.")

with generate_tab:
    st.header("🔑 Generate a Strong Password")
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)

    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password(length)
        
        # Show the password in a code block
        st.code(strong_password, language="plaintext")
        st.toast("Password generated! Click 'Copy Icons' to copy it to your clipboard.")



st.info("💡 Tip: Consider using a passphrase instead of a password. A passphrase is a sequence of words that is easier for you to remember, but harder for others to guess.")

