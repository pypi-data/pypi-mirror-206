supylib 0.31
-------------------------
Eine Python-basierte Utility-Bibliothek für Datenbanken, Computer Vision, Signalverarbeitung und Machine Learning
(c) Andreas Knoblauch, HS Albstadt-Sigmaringen, 2015-2023

Aktivierung/Sichtbarkeit
-------------------------
Der folgende Shell-Befehl macht das suplib/python Verzeichnis global sichtbar,
indem vorne in PYTHONPATH und PATH gestellt wird (ggf. in .bashrc einfügen...):

source /home/ak/projects/supylib/python/BashSrc


Versionskontrolle mit Git/GitHub
---------------------------------
python: Python Sources von Supylib
shipping: Packages prepared for shipping
testing: testing area
README: this file

Excluded from Versionskontrolle:
---------------------------------
see python/.gitignore:

Packaging:
-----------
see                        : https://packaging.python.org/en/latest/tutorials/packaging-projects/
build package              : python3 -m build
upload package to test-repo: python3 -m twine upload --repository testpypi dist/*
upload package to PyPI     : python3 -m twine upload dist/*
install from test-repo     : pip3 install --index-url https://test.pypi.org/simple/ --no-deps supylib
install from PyPI          : pip3 install supylib
