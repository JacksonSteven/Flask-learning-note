from flask import Flask, render_template

app = Flask(__name__)
# 1.使用Manager管理app对象
manager = Manager(app)

#2.如何返回一个网页（模板）
#3.如何给模板填充数据
@app.route('/')
def index():
    url_str = 'www.baidu.com'
    my_list = {1,3,5,7,9,}
    my_dict ={
        'name':'lilin',
        'url':'www.baidu.com'
    }

    return render_template('index.html',url_str = url_str,my_list = my_list,my_dict = my_dict)


if __name__ == '__main__':
    manager.run(debug = True)
