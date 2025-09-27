PYFILES=$(shell find src -type f -name "*.py")

style:
	black --check --line-length=99 $(PYFILES)

format:
	black --line-length=99 $(PYFILES)

test:
	pytest
