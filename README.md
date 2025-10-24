<p align="center">
  <img src="https://img.icons8.com/fluency/96/inventory.png" alt="Inventory Icon"/>
</p>

<h1 align="center">📦 Inventory Management System</h1>

<p align="center">
  A Python-based Inventory Management System using JSON for persistent data storage.
  Manage products, categories, and transactions with ease through a simple CLI.
</p>

<p align="center">
  <a href="https://github.com/your-username/inventory_management">
    <img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github" alt="GitHub Repo"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python Version"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License"/>
  </a>
</p>

---

## 📝 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Requirements](#system-requirements)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation & Usage](#installation--usage)
- [Example Usage](#example-usage)
- [Running Tests](#running-tests)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🧩 Project Overview

This Inventory Management System is a **modular Python project** that uses JSON files to store data.  
It allows users to manage:

- **Products**  
- **Categories**  
- **Transactions (Sales/Purchases)**  

The project is structured to **separate concerns**, making it easier to maintain, test, and extend.

---

## 🔹 Features

- ✅ Add, update, delete, and view products  
- ✅ Manage categories for products  
- ✅ Record transactions (sales/purchases)  
- ✅ View transaction history  
- ✅ Persistent storage with JSON (`data/` folder)  
- ✅ Command-line interface (CLI) for user interaction  
- ✅ Modular design with separate managers for products, categories, and transactions  
- ✅ Unit tests for core functionality  

---

## ⚙️ Technologies Used

| Technology       | Purpose |
|-----------------|---------|
| Python 3.x      | Core programming language |
| JSON            | Persistent data storage |
| CLI             | Command-line interface |
| pytest          | Unit testing framework |

---

## 💻 System Requirements

- Python 3.8+ installed  
- Windows / macOS / Linux  
- Terminal or command prompt  

---

## 📂 Project Structure

```

inventory_management/
│
├── data/                 # JSON files storing persistent data
│   ├── products.json
│   ├── categories.json
│   └── transactions.json
│
├── src/                  # Main source code
│   ├── **init**.py
│   ├── main.py
│   ├── inventory.py
│   ├── utils.py
│   ├── product_manager.py
│   ├── category_manager.py
│   └── transaction_manager.py
│
├── requirements.txt      # Dependencies (if any)
├── README.md
└── config.json           # Configuration file (optional settings)

````

---

## ⚡ How It Works

1. Program loads data from the JSON files in `data/`.  
2. Users interact via the CLI in `src/main.py`.  
3. CRUD operations for **products, categories, and transactions** are handled by separate managers (`product_manager.py`, `category_manager.py`, `transaction_manager.py`).  
4. Utility functions (`utils.py`) handle validation, formatting, and shared operations.  
5. Data is automatically saved back to JSON after each operation.  

---

## 🏗️ Installation & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/inventory_management.git
cd inventory_management
````

2. **Install dependencies** (if any):

```bash
pip install -r requirements.txt
```

3. **Run the application:**

```bash
python src/main.py
```

4. Follow the **interactive CLI menu** to manage products, categories, and transactions.

---

## 🖥️ Example Usage

```
Welcome to Inventory Management System
--------------------------------------
1. Manage Products
2. Manage Categories
3. Record Transaction
4. View Transactions
5. Exit

Enter your choice: 1

[Product Menu]
1. Add Product
2. Update Product
3. Delete Product
4. View Products
5. Back
```

*Similar menus exist for categories and transactions.*

---

## 🧪 Running Tests

This project includes **unit tests** using `pytest`. Run tests as follows:

```bash
pytest tests/
```

Ensure all core functionality passes before adding new features.

---

## ⚠️ Limitations

* Not suitable for large-scale enterprise usage
* No authentication or encryption
* JSON files may not handle concurrent access efficiently
* CLI-only interface (no GUI yet)

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch (`git checkout -b feature-name`)
3. Make your changes
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License

MIT License © 2025

---

<p align="center">
  Made with ❤️ using Python
</p>
```
---