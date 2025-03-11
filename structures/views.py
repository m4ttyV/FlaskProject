from flask import Blueprint, render_template
from structures.models import get_all_buildings
from app import app
views = Blueprint('views', __name__)

@views.route('/')
@app.route('/')
def index():

    [buildings_head, buildings_body] = get_all_buildings()

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html
