from apps.plot import blueprint
from flask import render_template, request
from jinja2 import TemplateNotFound
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

fig = plt.figure()
ax = fig.subplots()
ax.plot([1, 2])
buf = BytesIO()
fig.savefig(buf, format="png")
data = base64.b64encode(buf.getbuffer()).decode("ascii")

@blueprint.route('/dashboard')
def route_template():

    try:
        template = 'dashboard.html'

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, stock_name='Test Stock', user_image=f'data:image/png;base64,{data}')

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500