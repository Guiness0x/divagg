#!/usr/bin/env bash

while true; do

  echo "==================================="
  echo "DIVAGG SCHEDULED RUNTIME START"
  echo "==================================="

  python /runtime/automation/runtime_cycle.py

  python /runtime/automation/export_runtime_report.py

  echo "==================================="
  echo "DIVAGG SCHEDULED RUNTIME COMPLETE"
  echo "Sleeping for 60 seconds..."
  echo "==================================="

  sleep 60

done
