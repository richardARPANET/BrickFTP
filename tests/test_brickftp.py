from pathlib import Path
import os
from uuid import uuid4
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
        yield client
        paths = (i['path'] for i in client.dir(BASE_DIR))
        for path in paths:
            client.delete(path)

    def test_thing(self, brickftp):
        # create subdir
        remote_subdir_path = Path(BASE_DIR, str(uuid4()))
        brickftp.mkdir(remote_subdir_path)
        # check it worked
        brickftp.dir(remote_subdir_path)
        # upload a file to it
        remote_subsubdir_path = str(Path(remote_subdir_path, str(uuid4())))
        brickftp.mkdir(remote_subsubdir_path)
        filename = f'my_test_file{uuid4()}'
        brickftp.upload(
            upload_path=Path(remote_subsubdir_path, filename),
            local_path=Path(__file__),
            encoding='latin-1'
        )
