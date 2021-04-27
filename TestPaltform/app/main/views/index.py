
from app.main.views import main


@main.route('/')
def index():
    return 'Hello World'