import os, json
from firebase_admin import credentials, initialize_app

# Load JSON from environment variable
cred_dict = json.loads(os.environ["FIREBASE_CREDENTIALS"])

# Replace escaped newlines with real newlines
cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")

# Initialize Firebase
cred = credentials.Certificate(cred_dict)
initialize_app(cred, {
    "databaseURL": "https://django-eebe7-default-rtdb.firebaseio.com"
})
