import os

MONTH = '06 JUN 2021'  # change this to adjust the month you want to clean
FULL_MONTH_FILE = open('result.txt')
DIRECTORY = os.path.join('data', '2021 MPC JNLS', f'{MONTH}', '*.txt')  # use os instead of hard path to be os agnostic
CC = 50
