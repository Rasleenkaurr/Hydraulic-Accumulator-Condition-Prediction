
import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import streamlit.components.v1 as components
from pathlib import Path


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Hydraulic Accumulator Monitoring",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

px.defaults.template = "plotly_dark"


# =========================================================
# 2. FILE PATHS
# =========================================================

APP_DIR = Path(__file__).resolve().parent

DATA_PATH = APP_DIR / "data"

IMAGE_PATH = APP_DIR / "assets" / "hydraulic_accumulator.png"


# =========================================================
# 3. HYDRAULIC INDUSTRIAL THEME
# =========================================================

st.markdown("""
<style>

/* Main background */

.stApp {
    background-color: #0B1722;
    color: #E8F0F5;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #10283B 0%,
        #091723 100%
    );
    border-right: 1px solid #28465B;
}

[data-testid="stSidebar"] * {
    color: #E5EDF3;
}

[data-testid="stSidebar"] h1 {
    color: #F59E0B !important;
}

/* Headings */

h1 {
    color: #F59E0B !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #E5EDF3 !important;
    font-weight: 650 !important;
}

/* General text */

p, label, li {
    color: #B9C9D5;
}

/* KPI cards */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #193449,
        #102536
    );
    border: 1px solid #31546B;
    border-left: 4px solid #F59E0B;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

[data-testid="stMetricLabel"] {
    color: #AFC2D0 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 750 !important;
}

/* Charts */

div[data-testid="stPlotlyChart"] {
    background-color: #102536;
    border: 1px solid #29485D;
    border-radius: 12px;
    padding: 10px;
}

/* Containers */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #11283A;
    border: 1px solid #29485D;
    border-radius: 12px;
    padding: 12px;
}

/* Dropdowns */

div[data-baseweb="select"] > div {
    background-color: #193449;
    border-color: #42647A;
}

/* Alerts */

div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Dividers */

hr {
    border-color: #29485D;
}

/* Buttons */

.stButton button {
    background-color: #E58B16;
    color: #101D29;
    border: none;
    border-radius: 8px;
    font-weight: 700;
}

.stButton button:hover {
    background-color: #FFAD35;
    color: #101D29;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 4. LOAD DATASETS
# =========================================================

try:

    sensor_data = pd.read_csv(
        DATA_PATH / "Sensor_Data.csv"
    )

    model_comparison = pd.read_csv(
        DATA_PATH / "Model_Comparison.csv"
    )

    predictions = pd.read_csv(
        DATA_PATH / "Final_Predictions.csv"
    )

    feature_importance = pd.read_csv(
        DATA_PATH / "Feature_Importance.csv"
    )

except FileNotFoundError as e:

    st.error(
        f"Dataset file not found: {e.filename}. "
        "Please check your data folder."
    )

    st.stop()


# =========================================================
# 5. PHOTOGRAPHIC HYDRAULIC HEADER
# =========================================================

if IMAGE_PATH.exists():

    image_base64 = base64.b64encode(
        IMAGE_PATH.read_bytes()
    ).decode("utf-8")

    hero_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: transparent;
        }}

        .hero {{
            width: 100%;
            height: 320px;
            position: relative;
            overflow: hidden;
            border-radius: 16px;
            border: 1px solid #36566C;
        }}

        .hero img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            position: absolute;
            top: 0;
            left: 0;
        }}

        .overlay {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            padding: 35px 42px;
            background: linear-gradient(
                90deg,
                rgba(5,17,29,0.96) 0%,
                rgba(5,17,29,0.78) 52%,
                rgba(5,17,29,0.12) 100%
            );
        }}

        .content {{
            max-width: 780px;
        }}

        .tag {{
            color: #FFAD35;
            font-size: 12px;
            font-weight: bold;
            letter-spacing: 3px;
            margin-bottom: 18px;
        }}

        .title {{
            color: #FFFFFF;
            font-size: 39px;
            font-weight: 850;
            line-height: 1.15;
            letter-spacing: 1px;
        }}

        .description {{
            color: #D1E0EA;
            font-size: 15px;
            margin-top: 17px;
        }}

        .indicators {{
            display: flex;
            flex-wrap: wrap;
            gap: 9px;
            margin-top: 23px;
        }}

        .indicators span {{
            color: #FFD28A;
            background: rgba(14,39,56,0.9);
            border: 1px solid #A76D24;
            border-radius: 5px;
            padding: 7px 10px;
            font-size: 10px;
            font-weight: bold;
            letter-spacing: 0.5px;
        }}

        @media (max-width: 600px) {{
            .hero {{
                height: 300px;
            }}

            .overlay {{
                padding: 20px;
            }}

            .title {{
                font-size: 26px;
            }}

            .description {{
                font-size: 12px;
            }}
        }}

    </style>
    </head>

    <body>

        <div class="hero">

            <img
                src="data:image/png;base64,{image_base64}"
                alt="Hydraulic accumulator"
            >

            <div class="overlay">

                <div class="content">

                    <div class="tag">
                        HYDRAULIC SYSTEMS | CONDITION MONITORING
                    </div>

                    <div class="title">
                        HYDRAULIC ACCUMULATOR
                        <br>
                        CONDITION MONITORING
                    </div>

                    <div class="description">
                        Sensor Analytics | Condition Classification |
                        Machine Learning
                    </div>

                    <div class="indicators">
                        <span>PRESSURE ANALYSIS</span>
                        <span>TEMPERATURE MONITORING</span>
                        <span>FLOW & VIBRATION</span>
                    </div>

                </div>

            </div>

        </div>

    </body>
    </html>
    """

    components.html(
        hero_html,
        height=335,
        scrolling=False
    )

else:

    st.error(
        "Hydraulic accumulator photograph not found. "
        "Please check assets/hydraulic_accumulator.png"
    )


# =========================================================
# 6. SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("⚙️ Hydraulic Monitoring")

st.sidebar.markdown("### Dashboard Navigation")

page = st.sidebar.radio(
    "Select a Section",
    [
        "Dataset Overview",
        "Sensor Analysis",
        "Model Performance",
        "About the Project"
    ]
)


# =========================================================
# PAGE 1: DATASET OVERVIEW
# =========================================================

if page == "Dataset Overview":

    st.header("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Cycles",
            f"{len(sensor_data):,}"
        )

    with col2:
        st.metric(
            "Accumulator Conditions",
            sensor_data["Accumulator_Condition"].nunique()
        )

    with col3:
        st.metric(
            "Original Sensor Features",
            "84"
        )

    with col4:
        st.metric(
            "Selected Sensor Features",
            "80"
        )

    st.divider()

    st.subheader("Accumulator Condition Distribution")

    condition_counts = (
        sensor_data["Accumulator_Condition"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    condition_counts.columns = [
        "Condition",
        "Number of Cycles"
    ]

    fig = px.bar(
        condition_counts,
        x="Condition",
        y="Number of Cycles",
        color="Condition",
        text="Number of Cycles",
        title="Distribution of Accumulator Conditions"
    )

    fig.update_layout(
        xaxis_title="Accumulator Condition",
        yaxis_title="Number of Cycles",
        legend_title="Condition"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# PAGE 2: SENSOR ANALYSIS
# =========================================================

elif page == "Sensor Analysis":

    st.header("Sensor Analysis")

    st.write(
        "Explore hydraulic system sensor measurements "
        "across operating cycles and accumulator conditions."
    )

    conditions = sorted(
        sensor_data["Accumulator_Condition"].unique()
    )

    selected_conditions = st.multiselect(
        "Select Accumulator Conditions",
        conditions,
        default=conditions
    )

    cycle_range = st.slider(
        "Select Cycle Range",
        min_value=int(sensor_data["Cycle"].min()),
        max_value=int(sensor_data["Cycle"].max()),
        value=(
            int(sensor_data["Cycle"].min()),
            int(sensor_data["Cycle"].max())
        )
    )

    filtered_data = sensor_data[
        (
            sensor_data["Accumulator_Condition"]
            .isin(selected_conditions)
        )
        &
        (
            sensor_data["Cycle"]
            .between(cycle_range[0], cycle_range[1])
        )
    ]

    sensor_columns = (
        sensor_data
        .select_dtypes(include="number")
        .columns
        .drop(
            ["Cycle", "Accumulator_Condition"],
            errors="ignore"
        )
    )

    selected_sensor = st.selectbox(
        "Select a Sensor Feature",
        sensor_columns
    )

    if filtered_data.empty:

        st.info(
            "No data available for the selected filters. "
            "Please change your selection."
        )

    else:

        fig = px.line(
            filtered_data,
            x="Cycle",
            y=selected_sensor,
            color="Accumulator_Condition",
            title=f"{selected_sensor} Across Operating Cycles"
        )

        fig.update_layout(
            xaxis_title="Operating Cycle",
            yaxis_title=selected_sensor,
            legend_title="Accumulator Condition"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    st.subheader("Top 10 Important Features")

    top_features = (
        feature_importance
        .head(10)
        .sort_values("Importance")
    )

    fig = px.bar(
        top_features,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance - Decision Tree"
    )

    fig.update_layout(
        xaxis_title="Importance Score",
        yaxis_title="Sensor Feature"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# PAGE 3: MODEL PERFORMANCE
# =========================================================

elif page == "Model Performance":

    st.header("Model Performance")

    st.write(
        "Comparison of classification models and evaluation "
        "of the final Decision Tree on unseen test data."
    )

    st.subheader("Model Comparison")

    fig = px.bar(
        model_comparison,
        x="Model",
        y=["Accuracy", "Macro F1"],
        barmode="group",
        title="Validation Performance Comparison"
    )

    fig.update_layout(
        xaxis_title="Classification Model",
        yaxis_title="Score",
        legend_title="Evaluation Metric"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Final Model Test Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Test Accuracy", "28.84%")

    with col2:
        st.metric("Test Macro F1", "22.34%")

    st.divider()

    st.subheader("Actual vs Predicted Conditions")

    confusion_data = pd.crosstab(
        predictions["Actual_Condition"],
        predictions["Predicted_Condition"]
    )

    fig = px.imshow(
        confusion_data,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues",
        labels={
            "x": "Predicted Condition",
            "y": "Actual Condition",
            "color": "Number of Cycles"
        },
        title="Confusion Matrix"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.warning(
        "The final model achieved limited generalization "
        "on unseen cycles. Test accuracy was 28.84% "
        "and Macro F1 was 22.34%."
    )


# =========================================================
# PAGE 4: ABOUT THE PROJECT
# =========================================================

elif page == "About the Project":

    st.header("About the Project")

    st.subheader(
        "Hydraulic Accumulator Condition Monitoring"
    )

    st.write("""
    Hydraulic accumulators are important components of
    hydraulic systems. They store hydraulic energy and help
    maintain system pressure and stability.

    Monitoring their operating condition helps identify
    changes in system behaviour and supports maintenance
    decisions.
    """)

    st.divider()

    st.subheader("Project Objective")

    st.write("""
    The objective of this project is to analyse hydraulic
    system sensor measurements and classify the condition
    of the hydraulic accumulator into four condition levels:
    90, 100, 115 and 130.
    """)

    st.divider()

    st.subheader("Dataset Information")

    st.markdown("""
    - **Dataset:** Condition Monitoring of Hydraulic Systems
    - **Source:** UCI Machine Learning Repository
    - **Total observations:** 2,205 cycles
    - **Original sensor features:** 84
    - **Selected features:** 80
    - **Condition classes:** 4
    """)

    st.divider()

    st.subheader("Machine Learning Workflow")

    st.markdown("""
    1. Data understanding and preprocessing
    2. Feature selection and removal of redundant features
    3. Chronological training, validation and test splitting
    4. Comparison of multiple classification algorithms
    5. Hyperparameter tuning of the Decision Tree
    6. Final evaluation on unseen test data
    """)

    st.divider()

    st.subheader("Final Model Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Test Accuracy", "28.84%")

    with col2:
        st.metric("Test Macro F1", "22.34%")

    st.warning("""
    The final model showed limited generalization on unseen
    cycles. Further improvements are needed before the model
    can be considered reliable for practical deployment.
    """)

    st.divider()

    st.subheader("Project Conclusion")

    st.write("""
    This project demonstrates how sensor data and machine
    learning can be used to investigate hydraulic accumulator
    conditions.

    The results also highlight the challenges of model
    generalization and the importance of evaluating models
    on unseen data.
    """)
