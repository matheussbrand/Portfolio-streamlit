#!/usr/local/bin/python
import os
import argparse
from pathlib import Path
import yaml
import streamlit as st
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
    try:
        # Load the YAML file with safe_loader
        with source.open() as file:
            portfolio = yaml.safe_load(file)

        if portfolio is None:
            st.error("Failed to load portfolio data.")
            return

        # Check and display "About Me" section if available
        if "about_me" in portfolio:
            about_me(portfolio.get("about_me"), source_path=source.parent)
        else:
            st.warning("No 'About Me' section found in the portfolio.")

        # Check and display "Experience" section if available
        if "experience" in portfolio:
            experience(portfolio.get("experience"))
        else:
            st.warning("No 'Experience' section found in the portfolio.")

    except FileNotFoundError:
        st.error(f"Portfolio file not found: {source}")
    except yaml.YAMLError as e:
        st.error(f"Error parsing YAML file: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


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

    # If no argument is provided, fall back to default
    portfolio = args.portfolio or Path(
        os.environ.get("PORTFOLIO_PATH", DEFAULT_PORTFOLIO_PATH)
    )

    if portfolio.exists():
        app(portfolio)
    else:
        st.error(f"Portfolio file not found at {portfolio}")
        st.stop()


if __name__ == "__main__":
    main()
