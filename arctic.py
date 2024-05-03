import streamlit as st

def main():
    st.title("My Streamlit App")

    col1, col2, col3, col4 = st.beta_columns(4)

    button1 = col1.button("Button 1")
    button2 = col2.button("Button 2")
    button3 = col3.button("Button 3")
    button4 = col4.button("Button 4")

    textbox1 = col1.text_input("Textbox 1", "Enter text here")
    textbox2 = col2.text_input("Textbox 2", "Enter text here")
    textbox3 = col3.text_input("Textbox 3", "Enter text here")
    textbox4 = col4.text_input("Textbox 4", "Enter text here")

if __name__ == "__main__":
    main()
