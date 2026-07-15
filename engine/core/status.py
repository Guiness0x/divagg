from pathlib import Path

divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: SYSTEM STATUS")
print(divider)

#
# Infrastructure Paths
#

checks = {
    "PORTFOLIOS": Path("../data/portfolios"),
    "REGISTRY": Path("../data/registry/tickers.csv"),
    "SNAPSHOTS": Path("../snapshots"),
    "REPORTS": Path("../reports"),
    "EXPORTS": Path("../exports"),
    "SIMULATIONS": Path("../simulations"),
    "AUDIT LOG": Path("../logs/audit.log"),
    "CONFIG": Path("../config/config.toml")
}

#
# Output
#

print("\nENVIRONMENT STATUS:\n")

print(subdivider)

healthy = True

for label, path in checks.items():

    if path.exists():

        status = "OK"

    else:

        status = "MISSING"

        healthy = False

    print(
        f"{label:<20}"
        f"{status}"
    )

print(subdivider)

#
# Final System State
#

print()

if healthy:

    print("[SYSTEM STATUS] OPERATIONAL")

else:

    print("[SYSTEM STATUS] DEGRADED")

print(f"\n{divider}")
print("END STATUS")
print(divider)
