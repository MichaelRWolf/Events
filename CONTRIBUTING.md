# Contributing

## Prerequisites

- Git
- `pre-commit` (<https://pre-commit.com/>)

## Setup (after clone)

Run:

```bash
./scripts/setup
```

This installs the repo's pre-commit hooks so checks run consistently on every machine.

## Running checks

- Run on all files:

```bash
pre-commit run --all-files
```

- Update hook versions (maintainers):

```bash
pre-commit autoupdate
```
