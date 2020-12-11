#-*-coding:utf-8-*-
#1.导入Flask扩展
from flask import Flask

#2.创建Flask应用程序实现
app = Flask(__name__)

#定义路由及视图函数
#Flask中定义路由是通过装饰器实现的
#路由默认只支持GET，如果需要增加，需要自行指定
@app.route("/",methods=['GET','POST'])
def index():
    return "Hello Flask"
#4.启动程序
if __name__ == '__main__':
#执行了app.run,就会将Flask程序运行在一个简易服务器（Flask提供，用于测试）
    app.run()