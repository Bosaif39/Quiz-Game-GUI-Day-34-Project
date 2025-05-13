import requests

# Parameters for API request to get 10 true/false questions
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Send GET request to the Open Trivia DB API 
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

# Extract the list of questions from the 'results' field
question_data = data["results"]
