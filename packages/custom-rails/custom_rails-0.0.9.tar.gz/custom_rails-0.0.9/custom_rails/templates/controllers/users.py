"""
Simple example
"""

from custom_rails.app import App
from custom_rails.router import Path
from custom_rails.response import HttpResponse, RenderResponse, JsonResponse, JinjaResponse
from custom_rails.db import Db
from helpers import my_helper


def index(request):
    model = Db("users")

    random_number = my_helper.generate_random_int(1, 10)
    vars = {
        'title': 'Users',
        'body': 'Welcome!!!!',
        'random': random_number,
        'elems': model.get_all()
    }
    print(vars['elems'])
    return JinjaResponse(request, "users.html.jinja2", vars)

def json_point(request):
    
    data = [{'hello': 'hi', 'there':'me'},
    {'name': 'John', 'age': 15},
    {'name': 'Ama', 'age': 18},
    {'name': 'Someone', 'age': 20},

    ]
    return JsonResponse(request,data)

def form(request):
    
    return HttpResponse(request,"""
    <html>
    <body>
    <form method="post" action="", enctype="multipart/form-data">

    <input type="file" id="age" name="age" value="age">
    <input type="submit" value="submit">
    </form>

    </body>
    </html>
    """)

