from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging to file
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Default valid credentials
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "password123"

@app.route('/')
def home():
    return "Welcome to the honeypot web app!"

# New route to serve the login form (GET method)
@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username" required />
        <input type="password" name="password" placeholder="Password" required />
        <input type="submit" value="Login" />
    </form>
    '''

# Existing route to handle login attempts (POST method)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log login attempts for analysis
    logging.info(f"Login attempt - Username: {username}, Password: {password}, IP: {request.remote_addr}")

    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        return "Login successful", 200
    else:
        return "Login failed", 401

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Log search queries for detection purposes
    logging.info(f"Search query: {query} from IP: {request.remote_addr}")
    return f"Results for: {query}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
