import os
import random
from dotenv import load_dotenv, set_key
from urllib.parse import unquote
import requests


class EmailnatorError(Exception):
    pass


class EnvManager:
    """
    EnvManager is a class that handles interactions with environment variables
    and the .env file.
    """
    def __init__(self, env_path=None):
        self.env_path = env_path or os.path.dirname(os.path.abspath(__file__))
        self.dotenv_path = os.path.join(self.env_path, ".env")
        load_dotenv(self.dotenv_path)

    def get(self, key):
        """
        Get the value of an environment variable.

        key (str): The name of the environment variable.

        Returns:
            str: The value of the environment variable.
        """
        return os.getenv(key)

    def set(self, key, value):
        """
        Set the value of an environment variable in the .env file.

        key (str): The name of the environment variable.
        value (str): The value to set for the environment variable.
        """
        set_key(self.dotenv_path, key, value)


class Emailnator:
    """
    Emailnator is a class that interacts with the Emailnator API to generate and manage temporary email addresses.
    """

    def __init__(self, env_path=None):
        """
        Initialize the Emailnator class.

        env_path (str, optional): The path to the .env file. Defaults to the current directory.
        """
        self.env_manager = EnvManager(env_path)

        self.email = self.env_manager.get("EMAIL")
        self.xsrf_token = self.env_manager.get("XSRF_TOKEN")
        self.gmailnator_session = self.env_manager.get("GMAILNATOR_SESSION")
        self.base_url = "https://www.emailnator.com"

        if not (self.xsrf_token and self.gmailnator_session):
            self.xsrf_token, self.gmailnator_session = self.get_authentication_tokens()
            self.env_manager.set("XSRF_TOKEN", self.xsrf_token)
            self.env_manager.set("GMAILNATOR_SESSION", self.gmailnator_session)

        self.headers = {
            "Content-Type": "application/json",
            "Cookie": f"XSRF-TOKEN={self.xsrf_token}; gmailnator_session={self.gmailnator_session}",
            "X-XSRF-TOKEN": unquote(self.xsrf_token)
        }

    def get_authentication_tokens(self):
        """
        Fetch and return the authentication tokens (XSRF-TOKEN and gmailnator_session) from the Emailnator API.

        Returns:
            tuple: A tuple containing the XSRF-TOKEN and gmailnator_session.

        Raises:
            EmailnatorError: If the authentication tokens are not found in the response cookies or there's an unexpected status code.
        """
        url = self.base_url
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            xsrf_token = response.cookies.get("XSRF-TOKEN")
            gmailnator_session = response.cookies.get("gmailnator_session")
            if xsrf_token and gmailnator_session:
                return xsrf_token, gmailnator_session
            else:
                raise EmailnatorError("Authentication tokens not found in the response cookies")
        else:
            raise EmailnatorError(f"Unexpected status code: {response.status_code}")

        
    def _handle_response(self, response):
        """
        Handle the response from the Emailnator API by checking the status code and returning the JSON data if successful.

        response (requests.Response): The response object from the API request.

        Returns:
            dict: The JSON data from the response.

        Raises:
            EmailnatorError: If the response status code is not 200.
        """
        if response.status_code != 200:
            raise EmailnatorError(f"Error: {response.status_code}: {response.text}")
        return response.json()

    def generate_email(self, options=None):
        """
        Generate Email
        
        options (Array): ["domain", "plusGmail", "dotGmail"]
        """
        
        valid_options = ["domain", "plusGmail", "dotGmail"]
        
        if options is None:
            options = [random.choice(valid_options)]
        else:
            if not all(option in valid_options for option in options):
                raise EmailnatorError("Invalid input: options should be a list containing valid option strings.")


        url = f"{self.base_url}/generate-email"
        payload = {"email": options}
        response = requests.post(url, json=payload, headers=self.headers)
        json_data = self._handle_response(response)

        self.email = json_data["email"][0]
        self.env_manager.set("EMAIL", self.email)

        return json_data

    def inbox(self, email):
        """
        Retrieve Inbox

        email: Email address
        """
        if not isinstance(email, str):
            raise EmailnatorError("Invalid input: email should be a string.")

        url = f"{self.base_url}/message-list"
        payload = {"email": email}
        response = requests.post(url, json=payload, headers=self.headers)
        return self._handle_response(response)

    def get_message(self, email, message_id):
        """
        Get Message

        email: Email address
        message_id: Message ID
        """
        if not isinstance(email, str):
            raise EmailnatorError("Invalid input: email should be a string.")

        if not isinstance(message_id, str):
            raise EmailnatorError("Invalid input: message_id should be a string.")

        url = f"{self.base_url}/message-list"
        payload = {"email": email, "messageID": message_id}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.text

    
    def get_existing_email(self):
        """
        Get the existing generated email from the .env file, if available.

        Returns:
            str: The existing email, or None if no email exists in the .env file.
        """
        return self.email
