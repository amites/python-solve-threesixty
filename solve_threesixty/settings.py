SOLVE360_USER = "user@email.address"
SOLVE360_PASS = "API-KEY"
SOLVE360_SERVER = "secure.solve360.com"
SOLVE360_OWNERID = "id for default owner of new items"
DEBUG = False

try:
    from local_settings import *
except ImportError:
    pass
