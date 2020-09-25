import re
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sys
from ewords import app
from functools import wraps
from ewords.models.entries import Entry
from flask_table import Table, Col
from sqlalchemy.sql import func

class ItemTable(Table):
    no = Col('no')
    english = Col('English')

@app.route('/', methods=['GET', 'POST'])
def show_page():
    # qry = Entry.query(func.max(Entry.page).label("max_page"))
    # res = qry.one()
    # maxPage = res.max_page
    selPage = request.args.get('page', '')
    maxPage = app.config['MAX_PAGE']
    ipage = 1
    try:
        ipage = int(selPage)
        if ipage < 1:
            ipage = 1
        if ipage > int(maxPage):
            ipage = int(maxPage)
    except:
        ipage = 1
    items = Entry.query.filter(Entry.page == ipage).order_by(Entry.id.asc()).all()
    table = ItemTable(items)
    return render_template('entries/index.html', title='Ewords', table=table, maxPage=int(maxPage), page=ipage)


@app.route('/find/', methods=['GET', 'POST'])
def search_word():
    maxPage = app.config['MAX_PAGE']
    searchWord = request.args.get('word', '')
    ptn = re.compile("^.*" + searchWord + ".*$")
    items = Entry.query.filter().order_by(Entry.id.asc()).all()
    newList = []
    print(request.form.get('srchWord'))
    for item in items:
        m = ptn.match(item.english)
        if m:
            newList.append(item)
    table = ItemTable(newList)
    return render_template('entries/index.html', title='Ewords', table=table, maxPage=int(maxPage), page=1)
