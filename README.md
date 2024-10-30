```markdown
# Project Monitor

**Project Monitor** is a Flask-based server monitoring tool that checks if specific projects on designated ports are active or down. If a project goes down, it sends an SMS alert to notify the admin.

## Features

- Monitors specified projects on custom ports.
- Sends an SMS alert if any project is detected as down.
- Runs checks every 10 minutes by default.

## Requirements

- Python 3.6+
- Flask
- `requests` library for HTTP requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tohidnamdari/project-monitor
   cd project-monitor
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

- Open the `app.py` file to add or modify projects and their respective ports.
- Update the `projects` dictionary to include each project's name and port:
   ```python
   projects = {
       "project1": 8000,
       "project2": 8001,
       # Add additional projects as needed
   }
   ```

- Implement the `send_sms` function with your preferred SMS API provider.

## Usage

1. Start the Flask app in a screen session to keep it running in the background:
   ```bash
   screen -S project_monitor
   python app.py
   ```

2. To detach from the screen session without stopping the script, press `Ctrl + A` followed by `D`.

3. To reattach to the screen session later, run:
   ```bash
   screen -r project_monitor
   ```

## Project Structure

```
project-monitor/
├── app.py               # Main application file
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## How It Works

1. **Port Monitoring**: The application sends a request to `127.0.0.1:<port>` for each project every 10 minutes.
2. **SMS Alert**: If a project is detected as down, the `send_sms` function triggers an SMS alert.




##### I hope you enjoy the project 😊


##### powerd by Tohid Namdari

