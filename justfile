@_default:
    just --list

bootstrap:
    #!/usr/bin/env bash
    set -euo pipefail

    python -m pip install --upgrade pip uv
    python -m uv pip install --requirement requirements.in

    if [ ! -f "compose.override.yml" ]; then
        echo "compose.override.yml created"
        cp compose.override.yml-dist compose.override.yml
    fi

@build:
    python -m mkdocs build

@lock:
    python -m uv pip compile --output-file requirements.txt requirements.in

@serve:
    python -m mkdocs serve
