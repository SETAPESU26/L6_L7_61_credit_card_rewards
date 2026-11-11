def mask_card_number(number):
    """Mask a card number, showing only its last four digits."""
    if not isinstance(number, str) or not number.strip():
        return "*" * 16

    digits = "".join(ch for ch in number if ch.isdigit())

    if not digits:
        return "*" * 16

    return "*" * 12 + digits[-4:]


def parse_transaction(line):
    """Parse date, category and amount safely."""
    if not isinstance(line, str):
        return ("unknown", 0)

    parts = line.split(",")

    if len(parts) != 3:
        return ("unknown", 0)

    date = parts[0].strip()
    category = parts[1].strip().lower()
    amount_text = parts[2].strip().replace(",", "")

    if not date or not category:
        return ("unknown", 0)

    try:
        amount = int(amount_text)
    except (ValueError, TypeError):
        return ("unknown", 0)

    return (category, amount)


def parse_statement_total(text):
    """Safely extract a statement total."""
    if not isinstance(text, str) or ":" not in text:
        return 0

    amount = text.split(":", 1)[1].strip()
    amount = amount.replace(",", "")

    try:
        return int(amount)
    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running mask_card_number ====")
    value = input("Enter a card number (e.g. 4111 1111 1111 1234): ")
    print("Masked card number:", mask_card_number(value))

    print("\n==== Running parse_transaction ====")
    value = input("Enter a transaction as DATE,CATEGORY,AMOUNT (e.g. 2026-11-05,dining,1550): ")
    print("Category and amount:", parse_transaction(value))

    print("\n==== Running parse_statement_total ====")
    value = input("Enter the statement total line (e.g. Total: 12,500): ")
    print("Statement total:", parse_statement_total(value))


if __name__ == "__main__":
    main()
