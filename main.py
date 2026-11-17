
from data_manager import DataManager
from price_engine import PriceEngine


# -----------------------------------------
# DISPLAY MAIN MENU
# -----------------------------------------

def display_menu():
    print("\n========== MEDIPRICE GUARDIAN ==========")
    print("1. View All Hospitals")
    print("2. View All Medical Procedures")
    print("3. View Government Schemes")
    print("4. Calculate Procedure Cost")
    print("5. Compare Prices Across Hospitals")
    print("6. Check Scheme Availability")
    print("7. Overall Price Gouging Report")
    print("0. Exit")
    print("========================================")


# -----------------------------------------
# SELECT HOSPITAL
# -----------------------------------------

def select_hospital(hospitals):
    print("\nAvailable Hospitals:")

    for index, hospital in enumerate(hospitals, start=1):
        print(f"{index}. {hospital.name}")

    try:
        choice = int(input("\nSelect hospital number: "))

        if 1 <= choice <= len(hospitals):
            return hospitals[choice - 1]

        print("Invalid hospital selection.")
        return None

    except ValueError:
        print("Please enter a valid number.")
        return None


# -----------------------------------------
# SELECT PROCEDURE
# -----------------------------------------

def select_procedure(procedures):
    print("\nAvailable Medical Procedures:")

    for index, procedure in enumerate(procedures, start=1):
        print(f"{index}. {procedure.name}")

    try:
        choice = int(input("\nSelect procedure number: "))

        if 1 <= choice <= len(procedures):
            return procedures[choice - 1]

        print("Invalid procedure selection.")
        return None

    except ValueError:
        print("Please enter a valid number.")
        return None


# -----------------------------------------
# OPTION 1: VIEW HOSPITALS
# -----------------------------------------

def view_hospitals(hospitals):
    print("\n========== HOSPITAL DIRECTORY ==========")

    for index, hospital in enumerate(hospitals, start=1):
        print(f"\nHospital Number: {index}")
        print("Hospital Name:", hospital.name)
        print("Hospital Pricing:")

        for item, price in hospital.pricing.items():
            print(f"  {item}: Rs. {price}")

        print("Accepted Schemes:")

        if hospital.accepted_schemes:
            for scheme in hospital.accepted_schemes:
                print("  -", scheme)
        else:
            print("  No schemes listed")

        print("----------------------------------------")

    print("\nTotal Hospitals:", len(hospitals))
    print("========================================")


# -----------------------------------------
# OPTION 2: VIEW PROCEDURES
# -----------------------------------------

def view_procedures(procedures):
    print("\n========== MEDICAL PROCEDURES ==========")

    for index, procedure in enumerate(procedures, start=1):
        print(f"\nProcedure Number: {index}")
        print("Procedure Code:", procedure.code)
        print("Procedure Name:", procedure.name)
        print("Surgeon Fee: Rs.", procedure.surgeon_fee)
        print("Required Consumables:")

        for item in procedure.consumables:
            print("  -", item)

        print("----------------------------------------")

    print("\nTotal Procedures:", len(procedures))
    print("========================================")


# -----------------------------------------
# OPTION 3: VIEW GOVERNMENT SCHEMES
# -----------------------------------------

def view_schemes(schemes):
    print("\n========== GOVERNMENT SCHEMES ==========")

    for scheme in schemes:
        scheme.display_details()

    print("========================================")


# -----------------------------------------
# OPTION 4: CALCULATE PROCEDURE COST
# -----------------------------------------

def calculate_cost(engine, hospitals, procedures):
    hospital = select_hospital(hospitals)

    if hospital is None:
        return

    procedure = select_procedure(procedures)

    if procedure is None:
        return

    estimate = engine.calculate_estimate(hospital, procedure)
    alerts = engine.check_price_gouging(hospital, procedure)

    print("\n========== COST ESTIMATION ==========")
    print("Hospital:", estimate["hospital"])
    print("Procedure:", estimate["procedure"])
    print("Surgeon Fee: Rs.", estimate["surgeon_fee"])

    print("\nConsumable Details:")

    for item in estimate["items"]:
        print("\nItem:", item["name"])
        print("Market Price: Rs.", item["market_price"])
        print("Hospital Price: Rs.", item["hospital_price"])

    print("\nTotal Estimated Cost: Rs.", estimate["total_cost"])

    if estimate["missing_items"]:
        print("\nMissing Price Information:")
        for item in estimate["missing_items"]:
            print("-", item)

    print("\nPrice Gouging Check:")

    if alerts:
        for alert in alerts:
            print("\nALERT:", alert["item"])
            print("Market Price: Rs.", alert["market_price"])
            print("Hospital Price: Rs.", alert["hospital_price"])
            print("Alert Threshold: Rs.", alert["threshold_price"])

        print("\nStatus: PRICE GOUGING DETECTED")
    else:
        print("No price-gouging alerts detected.")

    print("====================================")


