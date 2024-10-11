#!/usr/local/bin/python
import os
import argparse
from pathlib import Path
import yaml
import streamlit as st
from streamlit import runtime
from streamlit.web import cli
from streamlit_option_menu import option_menu

# Import the functions directly
from experience import experience
from about_me import about_me

### Set layout page to wide
st.set_page_config(layout="wide")

DEFAULT_PORTFOLIO_PATH = (
    Path(__file__).resolve().parent.parent / "info" / "portfolio.yml"
)

def app(source):
    portfolio = yaml.load(source.open(), Loader=yaml.BaseLoader)
    if "About Me":
        about_me(portfolio.get("about_me"), source_path=source.parent)
    elif "Experience":
        # Call the experience function directly
        experience(portfolio.get("experience"))


def main():
    parser = argparse.ArgumentParser(
        prog="Matheus Brandão - Portfolio",
        description="Matheus Brandão - portfolio",
        epilog="Brought to you by youngpada1 :heart:",
    )

    parser.add_argument(
        "portfolio", type=Path, help="Path to the YAML portfolio file", nargs="?"
    )
    args = parser.parse_args()

    if args.portfolio is None:
        portfolio = Path(os.environ.get("PORTFOLIO_PATH", DEFAULT_PORTFOLIO_PATH))
    else:
        portfolio = args.portfolio

    if runtime.exists():
        app(portfolio)
    else:
        import sys

        sys.argv = [
            "streamlit",
            "run",
            __file__,
            "--server.headless=true",
            "--server.enableXsrfProtection=false",
            "--server.enableCORS=false",
            str(portfolio),
        ]
        st.write("Relaunching...")
        sys.exit(cli.main())


if __name__ == "__main__":
    main()
