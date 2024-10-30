from flask import Flask
from threading import Thread
import requests
import time

app = Flask(__name__)

# Function to send SMS
def send_sms(message):
    # Place SMS sending code here
    pass

# Dictionary of projects and their ports
projects = {
    "project1": 8000,
    "project2": 8001,
    # Add projects manually
}

# Function to check the status of projects
def check_projects():
    while True:
        for project_name, port in projects.items():
            try:
                # Send request to each project using 127.0.0.1
                response = requests.get(f"http://127.0.0.1:{port}")
                if response.status_code != 200:
                    raise Exception("Project is down")
            except Exception:
                # If the project is down, send an SMS
                message = f"{project_name} on port {port} is down!"
                send_sms(message)
                print(message)  # Log display
        # Wait for 10 minutes (600 seconds)
        time.sleep(600)

# Function to start checking projects asynchronously
def start_checking_projects():
    thread = Thread(target=check_projects)
    thread.start()

@app.route('/')
def home():
    return "Project Monitor is running."

if __name__ == "__main__":
    start_checking_projects()
    app.run(port=7172)
