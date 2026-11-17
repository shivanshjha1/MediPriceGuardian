
import streamlit as st

from data_manager import DataManager
from price_engine import PriceEngine


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="MediPrice Guardian",
    page_icon="🏥",
    layout="wide"
)


# ==========================================
# LOAD PROJECT DATA
# ==========================================

manager = DataManager()
data = manager.load_data()

hospitals = data["hospitals"]
procedures = data["procedures"]
schemes = data["schemes"]

engine = PriceEngine()


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("🏥 MediPrice Guardian")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Hospital Directory",
        "Medical Cost Estimator",
        "Hospital Price Comparison",
        "Government Scheme Finder"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "An Integrated Healthcare Information System"
)


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.title("🏥 MediPrice Guardian")

    st.subheader(
        "An Integrated Healthcare Information System"
    )

    st.markdown(
        "### Making Healthcare Pricing Transparent"
    )

    st.write(
        "Compare hospital treatment costs, "
        "identify potentially excessive charges, "
        "and explore government healthcare schemes "
        "through one integrated platform."
    )

    st.divider()

    # DASHBOARD STATISTICS

    st.subheader("📊 Project Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏥 Hospitals",
            len(hospitals)
        )

    with col2:
        st.metric(
            "🩺 Procedures",
            len(procedures)
        )

    with col3:
        st.metric(
            "🏛️ Scheme Entries",
            len(schemes)
        )

    st.divider()

    # PROJECT FEATURES

    st.subheader("✨ Our Features")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### 🏥 Hospital Directory")

        st.write(
            "Explore hospitals, available consumable "
            "prices, and listed government schemes."
        )

        st.markdown("#### 💰 Medical Cost Estimator")

        st.write(
            "Calculate estimated treatment costs "
            "with a detailed consumable breakdown."
        )

    with col2:

        st.markdown(
            "#### 📊 Hospital Price Comparison"
        )

        st.write(
            "Compare estimated procedure costs "
            "across hospitals."
        )

        st.markdown(
            "#### 🏛️ Government Scheme Finder"
        )

        st.write(
            "Explore government healthcare programmes, "
            "benefits, eligibility, and listed hospitals."
        )

    st.divider()

    st.info(
        "This application currently uses demonstration "
        "data for educational purposes. Hospital prices "
        "and scheme participation are not verified."
    )


# ==========================================
# HOSPITAL DIRECTORY
# ==========================================

