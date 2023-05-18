from flask import Flask, session, render_template, make_response, jsonify, request, redirect, url_for

import cx_Oracle

import random
app = Flask(__name__)
app.secret_key ='111222'

@app.route('/')
def index():
    tel = str(random.randint) + str(random.randint)
    session['my_key_tel'] = tel
    render_template('index.html')

@app.route('/menu')
def menu():
    conn = cx_Oracle.connect('ai','0000','localhost:1521/XE')
    cur = conn.cursor()
    sql = 'select GOOD_SEQ,GOOD_NAME,GOOD_IMG,GOOD_PRICE,GOOD_DESC from kio_goods order by reg_date desc'
    cur.execute(sql)
    menu_list_dict = []
    for row in cur:
        dic = {}
        dic.GOOD_SEQ = row[0]
        dic.GOOD_NAME = row[1]
        dic.GOOD_IMG = row[2]
        dic.GOOD_PRICE = row[3]
        dic.GOOD_DESC = row[4]
        menu_list_dict.append(dic)


