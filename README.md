Asset Management System

Overview
The Asset Management System** is a Python-based application with a **Tkinter GUI** that allows users to track and manage their financial assets. Users can add various asset types, view their portfolio, and sell assets when needed.

Features
- Add Assets: Users can input asset details such as name, type, quantity, purchase price, and date.
- Real Estate Support: Includes an address field for real estate assets.
- Portfolio Management: Displays all added assets in a structured table format.
- Dynamic Asset Pricing: Fetches the latest asset prices via the `finance` module.
- User-friendly Interface: Designed with a clean and simple Tkinter GUI.

Installation
git clone https://github.com/yourusername/asset-management-system.git
cd asset-management-system

Prerequisites
Ensure you have **Python 3.x** installed on your system.

Clone the Repository
bash
git clone https://github.com/yourusername/asset-management-system.git
cd asset-management-system

Install Dependencies
bash
pip install -r requirements.txt  # If a requirements.txt file is available


Usage
Run the application using:
bash
python main.py


File Structure

asset-management-system 
│── finance.py         # Handles fetching asset prices
│── portfolio.py       # Manages adding, viewing, and selling assets
│── gui.py             # Contains the Tkinter-based GUI
│── utils.py           # Helper functions (e.g., placeholders for inputs)
│── main.py            # Entry point for the application
│── README.md          # Project documentation
│── .gitignore         # Ignore unnecessary files like __pycache__
```

Contributing
Feel free to fork this repository, create feature branches, and submit pull requests!

License
This project is licensed under the **MIT License**.

---
Happy coding! 🚀

