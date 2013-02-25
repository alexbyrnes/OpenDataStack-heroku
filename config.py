import os
import urlparse

urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(os.environ.get('HEROKU_POSTGRESQL_IVORY_URL', 'postgres://nodatabasefound'))


DEBUG = True 
SERVER_NAME = '0.0.0.0'
SERVER_PORT = 80
DB_CONNECTION = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
METADATA_DB = 'metadb'
METADATA_COLLECTION = 'metadata'

