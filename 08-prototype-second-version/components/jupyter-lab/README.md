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

1. Create an `.env` file from the example file: `cp .env.example .env`
2. Update the environment varialbes in `.env` if required (e.g., a strong `JUPYTER_TOKEN`).
3. Build the container image: `docker compose build --no-cache`

   - Note: `--no-cache` is recommended for the first build to ensure a clean environment.

## Run

1. Start Jupyter Lab server: `docker compose up -d`
2. Optionally, view logs: `docker compose logs -f jupyter-lab`
3. Open Jupyter Lab in your browser: `http://localhost:<JUPYTER_PORT>`
4. Enter your `JUPYTER_TOKEN` from `.env` when prompted in the Jupyter Lab UI.
5. Optionally, stop the server again: `docker compose down`

All Jupyter Lab server data (notebooks, checkpoints, etc.) will be stored in the new `workspace` folder.
