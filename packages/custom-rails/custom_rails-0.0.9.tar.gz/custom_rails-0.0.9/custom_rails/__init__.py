
import shutil
from pkg_resources import resource_filename

def copy_folder_contents(src_folder):
    template_dir = resource_filename("custom_rails", "templates")
    dest_dir = os.getcwd()
    shutil.copytree(template_dir, dest_dir, dirs_exist_ok=True, copy_function=shutil.copy2)

def build_app():
    copy_folder_contents("./custom_rails/templates")


def make_app():
    print("okkkkkkk")
    build_app()

import os

cmd = "python3 main_app.py"

# Execute the command

def start_app():
    os.system(cmd)
