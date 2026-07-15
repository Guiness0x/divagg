import subprocess

print("===================================")
print("DIVAGG FINANCIAL COGNITION CYCLE")
print("===================================")

subprocess.run(["python", "/runtime/portfolio/create_snapshot.py"], check=True)

subprocess.run(["python", "/runtime/portfolio/snapshot_analytics.py"], check=True)

subprocess.run(["python", "/runtime/portfolio/snapshot_delta.py"], check=True)

print("===================================")
print("DIVAGG FINANCIAL COGNITION COMPLETE")
print("===================================")
