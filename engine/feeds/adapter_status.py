import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ADAPTER_REGISTRY = (
    BASE_DIR /
    "data" /
    "adapters" /
    "adapter_registry.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: ADAPTER STATUS")
print(divider)

if not ADAPTER_REGISTRY.exists():

    print("\n[ERROR] Adapter registry missing.")
    raise SystemExit(1)

with open(
    ADAPTER_REGISTRY,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nADAPTER TOPOLOGY:\n")

print(subdivider)

print(
    f"{'ADAPTER':<24}"
    f"{'TYPE':<20}"
    f"{'STATUS':<12}"
    f"{'CACHE':<10}"
    f"{'NOTES':<25}"
)

print(subdivider)

active_adapters = 0
planned_adapters = 0
disabled_adapters = 0

for row in rows:

    adapter_name = (
        row.get(
            "adapter_name"
        )
        or "UNKNOWN"
    )

    provider_type = (
        row.get(
            "provider_type"
        )
        or "UNKNOWN"
    )

    status = (
        row.get(
            "status"
        )
        or "UNKNOWN"
    )

    cache_ready = (
        row.get(
            "cache_ready"
        )
        or "UNKNOWN"
    )

    notes = (
        row.get(
            "notes"
        )
        or ""
    )

    if status == "active":

        active_adapters += 1

    elif status == "planned":

        planned_adapters += 1

    elif status == "disabled":

        disabled_adapters += 1

    print(
        f"{adapter_name:<24}"
        f"{provider_type:<20}"
        f"{status:<12}"
        f"{cache_ready:<10}"
        f"{notes:<25}"
    )

print(subdivider)

print(
    f"{'ACTIVE ADAPTERS':<30}"
    f"{active_adapters}"
)

print(
    f"{'PLANNED ADAPTERS':<30}"
    f"{planned_adapters}"
)

print(
    f"{'DISABLED ADAPTERS':<30}"
    f"{disabled_adapters}"
)

print(subdivider)

#
# Runtime Assessment
#

if active_adapters == 0:

    runtime_status = (
        "NO ACTIVE ADAPTERS"
    )

elif disabled_adapters >= 2:

    runtime_status = (
        "PARTIAL INGESTION COVERAGE"
    )

else:

    runtime_status = (
        "ADAPTER LAYER STABLE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END ADAPTER STATUS")
print(divider)
