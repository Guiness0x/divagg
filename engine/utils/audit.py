from pathlib import Path
from datetime import datetime

AUDIT_LOG = Path("../logs/audit.log")

def write_audit_log(action, details):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = (
        f"{timestamp} | "
        f"{action.upper()} | "
        f"{details}\n"
    )

    AUDIT_LOG.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(AUDIT_LOG, "a") as logfile:

        logfile.write(log_entry)
