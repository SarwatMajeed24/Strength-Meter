import streamlit as st
import random
import string
import tkinter as tk  # For copying password to clipboard

# Custom CSS for the new UI design with background color and image
st.markdown("""
    <style>
        /* Set background with a gradient and image */
        body {
            background: linear-gradient(45deg, rgba(0, 191, 255, 0.8), rgba(30, 30, 30, 0.8)), url('https://source.unsplash.com/1600x900/?technology,abstract');
            background-size: cover;
            color: #E1E1E1;
            font-family: 'Arial', sans-serif;
            padding: 0;
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        /* Container for the content */
        .container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 4px 20px rgba(0, 191, 255, 0.5);
            width: 80%;
            max-width: 600px;
        }

        /* Title styling */
        h1 {
            font-size: 40px;
            font-weight: bold;
            color: #00BFFF;
            margin-bottom: 20px;
        }

        /* Checkbox and slider styling */
        .stCheckbox>label,
        .stSlider>div>div>div>span {
            color: #E1E1E1;
            font-size: 18px;
        }

        /* Password output box */
        .password-output {
            background-color: #1e1e1e;
            color: #fff;
            font-family: 'Courier New', monospace;
            font-size: 22px;
            padding: 20px;
            border-radius: 12px;
            margin-top: 30px;
            box-shadow: 0px 0px 20px rgba(0, 191, 255, 0.5);
        }

        /* Button styling */
        .stButton>button {
            background-color: #00BFFF;
            color: #fff;
            border-radius: 30px;
            padding: 12px 40px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #1E90FF;
            transform: scale(1.05);
        }

        /* Footer styling */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #bbb;
            margin-top: 50px;
        }

        /* Success and error message styling */
        .stSuccess {
            color: #32CD32;
            font-weight: bold;
        }

        .stError {
            color: #FF6347;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Function to generate password
def generate_password(length, use_digits, use_special, exclude_ambiguous, use_uppercase, use_lowercase):
    characters = ""
    
    # Add uppercase letters if selected
    if use_uppercase:
        characters += string.ascii_uppercase
    
    # Add lowercase letters if selected
    if use_lowercase:
        characters += string.ascii_lowercase
    
    # Add digits if selected
    if use_digits:
        characters += string.digits
    
    # Add special characters if selected
    if use_special:
        characters += string.punctuation
    
    # Exclude ambiguous characters if selected
    if exclude_ambiguous:
        ambiguous_characters = '0OIl1'
        characters = ''.join(c for c in characters if c not in ambiguous_characters)
    
    # Check if there are any characters to choose from
    if not characters:
        raise ValueError("No characters available for password generation. Please select at least one option.")
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Function to calculate password strength
def calculate_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 16:
        return "Medium"
    else:
        return "Strong"

# Function to copy text to clipboard using tkinter
def copy_to_clipboard(text):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Append the password
    root.update()  # Update the clipboard
    root.destroy()  # Destroy the Tkinter root window

# Streamlit UI
# st.title("Password Generator", anchor="title")

# Container with centered content
with st.container():
    st.markdown("<h1>Password Generator</h1>", unsafe_allow_html=True)
    
    # User input for password length
    length = st.slider("Select Password Length", min_value=6, max_value=32, value=12, step=1)
    
    # User options for character inclusion with checkboxes
    use_digits = st.checkbox("Include Digits")
    use_special = st.checkbox("Include Special Characters")
    exclude_ambiguous = st.checkbox("Exclude Ambiguous Characters (e.g., 0, O, I, l, 1)")
    use_uppercase = st.checkbox("Include Uppercase Letters")
    use_lowercase = st.checkbox("Include Lowercase Letters")

    # Button to generate password
    if st.button("Generate Password"):
        try:
            password = generate_password(length, use_digits, use_special, exclude_ambiguous, use_uppercase, use_lowercase)
            
            # Display password in a beautiful container
            st.markdown(f'<div class="password-output">Generated Password: {password}</div>', unsafe_allow_html=True)
            
            # Show password strength
            strength = calculate_strength(password)
            st.markdown(f"**Password Strength**: {strength}", unsafe_allow_html=True)
            
            # Copy to clipboard functionality
            if st.button("Copy to Clipboard"):
                copy_to_clipboard(password)
                st.success("Password copied to clipboard!")
            
            # Save password as a .txt file
            if st.button("Save Password as .txt"):
                with open("generated_password.txt", "w") as f:
                    f.write(password)
                st.success("Password saved as 'generated_password.txt'!")
        
        except ValueError as e:
            st.error(f"Error: {e}")

# Footer with personalized message
st.markdown("<div class='footer'>Built with ❤️ by Sarwat Majeed</div>", unsafe_allow_html=True)

