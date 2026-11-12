import argparse


def parse_expense(text):
    category, separator, raw_amount = text.partition("=")
    category = category.strip()
    if not separator or not category:
        raise argparse.ArgumentTypeError("Use category=amount, for example food=8000.")
    try:
        amount = int(raw_amount)
    except ValueError:
        raise argparse.ArgumentTypeError("Amount must be a non-negative integer.") from None
    if amount < 0:
        raise argparse.ArgumentTypeError("Amount must be a non-negative integer.")
    return category, amount


def main():
    parser = argparse.ArgumentParser(description="Add up expenses by category.")
    parser.add_argument("expenses", nargs="+", type=parse_expense, metavar="category=amount")
    args = parser.parse_args()

    totals = {}
    for category, amount in args.expenses:
        totals[category] = totals.get(category, 0) + amount

    for category in sorted(totals):
        print(f"{category}: {totals[category]:,}")
    print(f"Total: {sum(totals.values()):,}")


if __name__ == "__main__":
    main()
