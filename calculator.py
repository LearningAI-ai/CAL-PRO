import streamlit as st

# Function to perform the calculations
def calculate(num1, num2, operation):
    try:
        if operation == "Add":
            return num1 + num2
        elif operation == "Subtract":
            return num1 - num2
        elif operation == "Multiply":
            return num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                return num1 / num2
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
try:
    st.title("Simple Calculator")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)

    # Dropdown for operation selection
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Calculate button
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.write(f"The result of {operation} is: {result}")
except Exception as e:
    st.write(f"An error occurred in the UI: {e}")
