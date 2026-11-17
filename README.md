# 🏥 MediPrice Guardian

### An Integrated Healthcare Information System

**MediPrice Guardian** is a Python-based healthcare information system developed as an educational project to demonstrate medical cost estimation, hospital price comparison, government healthcare scheme information, and transparent healthcare pricing.

The application is built using **Python, Streamlit, Object-Oriented Programming (OOP), and JSON**.

It provides an interactive web interface where users can explore hospital information, estimate medical procedure costs, compare hospital prices, and view government healthcare programmes.

> **Important Disclaimer:** This project uses demonstration data. Hospital prices, treatment estimates, and scheme mappings are not verified real-world healthcare information.

**---**

## 1. Project Features

MediPrice Guardian includes five main pages.

### 🏠 Dashboard

The dashboard provides an overview of the application.

**Features:**

- Displays the total number of hospitals.

- Displays the total number of medical procedures.

- Displays the number of government scheme entries.

- Introduces the main features of the application.

- Provides a clean and user-friendly interface.

### 🏥 Hospital Directory

The Hospital Directory allows users to explore hospital information.

**Features:**

- View hospitals available in the dataset.

- View consumable prices for selected hospitals.

- See government schemes listed by each hospital.

- Explore hospital-specific pricing information.

### 💰 Medical Cost Estimator

The Medical Cost Estimator calculates the estimated cost of a medical procedure at a selected hospital.

**Features:**

- Select a hospital.

- Select a medical procedure.

- Calculate the estimated treatment cost.

- View the surgeon fee.

- View the estimated total cost.

- Examine the consumable cost breakdown.

- Compare consumable prices with demonstration market prices.

**Cost Calculation Formula:**

```python

estimated_cost = surgeon_fee + total_consumable_cost

```

The estimate combines the procedure's surgeon fee and the hospital's consumable charges.

### 📊 Hospital Price Comparison

This feature allows users to compare estimated procedure costs across hospitals.

**Features:**

- Select a medical procedure.

- Compare estimated costs at different hospitals.

- View a hospital-wise comparison table.

- Visualize costs using a horizontal bar chart.

- Identify the hospital with the lowest complete estimate.

### 🏛️ Government Scheme Finder

The Government Scheme Finder provides information about government healthcare schemes and programmes.

**Features:**

- Select a healthcare scheme.

- View its name and code.

- Read the scheme description.

- View listed benefits.

- Explore eligibility information.

- Find hospitals associated with the selected scheme in the demonstration dataset.

Some entries are public-health programmes or digital-health initiatives rather than health insurance schemes.

Actual eligibility, benefits, and hospital participation must be verified through official sources.

**---**

## 2. Price-Gouging Detection (Backend)

MediPrice Guardian includes a Python backend module that detects potentially excessive consumable prices.

This functionality is retained in the backend but is not displayed in the current Streamlit Medical Cost Estimator.

### Detection Rule

The system currently uses a demonstration threshold of **20% above market price**.

**Formula:**

```python

threshold_price = market_price * 1.20

```

A price alert is generated when:

```python

hospital_price > threshold_price

```

### Example

| Market Price | Hospital Price | Result |

|---|---|---|

| ₹100 | ₹110 | No Alert |

| ₹100 | ₹120 | No Alert |

| ₹100 | ₹121 | Alert |

| ₹100 | ₹150 | Alert |

A hospital price exactly equal to 120% of the market price is not flagged.

**Note:** This is a project-defined detection rule, not an official legal or regulatory standard for determining price gouging.

**---**

## 3. Technologies Used

| Technology | Purpose |

|---|---|

| Python 3 | Core programming language |

| Streamlit | Interactive web application |

| Object-Oriented Programming | Backend models and program structure |

| JSON | Healthcare demonstration dataset |

| File Handling | Reading and managing data |

| Python Unit Testing | Testing backend functionality |

| Git | Version control |

| GitHub | Source code hosting |

| VS Code | Development environment |

**---**

## 4. Project Architecture

The application uses a modular architecture that separates the user interface, data management, and calculation logic.

```text

                  USER

                   |

                   v

           STREAMLIT FRONTEND

                 app.py

                   |

          +--------+--------+

          |                 |

          v                 v

      DATA MANAGER      PRICE ENGINE

     data_manager.py   price_engine.py

          |                 |

          v                 |

     JSON DATA FILE         |

   hospital_data.json       |

          |                 |

          v                 |

      DATA MODELS           |

       models.py            |

          |                 |

          +--------+--------+

                   |

                   v

          ESTIMATED COSTS

          AND INFORMATION

                   |

                   v

           STREAMLIT DISPLAY

```

The frontend loads information through the data manager and uses the price engine for cost calculations.

**---**

## 5. Project Structure

```text

MediPriceGuardian/

├── .streamlit/

│   └── config.toml

├── app.py

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

### File Descriptions

| File | Description |

|---|---|

| `app.py` | Main Streamlit web application |

| `main.py` | Python command-line application |

| `models.py` | Hospital, procedure, consumable, and scheme classes |

| `data_manager.py` | Loads and manages JSON data |

| `price_engine.py` | Cost estimation and price-alert calculations |

| `hospital_data.json` | Demonstration healthcare dataset |

| `requirements.txt` | Python dependencies |

| `test_project.py` | Automated unit tests |

| `.streamlit/config.toml` | Streamlit theme configuration |

| `.gitignore` | Files excluded from version control |

**---**

## 6. Demonstration Dataset

The project includes a sample healthcare dataset containing:

- **8 hospitals**

- **3 medical procedures**

- **6 medical consumables**

- **25 government scheme or programme entries**

The dataset is stored in:

```text

