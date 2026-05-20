import json
import re
from utils.chatgpt_helper import ask_chatgpt


def process_inventory_command(command):

    prompt = f"""
    Analyze this inventory command.

    Command:
    "{command}"

    Return ONLY valid JSON format:

    {{
      "intent": "update_inventory",
      "action": "",
      "product": "",
      "old_quantity": 0,
      "new_quantity": 0
    }}

    Example:

    Input:
    Increase Laptop inventory from 10 to 50

    Output:
    {{
      "intent": "update_inventory",
      "action": "increase",
      "product": "Laptop",
      "old_quantity": 10,
      "new_quantity": 50
    }}
    """

    response = ask_chatgpt(prompt)

    try:

        cleaned_response = re.sub(
            r"```json|```",
            "",
            response
        ).strip()

        parsed = json.loads(cleaned_response)

        with open(
            "data/inventory.json",
            "r"
        ) as file:

            inventory = json.load(file)

        product_found = False

        for item in inventory:

            if (
                item["product"].lower()
                == parsed["product"].lower()
            ):

                item["stock"] = parsed[
                    "new_quantity"
                ]

                product_found = True

        with open(
            "data/inventory.json",
            "w"
        ) as file:

            json.dump(
                inventory,
                file,
                indent=4
            )

        parsed["status"] = (
            "inventory_updated"
            if product_found
            else "product_not_found"
        )

        return parsed

    except Exception as e:

        return {
            "error": str(e),
            "raw_response": response
        }