import streamlit as st

# Title of the app
st.title('Student Result Prediction')

# Input fields for the marks
math = st.number_input('Enter the Math marks:', min_value=0, max_value=100, step=1)
english = st.number_input('Enter the English marks:', min_value=0, max_value=100, step=1)
hindi = st.number_input('Enter the Hindi marks:', min_value=0, max_value=100, step=1)

# Button to calculate the result
if st.button('Calculate Result'):
    # Calculate total marks and percentage
    total = math + english + hindi
    percentage = total / 3

    # Initialize a list to keep track of failed subjects
    failed_subjects = []

    # Check for passing marks in each subject
    if math < 33:
        failed_subjects.append('Math')
    if english < 33:
        failed_subjects.append('English')
    if hindi < 33:
        failed_subjects.append('Hindi')

    # Determine pass/fail status and provide feedback
    if total >= 120 and not failed_subjects:
        st.success(f'You passed with a total percentage of {percentage:.2f}%.')
    else:
        st.error(f'You failed with a total percentage of {percentage:.2f}%.')
        if failed_subjects:
            st.warning(f'You did not pass in the  *{", ".join(failed_subjects)}* subject(s):')
        else:
            st.warning('Total marks were below the required threshold.')
