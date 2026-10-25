from __future__ import annotations

import argparse
import os

from .run import create


def launch(app_file: str = "app.py"):
    if not app_file.endswith(".py"):
        app_file += ".py"
    app_file = os.path.join(os.getcwd(), app_file)
    config_file = os.path.join(os.getcwd(), app_file + ".json")
    print("* Sketch will be saved to: ", app_file)
    create(app_file, config_file).launch()


def main():
    parser = argparse.ArgumentParser(
        description="Open Gradio Sketch, a visual editor for Gradio apps."
    )
    parser.add_argument(
        "app_file",
        nargs="?",
        default="app.py",
        help="Python file to generate (default: app.py)",
    )
    args = parser.parse_args()
    launch(args.app_file)
