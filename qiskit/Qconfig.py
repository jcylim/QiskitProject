import os

# Replace 'None' with your own API token (put it within quotes)
# Optionally, you can set the environment variable IBMQE_API as decribed in the
# aforementioned note. NOTE: If you set your APItoken below, it will OVERRIDE the
# value of the environment variable.

APItoken = 'dcdb2d9414a625c1f57373c544add3711c78c3d7faf39397fe2c41887110e8b59caf81bcb2bc32714d936da41a261fea510f96df379afcbdfa9df6cc6bfe3829'

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

'''def update_token(token=None):
    """Update the APItoken.

       :param token: The API token.(optional argument)
              If thisis set, it must be a string. The default value is None
    """
    global APItoken

    # If a token is given as an argument, use it.
    if token:
        APItoken = token
    else:
        # First check if APItoken is already set. If so, just use it.
        if APItoken:
            # Do nothing. The APItoken will override
            pass
        else:
            APItoken = os.getenv("IBMQE_API")

    assert (APItoken not in (None, '') and type(APItoken) is str), "Please set up a valid API access token. See Qconfig.py."

# Update the APItoken
update_token()'''

if 'APItoken' not in locals():
     raise Exception('Please set up your access token. See Qconfig.py.')
