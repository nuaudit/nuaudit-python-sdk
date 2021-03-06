.EXPORT_ALL_VARIABLES:
-include .env

.PHONY: build b
build b:
	@pipenv run python setup.py sdist bdist_wheel

.PHONY: clean c
clean c:
	@pipenv run python setup.py clean --all

.PHONY: deploy d
deploy d:
	@twine upload dist/*

.PHONY: sync s
sync s:
	@pipenv run pipenv-setup sync