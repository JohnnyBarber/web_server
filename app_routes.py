from flask import Blueprint, redirect, render_template
import datetime
import pandas as pd

app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/', methods=['GET'])
def welcome():
    return redirect('http://localhost:8080/index')


@app_routes.route('/index')
def index():
    return render_template('home/index.html', segment='index')


@app_routes.route('/callback', methods=['GET', 'POST'])
def callback():
    return get('00001','2021-6-28', '2022-6-27')


def get(code, start, end, url='https://www.hkexnews.hk/sdw/search/searchsdw.aspx'):
    days = end - start
    db = pd.DataFrame(columns=['date', 'shareholding'])
    for i in range(days):
        current = start + datetime.timedelta(days=i)
