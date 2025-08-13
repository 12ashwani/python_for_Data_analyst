from flask import Flask, render_template, request

'''Imports necessary modules from Flask:
- Flask to create the application.
- render_template to render HTML templates.
- request to handle form data from the client.'''

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# '''Defines a route for the root URL ('/'). This route handles both GET and POST requests:
# - GET request: Renders the HTML form for user input.
# - POST request: Processes the form data submitted by the user.'''

def index():
    '''
    Handles requests to the root URL ('/'). This function:
    - Renders the HTML form and processes form submissions if the request method is POST.
    - Retrieves input data, performs calculations, and generates a result based on the input marks.
    '''
    result = None
    if request.method == 'POST':
        # Initializes result as None. Checks if the request method is POST to process the submitted form.
        try:
            # Retrieve marks from the form fields, converting the data to integers.
            math = int(request.form['math'])
            english = int(request.form['english'])
            hindi = int(request.form['hindi'])
            science = int(request.form['science'])
            social_science = int(request.form['social_science'])
            
            # Calculate total marks and percentage.
            total = math + english + hindi + science + social_science
            percentage = total / 5
            failed_subjects = []

            # Dictionary to hold subjects and their marks
            marks_dict = {
                'Math': math,
                'English': english,
                'Hindi': hindi,
                'Science': science,
                'Social Science': social_science
            }

            # Check if the marks in each subject are below the passing threshold (33).
            for subject, marks in marks_dict.items():
                if marks < 33:
                    failed_subjects.append(f'{subject} (Marks: {marks})')
            
            # Determine pass/fail status based on total marks and passing criteria.
            if total >= 200 and not failed_subjects:
                result = f'You passed with a total percentage of {percentage:.2f}%.'
            else:
                result = f'You failed with a total percentage of {percentage:.2f}%.'
                if failed_subjects:
                    result += ' You did not pass in the following subject(s): ' + ', '.join(failed_subjects) + '.'
                else:
                    result += ' Total marks were below the required threshold.'

        except ValueError:
            # Handle case where the input is not a valid integer.
            result = 'Please enter valid numbers for all fields.'

    # Render the HTML template and pass the result to it.
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Run the Flask application in debug mode to enable live reloading and detailed error messages.
    app.run(debug=True)
