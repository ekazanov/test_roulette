#! /usr/bin/bash

# Get help message
# python3 check_roulette.py --help

# Try 1 session. Read verbose reports.
# python3 check_roulette.py --wallet 50 --first_bet 2 --goal_amount 70 --session_num 1 --verbose 1

# Try 100 sessions.
python3 check_roulette.py --wallet 10 --first_bet 2 --goal_amount 45 --session_num 100 --verbose 0
