import csv

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

EVENT_LOG = (
    BASE_DIR /
    "logs" /
    "runtime_events" /
    "runtime_events.csv"
)

divider = "=" * 90
subdivider = "-" * 90

print(divider)
print("DIVAGG :: EVENT INTELLIGENCE")
print(divider)

if not EVENT_LOG.exists():

    print("\n[ERROR] Runtime event log missing.")
    raise SystemExit(1)

with open(
    EVENT_LOG,
    newline="",
    encoding="utf-8"
) as csvfile:

    rows = list(
        csv.DictReader(csvfile)
    )

activation_events = 0
restart_events = 0
shutdown_events = 0

for row in rows:

    event_type = (
        row.get(
            "event_type"
        )
        or ""
    )

    if event_type == "activation":
        activation_events += 1

    elif event_type == "restart":
        restart_events += 1

    elif event_type == "shutdown":
        shutdown_events += 1

print("\nRUNTIME EVENT ANALYSIS:\n")

print(subdivider)

print(
    f"{'EVENT TYPE':<24}"
    f"{'COUNT':<12}"
)

print(subdivider)

print(
    f"{'activation':<24}"
    f"{activation_events:<12}"
)

print(
    f"{'restart':<24}"
    f"{restart_events:<12}"
)

print(
    f"{'shutdown':<24}"
    f"{shutdown_events:<12}"
)

print(subdivider)

total_events = (
    activation_events +
    restart_events +
    shutdown_events
)

print(
    f"{'TOTAL EVENTS':<30}"
    f"{total_events}"
)

print(subdivider)

if total_events == 0:

    runtime_status = (
        "NO RUNTIME EVENTS"
    )

elif total_events < 10:

    runtime_status = (
        "EARLY EVENT HISTORY"
    )

else:

    runtime_status = (
        "ACTIVE EVENT OBSERVABILITY"
    )

print(
    f"{'RUNTIME STATUS':<30}"
    f"{runtime_status}"
)

print(divider)
print("END EVENT INTELLIGENCE")
print(divider)
