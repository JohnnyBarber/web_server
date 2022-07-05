from flask_admin import BaseView, expose


class Http404(BaseView):
    @expose('/')
    def index(self):
        return self.render('handler/http_404.html')

    def is_accessible(self):
        return True

    def is_visible(self):
        return False
