from os import system

system("python3 setup.py sdist bdist_wheel")
system("twine upload dist/* --verbose")
