from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Fetch JSON data from the API
        api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse JSON data into a list of dictionaries
        try:
            data = response.json()
        except ValueError as e:
            # Handle JSON parsing errors
            return f"Error parsing JSON: {e}"

        # Ensure 'Popularity' key exists in each dictionary
        # Use a default value (e.g., 0) if 'Popularity' is missing
        sorted_data = sorted(data, key=lambda x: x.get('Popularity', 0), reverse=True)

        return render_template('index.html', products=sorted_data)

    except requests.exceptions.RequestException as e:
        # Handle request-related errors
        return f"Error during request: {e}"

if __name__ == '__main__':
    app.run(debug=True)
