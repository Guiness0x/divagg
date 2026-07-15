from pathlib import Path
from datetime import datetime
import shutil

divider = "=" * 60

source_file = Path("../data/portfolio.csv")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

destination_file = (
    Path("../snapshots") /
    f"portfolio_snapshot_{timestamp}.csv"
)

print(divider)
print("DIVAGG :: PORTFOLIO SNAPSHOT")
print(divider)

if not source_file.exists():

    print("[ERROR] portfolio.csv not found.")

else:

    shutil.copy2(source_file, destination_file)

    print("\n[INFO] Snapshot created:")
    print(destination_file)

print(f"\n{divider}")
print("END SNAPSHOT")
print(divider)
