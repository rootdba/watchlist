#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
File Name：app.py
Author: mahongliang
Mail: mahongliang@139.com
Date：2020/8/24 15:29
"""
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


import os
import sys
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
name = 'Grey Li'
movies = [
    {'title':'My Neighbor Totoro','year':'1988'},
    {'title':'Dead Poest Society','year':'1822'},
]

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #主键
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20)) #标题
    year = db.Column(db.String(4))  #年份

#自定义initdb 自动创建数据库表操作
import click
@app.cli.command()   #注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:    #判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database')  #输出提示信息

import click
@app.cli.command()
def forge():
    db.create_all()
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('导入完成')