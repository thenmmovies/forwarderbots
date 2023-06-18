from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "6043062672:AAH76W9fh5Iw6KSN8epvG_2GETas94EAeZI"  # Your bot API key
    OWNER_ID = "1224313313" # Your user id

    # Make sure to include the '-' sign in group and channel ids.
     FROM_CHATS = [-1001862773794]  # List of chat id's to forward messages from
    TO_CHATS = [-1001982159948]  # List of chat id's to forward messages to


    REMOVE_TAG = False
    WORKERS = 4
