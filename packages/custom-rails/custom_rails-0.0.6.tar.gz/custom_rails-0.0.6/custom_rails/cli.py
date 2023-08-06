import argparse
from . import make_app, start_app

def main():
    parser = argparse.ArgumentParser(description="A command-line interface for custom_rails package")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    new_parser = subparsers.add_parser("new", help="Create a new custom_rails app")
    new_parser.set_defaults(func=make_app)

    start_parser = subparsers.add_parser("start", help="Start the custom_rails app")
    start_parser.set_defaults(func=start_app)

    args = parser.parse_args()
    args.func()
