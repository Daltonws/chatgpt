import requests
import json

def get_chat_response(stored_procedure, api_key):
    """
    Sends a modified stored procedure input to the OpenAI Azure model to request a BRD and retrieves the response.
    
    Parameters:
    - stored_procedure (str): The stored procedure input from the user.
    - api_key (str): The API key for authenticating with the OpenAI API.

    Returns:
    - str: The generated BRD from the Azure model.
    """
    # Updated URL for the OpenAI API endpoint (Azure)
    url = "https://acam-int-demo.openai.azure.com/"

    # Predefined request phrase for BRD generation
    brd_request = "Generate a Business Requirements Document for the following Insurance Stored Procedure:"

    full_message = brd_request + "\n" + stored_procedure 

    # Setting up the headers for the API request, including the authorization token
    headers = {
        "Authorization": f"Bearer {api_key}",  # Updated API key
        "Content-Type": "application/json"
    }

    # Updated model identifier
    data = {
        "model": "apt-35-turbo",  # Updated model name
        "messages": [{"role": "user", "content": full_message}],
        "temperature": 0.3
    }

    # Making the POST request to the API and handling the response
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # Successfully received response, return the content
        return response.json()['choices'][0]['message']['content']
    else:
        # Handling errors and returning error message
        return f"Error: {response.text}"


def get_multiline_input(prompt):
    """
    Captures and returns multi-line user input, ending when the user types 'END'.
    
    Parameters:
    - prompt (str): The prompt message displayed to the user.

    Returns:
    - str: The concatenated user input as a single string.
    """
    print(prompt)
    lines = []
    while True:
        line = input()
        # Check for the 'END' keyword to stop input capture
        if line.lower() == 'end':
            break
        lines.append(line)
    # Joining all input lines into a single string
    return '\n'.join(lines)

def main():
    """
    Main function to run the chatbot interface for generating a BRD.
    """
    # API key for OpenAI (Note: Securely manage the API key in production)
    #OPENAI_API_KEY = "de58119df4904cdb8ae17f150175edb7"
    OPENAI_API_KEY =  "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"

    print("Azure: Hi, I am a chatbot. I will be assisting you on generating a business requirement document using your stored procedure.")
    while True:
        # Capturing the user's stored procedure input
        user_input = get_multiline_input("Please enter your insurance stored procedure (type 'END' on a new line when done):") #
        if user_input.lower() == 'exit':
            # Exiting the loop if the user types 'exit'
            break
        # Generating the BRD based on the stored procedure input
        response = get_chat_response(user_input, OPENAI_API_KEY)
        print(f"Azure: {response}")

if __name__ == "__main__":
    main()
