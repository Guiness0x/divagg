#!/bin/sh

echo "==================================="
echo "DIVAGG CONTAINER RUNTIME STARTING"
echo "==================================="

python -u /runtime/jobs/runtime_check.py

echo "==================================="
echo "DIVAGG SCHEDULER STARTING"
echo "==================================="

python -u /runtime/schedulers/runtime_scheduler.py &

echo "==================================="
echo "DIVAGG RUNTIME ACTIVE"
echo "==================================="

tail -f /dev/null
