# DIVAGG

> **Dividend Aggregation Engine**
>
> Terminal-first financial observation platform focused on dividend portfolio intelligence, operational runtime automation, and historical financial persistence.

---

# Generation 1 Status

| Component | Status |
|-----------|--------|
| Market Observation | ✅ Complete |
| Dividend Observation Layer | ✅ Complete |
| Runtime Intelligence | ✅ Complete |
| Reconciliation Engine | ✅ Complete |
| Historical Persistence | ✅ Complete |
| Reporting Pipeline | ✅ Complete |
| Live Dividend Provider | ⏸ Deferred (Provider Licensing) |

---

# Purpose

DIVAGG (Dividend Aggregation Engine) is a financial observation engine designed to collect, normalize, persist, reconcile, and report dividend-oriented portfolio information.

The project emphasizes operational reliability over market speculation.

DIVAGG is intended to serve as an engineering platform for dividend portfolio observation rather than a brokerage, trading system, or investment advisor.

---

# Design Philosophy

Generation 1 was built around six operational principles.

```
Observe
        ↓
Normalize
        ↓
Persist
        ↓
Reconcile
        ↓
Detect
        ↓
Report
```

Every subsystem inside DIVAGG supports one or more of these principles.

---

# System Architecture

```
                    DIVAGG

              External Providers
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Market Observation         Dividend Observation
        │                           │
        └─────────────┬─────────────┘
                      │
             Runtime Intelligence
                      │
               Reconciliation
                      │
          Severity Classification
                      │
             Anomaly Detection
                      │
          Historical Persistence
                      │
             Reporting & Export
```

---

# Core Capabilities

## Market Observation

- Live Finnhub market quote ingestion
- Historical market quote persistence
- Quote normalization
- Timestamped observations
- Provider abstraction layer

---

## Dividend Observation

Generation 1 establishes a dedicated dividend observation architecture.

Implemented:

- Dividend snapshot model
- Historical persistence schema
- Payment metadata structure
- Ex-dividend support
- Provider abstraction

Live dividend ingestion has been intentionally deferred until a provider with appropriate licensing becomes available.

---

## Runtime Intelligence

DIVAGG includes a complete operational runtime capable of:

- Runtime cycle execution
- Portfolio reconciliation
- Severity classification
- Runtime summaries
- Historical runtime events
- Scheduled execution

---

## Reporting

Generation 1 includes:

- Runtime summaries
- Portfolio exports
- Operational reports
- Historical persistence

---

# Runtime Workflow

```
External Provider
        │
        ▼
Observation
        │
        ▼
Normalization
        │
        ▼
PostgreSQL Persistence
        │
        ▼
Runtime Intelligence
        │
        ▼
Reconciliation
        │
        ▼
Anomaly Detection
        │
        ▼
Reporting
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Database | PostgreSQL |
| Containers | Docker |
| Orchestration | Docker Compose |
| Market Provider | Finnhub |
| Financial Components | COBOL |
| Platform | Linux |

---

# Repository Layout

```
compose/
config/
containers/
data/
engine/
runtime/
```

---

# Configuration

Create a local environment file.

```bash
cp .env.example .env
```

Populate your own configuration.

```text
POSTGRES_USER=divagg
POSTGRES_PASSWORD=your_password
POSTGRES_DB=divagg
POSTGRES_PORT=5433
FINNHUB_API_KEY=your_finnhub_api_key
```

---

# Quick Start

Start the platform.

```bash
docker compose --env-file .env \
-f compose/docker-compose.yml up -d
```

Run a live market observation.

```bash
docker compose --env-file .env \
-f compose/docker-compose.yml \
exec divagg-core \
python /runtime/ingestion/ingest_finnhub_quotes.py
```

---

# Example Runtime Output

```text
===================================
DIVAGG FINNHUB MARKET OBSERVATION
===================================

Ticker: SCHD
Stored In PostgreSQL: YES

Ticker: JEPI
Stored In PostgreSQL: YES

Ticker: O
Stored In PostgreSQL: YES

Ticker: MAIN
Stored In PostgreSQL: YES

===================================
DIVAGG MARKET INGESTION COMPLETE

Stored Snapshots: 4
Failed Snapshots: 0

Status: SUCCESS
===================================
```

---

# Current Scope

DIVAGG is intentionally **not**:

- A brokerage platform
- A trading application
- A market prediction engine
- An algorithmic trading system

Its purpose is operational financial observation.

---

# Engineering Decisions

Generation 1 intentionally emphasizes:

- Runtime-first architecture
- Terminal-native workflow
- PostgreSQL persistence
- Historical observation
- Dockerized deployment
- Separation of market and dividend telemetry
- Provider abstraction

These decisions allow future data providers to be integrated without redesigning the engine.

---

# Generation Roadmap

## Generation 2

Planned improvements include:

- Live dividend provider integration
- Multi-provider observation
- Provider failover
- Expanded portfolio analytics
- Enhanced runtime intelligence

---

# License

This repository is provided as an engineering portfolio project and educational reference.

---

# Author

**Joshua Hurtado**

Designed and engineered as a terminal-first financial observation platform demonstrating systems engineering, runtime architecture, financial data processing, and operational automation.
