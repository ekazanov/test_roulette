# test_roulette

## Requirements ##
This code was written/tested using Ubuntu 23.04 and Python 3.11.4.

## Installation ##
```
 git clone https://github.com/ekazanov/test_roulette.git
 cd test_roulette
 apt-get install pyton3-venv
 python3 -m venv venv

```

## Running ##
```
cd test_roulette
./run.sh
```

## Usage ##

usage: check_roulette.py [-h] --wallet INTEGER --first_bet INTEGER
                         --goal_amount INTEGER --session_num INTEGER
                         [--verbose INTEGER]

Roulette startegy testing program.

options:
  -h, --help            show this help message and exit
  --wallet INTEGER, -w INTEGER
                        Wallet start amount
  --first_bet INTEGER, -f INTEGER
                        First bet value.
  --goal_amount INTEGER, -g INTEGER
                        Give up when program has got this amount in
                        the wallet.
  --session_num INTEGER, -s INTEGER
                        Number of game sessions to play. Int.
  --verbose INTEGER, -v INTEGER
                        Verbosity level. 0/1

## Usage examples ##

Usage examples can be found in run.sh file.

## Dependencies ##

The program does not use any third party dependencies.
