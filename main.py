import os
import pypiserver

BASE_DIR = os.path.dirname(__file__)

application = pypiserver.app(
    root=os.path.join(BASE_DIR, 'packages'),
    password_file=os.path.join(BASE_DIR, '.htpasswd')
)
