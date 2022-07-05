from admin.app import create_app
from app_routes import app_routes

app = create_app(app_routes)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)