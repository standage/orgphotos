PYFILES=$(shell find src -type f -name "*.py")

style:
	black --check --line-length=99 $(PYFILES)

format:
	black --line-length=99 $(PYFILES)

test:
	pytest

hooks:
	echo 'set -eo pipefail' > .git/hooks/pre-commit
	echo 'make style' >> .git/hooks/pre-commit
	chmod 755 .git/hooks/pre-commit
