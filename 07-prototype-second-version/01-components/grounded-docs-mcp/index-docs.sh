#!/usr/bin/env bash
set -euo pipefail

npx @arabold/docs-mcp-server@latest scrape "CrystFEL" https://www.desy.de/~twhite/crystfel/index.html --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EuXFEL DA Group" https://dataanalysis.pages.xfel.eu/user-documentation/ --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EuXFEL Website" https://xfel.eu/ --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EXtra" https://extra.readthedocs.io/en/latest/ --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EXtra-data" https://extra-data.readthedocs.io/en/latest/ --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "EXtra-geom" https://extra-geom.readthedocs.io/en/latest/index.html --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "DAMNIT" https://damnit.readthedocs.io/en/latest/ --scope hostname --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Maxwell" https://docs.desy.de/maxwell/ --scope subpages --max-depth 5 --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Offline Calibration" https://calibration.pages.xfel.eu/pycalibration/ --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "SCS Toolbox" https://scs.pages.xfel.eu/toolbox/ --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Slurm" https://slurm.schedmd.com --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Technique-Oriented Docs FXE" https://dataanalysis.pages.xfel.eu/techniques-docs/fxe/ --scope subpages --scrape-mode playwright
npx @arabold/docs-mcp-server@latest scrape "Technique-Oriented Docs SQS" https://dataanalysis.pages.xfel.eu/techniques-docs/sqs/ --scope subpages --scrape-mode playwright
