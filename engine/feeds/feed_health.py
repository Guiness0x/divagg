import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FEED_SOURCES = (
    BASE_DIR /
    "data" /
    "feeds" /
    "feed_sources.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: FEED HEALTH")
print(divider)

if not FEED_SOURCES.exists():

    print("\n[ERROR] Feed sources file missing.")
    raise SystemExit(1)

with open(
    FEED_SOURCES,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

print("\nFEED HEALTH ANALYSIS:\n")

print(subdivider)

print(
    f"{'SOURCE':<22}"
    f"{'STATUS':<12}"
    f"{'TYPE':<18}"
    f"{'HEALTH':<18}"
)

print(subdivider)

active_feeds = 0
planned_feeds = 0
disabled_feeds = 0

for row in rows:

    source = (
        row.get(
            "source_name"
        )
        or "UNKNOWN"
    )

    status = (
        row.get(
            "status"
        )
        or "UNKNOWN"
    )

    feed_type = (
        row.get(
            "feed_type"
        )
        or "UNKNOWN"
    )

    if status == "active":

        health = "ONLINE"
        active_feeds += 1

    elif status == "planned":

        health = "PENDING"
        planned_feeds += 1

    elif status == "disabled":

        health = "OFFLINE"
        disabled_feeds += 1

    else:

        health = "UNKNOWN"

    print(
        f"{source:<22}"
        f"{status:<12}"
        f"{feed_type:<18}"
        f"{health:<18}"
    )

print(subdivider)

print(
    f"{'ACTIVE FEEDS':<30}"
    f"{active_feeds}"
)

print(
    f"{'PLANNED FEEDS':<30}"
    f"{planned_feeds}"
)

print(
    f"{'DISABLED FEEDS':<30}"
    f"{disabled_feeds}"
)

print(subdivider)

#
# Runtime Feed Assessment
#

if active_feeds == 0:

    runtime_status = (
        "NO ACTIVE INGESTION"
    )

elif disabled_feeds >= 2:

    runtime_status = (
        "DEGRADED FEED TOPOLOGY"
    )

else:

    runtime_status = (
        "FEED LAYER STABLE"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END FEED HEALTH")
print(divider)
