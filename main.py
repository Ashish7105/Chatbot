from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Initialize the Flask app
app = Flask(__name__)

# Configure the API key
genai.configure(api_key="AIzaSyD6NOOYDNMrlE6_wrR-aagiNAKQhvzP6-o")

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")
# Define the route for the chatbot page
@app.route('/')
def home():
    return render_template('./chat.html')  # Render the chatbot interface

# Define the route for handling chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided!"})

    try:
        # Generate response using the AI model
        response = model.generate_content(user_input)
        ai_message = response.text
        return jsonify({"response": ai_message})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
