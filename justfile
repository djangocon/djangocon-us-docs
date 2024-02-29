@_default:
    just --list

@bootstrap:
    python -m pip install --upgrade pip uv
    python -m uv pip install --requirement requirements.in

@build:
    python -m mkdocs build

@lock:
    python -m uv pip compile --output-file requirements.txt requirements.in

@serve:
    python -m mkdocs serve
