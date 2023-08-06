# Emailnator

Emailnator is a Python wrapper for the Emailnator temporary email service. It provides a convenient way to generate temporary email addresses, retrieve inbox messages, and fetch individual messages.

## Installation

To install the Emailnator package, simply run:

```bash
pip install emailnator
```

## TODO

- [ ] Exapand temporary email service providers
  - [ ] https://mail.tm/
  - [ ] https://temp-mail.org/
  - [ ] https://tempmailo.com/
  - [ ] https://www.disposablemail.com/
  - [ ] https://internxt.com/en/temporary-email/
  - [ ] https://temp-mail.io/
  - [ ] https://getnada.com/
  - [ ] https://www.fakemail.net/
  - [x] https://www.emailnator.com/
- [ ] CLI to get an email and inbox of the email in from the terminal
- [ ] Add Logging 
- [ ] Expand the errors for better event capture
- [ ] Add a proxy?

To install the Emailnator package for development purposes, follow these steps:

1. Clone the repository to your local machine using the command:

```bash
git clone https://github.com/repollo/Emailnator.git
```

2. Navigate to the cloned repository directory:

```bash
cd Emailnator
```

3. Create a virtual environment for the project:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

Note: If you are using Windows, use the following command instead:

```bash
venv\Scripts\activate
```

5. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

6. Install the package in development mode:

```bash
pip install -e .
```

This will install the package in editable mode, allowing you to modify the source code and see the changes reflected immediately.


## Usage

First, import the `Emailnator` class:

```python
from emailnator import Emailnator
```

Then, create an `Emailnator` instance:

```python
emailnator = Emailnator()
```

By default, the `.env` file containing authentication tokens will be created in the same directory as the `emailnator.py` file. You can specify a custom directory using the `env_path` parameter:

```python
custom_path = "/path/to/your/custom/directory"
emailnator = Emailnator(env_path=custom_path)
```

### Generate a temporary email address

```python
email_data = emailnator.generate_email()
email_address = email_data["email"][0]
print(email_address)
```

### Retrieve inbox messages

```python
inbox_data = emailnator.inbox(email_address)
print(inbox_data)
```

### Get a specific message

```python
message_id = inbox_data["messageData"][3]["messageID"]
message_data = emailnator.get_message(email_address, message_id)
print(message_data)
```

### Example

```python
from emailnator import Emailnator

emailnator = Emailnator()

# Generate an email
email_data = emailnator.generate_email()
email = email_data["email"][0]

# Get existing email if generated before.
email = emailnator.get_existing_email()

# Get email inbox of email
emails = emailnator.inbox(email)

# Select a specific email message id
message_id = emails["messageData"][1]["messageID"]
    
# Get the email message id contents
email_content = emailnator.get_message(email, message_id)

```

## License

This project is licensed under the MIT License.