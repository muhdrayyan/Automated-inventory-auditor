import csv

def audit_inventory(file_name):
    to_restock = []
    to_dispose = []

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            name = item['name']
            stock = int(item['stock'])
            expired = item['expired'] == 'True'

            if expired:
                to_dispose.append(name)
                to_restock.append(name)
            elif stock <= 0:
                to_restock.append(name)

    return to_restock, to_dispose


def generate_report(restock, dispose):
    with open("audit_report.txt", "w") as report:
        report.write("INVENTORY AUDIT REPORT\n")
        report.write("=" * 30 + "\n\n")

        report.write(f"Total items to restock: {len(restock)}\n\n")

        report.write("ITEMS TO RESTOCK:\n")
        for item in restock:
            report.write(f"- {item}\n")

        report.write("\nITEMS TO DISPOSE:\n")
        for item in dispose:
            report.write(f"- {item}\n")

    print("Report generated successfully: audit_report.txt")


if __name__ == "__main__":
    restock_list, dispose_list = audit_inventory("inventory.csv")
    generate_report(restock_list, dispose_list)
