def process_inventory_command(command):

    command = command.lower()

    if "increase" in command:
        action = "increase"
    else:
        action = "update"

    return {
        "intent": "update_inventory",
        "action": action,
        "product": "Laptop",
        "old_quantity": 10,
        "new_quantity": 50,
        "status": "inventory_updated"
    }