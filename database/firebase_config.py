import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(json.loads(os.environ["FIREBASE_CREDENTIALS"]))  # path to your JSON
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://django-eebe7-default-rtdb.firebaseio.com"  # Replace with your DB URL
    })
