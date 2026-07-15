from pathlib import Path
import tomllib

CONFIG_FILE = Path("../config/config.toml")
PORTFOLIO_DIR = Path("../data/portfolios")

divider = "=" * 60

print(divider)
print("DIVAGG :: SWITCH PORTFOLIO")
print(divider)

#
# Load Current Config
#

with open(CONFIG_FILE, "rb") as config_file:
    config = tomllib.load(config_file)

current_portfolio = (
    config["engine"]["active_portfolio"]
)

#
# Find Portfolios
#

portfolios = sorted(
    [
        file.stem
        for file in PORTFOLIO_DIR.glob("*.csv")
    ]
)

if not portfolios:

    print("\n[ERROR] No portfolios found.")
    raise SystemExit(1)

print(f"\nCURRENT PORTFOLIO : {current_portfolio}")

print("\nAVAILABLE PORTFOLIOS:\n")

for index, portfolio in enumerate(portfolios, start=1):

    print(f"{index}. {portfolio}")

selection = input(
    "\nSelect portfolio number : "
).strip()

try:

    selection_index = int(selection) - 1

    if (
        selection_index < 0 or
        selection_index >= len(portfolios)
    ):
        raise ValueError

except Exception:

    print("\n[ERROR] Invalid selection.")
    raise SystemExit(1)

selected_portfolio = portfolios[selection_index]

#
# Rewrite Config
#

new_config = f"""[simulation]

annual_contribution = {config["simulation"]["annual_contribution"]}
dividend_growth_rate = {config["simulation"]["dividend_growth_rate"]}
years = {config["simulation"]["years"]}

[exports]

enable_txt_reports = true
enable_csv_exports = true

[engine]

currency_symbol = "{config["engine"]["currency_symbol"]}"
report_divider_length = {config["engine"]["report_divider_length"]}
active_portfolio = "{selected_portfolio}"
"""

with open(CONFIG_FILE, "w") as config_output:
    config_output.write(new_config)

print("\n[SUCCESS] Active portfolio switched.")
print(f"NEW ACTIVE PORTFOLIO : {selected_portfolio}")

print(f"\n{divider}")
print("END SWITCH")
print(divider)
