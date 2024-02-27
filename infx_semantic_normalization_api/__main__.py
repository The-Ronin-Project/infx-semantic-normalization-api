import argparse
import sys

import waitress

from .app import create_app

parser = argparse.ArgumentParser(
    description=f"Run infx-semantic-normalization-api: {sys.argv[0]}"
)
args: argparse.Namespace = parser.parse_args()


def main():
    app = create_app()
    waitress.serve(app=app, port=8000, threads=8, host="0.0.0.0")


if __name__ == "__main__":
    main()
