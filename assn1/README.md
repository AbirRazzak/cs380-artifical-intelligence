# Programming Assignment 1
Abir Razzak, amr439@drexel.edu

CS380 - Artificial Intelligence

## How to Run
Assignment 1:

run `python3 assn1Test.py`

Unit tests:

run `python3 pegBoardTest.py`

## Files
assn1Test.py - main file for assignment 1

helper.py - helper file to assist with data processing

pegBoard.py - main functions related to the pegboard (required functions are located here)

pegBoardTest.py - pegboard unit tests

## How It Works

The board is represented as a List of List of integers. This 2D list either has a value of 0 or 1 to represent an empty slot or filled slot respectively. The rules are represented as a List of List of integers as well. Each row in this 2D array contain 2 integers, the row number and column number of the jumper, goner, and newpos. rule[0] is the jumper, rule[1] is the goner, and rule[2] is newpos.

## Testing

All testing was done through the python interpreter and then created unit tests accordingly. See the `How to Run` section on how to run the unit tests.

## Technologies

Written and tested on macOS Mojave v10.14.4

Complied and ran on Python 3.7

IDE: PyCharm Professional

> PyCharm 2019.1.1 (Professional Edition)
> Build #PY-191.6605.12, built on April 3, 2019
> Licensed to Abir Razzak
> Subscription is active until April 2, 2020
> For educational use only.
> JRE: 11.0.2+9-b159.34 x86_64
> JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
> macOS 10.14.4
