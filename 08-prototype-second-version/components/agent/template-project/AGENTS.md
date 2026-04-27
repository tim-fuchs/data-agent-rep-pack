# AGENTS.md

## Project Overview

- This project is focused on the [offline data analysis process](https://www.xfel.eu/organization/scientific_and_technical_groups/data_department/data_analysis/documentation_and_training_material/index_eng.html) at [European XFEL (EuXFEL)](https://xfel.eu).
- The user works in this project with one of two workflows:
  1. To work on a Jupyter notebook that is stored locally in this project but is using a kernel stored on a remote Jupyter Lab server.
  2. To use the `jupyter-mcp` server to connect to a Jupyter notebook stored on a remote Jupyter Lab server.
- This Jupyter Lab server executes its processes on the high-performance computing (HPC) cluster [Maxwell](https://docs.desy.de/maxwell/) to enable resource-demanding data analysis processes.
- Your task: Support the user in data analysis by generating, improving, or explaining code in the notebook.

## Rules

ALWAYS follow the rules listed the files of the directory `.kilo/rules`.
