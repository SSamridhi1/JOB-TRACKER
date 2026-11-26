# Architecture

What belongs here:
- A high-level description of how the pieces fit together: React SPA <->
  FastAPI REST API <-> PostgreSQL, containerised with Docker Compose for
  local dev.
- A simple diagram (even ASCII art or a Mermaid `flowchart`) showing that
  request flow.
- Explicitly note what was deliberately left OUT (Redis, Kafka,
  microservices) and why - so future contributors understand the
  "small, reliable, well-engineered" constraint from the project brief
  instead of assuming it was an oversight.
