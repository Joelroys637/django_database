import os, json
from firebase_admin import credentials, initialize_app

# Initialize Firebase only once
if not firebase_admin._apps:
    cred_dict = json.loads(os.environ["FIREBASE_CREDENTIALS"])
    cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")# path to your JSON
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://django-eebe7-default-rtdb.firebaseio.com"  # Replace with your DB URL
    })
