import re
import string
import random
import streamlit as st


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1

    else:
        suggestions.append("Then Must me greater then 8")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("For Strong password length should be 12 or greater than 12")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters")

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
    characters = string.ascii_letters + string.digits + "@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def generate_custom_password():
    chars = ""
    if st.checkbox("Do you want Strings ?"):
        case = st.radio(
            "Which type of case characters you want", ["uppercase", "lowercase", "both"]
        )
        if case == "uppercase":
            chars += string.ascii_uppercase
        elif case == "lowercase":
            chars += string.ascii_lowercase
        elif case == "both":
            chars += string.ascii_letters
    if st.checkbox("Do you want numbers: "):
        chars += string.digits
    if st.checkbox("Do you want Special Characters: "):
        chars += "!@#$%^&*"
    length = st.number_input("Enter the Length of the password: ", 10)
    no_of_pwds = st.number_input("How many passwords you want to create ? ", 3)
    if st.button("Generate Password"):
        if chars == "":
            st.error("Please check any of the above checkbox")
            return
        pwd_collector = []
        for _ in range(no_of_pwds):
            password = "".join([random.choice(chars) for _ in range(length)])
            pwd_collector.append(password)
        st.subheader(f"The Generated Passwords are: ")
        # st.text("\t \n".join([pwd for pwd in pwd_collector])) # Alternative
        for index, password in enumerate(pwd_collector, 1):
            a, b = st.columns([1, 19])
            with a:
                st.write(index)
            with b:
                st.code(password, language="plaintext")
        st.toast("Password generated! Click 'Copy Icons' to copy it to your clipboard.")


st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.title("🔐 Password Strength Meter")

check_tab, generate_tab, generate_custom_pwd = st.tabs(
    [
        "🔍 Check Password Strength",
        "🔑 Generate Strong Password",
        "🛃Generate Custom Password",
    ]
)

with check_tab:
    st.header("🔍 Check Your Password Strength")
    password = st.text_input("Enter your password", type="password")

    score, suggestion = check_password_strength(password)
    if st.button("Check Password Strength"):
        st.write(f"Your Password Score is \n\t{score}\\5")
        if score >= 4:
            st.success("✅ Strong Password!")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        if suggestion:
            st.subheader("🔧 Suggestions:")
            for suggestion in suggestion:
                st.write(f"- {suggestion}")
        else:
            st.success("No Suggestions are required your password is secure 😪🥰")
    else:
        st.warning("Please enter a password to check.")

with generate_tab:
    st.header("🔑 Generate a Strong Password")
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    if st.button("🔑 Generate Password"):
        password = generate_strong_password(length=length)
        st.code(password, language="plaintext")
        st.toast("Password generated! Click 'Copy Icons' to copy it to your clipboard.")

with generate_custom_pwd:
    generate_custom_password()

st.info(
    "💡 Tip: Consider using a passphrase instead of a password. A passphrase is a sequence of words that is easier for you to remember, but harder for others to guess."
)
