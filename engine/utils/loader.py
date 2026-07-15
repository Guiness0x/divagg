from pathlib import Path
import tomllib

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

CONFIG_FILE = (
    BASE_DIR /
    "config" /
    "config.toml"
)

with open(CONFIG_FILE, "rb") as config_file:
    config = tomllib.load(config_file)

ACTIVE_PORTFOLIO = (
    config["engine"]["active_portfolio"]
)

PORTFOLIO_FILE = (
    BASE_DIR /
    "data" /
    "portfolios" /
    f"{ACTIVE_PORTFOLIO}.csv"
)
