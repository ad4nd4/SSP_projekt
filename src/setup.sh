VENV_DIR="./.venv"

python3 -m venv "$VENV_DIR"
source "$VENV_DIR"/bin/activate

"$VENV_DIR"/bin/pip3 install --upgrade pip
"$VENV_DIR"/bin/pip3 install -r requirements.txt
