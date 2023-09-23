install: 
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-games: 
	poetry run brain-even
	poetry run brain-calc
	poetry run brain-gcd
	