
from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/test')

from .views.index import index
from .views.projects import create_projects, list_projects
from .views.modules import create_modules, list_modules
from .views.suites import create_suites, list_suites
from .views.cases import create_cases, list_cases




