# Expense Tracker with Data Insights

![GitHub last commit](https://img.shields.io/github/last-commit/PioBisleri/expense_tracker )
![GitHub issues](https://img.shields.io/github/issues/PioBisleri/expense_tracker )
![GitHub license](https://img.shields.io/github/license/PioBisleri/expense_tracker )
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue )
![Status](https://img.shields.io/badge/status-WIP-orange )

> 🚧 WORK IN PROGRESS - This project is actively under development. Features and structure are subject to change.

A feature-rich personal finance management application built with Python that helps you track spending, categorize expenses, visualize financial trends, and manage budgets with real-time exchange rate support for travelers.

---

📸 Screenshots

Screenshots will be added as features are completed

---

✨ Features

- 💾 Robust Data Management: Persistent storage using JSON/CSV formats
- 🏷️ Smart Categorization: Organize expenses with custom categories and tags
- 📊 Data Visualization: Interactive charts and graphs using matplotlib
- 💱 Live Exchange Rates: Real-time currency conversion via API integration
- 🎯 Budget Tracking: Set spending limits and monitor progress
- 📅 Date Range Filtering: Analyze expenses by custom time periods
- 🖥️ Intuitive GUI: Clean, user-friendly interface built with Tkinter
- 💻 Terminal Interface: Command-line version for quick data access and testing
- 🔍 Search & Filter: Quickly find specific transactions
- 📈 Insight Generation: Automated spending pattern analysis

---

🛠️ Tech Stack

- Language: Python 3.8+
- GUI Framework: Tkinter
- CLI Interface: Standard library
- Data Storage: JSON (primary), CSV (export)
- Visualization: Matplotlib, Seaborn
- APIs: Exchange rate APIs (configurable)
- Data Processing: Pandas, NumPy
- Testing: pytest (planned)

---

📦 Installation

Prerequisites
- Python 3.8 or higher
- pip package manager

Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/PioBisleri/expense_tracker.git 
cd expense_tracker
```

2. Create a virtual environment (recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create the data directory

```bash
mkdir data
```

5. Create API key file (for exchange rates)

```bash
# Create a .env file in the root directory
echo "EXCHANGE_API_KEY=your_api_key_here" > .env
```

---

🚀 Usage

Running the Terminal Interface (Current Phase)

```bash
python terminal_menu.py
```

Running the GUI Application (Future)

```bash
python main.py
```

Terminal Menu Workflow
1. Launch the terminal app: `python terminal_menu.py`
2. Choose from available options:
   - `1. Add Expense`: Enter item, amount, category, and date
   - `2. View Expenses (Date Range)`: Filter expenses by start/end dates
   - `3. View Total by Category`: See spending totals for any category
   - `4. Delete Expense`: Remove entries by ID
   - `5. Exit`: Save changes and close the application
3. All data is automatically saved to `data/expenses.json` on exit

---

📁 Project Structure

```
expense_tracker/
│
├── main.py                   # Application entry point (GUI version)
├── terminal_menu.py          # Terminal-based interface for core functionality
├── requirements.txt          # Python dependencies
├── .env.example             # API key template
├── LICENSE                  # Project license
├── README.md               # This file
│
├── config/
│   ├── __init__.py
│   └── settings.py          # App constants (e.g., DATA_DIR = "data/")
│
├── data/
│   ├── expenses.json        # Primary data storage
│   ├── categories.json      # Category definitions
│   └── __init__.py
│
├── core/
│   ├── expense_manager.py   # CRUD operations for expenses
│   ├── category_manager.py  # Category management logic
│   ├── budget_tracker.py    # Budget calculation engine
│   └── __init__.py
│
├── gui/                     # GUI components (WIP)
│   ├── app_window.py        # Main application window
│   ├── expense_form.py      # Add/edit expense dialog
│   ├── dashboard.py         # Visualization dashboard
│   └── __init__.py
│
├── services/
│   ├── exchange_api.py      # Currency API integration
│   ├── data_export.py       # Export functionality
│   └── __init__.py
│
└── utils/
    ├── visualizer.py        # Chart generation utilities
    ├── validators.py        # Input validation
    └── __init__.py
```

---

🗺️ Roadmap

Phase 1: Core Functionality (In Progress)
- ✅ Basic expense CRUD operations
- ✅ JSON file storage system
- ✅ Terminal interface for data management
- 🟡 Tkinter GUI skeleton (next)
- Category management
- Input validation
- Basic matplotlib integration

Phase 2: Data Analysis (Planned)
- Advanced filtering and search
- Budget tracking system
- Monthly/weekly summaries
- CSV export functionality
- Expense trend analysis

Phase 3: API & Enhancements (Future)
- Live exchange rate integration
- Cloud sync capability
- Receipt scanning (OCR)
- Automated categorization
- Mobile companion app

Phase 4: Polish & Release (Future)
- Comprehensive test suite
- Documentation website
- PyPI package distribution
- Executable builds for Windows/macOS/Linux

---

🤝 Contributing

We welcome contributions! Since this is a WIP project, please check the [Issues](https://github.com/PioBisleri/expense_tracker/issues ) tab for active development areas.

Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings for new functions
- Update documentation as needed
- Test GUI changes on multiple platforms if possible

---

📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

📞 Contact

PioBisleri
- GitHub: [@PioBisleri](https://github.com/PioBisleri )
- Project Repository: [https://github.com/PioBisleri/expense_tracker ](https://github.com/PioBisleri/expense_tracker )
- Issues: [Report Bug/Request Feature](https://github.com/PioBisleri/expense_tracker/issues )

---

🙏 Acknowledgments

- Python community for excellent libraries
- Contributors and testers
- Open source financial tools for inspiration

---

⚠️ Disclaimer

This is a personal project created for educational and practical use. Always keep backups of your financial data. The developers are not responsible for any data loss or financial decisions made based on this application.