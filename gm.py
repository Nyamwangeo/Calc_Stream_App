import streamlit as st
from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Streamlit app
def main():
    st.title("Check Up App")
    
    # Ask for user's name
    name = st.text_input("Please enter your name:")
    
    if name:
        st.success(f"Good morning, {name}!")
        
        # Ask for user's date of birth
        dob = st.date_input("Please enter your date of birth (YYYY-MM-DD):", min_value=datetime(1900, 1, 1))
        
        if dob:
            # Calculate age
            age = calculate_age(dob)
            st.success(f"You are {age} years old today!")

if __name__ == "__main__":
    main()

