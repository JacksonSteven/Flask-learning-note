from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#设置连接数据库的url
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:381007875@127.0.0.1/flask_sql_demo'
#设置数据库追踪信息,压制警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#创建SQLAlchemy对象,读取app中配置信息
db = SQLAlchemy(app)
#定义角色模型(一方)
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    #设置关系属性,方便查询使用
    us = db.relationship('User', backref='role')
    #重写__repr__方法,方便查看对象输出内容
    def __repr__(self):
        return 'Role:%s'% self.name

#定义用户模型类(多方)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s'%self.name

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# 删除所有和db相关联的表
db.drop_all()
# 创建所有和db相关联的表
db.create_all()

# 创建测试数据
ro1 = Role(name='admin')
db.session.add(ro1)
db.session.commit()
# 再次插入一条数据
ro2 = Role(name='user')
db.session.add(ro2)
db.session.commit()
# 多条用户数据
us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
