from datetime import datetime
import tomllib

CONFIG_FILE = "../config/config.toml"

with open(CONFIG_FILE, "rb") as config_file:
    config = tomllib.load(config_file)

annual_contribution = config["simulation"]["annual_contribution"]
dividend_growth_rate = config["simulation"]["dividend_growth_rate"]
years = config["simulation"]["years"]

currency_symbol = config["engine"]["currency_symbol"]
divider_length = config["engine"]["report_divider_length"]

divider = "=" * divider_length

monthly_income = 76.08
yearly_income = monthly_income * 12

current_yearly_income = yearly_income

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

simulation_path = (
    f"../simulations/"
    f"simulation_{timestamp}.txt"
)

lines = []

header = [
    divider,
    "DIVAGG :: PORTFOLIO GROWTH SIMULATION",
    divider,
    "",
    f"STARTING YEARLY DIVIDEND : "
    f"{currency_symbol}{yearly_income:,.2f}",

    f"ANNUAL CONTRIBUTION      : "
    f"{currency_symbol}{annual_contribution:,.2f}",

    f"DIVIDEND GROWTH RATE     : "
    f"{dividend_growth_rate * 100:.2f}%",

    f"SIMULATION YEARS         : "
    f"{years}",

    "",
    divider
]

for line in header:
    print(line)
    lines.append(line)

for year in range(1, years + 1):

    current_yearly_income += (
        current_yearly_income * dividend_growth_rate
    )

    contribution_growth = (
        annual_contribution * dividend_growth_rate
    )

    current_yearly_income += contribution_growth

    yearly_line = (
        f"YEAR {year:<3}"
        f"PROJECTED YEARLY DIVIDEND : "
        f"{currency_symbol}"
        f"{current_yearly_income:,.2f}"
    )

    print(yearly_line)
    lines.append(yearly_line)

footer = [
    "",
    divider,
    "END OF SIMULATION",
    divider
]

for line in footer:
    print(line)
    lines.append(line)

with open(simulation_path, "w") as sim_file:
    sim_file.write("\n".join(lines))

print(f"\n[INFO] Simulation exported:")
print(simulation_path)