hospital_data.json

```

The information is intended for demonstrating application functionality.

Hospital prices, scheme associations, and medical treatment estimates are illustrative.

Some scheme entries are placeholders and do not represent verified government programmes.

**---**

## 7. System Requirements

Before running the project, ensure that you have:

- Python 3 installed.

- Git installed, if cloning the repository.

- An internet connection to install dependencies.

- VS Code or another code editor.

- A modern web browser.

**---**

## 8. Installation and Setup

### Step 1: Clone the Repository

Open Terminal and run:

```bash

git clone https://github.com/shivanshjha1/MediPriceGuardian.git

```

### Step 2: Open the Project Directory

```bash

cd MediPriceGuardian

```

### Step 3: Create a Virtual Environment

```bash

python3 -m venv .venv

```

### Step 4: Activate the Virtual Environment

**macOS / Linux:**

```bash

source .venv/bin/activate

```

**Windows PowerShell:**

```powershell

.venv\Scripts\Activate.ps1

```

**Windows Command Prompt:**

```cmd

.venv\Scripts\activate.bat

```

### Step 5: Install Dependencies

```bash

python -m pip install -r requirements.txt

```

Wait until the required Python packages are installed.

**---**

## 9. Run the Streamlit Web Application

Start the application using:

```bash

streamlit run app.py

```

Streamlit will display a local address, usually:

```text

http://localhost:8501

```

Open this address in your web browser.

### Available Pages

1. Dashboard

2. Hospital Directory

3. Medical Cost Estimator

4. Hospital Price Comparison

5. Government Scheme Finder

To stop the application, press **Ctrl + C** in Terminal.

**---**

## 10. Run the Python Command-Line Application

The project also includes a command-line interface.

Run:

```bash

python main.py

```

This allows users to access the project's Python command-line functionality separately from the Streamlit website.

**---**

## 11. Automated Unit Testing

MediPrice Guardian includes automated tests for backend functionality.

Run:

```bash

python -m unittest -v test_project.py

```

The test module contains six automated tests.

These tests are intended to validate data handling, pricing calculations, and related backend behavior.

The price-threshold tests should reflect the current 20% above-market detection rule.

When all tests pass, the terminal displays:

```text

OK

```

If a test fails, review the reported assertion and verify that its expected result matches the current application logic.

**---**

## 12. Streamlit User Interface

The project uses a custom Streamlit theme.

The theme configuration is stored in:

```text

.streamlit/config.toml

```

### Interface Features

- Sidebar navigation

- Dropdown menus

- Hospital information tables

- Medical cost summaries

- Consumable cost breakdowns

- Horizontal hospital comparison charts

- Government scheme information

- Healthcare-inspired teal and white theme

The interface is designed to make the demonstration data easier to understand.

**---**

## 13. Deploying the Application Online

MediPrice Guardian can be deployed using **Streamlit Community Cloud**.

### Deployment Instructions

1. Push the latest project files to GitHub.

2. Open https://share.streamlit.io/.

3. Sign in with GitHub.

4. Create a new application.

5. Select the `MediPriceGuardian` repository.

6. Choose the `main` branch.

7. Enter `app.py` as the main application file.

8. Deploy the application.

Streamlit Community Cloud will install the dependencies listed in `requirements.txt` and attempt to start the application.

Once deployment succeeds, the application will have a shareable website URL.

**Note:** A public deployment URL is available only after the deployment has completed successfully.

**---**

## 14. Project Objectives

The main objectives of MediPrice Guardian are:

1. Demonstrate transparent medical cost estimation.

2. Compare estimated treatment costs across hospitals.

3. Provide structured hospital information.

4. Present government healthcare scheme information.

5. Demonstrate detection of potentially excessive consumable prices.

6. Apply Object-Oriented Programming in a practical Python project.

7. Use JSON for structured data storage.

8. Build an interactive web application using Streamlit.

9. Implement automated backend testing.

10. Practice GitHub version control and web deployment.

**---**

## 15. Future Enhancements

Possible future improvements include:

- Integration with verified hospital pricing information.

- Official government healthcare scheme data.

- Hospital search by location.

- Additional medical procedures and consumables.

- Database integration.

- Improved cost comparison charts.

- User authentication.

- Saved hospital comparisons.

- More comprehensive automated testing.

- Regular healthcare data updates.

These are proposed enhancements and are not implemented in the current version.

**---**

## 16. Important Disclaimer

**MediPrice Guardian is an educational college project and is not an official healthcare service.**

The system uses demonstration hospital prices, procedure costs, and government scheme mappings.

The application does not provide:

- Verified hospital treatment quotations.

- Medical diagnoses or treatment recommendations.

- Official government scheme eligibility decisions.

- Guaranteed insurance coverage.

- Legal determinations of excessive pricing.

Users should confirm actual medical costs, scheme eligibility, hospital participation, and treatment information with the relevant healthcare provider or government authority.

**---**

## 17. GitHub Repository

**Project:** MediPrice Guardian

**Subtitle:** An Integrated Healthcare Information System

**GitHub Repository:** https://github.com/shivanshjha1/MediPriceGuardian

**---**

**🏥 MediPrice Guardian — Making Healthcare Pricing More Transparent.**
