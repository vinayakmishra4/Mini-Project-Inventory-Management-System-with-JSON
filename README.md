<h1 align="center">📦 Inventory Management System</h1>

<p align="center">
  <b>A Python-based CLI application to manage products, categories, and transactions — with persistent JSON storage.</b>
</p>

<p align="center">
  <a href="https://github.com/your-username/inventory_management">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white" alt="GitHub Repo"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white" alt="Python Version"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative&logoColor=white" alt="License"/>
  </a>
</p>

---

## 🧭 Table of Contents

- [Overview](#overview)
- [✨ Features](#-features)
- [🧰 Tech Stack](#-tech-stack)
- [⚙️ System Requirements](#️-system-requirements)
- [📁 Project Structure](#-project-structure)
- [⚡ How It Works](#-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [🧪 Running Tests](#-running-tests)
- [⚠️ Limitations](#️-limitations)
- [🌱 Future Enhancements](#-future-enhancements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🧩 Overview

This **Inventory Management System** is a modular and lightweight **Python application** designed to help efficiently manage inventory data using **JSON files** — no complex database setup required.  

It’s ideal for:
- 🏪 Small businesses tracking sales and stock  
- 🎓 Students learning Python, data handling, and modular design  
- 🧑‍💻 Developers prototyping POS (Point-of-Sale) systems  

With a clean architecture and a simple CLI, it demonstrates **real-world inventory control principles**, including data validation, persistence, and separation of logic.

---

## ✨ Features

✅ **Product Management** – Add, update, or remove items with names, prices, and quantities.  
✅ **Category Management** – Organize products by categories for easier tracking.  
✅ **Transaction Recording** – Log every sale or purchase and auto-update inventory.  
✅ **History Tracking** – Keep a record of past transactions for review.  
✅ **Persistent Storage** – Data remains saved even after closing the program.  
✅ **Command-Line Interface** – Interact easily through terminal menus.  
✅ **Unit Testing** – Ensures system reliability with `pytest`.  

---

## 🧰 Tech Stack

| Technology | Purpose | Why It’s Used |
|-------------|----------|---------------|
| 🐍 **Python 3.x** | Core programming language | Easy to learn, widely used for scripting and automation |
| 📄 **JSON** | Data persistence | Lightweight format for storing structured data |
| 💻 **CLI** | User interface | Simplifies user interaction without GUI overhead |
| 🧪 **pytest** | Testing framework | Ensures robust and maintainable code through tests |

---

## ⚙️ System Requirements

- Python **3.8+**  
- Works on **Windows**, **macOS**, or **Linux**  
- Terminal / Command Prompt access  

---

## 📁 Project Structure

```
inventory_management/
│
├── data/                 
│   ├── products.json
│   ├── categories.json
│   └── transactions.json
│
├── src/                  
│   ├── __init__.py
│   ├── main.py
│   ├── inventory.py
│   ├── utils.py
│   ├── product_manager.py
│   ├── category_manager.py
│   └── transaction_manager.py
│
├── tests/                # Unit tests
├── requirements.txt      
├── config.json           
└── README.md             
```

---

## ⚡ How It Works

1. 📂 Data is loaded from JSON files in the `data/` directory.  
2. 🧠 Managers (`product_manager.py`, `category_manager.py`, `transaction_manager.py`) handle logic.  
3. 💬 The CLI (`main.py`) presents menus for actions like adding or viewing products.  
4. 💾 Changes are saved automatically to JSON for persistence.  

**Example Workflow:**
- You add a product: *“Laptop” → Category: Electronics → Price: 700 → Quantity: 10*  
- You record a sale: *2 Laptops sold → Quantity updates to 8*  
- You check history: Transaction logged with timestamp and total value.  

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/your-username/inventory_management.git
cd inventory_management
pip install -r requirements.txt
python src/main.py
```

**Sample CLI Session:**
```
Welcome to Inventory Management System
---------------------------------------
1. Manage Products
2. Manage Categories
3. Record Transaction
4. View Transactions
5. Exit

Enter your choice: 1
> Add Product
> Product added successfully!
```

---

## 🎯 Use Cases

- 🏪 **Retail Shops** – Manage daily stock and sales efficiently.  
- 🧰 **Warehouse Management** – Keep track of quantities and restocks.  
- 🎓 **Student Projects** – Perfect example of file handling, OOP, and modular programming.  
- 💡 **Developer Demos** – Quick prototype for a Point-of-Sale or backend logic system.  

---

## 🧪 Running Tests

Run all unit tests with:

```bash
pytest tests/
```

Ensure all tests pass before contributing or adding new features.

---

## ⚠️ Limitations

- ❌ Not suited for enterprise-scale data  
- 🔒 No authentication or encryption  
- 🗃️ JSON files may not handle concurrent writes efficiently  
- 🖥️ CLI-only (no GUI — yet!)

---

## 🌱 Future Enhancements

- 🧾 **Report Generation (CSV, PDF)** – To provide exportable summaries for analysis.  
- 🌐 **Web Dashboard** – Build a web-based UI using Flask or Django.  
- 🧍 **User Authentication** – Add admin and staff roles for access control.  
- ☁️ **Database Integration** – Use SQLite or PostgreSQL for larger datasets.  
- 📊 **Analytics Module** – Offer inventory trends, sales charts, and insights.  

---

## 🤝 Contributing

Contributions are welcome! 💡

1. Fork the repo  
2. Create your feature branch  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes  
4. Push to your branch  
5. Open a Pull Request  

---

## 📜 License

This project is licensed under the **MIT License © 2025**.

---

<p align="center">
  Made with ❤️ and Python 🐍
</p>