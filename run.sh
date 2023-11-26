#! /usr/bin/bash

source venv/bin/activate

# Get help message
python3 check_roulette.py --help

# Try 1 session. Read verbose reports.
# python3 check_roulette.py --wallet 50 --first_bet 2 --goal_amount 70 --session_num 1 --verbose 1

# Try 100 sessions.
# python3 check_roulette.py --wallet 50 --first_bet 2 --goal_amount 70 --session_num 10 --verbose 0
