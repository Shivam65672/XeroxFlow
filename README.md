# NIT Xerox Rush Predictor

Target Person: Mr. Ramesh Mahato (Shopkeeper)  
Location: NIT Xerox & Printing Center, Near Mega Mess, NIT Jamshedpur  
Date of Fieldwork: November 17, 2026

## Overview
This tool helps Mr. Ramesh anticipate paper tray depletion and identify the safest windows for machine cool-downs and lunch breaks based on real print-volume data, rather than just queue headcount.

## How to Run the Tool
1.Ensure you have Python 3 installed on your machine. No external libraries are required.
2.Place the `data.csv` (containing the raw fieldwork data) and the `predictor.py` script in the same directory.
3.Open your terminal or command prompt, navigate to the directory, and run the following command:
   ```bash
   python predictor.py
   ```

## Real Output
When running the tool against the collected `data.csv`, the terminal outputs the following action plan:

```text
--- NIT XEROX DAILY OPERATIONS PLAN ---
Target: Mr. Ramesh Mahato

1. PAPER RELOAD ALERTS:
-> Tray will empty around 09:47. Pre-load a fresh ream on the desk 15 minutes before this.
-> Tray will empty around 11:12. Pre-load a fresh ream on the desk 15 minutes before this.

2. PEAK RUSH WARNING:
-> The 09:00 hour has the highest print volume (272 pages) and longest queues.
-> Action: Do not schedule breaks here. Ensure ₹200+ in loose change is ready for cash payers.

3. COOL-DOWN & LUNCH BREAK:
-> The 14:00 hour is practically empty (14 pages printed).
-> Action: Power down the main laser printer for 20 minutes to save the fuser roller, and take your lunch break.
---------------------------------------
```

## What It Gets Wrong
1.Dynamic Academic Schedules: The tool assumes daily traffic follows the same pattern as the sample data. In reality, if a professor assigns a sudden 50-page lab manual due at 2:00 PM the next day, the 13:00 hour will instantly become a peak, breaking this prediction.
2.Lunch Time Starvation: The script strictly finds the lowest printing volume of the day to suggest a break. If the shop is continuously busy from 10:00 AM to 4:00 PM, the script will cruelly tell the shopkeeper to wait until after 4:00 PM to eat, failing to account for normal human eating schedules.