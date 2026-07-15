#!/bin/sh

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

BACKUP_FILE="/backups/postgres/divagg_backup_${TIMESTAMP}.sql"

echo "==================================="
echo "DIVAGG DATABASE BACKUP STARTING"
echo "==================================="

pg_dump \
  -h divagg-db \
  -U ${POSTGRES_USER} \
  ${POSTGRES_DB} \
  > ${BACKUP_FILE}

echo "==================================="
echo "BACKUP COMPLETE"
echo "==================================="

echo "Backup File: ${BACKUP_FILE}"
