
from collections import defaultdict, Counter

def monthly_summary(file_name):
    totals = defaultdict(float)

    try:
        with open(file_name, "r") as file:
            for line in file:
                provider, category, amount, date = line.strip().split(",")

                month = date[:7]
                totals[month] += float(amount)

        print("\n=== Monthly Spending Summary ===")
        for month, total in totals.items():
            print(f"{month}: ${total:.2f}")

    except FileNotFoundError:
        print("No expense file found.")

def frequent_provider(file_name):
    providers = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                provider, category, amount, date = line.strip().split(",")
                providers.append(provider)

        if providers:
            most_common = Counter(providers).most_common(1)[0]
            print(f"\nMost Frequent Provider: {most_common[0]} ({most_common[1]} visits)")
        else:
            print("No provider data available.")

    except FileNotFoundError:
        print("No expense file found.")
