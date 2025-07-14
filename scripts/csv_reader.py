import csv

def read_csv(filepath):
    """Reads a CSV file and returns a list of dictionaries (rows)."""
    data = []
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    return data


def print_all_rows(data):
    """Prints all rows from the CSV."""
    print("\n--- All Rows ---")
    for i, row in enumerate(data, start=1):
        print(f"Row {i}: {row}")


def filter_by_column(data, column_name, value):
    """Returns rows where the column matches a given value."""
    return [row for row in data if row.get(column_name) == value]


def increase_prices(data, price_column, increase_by):
    """Increases price values in a given column by a fixed amount."""
    for row in data:
        try:
            original = float(row[price_column])
            row[price_column] = round(original + increase_by, 2)
        except (ValueError, KeyError):
            row[price_column] = 'N/A'
    return data


def main():
    filepath = 'scripts/products.csv'  # Example CSV file
    data = read_csv(filepath)

    if not data:
        return

    print_all_rows(data)

    # Example: Filter products by category
    category = 'Books'
    filtered = filter_by_column(data, 'category', category)
    print(f"\n--- Products in category '{category}' ---")
    for row in filtered:
        print(row)

    # Example: Increase prices by 2.50
    updated_data = increase_prices(data, 'price', 2.50)
    print("\n--- Updated Prices ---")
    for row in updated_data:
        print(row)


if __name__ == "__main__":
    main()
