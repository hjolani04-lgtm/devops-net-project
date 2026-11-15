# Production-Style 3-Tier Microservice (Docker, Linux, Networks & Git)

A containerized 3-tier web application demonstrating Linux security hardening, Docker multi-container orchestration, network segmentation, horizontal scaling, and CI automation.

## Architecture Overview

```text
[Client] ---> :8080 [Nginx Reverse Proxy] (frontend_net)
                            |
           +----------------+----------------+
           v                v                v
   [Backend Replica 1] [Backend Replica 2] [Backend Replica 3]  (frontend_net + backend_net)
           |                |                |
           +----------------+----------------+
                            v
                  [Redis Database :6379] (backend_net - Internal Isolated)
```

## Key Engineering Concepts Applied
- **Network Segmentation:** Isolated `backend_net` (`internal: true`) ensures Redis is completely unreachable from the external network or the Nginx proxy.
- **Load Balancing & Dynamic DNS:** Nginx uses Docker's embedded DNS server (`127.0.0.11`) to round-robin requests across 3 backend replicas.
- **Container & Linux Security:** Backend runs as a non-root user (`appuser`), environment secrets are restricted via `chmod 600 .env`, and only port `8080` is exposed to the host.
- **Data Persistence:** Named Docker volume (`redis_data`) preserves hit counts across container restarts.
- **CI Pipeline:** GitHub Actions validates Compose syntax and builds the Docker image on every push to `main`.

## Quick Start
```bash
cp .env.example .env
docker compose up -d --build
curl http://localhost:8080
```
