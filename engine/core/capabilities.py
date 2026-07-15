divider = "=" * 60
subdivider = "-" * 60

print(divider)
print("DIVAGG :: CAPABILITIES")
print(divider)

capabilities = {

    "Portfolio Operations": [
        "add",
        "remove",
        "update",
        "list",
        "search",
        "switch",
        "create",
        "snapshot",
        "restore"
    ],

    "Analytics": [
        "analytics",
        "health",
        "risk-analysis",
        "efficiency",
        "diversification",
        "sector-analysis",
        "payout-analysis",
        "compare",
        "summary"
    ],

    "Historical Infrastructure": [
        "history",
        "snapshot-history",
        "snapshot-compare",
        "audit-log"
    ],

    "Runtime Diagnostics": [
        "status",
        "metrics",
        "profile",
        "logs",
        "storage",
        "env",
        "session",
        "maintenance",
        "integrity"
    ],

    "Runtime Lifecycle": [
        "reset-session",
        "runtime-snapshot",
        "manifest",
        "version",
        "command-history"
    ],

    "Registry Intelligence": [
        "lookup",
        "registry-add",
        "registry-search"
    ],

    "Protection Infrastructure": [
        "backup",
        "export-health",
        "validate"
    ]
}

total_capabilities = 0

for category, commands in capabilities.items():

    print(f"\n{category.upper()}\n")

    print(subdivider)

    for command in commands:

        print(f"./divagg {command}")

        total_capabilities += 1

print(f"\n{subdivider}")

print(
    f"TOTAL CAPABILITIES :: "
    f"{total_capabilities}"
)

print(divider)
print("END CAPABILITIES")
print(divider)
