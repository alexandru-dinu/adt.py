SRC := $(shell find ./ -not -path '*/.*' -name "*.py")

format:
	@autoflake --remove-all-unused-imports -i $(SRC) \
		&& isort $(SRC) \
		&& black $(SRC)

test:
	poetry run pytest -vv tests/

clean:
	@find . -name "__pycache__" -print0 | xargs -0 rm -rfv
	@find . -name ".pytest_cache" -print0 | xargs -0 rm -rfv
	@find . -name ".hypothesis" -print0 | xargs -0 rm -rfv
