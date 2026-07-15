divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: COMMAND REFERENCE")
print(divider)

#
# Portfolio Operations
#

print("\nPORTFOLIO OPERATIONS")
print(subdivider)

portfolio_commands = [
    "add",
    "remove",
    "update",
    "list",
    "switch",
    "create",
    "snapshot",
    "restore",
    "search",
    "enriched-list"
]

for command in portfolio_commands:

    print(f"./divagg {command}")

#
# Analytics
#

print("\nANALYTICS")
print(subdivider)

analytics_commands = [
    "analytics",
    "efficiency",
    "risk-analysis",
    "health",
    "diversification",
    "sector-analysis",
    "payout-analysis",
    "compare",
    "summary"
]

for command in analytics_commands:

    print(f"./divagg {command}")

#
# Historical Infrastructure
#

print("\nHISTORICAL INFRASTRUCTURE")
print(subdivider)

historical_commands = [
    "history",
    "snapshot-history",
    "snapshot-compare",
    "audit-log"
]

for command in historical_commands:

    print(f"./divagg {command}")

#
# Registry Intelligence
#

print("\nREGISTRY INTELLIGENCE")
print(subdivider)

registry_commands = [
    "lookup",
    "registry-add",
    "registry-search"
]

for command in registry_commands:

    print(f"./divagg {command}")

#
# System Infrastructure
#

print("\nSYSTEM INFRASTRUCTURE")
print(subdivider)

system_commands = [
    "metrics",
    "validate",
    "export-health",
    "simulate",
    "report"
]

for command in system_commands:

    print(f"./divagg {command}")

print(f"\n{divider}")
print("END COMMAND REFERENCE")
print(divider)
