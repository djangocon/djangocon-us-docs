@_default:
    just --list

# Install project dependencies
@bootstrap:
    uv sync

# Build the static documentation site
@build:
    uv run mkdocs build

# Update uv.lock with latest dependency versions
@lock:
    uv lock

# Upgrade all dependencies to latest versions
@upgrade:
    uv lock --upgrade

# Serve docs locally at http://127.0.0.1:8000
@serve:
    uv run mkdocs serve

# Start Docker containers
@up *ARGS:
    docker compose up {{ ARGS }}

# Stop Docker containers
@down *ARGS:
    docker compose down {{ ARGS }}
