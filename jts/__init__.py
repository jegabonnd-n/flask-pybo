from flask import Flask
from flask_migrate import Migrate # 연동시켜주는
from flask_sqlalchemy import SQLAlchemy # 실제 ORM에 연관된
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate() # SQL을 사용하기 위해 불러와서 연동시켜주는 역할

def create_app():
    app = Flask(__name__) # Flask Class를 app이라는 객체로 지정
    # app.py 가 main이다.
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    
    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    # @app.route('/') # @: 어노테이션, Flask 객체가 갖고있는 route라는 함수: 경로를 지정해주는 함수
    # # c:\projects\myproject\ 를 말하는 것이며, * Running on http://127.0.0.1:5000 이 주소를 말하는 경로다.
    # # 이전 경로로 빠져나갈 수 없다.
    # def hello_pybo():
    #     return 'Hello, Pybo!'
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app

# 경로는 두 가지가 있는데,
# 경로 1. local 경로
# 경로 2. url 경로: route()는 url 경로임

# * Running on http://127.0.0.1:5000
# Flask server가 사용 중인 주소
