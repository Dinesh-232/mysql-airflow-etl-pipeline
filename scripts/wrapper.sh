
#!/bin/bash

set -e

PROJECT_DIR="$HOME/airflow_project"

source "$PROJECT_DIR/venv/bin/activate"

python "$PROJECT_DIR/scripts/etl_script.py"
