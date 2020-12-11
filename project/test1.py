#-*-coding:utf-8-*-
#1.����Flask��չ
from flask import Flask

#2.����FlaskӦ�ó���ʵ��
app = Flask(__name__)

#����·�ɼ���ͼ����
#Flask�ж���·����ͨ��װ����ʵ�ֵ�
#·��Ĭ��ֻ֧��GET�������Ҫ���ӣ���Ҫ����ָ��
@app.route("/",methods=['GET','POST'])
def index():
    return "Hello Flask"
#4.��������

app.run()

