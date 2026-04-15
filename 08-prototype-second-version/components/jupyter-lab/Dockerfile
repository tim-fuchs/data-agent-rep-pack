FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

RUN set -eux; \
    uv python install 3.14.4; \
    uv venv --python 3.14.4 /opt/venv; \
    uv pip install --python /opt/venv/bin/python \
    "jupyterlab==4.4.1" \
    "jupyter-collaboration==4.0.2" \
    "jupyter-mcp-tools>=0.1.4" \
    ipykernel; \
    uv pip uninstall --python /opt/venv/bin/python -y pycrdt datalayer_pycrdt || true; \
    uv pip install --python /opt/venv/bin/python "datalayer_pycrdt==0.12.17"

ENV PATH="/opt/venv/bin:/root/.local/bin:${PATH}"
WORKDIR /workspace

ENTRYPOINT ["jupyter", "lab"]
