from flask import Flask, redirect, request, g
from flask_login import current_user
from flask_admin import Admin, AdminIndexView
from admin.base_http_404 import Http404
from admin.base_http_500 import Http500
import time


def open_request():
    g.user = current_user
    g.start = int(time.time() * 1000)
    g.exception = None


def create_app(routes):
    app = Flask(__name__)
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.register_blueprint(routes, url_prefix='/')
    app.before_request(open_request)

    admin = Admin(name="Application",
                  url='/',
                  template_mode='bootstrap3',
                  index_view=AdminIndexView(
                      name=' ',
                      menu_icon_type='glyph',
                      menu_icon_value='glyphicon-home'
                  ))

    admin.init_app(app)
    admin.add_view(Http404(name='404'))
    admin.add_view(Http500(name='500'))

    app.template_context_processors[None].append(lambda: dict(
        app_name="App",
        app_long_name="Application",
        app_start='/welcome/',
        webenv='dev'
    ))

    return app
