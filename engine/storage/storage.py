from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TARGETS = {
    "PORTFOLIOS": BASE_DIR / "data" / "portfolios",
    "REPORTS": BASE_DIR / "reports",
    "EXPORTS": BASE_DIR / "exports",
    "SNAPSHOTS": BASE_DIR / "snapshots",
    "SIMULATIONS": BASE_DIR / "simulations",
    "LOGS": BASE_DIR / "logs",
    "BACKUPS": BASE_DIR / "backups"
}

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: STORAGE INSPECTION")
print(divider)

#
# Helper
#

def calculate_size(path):

    total = 0

    if path.is_file():

        return path.stat().st_size

    for item in path.rglob("*"):

        if item.is_file():

            total += item.stat().st_size

    return total

#
# Output
#

print("\nSTORAGE OVERVIEW:\n")

print(subdivider)

grand_total = 0

for label, path in TARGETS.items():

    if path.exists():

        size = calculate_size(path)

    else:

        size = 0

    grand_total += size

    kb_size = size / 1024

    print(
        f"{label:<20}"
        f"{kb_size:.2f} KB"
    )

print(subdivider)

grand_total_kb = grand_total / 1024

print(
    f"{'TOTAL STORAGE':<20}"
    f"{grand_total_kb:.2f} KB"
)

print(subdivider)

print(divider)
print("END STORAGE INSPECTION")
print(divider)
