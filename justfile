# List available commands
@default:
    just --list

# Install the package
@install:
    poetry install

# Install the package in development mode
@install-dev:
    poetry install --with dev

# generate the documentation
@gendocs:
  poetry run python generate_docs.py --only-managed-by-aws
  poetry run mkdocs gh-deploy --force
