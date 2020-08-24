#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
File Name：app.py
Author: mahongliang
Mail: mahongliang@139.com
Date：2020/8/24 15:29
"""
from flask import Flask, url_for, render_template

app = Flask(__name__)
name = 'Grey Li'
movies = [
    {'title':'My Neighbor Totoro','year':'1988'},
    {'title':'Dead Poest Society','year':'1822'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/home')
@app.route('/abc')
def hello():
    return u"<h1>大苏打撒旦Welcome to </h1><hr>My Whatchlist!<img src='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'>"

@app.route('/user/<name>')
def user_page(name):
    #return 'User page'
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    #print(url_for(user_page))
    print(url_for('user_page', name='greyli'))
    return 'Test Page'
