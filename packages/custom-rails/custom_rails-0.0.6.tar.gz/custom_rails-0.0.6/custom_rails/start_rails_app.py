import os
import json
import inspect
import importlib.util
from custom_rails.router import Path
from wsgiref.simple_server import make_server
from custom_rails.response import HttpResponse, RenderResponse, JsonResponse, JinjaResponse

from custom_rails.db import Db

from custom_rails.app import App

from helpers import my_helper

import os
import glob
import importlib

# set the path to the folder containing the modules
module_path = "./db_models"

module_files = glob.glob(module_path + "/*.py")

# loop through the module files and import each module
for module_file in module_files:
    # remove the path and file extension to get the module name
    module_name = module_file.split("/")[-1][:-3]
    module_name = f"{module_path.replace('./', '')}.{module_name}"
    print(module_name)
    # import the module dynamically using importlib
    module = importlib.import_module(module_name)
    globals().update(vars(module))

module_path = "./helpers"

module_files = glob.glob(module_path + "/*.py")

# loop through the module files and import each module
for module_file in module_files:
    # remove the path and file extension to get the module name
    module_name = module_file.split("/")[-1][:-3]
    module_name = f"{module_path.replace('./', '')}.{module_name}"
    print(module_name)
    # import the module dynamically using importlib
    module = importlib.import_module(module_name)
    globals().update(vars(module))


def start_rails():
  # set the directory path
  Db("users").print_db_structure("schema.txt")
  dir_path = 'controllers'

  # get all the filenames in the directory
  filenames = os.listdir(dir_path)

  the_rsp = None


  routes = [
      #Path('/', print_received),
      #Path('/json/', json_point),
      #Path('/form/', form),
  ]
  cnt = 0
  # print the filenames
  for filename in filenames:
      if filename.endswith('.py'):
          # get the module name
          module_name = filename[:-3]
          # import os.path.join(dir_path, filename)
          path = os.path.join(dir_path, filename)

          content = None
          with open(path, 'rb') as f:
            content = f.read()
          content = content.decode('utf-8')
          
          content = content.split("def ")
          vf = 0
          for elem in content:
            if vf == 0:
              vf = 1
              continue

            cnt = cnt + 1
            name = elem.split("(")[0]
            fct = "def " + elem
            the_rsp = None
            the_request = None
            fct =  fct + "\nprint(request)\nthe_rsp = " + name + "(request)\nprint(the_rsp)"
            print(fct)
            current_fct = fct
            def aux_fct(request, fct = current_fct): 
              print(fct)
              the_rsp = None
              the_locals = {'request': request}
              exec(fct, globals(), the_locals )
              the_rsp = the_locals.get('the_rsp')
              return the_rsp
            print("/" + module_name + "/" + name)
            routes = routes + [Path("/" + module_name + "/" + name, aux_fct)]

  def default_path(request):
    return HttpResponse(request,"""
    <html>
    <body>
    Welcome!!!
    </body>
    </html>
    """)
  routes = routes + [Path("/", default_path)]

  print(routes)

  route_names = []
  for route in routes:
      route_names.append(route.path)

  with open('routes.txt', 'w') as f:
      f.write('\n'.join(route_names))

  app = App()
  app.set_static('/static/', '.')

  app.set_routes(routes)

  server = make_server('127.0.0.1', 3000, app)
  server.serve_forever()
