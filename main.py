import logging
import sys
from flask import Flask

from app.client import Client
from app.store import Store

LOG = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, format='[%(levelname)s] %(message)s', level=logging.INFO)

app = Flask(__name__)

LOG.info("Starting Store application...")
store = Store('./files/store.txt', 47)


if __name__ == '__main__':
    print("\n~~~ Welcome to the online store ~~~")

    client = Client(store)
    client.select_options()
