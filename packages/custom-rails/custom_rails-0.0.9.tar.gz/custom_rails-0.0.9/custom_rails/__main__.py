from argparse import ArgumentParser

from custom_rails import make_app, start_app

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="custom_rails",
        description="A command-line interface used for developing Rails-like web applications using Python and PyScript",
    )
    parser.add_argument("command", choices=["new", "start"])

    args = parser.parse_args()
    if args.command == "new":
        print("new")
        make_app()
        #copy_folder_contents("./custom_rails/templates")
    elif args.command == "start":
        print("start")
        start_app()