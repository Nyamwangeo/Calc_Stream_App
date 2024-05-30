import streamlit as st

# Streamlit app
def main():
    st.title("Morning Greeter")
    
    # Ask for user input
    user_input = st.text_input("Please type 'Good morning':")
    
    # Check if the input is correct and respond
    if user_input == "Good morning":
        st.success("Good morning to you too!")
    elif user_input:
        st.error("Please type exactly 'Good morning'.")

if __name__ == "__main__":
    main()
