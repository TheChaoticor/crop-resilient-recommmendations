# auth_setup.py

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def setup_authentication():
    # Load the configuration file
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Pre-hash passwords if necessary
    # Uncomment the following line if you want to pre-hash passwords
    # config['credentials'] = stauth.Hasher.hash_passwords(config['credentials'])

    # Initialize the authenticator
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized'],
        auto_hash=True  # Set to False if passwords are pre-hashed
    )

    return authenticator
