from pathlib import Path
import os
from json.decoder import JSONDecodeError

from requests.exceptions import RequestException
import pytest

from brickftp import BrickFTP, BrickFTPError

BRICK_FTP_USER = os.environ['BRICK_FTP_USER']
BRICK_FTP_PASS = os.environ['BRICK_FTP_PASS']
BRICK_FTP_SUBDOMAIN = os.environ['BRICK_FTP_SUBDOMAIN']
HERE = Path(__file__).parent
BASE_DIR = 'Test Folder 2'


class TestThing:

    @pytest.fixture(scope='module')
    def brickftp(self):
        client = BrickFTP(
            username=BRICK_FTP_USER,
            password=BRICK_FTP_PASS,
            subdomain=BRICK_FTP_SUBDOMAIN,
        )
        paths = (i['path'] for i in client.dir(BASE_DIR))
        for path in paths:
            client.delete(path)
        yield client

    def test_something(self):
        pass
