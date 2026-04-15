# Jupyter Lab Server

## Purpose

EuXFEL members would work on the [remote Jupyter Lab server](https://max-jhub.desy.de) running on the HPC cluster.
Non-members cannot access this server.
Therefore, this project provides a reproducible Jupyter Lab environment that runs in Docker.

It builds a container image with:

- Python 3.14.4 (managed by uv)
- jupyterlab 4.4.1
- jupyter-collaboration 4.0.2
- jupyter-mcp-tools (>= 0.1.4)
- ipykernel
- datalayer_pycrdt pinned to 0.12.17

The goal is to make local startup consistent across machines without requiring a local Python setup.

## Prerequisites

- Docker Desktop (or Docker Engine + Docker Compose plugin)
- A free local port for Jupyter (for example, 8888)
- Basic terminal access

Verify Docker is available:

```bash
docker --version
docker compose version
```

## Installation

1. Clone or copy this project locally.
2. Enter the project directory.
3. Create your runtime config from the example file.

   ```bash
   cp .env.example .env
   ```

4. Edit `.env` and set all required values:

   ```env
   JUPYTER_TOKEN=replace-with-a-strong-token
   JUPYTER_IP=0.0.0.0
   JUPYTER_PORT=8888
   ```

   If any of these variables are missing, `docker compose up` will fail fast with an explicit error.

5. Build the container image:

   ```bash
   docker compose build --no-cache
   ```

Note: `--no-cache` is recommended for the first build to ensure a clean environment.

## Run

Start Jupyter Lab:

```bash
docker compose up -d
```

View logs:

```bash
docker compose logs -f jupyter-lab
```

Open Jupyter Lab in your browser:

```text
http://localhost:<JUPYTER_PORT>
```

Use `JUPYTER_TOKEN` from `.env` when prompted.

## Stop and Cleanup

Stop containers:

```bash
docker compose down
```

Stop and remove associated volumes:

```bash
docker compose down -v
```

## Project Files

- `Dockerfile`: Builds the Jupyter Lab image and installs dependencies.
- `docker-compose.yml`: Defines service runtime, env wiring, ports, and volume mapping.
- `.env.example`: Template for required runtime variables.
- `.env`: Local runtime values used by Docker Compose.
