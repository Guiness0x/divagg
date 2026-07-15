from pathlib import Path

divider = "=" * 60

print(divider)
print("DIVAGG :: HISTORY INDEX")
print(divider)

directories = {
    "REPORTS": "../reports",
    "EXPORTS": "../exports",
    "SIMULATIONS": "../simulations"
}

for section, path in directories.items():

    print(f"\n{section}")
    print("-" * 60)

    files = sorted(
        Path(path).glob("*"),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    if not files:
        print("No files found.")
        continue

    for file in files[:10]:
        print(file.name)

print(f"\n{divider}")
print("END OF HISTORY")
print(divider)
