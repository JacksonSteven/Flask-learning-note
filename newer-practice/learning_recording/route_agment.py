#-*-coding:utf-8-*-
#1.����Flask��չ
from flask import Flask

#2.����FlaskӦ�ó���ʵ��
app = Flask(__name__)

#3.����·�ɼ���ͼ����
#Flask�ж���·����ͨ��װ����ʵ�ֵ�
#·��Ĭ��ֻ֧��GET�������Ҫ���ӣ���Ҫ����ָ��
@app.route("/",methods=['GET','POST'])
def index():
    return "Hello Flask"
#ʹ��ͬһ����ͼ����������ʾ��ͬ�û��Ķ�����Ϣ��
#<>����·�ɵĲ�����<>����Ҫ�������
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):

    #�������ͣ�Ĭ�����ַ�����unicode
    print(type(order_id))
    #�е�ʱ����Ҫ��·���������Ż�������IDӦ����int����
    return 'order_id %s' %order_id
    #��Ҫ����ͼ�����ģ������������������ô����Ĵ��������
#4.��������
if __name__ == '__main__':
#ִ����app.run,�ͻὫFlask����������һ�����׷�������Flask�ṩ�����ڲ��ԣ�
    app.run()