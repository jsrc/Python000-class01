from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# 实例化
app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy()
# 绑定db
db.init_app(app)

# 注册蓝图
from .home import home as home_blueprint
app.register_blueprint(home_blueprint)



