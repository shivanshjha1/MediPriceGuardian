# MediPrice Guardian
### An Integrated Healthcare Information System

MediPrice Guardian is a Python-based healthcare information system designed to demonstrate medical procedure cost estimation, hospital price comparison, government scheme mapping, and price-gouging detection.

## 1. Project Features

1. **Hospital Directory** – View hospital information and pricing.
2. **Medical Procedures** – View available procedures and their consumables.
3. **Government Schemes** – View the scheme directory.
4. **Procedure Cost Calculator** – Estimate procedure costs using surgeon fees and consumable prices.
5. **Hospital Price Comparison** – Compare estimated procedure costs across hospitals.
6. **Scheme-Hospital Mapper** – Check which listed hospitals accept a selected scheme.
7. **Overall Price Gouging Report** – Identify consumable prices exceeding the configured threshold.

## 2. Price-Gouging Detection Rule

The system uses a threshold of 150% of the market price.

**Formula:**

Hospital Price > Market Price × 1.5

A price exactly equal to 150% is not flagged.

## 3. Technology Used

- Python
- Object-Oriented Programming
- JSON
- File Handling
- Unit Testing

## 4. Project Structure

```text
MediPriceGuardian/
├── main.py
├── models.py
├── data_manager.py
├── price_engine.py
├── hospital_data.json
├── requirements.txt
├── test_project.py
├── README.md
└── .gitignore
```

## 5. Requirements

- Python 3
- VS Code or another Python editor

The project currently uses Python standard-library modules and requires no third-party packages.

## 6. How to Run

1. Clone or download this repository.
2. Open the project folder in Terminal.
3. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment on macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## 7. Run Automated Tests

Execute:

```bash
python -m unittest -v test_project.py
```

The current test suite contains six automated tests.

## 8. Important Disclaimer

This project uses demonstration hospital prices and scheme mappings for educational purposes. The data is not verified real-world hospital pricing or official scheme eligibility information. Always verify actual prices, hospital participation, and eligibility with the relevant hospital or official authority.

## 9. Project Purpose

This project demonstrates how Python programming, data management, object-oriented design, and automated testing can be combined to build a basic healthcare information system.