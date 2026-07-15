from pathlib import Path

PORTFOLIO_DIR = Path("../data/portfolios")
REPORT_DIR = Path("../reports")
EXPORT_DIR = Path("../exports")
SNAPSHOT_DIR = Path("../snapshots")
SIMULATION_DIR = Path("../simulations")

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: DATASET INVENTORY")
print(divider)

#
# Dataset Counts
#

portfolio_files = sorted(
    PORTFOLIO_DIR.glob("*.csv")
)

report_files = sorted(
    REPORT_DIR.glob("*.txt")
)

export_files = sorted(
    EXPORT_DIR.glob("*")
)

snapshot_files = sorted(
    SNAPSHOT_DIR.glob("*.csv")
)

simulation_files = sorted(
    SIMULATION_DIR.glob("*.txt")
)

#
# Output
#

print("\nDATASET OVERVIEW:\n")

print(subdivider)

print(
    f"{'PORTFOLIOS':<25}"
    f"{len(portfolio_files)}"
)

print(
    f"{'REPORTS':<25}"
    f"{len(report_files)}"
)

print(
    f"{'EXPORTS':<25}"
    f"{len(export_files)}"
)

print(
    f"{'SNAPSHOTS':<25}"
    f"{len(snapshot_files)}"
)

print(
    f"{'SIMULATIONS':<25}"
    f"{len(simulation_files)}"
)

print(subdivider)

#
# Latest Files
#

print("\nLATEST DATASETS:\n")

latest_sets = [
    ("Portfolio", portfolio_files),
    ("Report", report_files),
    ("Export", export_files),
    ("Snapshot", snapshot_files),
    ("Simulation", simulation_files)
]

for label, dataset in latest_sets:

    if dataset:

        latest = dataset[-1].name

    else:

        latest = "None"

    print(
        f"{label:<15}"
        f"{latest}"
    )

print(f"\n{divider}")
print("END DATASET INVENTORY")
print(divider)
