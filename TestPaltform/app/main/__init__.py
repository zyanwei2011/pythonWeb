
from flask import Blueprint, request

main = Blueprint('main', __name__, url_prefix='/main')

from .views.index import index
from .views.projects import project_create, project_list, project_edit
from .views.modules import create_modules, list_modules
from .views.suites import create_suites, list_suites
from .views.cases import create_cases, list_cases




