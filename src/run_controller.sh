if [ "$#" -ne 1 ]; then
    echo "Expected 1 argument."
    echo "Run as \"./run_controller.sh <path/to/controller.py>\""
    exit 1
fi

VENV_DIR="./.venv"

exec "$VENV_DIR"/bin/python3 -c "from os_ken.cmd.manager import main; main()" --verbose "$1"
