#!/usr/bin/env python3
"""
Mapper for Hadoop Streaming.

Input:  CSV rows from stdin.
Output: Mental_Fatigue_Score<TAB>Doomscrolling_Hours for students whose
        Reported_Stress_Level is 7 or higher.
"""

import csv
import sys


def main():
    reader = csv.DictReader(sys.stdin)

    for row in reader:
        try:
            stress_level = int(row["Reported_Stress_Level"])
            doomscrolling_hours = float(row["Doomscrolling_Hours"])
            fatigue_score = row["Mental_Fatigue_Score"].strip()
        except (KeyError, TypeError, ValueError):
            # Ignore malformed rows so one bad record does not stop the job.
            continue

        # Filtering step: keep only high-stress students.
        if stress_level >= 7:
            # Mapping step: emit key-value pairs separated by a tab.
            print(f"{fatigue_score}\t{doomscrolling_hours}")


if __name__ == "__main__":
    main()
