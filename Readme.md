# Smart POS AI Assistant

An AI-powered Smart POS (Point of Sale) Assistant built using Python, Flask, and LLM APIs to automate product management and inventory operations.

## Project Objective

This project simulates AI-powered features for a Smart POS platform to automate:

- Product listing generation
- Inventory management using natural language commands

This project implements the following modules:

### Module 1 – AI Assisted Product Listing
### Module 2 – Voice/Text Based Inventory Operations (Text-Based)

---

## Features

### 1. AI Assisted Product Listing

Generate intelligent product information from product details.

#### Input
Product name/details

#### AI Features
- Generate product description
- Suggest product category
- Suggest GST rate
- Suggest HSN code
- Generate keywords/tags

#### Example Input

```json
{
  "product_name": "Dell Inspiron 15 Laptop 16GB RAM Intel i5"
}
```

#### Example Output

```json
{
  "product_name": "Dell Inspiron 15 Laptop 16GB RAM Intel i5",
  "description": "Mid-range Dell laptop featuring Intel i5 processor and 16GB RAM suitable for productivity and multitasking.",
  "category": "Laptops",
  "gst_rate": "18%",
  "hsn_code": "8471",
  "keywords": [
    "Dell",
    "Laptop",
    "Intel i5",
    "16GB RAM"
  ]
}
```

---

### 2. Text-Based Inventory Operations

Allows inventory updates using natural language.

#### Input Example

```json
{
  "command": "Increase Laptop inventory from 10 to 50"
}
```

#### Features
- Detect user intent
- Extract structured inventory action
- Generate JSON output
- Simulate inventory update workflow

#### Example Output

```json
{
  "intent": "update_inventory",
  "action": "increase",
  "product": "Laptop",
  "old_quantity": 10,
  "new_quantity": 50,
  "status": "inventory_updated"
}
```

---

## Tech Stack

- Python
- Flask
- OpenRouter API (LLM)
- JSON Dataset
- Postman

---

## Project Structure

```txt
smart-pos-ai/
│── app.py
│── requirements.txt
│── README.md
│── .env
│
├── data/
│   └── inventory.json
│
├── modules/
│   ├── product_listing.py
│   └── inventory_operations.py
│
├── utils/
│   └── chatgpt_helper.py
│
└── venv/
```

---

## Installation

### Clone Repository

```bash
git clone <your_repo_link>
cd smart-pos-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
```

---

## Run Project

```bash
py app.py
```

Server runs on:

```txt
http://127.0.0.1:5000
```

---

## API Endpoints

### Generate Product Listing

**POST**

```txt
/generate-product
```

---

### Inventory Command

**POST**

```txt
/inventory-command
```

---

## Testing

Use Postman to test APIs.

---

## Future Improvements

- Voice-based inventory operations
- Database integration
- Sales analytics dashboard
- Admin UI

---

## Author

Shitij Alok