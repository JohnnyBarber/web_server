from flask_admin import BaseView, expose


class Http500(BaseView):
    @expose('/')
    def index(self):
        return self.render('handler/http_500.html')

    def is_accessible(self):
        return True

    def is_visible(self):
        return False