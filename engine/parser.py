import csv
import sys
import subprocess
from datetime import datetime

from utils.loader import (
    ACTIVE_PORTFOLIO,
    PORTFOLIO_FILE
)

VALID_FREQUENCIES = {
    "monthly",
    "quarterly",
    "yearly"
}

monthly_total = 0.0
yearly_total = 0.0

processed_rows = 0
skipped_rows = 0

report_lines = []
spreadsheet_rows = []

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

divider = "=" * 60
subdivider = "-" * 60

header = [
    divider,
    "DIVAGG :: DIVIDEND AGGREGATION REPORT",
    divider,
    f"GENERATED : {timestamp}",
    f"ACTIVE PORTFOLIO : {ACTIVE_PORTFOLIO}",
    ""
]

for line in header:
    print(line)
    report_lines.append(line)

try:

    with open(PORTFOLIO_FILE, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        table_header = (
            f"{'TICKER':<10}"
            f"{'SHARES':>10}"
            f"{'DIVIDEND':>15}"
            f"{'FREQ':>15}"
            f"{'MONTHLY':>15}"
        )

        print(table_header)
        print(subdivider)

        report_lines.append(table_header)
        report_lines.append(subdivider)

        for row in reader:

            try:

                ticker = row['ticker'].strip()
                shares = float(row['shares'])
                dividend = float(row['dividend'])
                frequency = row['frequency'].strip().lower()

                if not ticker:
                    raise ValueError("Missing ticker")

                if shares < 0:
                    raise ValueError("Negative shares")

                if dividend < 0:
                    raise ValueError("Negative dividend")

                if frequency not in VALID_FREQUENCIES:
                    raise ValueError("Invalid frequency")

                payout = shares * dividend

                if frequency == "monthly":
                    monthly_income = payout
                    yearly_income = payout * 12

                elif frequency == "quarterly":
                    monthly_income = (payout * 4) / 12
                    yearly_income = payout * 4

                elif frequency == "yearly":
                    monthly_income = payout / 12
                    yearly_income = payout

                monthly_total += monthly_income
                yearly_total += yearly_income

                processed_rows += 1

                output_line = (
                    f"{ticker:<10}"
                    f"{shares:>10.2f}"
                    f"{dividend:>15.2f}"
                    f"{frequency:>15}"
                    f"{monthly_income:>15,.2f}"
                )

                print(output_line)
                report_lines.append(output_line)

                spreadsheet_rows.append({
                    "ticker": ticker,
                    "shares": shares,
                    "dividend": dividend,
                    "frequency": frequency,
                    "monthly_income": round(monthly_income, 2),
                    "yearly_income": round(yearly_income, 2)
                })

            except Exception as row_error:

                skipped_rows += 1

                error_line = (
                    f"[SKIPPED] "
                    f"{row} :: {row_error}"
                )

                print(error_line)
                report_lines.append(error_line)

except FileNotFoundError:

    print(f"[ERROR] Portfolio not found:")
    print(PORTFOLIO_FILE)

    sys.exit(1)

except Exception as error:

    print(f"[ERROR] {error}")
    sys.exit(1)

summary_block = [
    "",
    subdivider,
    f"PROCESSED ROWS : {processed_rows}",
    f"SKIPPED ROWS   : {skipped_rows}",
    subdivider,
    "",
    "COBOL AGGREGATION TOTALS",
    subdivider
]

for line in summary_block:
    print(line)
    report_lines.append(line)

try:

    cobol_input = (
        f"{monthly_total:.2f}\n"
        f"{yearly_total:.2f}\n"
    )

    result = subprocess.run(
        ["./compute"],
        input=cobol_input,
        text=True,
        capture_output=True
    )

    cobol_output = result.stdout.strip().splitlines()

    if len(cobol_output) >= 2:

        monthly_line = (
            f"MONTHLY TOTAL : "
            f"${cobol_output[0]}"
        )

        yearly_line = (
            f"YEARLY TOTAL  : "
            f"${cobol_output[1]}"
        )

        print(monthly_line)
        print(yearly_line)

        report_lines.append(monthly_line)
        report_lines.append(yearly_line)

    else:

        print("[ERROR] Unexpected COBOL output")

except Exception as cobol_error:

    print(f"[ERROR] COBOL FAILURE :: {cobol_error}")

report_path = (
    f"../reports/"
    f"{ACTIVE_PORTFOLIO}_report_{filename_timestamp}.txt"
)

with open(report_path, "w") as report_file:
    report_file.write("\n".join(report_lines))

spreadsheet_path = (
    f"../exports/"
    f"{ACTIVE_PORTFOLIO}_export_{filename_timestamp}.csv"
)

with open(spreadsheet_path, "w", newline='') as csv_export:

    fieldnames = [
        "ticker",
        "shares",
        "dividend",
        "frequency",
        "monthly_income",
        "yearly_income"
    ]

    writer = csv.DictWriter(
        csv_export,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for export_row in spreadsheet_rows:
        writer.writerow(export_row)

    writer.writerow({})

    writer.writerow({
        "ticker": "TOTAL",
        "monthly_income": round(monthly_total, 2),
        "yearly_income": round(yearly_total, 2)
    })

footer = [
    "",
    subdivider,
    f"REPORT EXPORTED : {report_path}",
    f"CSV EXPORTED    : {spreadsheet_path}",
    divider,
    "END OF REPORT",
    divider
]

for line in footer:
    print(line)
    report_lines.append(line)