elif page == "Hospital Directory":

    st.title("🏥 Hospital Directory")

    st.write(
        "Explore hospitals and their accepted "
        "government schemes."
    )

    hospital_rows = []

    for hospital in hospitals:

        hospital_rows.append({
            "Hospital Name": hospital.name,
            "Accepted Schemes": (
                ", ".join(hospital.accepted_schemes)
                if hospital.accepted_schemes
                else "None listed"
            ),
            "Consumables Listed": len(hospital.pricing)
        })

    st.dataframe(
        hospital_rows,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        f"Displaying {len(hospitals)} hospitals."
    )

    st.divider()

    st.subheader("Hospital Details")

    selected_hospital_name = st.selectbox(
        "Select a hospital",
        [hospital.name for hospital in hospitals]
    )

    selected_hospital = next(
        hospital for hospital in hospitals
        if hospital.name == selected_hospital_name
    )

    st.write(
        "**Hospital:**",
        selected_hospital.name
    )

    st.write(
        "**Accepted Schemes:**",
        (
            ", ".join(selected_hospital.accepted_schemes)
            if selected_hospital.accepted_schemes
            else "None listed"
        )
    )

    st.subheader("Consumable Pricing")

    pricing_rows = []

    for item, price in selected_hospital.pricing.items():

        pricing_rows.append({
            "Consumable": item,
            "Hospital Price (₹)": price
        })

    st.dataframe(
        pricing_rows,
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# MEDICAL COST ESTIMATOR
# ==========================================

elif page == "Medical Cost Estimator":

    st.title("💰 Medical Cost Estimator")

    st.write(
        "Select a hospital and medical procedure "
        "to calculate the estimated treatment cost."
    )

    st.divider()

    hospital_name = st.selectbox(
        "Select Hospital",
        [hospital.name for hospital in hospitals]
    )

    procedure_name = st.selectbox(
        "Select Medical Procedure",
        [procedure.name for procedure in procedures]
    )

    selected_hospital = next(
        hospital for hospital in hospitals
        if hospital.name == hospital_name
    )

    selected_procedure = next(
        procedure for procedure in procedures
        if procedure.name == procedure_name
    )

    if st.button(
        "Calculate Estimated Cost",
        type="primary"
    ):

        estimate = engine.calculate_estimate(
            selected_hospital,
            selected_procedure
        )

        st.divider()

        st.subheader("Cost Estimation Report")

        st.write(
            "**Hospital:**",
            estimate["hospital"]
        )

        st.write(
            "**Procedure:**",
            estimate["procedure"]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Surgeon Fee",
                f"₹{estimate['surgeon_fee']:,.2f}"
            )

        with col2:
            st.metric(
                "Estimated Total",
                f"₹{estimate['total_cost']:,.2f}"
            )

        st.divider()

        st.subheader("Consumable Cost Breakdown")

        item_rows = []

        for item in estimate["items"]:

            item_rows.append({
                "Consumable": item["name"],
                "Market Price (₹)": item["market_price"],
                "Hospital Price (₹)": item["hospital_price"]
            })

        if item_rows:

            st.dataframe(
                item_rows,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "No consumable prices were available."
            )

        if estimate["missing_items"]:

            st.warning(
                "Missing prices for: "
                + ", ".join(estimate["missing_items"])
                + ". The estimate may be incomplete."
            )


# ==========================================
# HOSPITAL PRICE COMPARISON
# ==========================================

elif page == "Hospital Price Comparison":

    st.title("📊 Hospital Price Comparison")

    st.write(
        "Compare estimated procedure costs "
        "across all available hospitals."
    )

    st.divider()

    procedure_name = st.selectbox(
        "Select Medical Procedure",
        [procedure.name for procedure in procedures]
    )

    selected_procedure = next(
        procedure for procedure in procedures
        if procedure.name == procedure_name
    )

    comparison_rows = []
    complete_rows = []

    for hospital in hospitals:

        estimate = engine.calculate_estimate(
            hospital,
            selected_procedure
        )

        row = {
            "Hospital": hospital.name,
            "Estimated Cost (₹)": estimate["total_cost"]
        }

        comparison_rows.append(row)

        if not estimate["missing_items"]:
            complete_rows.append(row)

    # Sort hospitals by estimated cost
    comparison_rows.sort(
        key=lambda row: row["Estimated Cost (₹)"]
    )

    st.subheader("Cost Comparison Table")

    st.dataframe(
        comparison_rows,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Hospital Cost Comparison Chart")

    st.bar_chart(
        comparison_rows,
        x="Hospital",
        y="Estimated Cost (₹)",
        horizontal=True
    )

    st.divider()

    # Identify the lowest complete estimate
    if complete_rows:

        lowest = min(
            complete_rows,
            key=lambda row: row["Estimated Cost (₹)"]
        )

        st.success(
            f"Lowest complete estimate: "
            f"{lowest['Hospital']} — "
            f"₹{lowest['Estimated Cost (₹)']:,.2f}"
        )

    else:

        st.warning(
            "No hospital has complete pricing "
            "for this procedure."
        )

    st.caption(
        "All prices are demonstration data. "
        "Incomplete estimates may be understated."
    )


# ==========================================
# GOVERNMENT SCHEME FINDER
# ==========================================

elif page == "Government Scheme Finder":

    st.title("🏛️ Government Healthcare Scheme Finder")

    st.write(
        "Explore government healthcare programmes, "
        "their benefits, eligibility information, "
        "and hospitals listing the selected scheme."
    )

    st.divider()

    st.subheader("Select a Government Scheme")

    selected_scheme_name = st.selectbox(
        "Choose a scheme",
        [scheme.name for scheme in schemes]
    )

    selected_scheme = next(
        scheme for scheme in schemes
        if scheme.name == selected_scheme_name
    )

    st.divider()

    # ==================================
    # SCHEME INFORMATION
    # ==================================

    st.subheader("Scheme Information")

    st.write(
        "**Scheme Name:**",
        selected_scheme.name
    )

    st.write(
        "**Scheme Code:**",
        selected_scheme.code
    )

    st.write(
        "**Description:**",
        selected_scheme.description
    )

    st.write(
        "**Benefits:**",
        selected_scheme.benefits
    )

    st.write(
        "**Eligibility:**",
        selected_scheme.eligibility
    )

    st.divider()

    # ==================================
    # MATCHING HOSPITALS
    # ==================================

    st.subheader("Hospitals Listing This Scheme")

    matching_hospitals = []

    for hospital in hospitals:

        if selected_scheme.code in hospital.accepted_schemes:

            matching_hospitals.append({
                "Hospital Name": hospital.name,
                "Scheme Code": selected_scheme.code
            })

    if matching_hospitals:

        st.dataframe(
            matching_hospitals,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            f"{len(matching_hospitals)} hospital(s) "
            "list this scheme as accepted."
        )

    else:

        st.info(
            "No hospitals in the demonstration dataset "
            "list this scheme as accepted."
        )

    st.divider()

    st.caption(
        "Scheme details and hospital acceptance are "
        "demonstration information. Verify current "
        "benefits, eligibility and hospital participation "
        "through official government sources."
    )


# ==========================================
# DATA DISCLAIMER
# ==========================================

st.divider()

st.caption(
    "MediPrice Guardian | College Project | "
    "Hospital prices and scheme acceptance are "
    "demonstration data, not verified medical "
    "or government information."
)
