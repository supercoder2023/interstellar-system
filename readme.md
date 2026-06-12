# Interstellar Complex Exploration System: Genesis Node

> **Mission Directive:** Survive and Explore.
> **Operational Horizon:** Year 0 to Year 2000.

This repository holds the genesis container for an interstellar complex exploration system. It is designed to be completely self-contained, hardware-agnostic, and resilient against dependency rot over extended timelines.

## The 2,000-Year Manifesto

This system is explicitly engineered to remain operational, readable, and deployable for the next 2,000 years. To achieve this, all future code contributions, architectural changes, and module additions must strictly adhere to the following survival protocols:

1. **The Single-File Mandate:** Complex framework distributions degrade over time. Core API logic must remain consolidated in single-file structures (e.g., `main.py`). Do not introduce highly distributed micro-frameworks that require extensive dependency mapping.
2. **Database Fluidity:** Rigid, relation-heavy databases fail when schemas must evolve unpredictably over centuries. All data must flow into document-based storage (NoSQL) to ensure that incoming, unforeseen telemetry structures do not crash the system. 
3. **Zero External Dependencies:** The system must assume it has no access to the broader terrestrial internet. It cannot rely on external CDNs, cloud-hosted configuration files, or real-time package fetching during operation. 
4. **Hardware Agnosticism:** The node is containerized at the lowest functional level. As long as the future host can process standard container operations, the Genesis Node will boot.
5. **Human-Readable Fallback:** Every core protocol must be documented in plain, uncompiled text formats (Markdown/TXT). If the software execution environment is entirely lost, the logic must still be mathematically and logically legible to a human reader.

Any pull request or modification that violates these five protocols will be rejected to preserve the long-term integrity of the mission.

---

## System Architecture

* **Core Interface:** Python 3.11 + FastAPI
* **Data Persistence:** MongoDB
* **Orchestration:** Docker & Docker Compose
* **State:** Stateless application logic attached to persistent data volumes.

## Directory Structure

\`\`\`text
.
├── docker-compose.yml   # System orchestration map
├── Dockerfile           # Genesis container blueprint
├── main.py              # Single-file core logic and API
├── requirements.txt     # Strict dependency locks
└── docs/                # System manifests and offline manuals
\`\`\`

## Initiation Sequence

To bring the Genesis Node online, ensure you have Docker and Docker Compose installed on your host system.

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/YOUR_USERNAME/interstellar-system.git
   cd interstellar-system
   \`\`\`

2. **Engage the orchestration:**
   \`\`\`bash
   docker-compose up -d --build
   \`\`\`

3. **Verify system status:**
   The node will expose its interface on port `8000`.
   \`\`\`bash
   curl http://localhost:8000/
   \`\`\`
   *Expected Response:*
   \`\`\`json
   {
       "directive": "Survive and Explore",
       "uptime_epoch": "2026-06-12T02:25:02+00:00",
       "systems": "Nominal"
   }
   \`\`\`

## Telemetry Interface

The system accepts telemetry data via standard HTTP POST protocols. 

**Log Data:**
\`\`\`bash
curl -X 'POST' \
  'http://localhost:8000/telemetry/log' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sector": "Alpha Centauri",
  "status": "Approaching",
  "timestamp": "2026-06-12T02:25:02Z"
}'
\`\`\`

## Maintenance & Shut Down

To safely spin down the containers while preserving the `system_data` volume:
\`\`\`bash
docker-compose down
\`\`\`

To completely wipe the system and its persistent memory (Use with extreme caution):
\`\`\`bash
docker-compose down -v
\`\`\`