#!/usr/bin/env bash
set -euo pipefail

npx @arabold/docs-mcp-server@latest scrape "EuXFEL DA Group" https://dataanalysis.pages.xfel.eu/user-documentation/ --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EXtra" https://extra.readthedocs.io/en/latest/ --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EXtra-data" https://extra-data.readthedocs.io/en/latest/ --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EXtra-geom" https://extra-geom.readthedocs.io/en/latest/index.html --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Maxwell" https://docs.desy.de/maxwell/documentation/ --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Technique-Oriented Docs FXE" https://dataanalysis.pages.xfel.eu/techniques-docs/fxe/ --scope subpages --scrape-mode playwright
