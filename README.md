# Flatten Algorithm
-----
### Synopsis
This repo contains a simple function which will flatten an array of arbitrarily nested integers. It includes unit tests which have been used to verify the code functions as expected. Non-integer items will raise a type error.
-----
### Usage

Open a Python interpreter, import the function, and run it as follows:

```
vagrant@ubuntu-xenial:~$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from flatten import flatten
>>> arr = [[], [[2, 3, 4], [[5]]], [1]]
>>> flatten(arr)
[2, 3, 4, 5, 1]
>>>
```

Tests can be run like so:

```
python3 -m unittest discover tests
```
-----
### Environment

Code written in Python v3.6.5

### Authors

Jesse Hedden <jesse.hedden@holbertonschool.com>
