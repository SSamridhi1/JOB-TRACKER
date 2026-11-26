# API Design

What belongs here:
- The API contract: endpoint list, request/response shapes, status codes.
- This can start as a written Markdown table (mirroring the "PLANNED API
  ENDPOINTS" section of the project brief) and later be replaced or
  supplemented by an exported OpenAPI spec from FastAPI's auto-generated
  `/docs` (Swagger UI) once endpoints are implemented.
- Any breaking change to an endpoint's shape should be documented here
  before the PR that makes the change.
