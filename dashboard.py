import streamlit as st
import pandas as pd

from weather import get_weather
from predictor import predict
from trader import paper_trade


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Weather AI Agent",
    layout="wide"
)


# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title(" Weather AI Agent")

st.caption(
    "Weather Prediction, Risk Analysis & Paper Trading Dashboard"
)


# -------------------------------------------------
# CITY SELECTION
# -------------------------------------------------

cities = [
    "Dehradun",
    "Mumbai",
    "Delhi",
    "Tokyo",
    "New York"
]

city = st.selectbox(
    "Select City",
    cities
)


# -------------------------------------------------
# RUN PREDICTION
# -------------------------------------------------

if st.button(
    "Run Prediction",
    type="primary"
):

    try:

        # Fetch live weather
        weather = get_weather(city)

        if weather is None:
            st.error(
                "Weather data could not be fetched."
            )
            st.stop()

        # Generate prediction
        result = predict(weather)

        # Execute simulated paper trade
        trade_result = paper_trade(
            result["trade"],
            result["confidence"]
        )


        # -----------------------------------------
        # CURRENT WEATHER METRICS
        # -----------------------------------------

        st.subheader(
            f" Current Weather — {city}"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            " Temperature",
            f'{result["temperature"]} °C'
        )

        col2.metric(
            " Humidity",
            f'{result["humidity"]}%'
        )

        col3.metric(
            " Confidence",
            f'{result["confidence"]}%'
        )


        # -----------------------------------------
        # PREDICTION RESULT
        # -----------------------------------------

        st.divider()

        st.subheader(
            " Prediction Result"
        )

        pred_col1, pred_col2 = st.columns(2)

        pred_col1.metric(
            "Weather Prediction",
            result["prediction"]
        )

        pred_col2.metric(
            "Trade Signal",
            result["trade"]
        )


        # -----------------------------------------
        # PAPER TRADE ORDER
        # -----------------------------------------

        st.subheader(
            " Paper Trade Order"
        )

        if result["trade"] == "BUY":

            st.success(
                " BUY order simulated successfully"
            )

        elif result["trade"] == "SELL":

            st.error(
                " SELL order simulated successfully"
            )

        else:

            st.warning(
                " HOLD — No new position opened"
            )


        # -----------------------------------------
        # KELLY CRITERION & RISK ANALYSIS
        # -----------------------------------------

        st.divider()

        st.subheader(
            " Kelly Criterion Risk Analysis"
        )

        risk1, risk2, risk3, risk4 = st.columns(4)

        risk1.metric(
            "Paper Balance",
            f'₹{trade_result["balance"]:.2f}'
        )

        risk2.metric(
            "Kelly Stake",
            f'₹{trade_result["stake"]:.2f}'
        )

        risk3.metric(
            "Kelly Fraction",
            f'{trade_result["kelly_fraction"]:.4f}'
        )

        risk4.metric(
            "Risk Level",
            trade_result["risk_level"]
        )


        # -----------------------------------------
        # RISK MESSAGE
        # -----------------------------------------

        if trade_result["risk_level"] == "LOW":

            st.success(
                "Risk Assessment: LOW"
            )

        elif trade_result["risk_level"] == "MEDIUM":

            st.warning(
                "Risk Assessment: MEDIUM"
            )

        else:

            st.error(
                "Risk Assessment: HIGH"
            )


        # -----------------------------------------
        # DETAILS
        # -----------------------------------------

        with st.expander(
            "View Complete Prediction Details"
        ):

            st.json(
                {
                    "city": city,
                    "temperature": result["temperature"],
                    "humidity": result["humidity"],
                    "prediction": result["prediction"],
                    "confidence": result["confidence"],
                    "trade_signal": result["trade"],
                    "paper_balance": trade_result["balance"],
                    "kelly_stake": trade_result["stake"],
                    "kelly_fraction": trade_result["kelly_fraction"],
                    "risk_level": trade_result["risk_level"]
                }
            )


    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )


# -------------------------------------------------
# STATISTICAL RESULTS
# -------------------------------------------------

st.divider()

st.subheader(
    " Statistical Results"
)

try:

    df = pd.read_csv(
        "outputs/statistical_results.csv"
    )

    # Display table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    # ---------------------------------------------
    # SUMMARY METRICS
    # ---------------------------------------------

    st.subheader(
        " Performance Summary"
    )

    stat1, stat2, stat3 = st.columns(3)

    stat1.metric(
        "Cities Analysed",
        len(df)
    )

    stat2.metric(
        "Average Confidence",
        f'{df["confidence"].mean():.1f}%'
    )

    stat3.metric(
        "Highest Confidence",
        f'{df["confidence"].max()}%'
    )


    st.subheader("📊 Sample Historical Statistical Results")
    st.caption(
    "These records are sample historical results and may differ "
    "from the current live weather reading."
)

    confidence_chart = (
        df.set_index("city")["confidence"]
    )

    st.bar_chart(
        confidence_chart
    )


    # ---------------------------------------------
    # TEMPERATURE CHART
    # ---------------------------------------------

    st.subheader(
        " Temperature by City"
    )

    temperature_chart = (
        df.set_index("city")["temperature"]
    )

    st.line_chart(
        temperature_chart
    )


    # ---------------------------------------------
    # TRADE SIGNAL DISTRIBUTION
    # ---------------------------------------------

    st.subheader(
        " Trade Signal Distribution"
    )

    trade_counts = (
        df["trade_signal"]
        .value_counts()
    )

    st.bar_chart(
        trade_counts
    )


except FileNotFoundError:

    st.warning(
        "Statistical results file not found. "
        "Create outputs/statistical_results.csv"
    )

except Exception as e:

    st.error(
        f"Statistics could not be loaded: {e}"
    )


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    " Educational project — simulated paper trading only. "
    "No real-money trades are executed."
)