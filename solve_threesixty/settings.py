# Create file local_settings.py on your PYTHONPATH to set SOLVE360 settings.
SOLVE360_USER = "user@email.address"
SOLVE360_PASS = "API-KEY"
SOLVE360_SERVER = "secure.solve360.com"
SOLVE360_OWNERID = "id for default owner of new items"


DEBUG = False

# TODO: update to use server .env

try:
    from local_settings import *
except ImportError:
    pass
