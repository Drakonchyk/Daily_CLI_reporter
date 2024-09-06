import requests

# Define the API token for authentication with Clockify API
API_TOKEN = 'NjZkNTI5YzUtYmM2MC00Yzc2LWJhYmQtZDBjNDI3MzUzNDZh'
# The workspace ID where the time entries are stored
WORKSPACE_ID = '66daf458b714774bff4540fe'
# The user ID for which we are retrieving time entries
USER_ID = '66daf458b714774bff4540fd'
# Base URL for Clockify's API
BASE_URL = 'https://api.clockify.me/api/v1'

# Define headers to be used in the API request (API key and content type)
headers = {
    'X-Api-Key': API_TOKEN,  # API token for authentication
    'Content-Type': 'application/json'  # Specify JSON format for the API request/response
}

# Function to get time entries for a specific user in a workspace
def get_time_entries():
    # Construct the full API URL for retrieving time entries
    url = f'{BASE_URL}/workspaces/{WORKSPACE_ID}/user/{USER_ID}/time-entries'
    
    # Send a GET request to the API with the authentication headers
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python list/dictionary
        time_entries = response.json()
        return time_entries
    else:
        # Print an error message if the request fails and return None
        print(f"Error for getting data: {response.status_code}")
        return None

# Retrieve the time entries from the API
time_entries = get_time_entries()

# If time entries were successfully retrieved, loop through and print each entry
if time_entries:
    for entry in time_entries:
        # Print each time entry (it will be a dictionary containing details about the entry)
        print(f"Entry: {entry}")
