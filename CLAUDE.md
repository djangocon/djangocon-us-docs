# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the DjangoCon US documentation site, built with MkDocs using the Material theme. It contains organizer documentation, checklists, and templates for running DjangoCon US conferences.

## Common Commands

```bash
# Install dependencies
just bootstrap

# Serve docs locally (http://127.0.0.1:8000)
just serve

# Build static site
just build

# Update uv.lock
just lock
```

Alternatively, using Docker:
```bash
docker compose up
```

## Project Structure

- `docs/` - Markdown documentation files organized by topic
- `mkdocs.yml` - MkDocs configuration and navigation structure
- `justfile` - Task runner commands
- `pyproject.toml` - Project metadata and dependencies
- `uv.lock` - Locked dependencies

## Documentation Organization

Each topic area typically has:
- A `checklist.md` - Tasks and timeline for that area
- Additional `.md` files with detailed documentation

Key sections: Conference Chair, A/V, Community, Conduct, Contribution Sprints, Health and Safety, Lightning Talks, Logistics, Marketing, Online Committee, Opportunity Grants, Program and Schedule, Social Events, Sponsors, Swag, Tickets, Venue, Volunteer Team, Website

## Writing Guidelines

- Follow existing markdown formatting conventions
- Use task lists (`- [ ]`) for checklists
- Keep documentation practical and actionable for conference organizers
- When adding new pages, update `mkdocs.yml` nav section
