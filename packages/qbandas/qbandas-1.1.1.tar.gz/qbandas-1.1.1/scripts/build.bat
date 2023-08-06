python -m pip install -U pip build twine
rm ./dist/*
python -m build
python -m twine upload -r pypi ./dist/*