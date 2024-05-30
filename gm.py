import streamlit as st
from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age_months = 12 - birthdate.month + today.month - 1
    else:
        age_months = today.month - birthdate.month
        
    if today.day < birthdate.day:
        # Calculate days until birthday
        days_until_birthday = (30 - birthdate.day) + today.day
        # Adjust months if today is the birth month
        if today.month == birthdate.month:
            age_months -= 1
    else:
        days_until_birthday = today.day - birthdate.day
        
    return age_years, age_months, days_until_birthday

# Streamlit app
def main():
    st.title("Age Calculation Application")
    
    # Ask for user's name
    name = st.text_input("Please enter your name:")

    if name:
        st.success(f"Good morning, {name}!")
        
        # Ask for user's date of birth
        dob = st.date_input("Please enter your date of birth (YYYY-MM-DD):", min_value=datetime(1900, 1, 1))
        
        # Button to calculate age
        if st.button("Calculate Age"):
            if dob:
                # Calculate age
                age_years, age_months, days_until_birthday = calculate_age(dob)

                # Display age
                st.write(f"{Name}, you are {age_years} years, {age_months} months, and {days_until_birthday} days old today!")

if __name__ == "__main__":
    main()

