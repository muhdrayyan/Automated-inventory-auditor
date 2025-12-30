inventory = [{'name': 'Vitamin C', 'stock': 70, 'expired': False},
             {'name': 'Amoxicillin', 'stock': 30, 'expired': True},
             {'name': 'Paracetamol', 'stock': 20, 'expired': False},
             {'name': 'Ibupropen', 'stock': 100, 'expired': False},
             {'name': 'Asprin', 'stock': -5, 'expired': False},
             {'name': 'Cough Syrup', 'stock': 20, 'expired': False},
             {'name': 'multivitamins', 'stock': 0, 'expired': False}
]
to_restock = [] # shopping list for items to restock
do_dispose = []  # list for items to dispose of
for index, item in enumerate(inventory):
    if item['expired'] == True:
        print(f"DANGEROUS ITEM DETECTED: '{item['name']}' is expired. REMOVE IMMEDIATELY!")
        do_dispose.append(item['name']) # add items that need to be disposed of to the list
        to_restock.append(item['name']) # also add to restock list
    elif item['stock'] <= 0:
        to_restock.append(item['name']) # add items that need to be restock to the list
        print(f"OUT OF STOCK: '{item['name']}' is out of stock")
print(f"Total items to restock: {len(to_restock)}")

print("--- ITEMS TO RESTOCK ---")
for item in to_restock:
    print(f"- {item}")

print("--- ITEMS TO DISPOSE OF ---")
for item in do_dispose:
    print(f"- {item}")
