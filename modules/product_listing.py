import json
import re
from utils.chatgpt_helper import ask_chatgpt


def generate_product_listing(product_name):

    prompt = f"""
    Analyze this product:

    {product_name}

    Generate the following in VALID JSON format only:

    {{
      "product_name": "",
      "description": "",
      "category": "",
      "gst_rate": "",
      "hsn_code": "",
      "keywords": []
    }}

    Rules:
    - Suggest Indian GST rate
    - Suggest HSN code
    - Generate 5 keywords
    - Return ONLY JSON
    """

    response = ask_chatgpt(prompt)

    try:
        # remove markdown if chatgpt sends ```json
        cleaned_response = re.sub(
            r"```json|```",
            "",
            response
        ).strip()

        return json.loads(cleaned_response)

    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response
        }