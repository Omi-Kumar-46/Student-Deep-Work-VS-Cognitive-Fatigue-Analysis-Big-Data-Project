#!/usr/bin/env python3
"""
Reducer for Hadoop Streaming.

Input:  Sorted mapper output as Mental_Fatigue_Score<TAB>Doomscrolling_Hours.
Output: Mental_Fatigue_Score<TAB>Average_Doomscrolling_Hours.
"""

import sys


def emit_average(fatigue_score, total_doomscrolling, count):
    """Print the average doomscrolling hours for one fatigue category."""
    if fatigue_score is not None and count > 0:
        average = total_doomscrolling / count
        print(f"{fatigue_score}\t{average:.2f}")


def main():
    current_fatigue_score = None
    total_doomscrolling = 0.0
    count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            fatigue_score, doomscrolling_text = line.split("\t", 1)
            doomscrolling_hours = float(doomscrolling_text)
        except ValueError:
            # Ignore malformed mapper output.
            continue

        # Hadoop sorts mapper output by key, so equal keys arrive together.
        if current_fatigue_score == fatigue_score:
            total_doomscrolling += doomscrolling_hours
            count += 1
        else:
            # Finished one key group; emit its aggregate before starting another.
            emit_average(current_fatigue_score, total_doomscrolling, count)
            current_fatigue_score = fatigue_score
            total_doomscrolling = doomscrolling_hours
            count = 1

    # Emit the final key group after stdin is exhausted.
    emit_average(current_fatigue_score, total_doomscrolling, count)


if __name__ == "__main__":
    main()
