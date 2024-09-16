# Daily_CLI_reporter

This Python script retrieves time entries for a specific user in a Clockify workspace using the Clockify API. It can be useful for tracking time logs and project activities programmatically.

## Features

- Retrieve all time entries for a specific user in a given workspace.
- Prints the report of all dates with time entries with details like description, end time, time taken for completing the task and summary time of work during that date.
- Basic error handling to help troubleshoot API issues.
  
## Prerequisites

- **Python 3.x** installed.
- **`requests` library** installed. To install it, run:
  ```bash
  pip install requests

## Installation

- Clone or Download the Repository:
  ```bash
  git clone https://github.com/Drakonchyk/Daily_CLI_reporter.git
- Install Dependencies:
  ```bash
  pip install -r requirements.txt

## Configuration
You need the following information to configure the script:

- API Token: Your Clockify API token. You can find this in your Clockify account settings.
- Workspace ID: The ID of the workspace where you want to retrieve time entries.
- User ID: The ID of the user whose time entries you are interested in.

## Modify the Script
Open the main.py in a text editor.
Update the following constants with your API credentials:
  ```python
  API_TOKEN = 'your_api_token_here'
  WORKSPACE_ID = 'your_workspace_id_here'
  USER_ID = 'your_user_id_here'
  ```
You may also update your time zone to get exact ending time of your tasks:
  ```python
  LOCAL_TIMEZONE = pytz.timezone('Europe/Kyiv')
  ```

## Usage
### Run the Script:
To run the script, navigate to the directory containing the script and execute the following command:
``` bash
python main.py
```
### Example Output: 
If successful, the script will output a report like this:
```plaintext
Summary Report:

Date: 2024-09-06
        Task: Task1
        - Completed at: 15:25:25
        - Time spent: 0:01:25
        ---
        Task: Task2
        - Completed at: 15:25:31
        - Time spent: 0:20:31
        ---
```
### Error Handling:
If there’s an issue with the request, such as an incorrect API token or user/workspace ID, an error message with the status code will be printed:
```plaintext
Error for getting data: 401
```

## Troubleshooting
- 401 Unauthorized: Double-check your API token. If it's invalid, Clockify will reject the request.
- 404 Not Found: Verify that the Workspace ID and User ID are correct.
- 500 Server Error: This might be an issue on the API side. Try again later or check the Clockify status page.

## Contact
For any issues or questions, feel free to contact me at [icecoldwhoa@gmail.com].



