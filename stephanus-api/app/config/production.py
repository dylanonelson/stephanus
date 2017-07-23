import os

DEBUG=False
MAXIMUM_STEPHANUS_PAGE='354c'
MINIMUM_STEPHANUS_PAGE='327a'
MONGO_URL=f"mongodb://{os.environ['MONGO_USER']}:{os.environ['MONGO_PW']}@ds119103-a0.mlab.com:19103,ds119103-a1.mlab.com:19103/stephanus?replicaSet=rs-ds119103"
MONGO_DB_NAME='stephanus'
