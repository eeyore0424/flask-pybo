from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xb0\xb5\xbc\x12\x84\xd8]\x01\x8dF\xe4\xa3\xec\xb8(\xcb'