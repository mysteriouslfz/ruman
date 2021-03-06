#!/usr/bin/env python
#encoding: utf-8

from flask import Flask, render_template, request, jsonify, Blueprint, send_from_directory, url_for, session
from ruman.db import *
from . import index
import json
from ruman.config import *

from ruman.es import *

@index.route('/lieDetail/')
def lieDetail():
    return render_template('index/lieDetail.html')

@index.route('/setDetail/')
def setDetail():
    stock = request.args.get('stock','')
    id = request.args.get('id','')
    manipulate_type_num = request.args.get('manipulate_type_num','')
    return render_template('index/setDetail.html',stock=stock,id=id,manipulate_type_num=manipulate_type_num)

@index.route('/hotDetail/')
def hotDetail():
    id = request.args.get('id','')
    return render_template('index/hotDetail.html',id=id)

@index.route('/hotweiboDetail/')
def hotweiboDetail():
    # stock = request.args.get('stock','')
    # id = request.args.get('id','')
    return render_template('index/hotweiboDetail.html')

@index.route('/test/')
def test():
    result = 'Hello World!'
    return json.dumps(result,ensure_ascii=False)

