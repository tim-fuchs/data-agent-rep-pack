FROM python:3.14.4-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    python -m venv /opt/venv; \
    /opt/venv/bin/pip install --upgrade pip; \
    /opt/venv/bin/pip install \
    "jupyterlab==4.4.1" \
    "jupyter-collaboration==4.0.2" \
    "jupyter-mcp-tools>=0.1.4" \
    ipykernel; \
    /opt/venv/bin/pip uninstall -y pycrdt datalayer_pycrdt || true; \
    /opt/venv/bin/pip install "datalayer_pycrdt==0.12.17"; \
    /opt/venv/bin/pip install \
    "EXtra-data==1.24.0" \
    "h5glance==0.9.0" \
    "pyFAI==2026.3.0";

ENV PATH="/opt/venv/bin:${PATH}"
WORKDIR /workspace

ENTRYPOINT ["jupyter", "lab"]
