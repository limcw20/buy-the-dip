# Buy the Dip

### Goal of This Project
To build a personal CLI Tool for stocks movement information and notifications while learning new things such as libraries (typer, yfinance), webhooks, github actions, etc.

### LATEST UPDATE (22/02/26):
- Refine subcommand that scans specific stock
  - Removed interval and tracks past 5 trading days instead. Reason: Intervals should be used on future functions such as notifications on dips.
  - Changed Option to Argument
- Init JSON file for watchlist, which will be the focus for the next subcommand.
- Refactor codes into separate files for cleaner coding workspace

### Current Features
- Scan (subcommand)
  - Prompts a specific stock input from user
  - Scans for the past 5 trading days and returns the percentage increase/decrease.
 
### Next Steps:
- Watchlist -> fetch, add, remove functions


## Changelog:

### 15/02/26
- Init basic project setup
- Tried Typer for the first time
- Init README

### 21/02/26
- Implement function that checks for single stock movement
  - In terminal, enter "python script.py", then user will be prompted to input a stock ticker
