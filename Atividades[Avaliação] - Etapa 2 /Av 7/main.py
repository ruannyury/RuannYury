from app import create_app
from app.views import instanciar

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    instanciar()
