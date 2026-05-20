from flask import Flask, request, jsonify
from modules.product_listing import generate_product_listing
from modules.inventory_operations import process_inventory_command

app = Flask(__name__)


@app.route("/")
def home():
    return "Smart POS AI Running"


@app.route("/generate-product", methods=["POST"])
def generate_product():

    data = request.get_json()

    product_name = data.get("product_name")

    if not product_name:
        return jsonify({
            "error": "Product name required"
        }), 400

    result = generate_product_listing(product_name)

    return jsonify(result)


@app.route("/inventory-command", methods=["POST"])
def inventory_command():

    data = request.get_json()

    command = data.get("command")

    if not command:
        return jsonify({
            "error": "Command required"
        }), 400

    result = process_inventory_command(command)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)