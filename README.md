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
| Live Dividend Provider | ⏸ Deferred — provider licensing limitation |

---

# Purpose

DIVAGG is a financial observation engine designed to collect, normalize, persist, reconcile, and report dividend-oriented portfolio information.

The project emphasizes operational reliability over market speculation.

DIVAGG is an engineering platform for dividend portfolio observation. It is not a brokerage, trading system, or investment advisor.

---

# Design Philosophy

Generation 1 was built around six operational principles:

```text
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

```text
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
- Provider-specific source tracking

## Dividend Observation

Generation 1 establishes a dedicated dividend observation architecture.

Implemented:

- Dividend snapshot model
- Historical persistence schema
- Payment metadata structure
- Ex-dividend support
- Provider abstraction boundary

Live dividend ingestion is deferred until a provider with suitable access and licensing becomes available.

## Runtime Intelligence

DIVAGG includes an operational runtime capable of:

- Runtime cycle execution
- Portfolio reconciliation
- Severity classification
- Anomaly detection
- Runtime summaries
- Historical runtime events
- Scheduled execution

## Reporting

Generation 1 includes:

- Runtime summaries
- Portfolio exports
- Operational reports
- Historical persistence

---

# Runtime Workflow

```text
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

```text
compose/       Docker Compose topology
config/        Engine configuration
containers/    Container-specific Dockerfiles
data/          Registries and demonstration datasets
engine/        Core finance and runtime modules
runtime/       Live ingestion, automation, telemetry, and reporting
```

---

# Configuration

Create a local environment file:

```bash
cp .env.example .env
```

Populate your own configuration:

```env
POSTGRES_USER=divagg
POSTGRES_PASSWORD=your_password
POSTGRES_DB=divagg
POSTGRES_PORT=5432
FINNHUB_API_KEY=your_finnhub_api_key
```

The real `.env` file is excluded from Git.

---

# Quick Start

Start the platform:

```bash
docker compose --env-file .env \
-f compose/docker-compose.yml up -d
```

Verify the containers:

```bash
docker ps
```

Run a live market observation:

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
===================================
Ticker: JEPI
Stored In PostgreSQL: YES
===================================
Ticker: O
Stored In PostgreSQL: YES
===================================
Ticker: MAIN
Stored In PostgreSQL: YES
===================================
===================================
DIVAGG MARKET INGESTION COMPLETE
Stored Snapshots: 4
Failed Snapshots: 0
Status: SUCCESS
===================================
```

---

# Current Scope

DIVAGG is intentionally not:

- A brokerage platform
- A trading application
- A market prediction engine
- An algorithmic trading system

Its purpose is operational financial observation centered on dividend-oriented portfolios.

---

# Engineering Decisions

Generation 1 emphasizes:

- Runtime-first architecture
- Terminal-native operation
- PostgreSQL persistence
- Historical observation
- Dockerized deployment
- Separation of market and dividend telemetry
- Replaceable external providers
- Explicit operational status reporting

These decisions allow future providers to be integrated without redesigning the engine.

---

# Generation Roadmap

## Generation 2

Potential future work:

- Live dividend provider integration
- Multi-provider observation
- Provider failover
- Expanded portfolio analytics
- Enhanced runtime intelligence

---

# License

This repository is presented as an engineering portfolio project and educational reference.

No open-source license has been assigned.

---

# Author

**Joshua Hurtado**

Designed and engineered as a terminal-first financial observation platform demonstrating systems architecture, runtime automation, financial data processing, persistence, and operational tooling.
