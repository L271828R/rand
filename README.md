
# rand.py a /dev/random clone

This is an attempt to create a pseudorandom number generator, similar to that
found on linux systems. It creates a sha256 utf-8 in hexadecimal digits.

## getting started

To install, kindly use a linux system and in the case of Ubuntu Linix
you can use the package installer like the below to install Python3.

apt-get install python3.7

## installing dependencies

You can install the libraries needed by typing:

pip install requirements.txt

Or by installing the needed libraries individually:


pip install numpy

pip install pandas

pip install scipy

pip install pytest

### running rand.py

python rand.py


![example](https://i.imgur.com/bcJrRg5.png)

### running tests
pytest rand_tests.py