# -----------------------------------------
# OPTION 5: COMPARE HOSPITAL PRICES
# -----------------------------------------

def compare_hospitals(engine, hospitals, procedures):
    procedure = select_procedure(procedures)

    if procedure is None:
        return

    print("\n========== HOSPITAL PRICE COMPARISON ==========")
    print("Procedure:", procedure.name)

    for hospital in hospitals:
        estimate = engine.calculate_estimate(hospital, procedure)
        alerts = engine.check_price_gouging(hospital, procedure)

        print("\nHospital:", hospital.name)
        print("Estimated Cost: Rs.", estimate["total_cost"])
        print("Price Gouging Alerts:", len(alerts))

        if alerts:
            for alert in alerts:
                print(
                    "  ALERT:",
                    alert["item"],
                    "| Market: Rs.", alert["market_price"],
                    "| Hospital: Rs.", alert["hospital_price"]
                )
        else:
            print("  No price-gouging alerts.")

    print("\n===============================================")


# -----------------------------------------
# OPTION 6: SCHEME-HOSPITAL MAPPER
# -----------------------------------------

def check_scheme_availability(hospitals, schemes):
    print("\n========== SCHEME-HOSPITAL MAPPER ==========")

    scheme_codes = []

    for scheme in schemes:
        if isinstance(scheme, dict):
            code = scheme.get("code", "")
        else:
            code = getattr(scheme, "code", "")

        if code and not code.startswith("PENDING-"):
            scheme_codes.append(code)

    print("Available Scheme Codes:")

    for code in scheme_codes:
        print("-", code)

    selected_scheme = input(
        "\nEnter Government Scheme Code: "
    ).strip()

    if not selected_scheme:
        print("Scheme code cannot be empty.")
        return

    if scheme_codes and not any(
        selected_scheme.lower() == code.lower()
        for code in scheme_codes
    ):
        print("Scheme not found in the scheme directory.")
        return

    print("\nScheme:", selected_scheme.upper())
    print("\nHospital Availability:")

    found = False

    for hospital in hospitals:
        accepted = any(
            selected_scheme.lower() == scheme.lower()
            for scheme in hospital.accepted_schemes
        )

        if accepted:
            print(hospital.name, "- ACCEPTS")
            found = True
        else:
            print(hospital.name, "- DOES NOT ACCEPT")

    print("\nMapper completed.")

    if not found:
        print("No hospital in the database accepts this scheme.")

    print("============================================")


# -----------------------------------------
# OPTION 7: OVERALL PRICE GOUGING REPORT
# -----------------------------------------

def overall_price_gouging_report(engine, hospitals, procedures):
    print("\n========== OVERALL PRICE GOUGING REPORT ==========")

    total_alerts = engine.generate_gouging_report(
        hospitals,
        procedures
    )

    print("\nTotal Price Gouging Alerts:", total_alerts)
    print("Price Threshold: Strictly greater than 150% of market price")
    print("==================================================")


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

def main():

    print("\nWelcome to MediPrice Guardian!\n")

    manager = DataManager()
    data = manager.load_data()

    hospitals = data["hospitals"]
    procedures = data["procedures"]
    schemes = data["schemes"]

    engine = PriceEngine()

    print("Database loaded successfully.")
    print(
        "\nNOTICE: DEMONSTRATION DATA ONLY. "
        "Hospital prices, hospital scheme mappings and eligibility "
        "must be verified before real-world use."
    )

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_hospitals(hospitals)

        elif choice == "2":
            view_procedures(procedures)

        elif choice == "3":
            view_schemes(schemes)

        elif choice == "4":
            calculate_cost(engine, hospitals, procedures)

        elif choice == "5":
            compare_hospitals(engine, hospitals, procedures)

        elif choice == "6":
            check_scheme_availability(hospitals, schemes)

        elif choice == "7":
            overall_price_gouging_report(
                engine,
                hospitals,
                procedures
            )

        elif choice == "0":
            print("\nThank you for using MediPrice Guardian!")
            print("Exiting program...")
            break

        else:
            print("\nInvalid choice. Please try again.")


# -----------------------------------------
# PROGRAM ENTRY POINT
# -----------------------------------------

if __name__ == "__main__":
    main()
