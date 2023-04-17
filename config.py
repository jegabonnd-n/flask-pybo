import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# URI는 주로 local에서 사용하는 개념(이름)
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 이벤트에 관련된 내용은 막아둠.
SECRET_KEY = "dev"