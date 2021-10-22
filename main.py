import logging
import sys

from app.client import Client
from app.store import Store

LOG = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, format='[%(levelname)s] %(message)s', level=logging.INFO)

if __name__ == '__main__':
    LOG.info("Starting Store application...")
    print("\n~~~ Welcome to the online store ~~~")
    store = Store('./files/store.txt', 47)

    client = Client(store)
    client.select_options()
