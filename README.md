# DjangoCon US Docs

Want to help run DjangoCon US? Say [hello!](mailto:hello@djangocon.us)

We'll chat with you about how you'd like to contribute, then add you to our mailing list, Slack workspace, GitHub, and all the places.

## Code of Conduct

As a contributor, you can help us keep the Django community open and inclusive.
Please read and follow our [Code of Conduct](https://www.djangoproject.com/conduct/).

## To run locally

### With uv

Requires [uv](https://docs.astral.sh/uv/) to be installed.

```bash
# Install dependencies
uv sync

# Serve docs locally
uv run mkdocs serve

# Build static site
uv run mkdocs build
```

The docs will be available at http://127.0.0.1:8000

### With just

Requires [just](https://github.com/casey/just) and [uv](https://docs.astral.sh/uv/) to be installed.

```bash
# Install dependencies
just bootstrap

# Serve docs locally
just serve

# Build static site
just build
```

The docs will be available at http://127.0.0.1:8000

### With Docker Compose

Requires [just](https://github.com/casey/just) and [Docker](https://www.docker.com/) to be installed.

```bash
# Start the docs server
just up

# Or run in detached mode
just up -d

# Stop the server
just down
```

The docs will be available at http://127.0.0.1:8000
