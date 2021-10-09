import logging
import sys

from app.store import Store

LOG = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, format='[%(levelname)s] %(message)s', level=logging.DEBUG)


if __name__ == '__main__':
    LOG.info("Starting Store application...")
    store = Store('./files/store.txt', 47)
    item = store.find_item('sweet potatoes')
