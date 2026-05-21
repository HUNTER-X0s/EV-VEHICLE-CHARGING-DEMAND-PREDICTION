import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt


st.set_page_config(page_title="EV Forecast", layout="wide")

model = joblib.load("forecasting_ev_model.pkl")

st.markdown(
    """
    <style>
        :root {
            --bg: #070a12;
            --panel: #101827;
            --panel-strong: #162236;
            --panel-soft: #0b111c;
            --text: #f5f8ff;
            --muted: #aebcd1;
            --subtle: #78889f;
            --accent: #35e6b3;
            --accent-2: #6ab6ff;
            --accent-3: #ffd166;
            --danger: #ff7a90;
            --border: rgba(255, 255, 255, 0.12);
        }

        body,
        .stApp {
            background:
                radial-gradient(circle at 12% 8%, rgba(53, 230, 179, 0.14), transparent 26%),
                radial-gradient(circle at 90% 0%, rgba(106, 182, 255, 0.17), transparent 30%),
                linear-gradient(135deg, #070a12 0%, #0b1220 46%, #101828 100%);
            color: var(--text);
        }

        .block-container {
            max-width: 1280px;
            padding-top: 1.25rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3, label, p, .stMarkdown, [data-testid="stWidgetLabel"] {
            color: var(--text) !important;
        }

        h2, h3 {
            letter-spacing: 0;
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 14px 18px;
            border: 1px solid var(--border);
            border-radius: 8px;
            background: rgba(11, 17, 28, 0.78);
            box-shadow: 0 16px 42px rgba(0, 0, 0, 0.25);
            margin-bottom: 18px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 11px;
            min-width: 0;
        }

        .brand-mark {
            width: 38px;
            height: 38px;
            border-radius: 8px;
            background: linear-gradient(135deg, var(--accent), var(--accent-2));
            box-shadow: 0 10px 32px rgba(53, 230, 179, 0.22);
        }

        .brand-title {
            color: var(--text);
            font-size: 17px;
            font-weight: 800;
            line-height: 1.2;
        }

        .brand-subtitle {
            color: var(--subtle);
            font-size: 12px;
            margin-top: 2px;
        }

        .status-pill {
            color: var(--accent);
            border: 1px solid rgba(53, 230, 179, 0.28);
            background: rgba(53, 230, 179, 0.1);
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 13px;
            font-weight: 700;
            white-space: nowrap;
        }

        .hero {
            display: grid;
            grid-template-columns: minmax(0, 1.05fr) minmax(320px, 0.95fr);
            align-items: stretch;
            gap: 18px;
            margin-bottom: 18px;
        }

        .hero-copy,
        .hero-media,
        .panel-card {
            border: 1px solid var(--border);
            border-radius: 8px;
            background: linear-gradient(180deg, rgba(16, 24, 39, 0.94), rgba(11, 17, 28, 0.92));
            box-shadow: 0 22px 60px rgba(0, 0, 0, 0.28);
        }

        .hero-copy {
            padding: 30px;
        }

        .hero-kicker {
            color: var(--accent);
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }

        .hero-title {
            color: var(--text);
            font-size: clamp(34px, 5vw, 58px);
            font-weight: 800;
            line-height: 1.08;
            margin-bottom: 12px;
        }

        .hero-subtitle {
            color: var(--muted);
            font-size: 18px;
            max-width: 780px;
            line-height: 1.6;
        }

        .hero-metrics {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin-top: 26px;
        }

        .mini-stat {
            padding: 14px;
            border: 1px solid var(--border);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.035);
        }

        .mini-stat-value {
            color: var(--text);
            font-size: 22px;
            font-weight: 850;
        }

        .mini-stat-label {
            color: var(--subtle);
            font-size: 12px;
            margin-top: 4px;
        }

        .hero-media {
            overflow: hidden;
            min-height: 330px;
        }

        [data-testid="stImage"] img {
            border-radius: 8px;
            border: 1px solid var(--border);
            box-shadow: 0 18px 48px rgba(0, 0, 0, 0.34);
        }

        .hero-media [data-testid="stImage"] img,
        .hero + div [data-testid="stImage"] img {
            max-height: 390px;
            object-fit: cover;
        }

        .panel-card {
            padding: 20px;
            margin: 18px 0;
        }

        .panel-title {
            color: var(--text);
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .panel-subtitle {
            color: var(--muted);
            font-size: 14px;
            margin-bottom: 14px;
        }

        .instruction {
            color: var(--text);
            font-size: 17px;
            font-weight: 600;
            margin: 0 0 10px;
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 14px;
            margin: 16px 0 20px;
        }

        .metric-card {
            border: 1px solid var(--border);
            border-radius: 8px;
            background: linear-gradient(180deg, rgba(22, 34, 54, 0.94), rgba(11, 17, 28, 0.94));
            padding: 18px;
        }

        .metric-label {
            color: var(--muted);
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .metric-value {
            color: var(--text);
            font-size: clamp(24px, 4vw, 34px);
            font-weight: 900;
            line-height: 1.12;
        }

        .metric-note {
            color: var(--subtle);
            font-size: 12px;
            margin-top: 8px;
        }

        div[data-baseweb="select"] > div {
            background-color: rgba(11, 17, 28, 0.98) !important;
            border: 1px solid rgba(255, 255, 255, 0.16) !important;
            color: var(--text) !important;
            min-height: 46px;
        }

        div[data-baseweb="select"] span,
        div[data-baseweb="select"] input {
            color: var(--text) !important;
        }

        .stAlert {
            border-radius: 8px;
            border: 1px solid rgba(53, 230, 179, 0.28);
            background-color: rgba(53, 230, 179, 0.1);
            color: var(--text) !important;
        }

        .stAlert p {
            color: var(--text) !important;
        }

        hr {
            border-color: var(--border);
            margin: 2rem 0;
        }

        .footer-note {
            color: var(--muted);
            text-align: center;
            margin-top: 26px;
        }

        @media (max-width: 900px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1rem;
            }

            .topbar {
                align-items: flex-start;
                flex-direction: column;
            }

            .hero {
                grid-template-columns: 1fr;
            }

            .hero-copy {
                padding: 22px;
            }

            .hero-metrics,
            .metric-grid {
                grid-template-columns: 1fr;
            }

            .hero-title {
                font-size: 34px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display image after config and styles
# Stylized title using markdown + HTML
st.markdown("""
    <div style='text-align: center; font-size: 36px; font-weight: bold; color: #FFFFFF; margin-top: 20px;'>
        EV Adoption Forecaster for a County in Washington State
    </div>
""", unsafe_allow_html=True)

# Welcome subtitle
st.markdown("""
    <div style='text-align: center; font-size: 22px; font-weight: bold; padding-top: 10px; margin-bottom: 25px; color: #FFFFFF;'>
        Welcome to the Electric Vehicle (EV) Adoption Forecast tool.
    </div>
""", unsafe_allow_html=True)

st.image("ev-car-factory.jpg", use_container_width=True)

st.markdown("""
    <div class="instruction">
        Select a county and see the forecasted EV adoption trend for the next 3 years.
    </div>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("preprocessed_ev_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def forecast_county(county_df, forecast_horizon=36):
    county_code = county_df["county_encoded"].iloc[0]
    historical_ev = list(county_df["Electric Vehicle (EV) Total"].values[-6:])
    cumulative_ev = list(np.cumsum(historical_ev))
    months_since_start = county_df["months_since_start"].max()
    latest_date = county_df["Date"].max()
    future_rows = []

    for i in range(1, forecast_horizon + 1):
        forecast_date = latest_date + pd.DateOffset(months=i)
        months_since_start += 1
        lag1, lag2, lag3 = historical_ev[-1], historical_ev[-2], historical_ev[-3]
        roll_mean = np.mean([lag1, lag2, lag3])
        pct_change_1 = (lag1 - lag2) / lag2 if lag2 != 0 else 0
        pct_change_3 = (lag1 - lag3) / lag3 if lag3 != 0 else 0
        recent_cumulative = cumulative_ev[-6:]
        ev_growth_slope = (
            np.polyfit(range(len(recent_cumulative)), recent_cumulative, 1)[0]
            if len(recent_cumulative) == 6
            else 0
        )

        new_row = {
            "months_since_start": months_since_start,
            "county_encoded": county_code,
            "ev_total_lag1": lag1,
            "ev_total_lag2": lag2,
            "ev_total_lag3": lag3,
            "ev_total_roll_mean_3": roll_mean,
            "ev_total_pct_change_1": pct_change_1,
            "ev_total_pct_change_3": pct_change_3,
            "ev_growth_slope": ev_growth_slope,
        }

        pred = model.predict(pd.DataFrame([new_row]))[0]
        future_rows.append({"Date": forecast_date, "Predicted EV Total": round(pred)})

        historical_ev.append(pred)
        if len(historical_ev) > 6:
            historical_ev.pop(0)

        cumulative_ev.append(cumulative_ev[-1] + pred)
        if len(cumulative_ev) > 6:
            cumulative_ev.pop(0)

    return pd.DataFrame(future_rows)


def style_axis(ax, title, xlabel="Date", ylabel="Cumulative EV Count"):
    ax.set_title(title, fontsize=15, color="#eef4ff", pad=16, weight="bold")
    ax.set_xlabel(xlabel, color="#9fb0c7", labelpad=10)
    ax.set_ylabel(ylabel, color="#9fb0c7", labelpad=10)
    ax.set_facecolor("#101824")
    ax.grid(True, color="#314258", alpha=0.45, linewidth=0.8)
    ax.tick_params(colors="#c8d4e8")
    ax.spines["bottom"].set_color("#314258")
    ax.spines["left"].set_color("#314258")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    legend = ax.legend(frameon=True)
    legend.get_frame().set_facecolor("#162233")
    legend.get_frame().set_edgecolor("#314258")
    for text in legend.get_texts():
        text.set_color("#eef4ff")


df = load_data()
forecast_horizon = 36
county_list = sorted(df["County"].dropna().unique().tolist())

county = st.selectbox("Select a County", county_list)

if county not in df["County"].unique():
    st.warning(f"County '{county}' not found in dataset.")
    st.stop()

county_df = df[df["County"] == county].sort_values("Date")
forecast_df = forecast_county(county_df, forecast_horizon)

historical_cum = county_df[["Date", "Electric Vehicle (EV) Total"]].copy()
historical_cum["Source"] = "Historical"
historical_cum["Cumulative EV"] = historical_cum["Electric Vehicle (EV) Total"].cumsum()

forecast_df["Source"] = "Forecast"
forecast_df["Cumulative EV"] = (
    forecast_df["Predicted EV Total"].cumsum() + historical_cum["Cumulative EV"].iloc[-1]
)

combined = pd.concat(
    [
        historical_cum[["Date", "Cumulative EV", "Source"]],
        forecast_df[["Date", "Cumulative EV", "Source"]],
    ],
    ignore_index=True,
)

st.subheader(f"Cumulative EV Forecast for {county} County")
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("#101824")
colors = {"Historical": "#5aa9ff", "Forecast": "#28d7a4"}
for label, data in combined.groupby("Source"):
    ax.plot(
        data["Date"],
        data["Cumulative EV"],
        label=label,
        marker="o",
        linewidth=2.4,
        markersize=4,
        color=colors.get(label, "#eef4ff"),
    )
style_axis(ax, f"Cumulative EV Trend - {county} (3 Years Forecast)")
st.pyplot(fig)

historical_total = historical_cum["Cumulative EV"].iloc[-1]
forecasted_total = forecast_df["Cumulative EV"].iloc[-1]

if historical_total > 0:
    forecast_growth_pct = ((forecasted_total - historical_total) / historical_total) * 100
    trend = "increase" if forecast_growth_pct > 0 else "decrease"
    st.success(
        f"Based on the graph, EV adoption in **{county}** is expected to show a "
        f"**{trend} of {forecast_growth_pct:.2f}%** over the next 3 years."
    )
else:
    st.warning("Historical EV total is zero, so percentage forecast change can't be computed.")

st.markdown("---")
st.header("Compare EV Adoption Trends for up to 3 Counties")

multi_counties = st.multiselect("Select up to 3 counties to compare", county_list, max_selections=3)

if multi_counties:
    comparison_data = []

    for cty in multi_counties:
        cty_df = df[df["County"] == cty].sort_values("Date")
        cty_forecast = forecast_county(cty_df, forecast_horizon)

        hist_cum = cty_df[["Date", "Electric Vehicle (EV) Total"]].copy()
        hist_cum["Cumulative EV"] = hist_cum["Electric Vehicle (EV) Total"].cumsum()

        cty_forecast["Cumulative EV"] = (
            cty_forecast["Predicted EV Total"].cumsum() + hist_cum["Cumulative EV"].iloc[-1]
        )

        combined_cty = pd.concat(
            [
                hist_cum[["Date", "Cumulative EV"]],
                cty_forecast[["Date", "Cumulative EV"]],
            ],
            ignore_index=True,
        )

        combined_cty["County"] = cty
        comparison_data.append(combined_cty)

    comp_df = pd.concat(comparison_data, ignore_index=True)

    st.subheader("Comparison of Cumulative EV Adoption Trends")
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#101824")
    palette = ["#28d7a4", "#5aa9ff", "#ffca5a"]
    for index, (cty, group) in enumerate(comp_df.groupby("County")):
        ax.plot(
            group["Date"],
            group["Cumulative EV"],
            marker="o",
            label=cty,
            linewidth=2.4,
            markersize=4,
            color=palette[index % len(palette)],
        )
    style_axis(ax, "EV Adoption Trends: Historical + 3-Year Forecast")
    st.pyplot(fig)

    growth_summaries = []
    for cty in multi_counties:
        cty_df = comp_df[comp_df["County"] == cty].reset_index(drop=True)
        historical_total = cty_df["Cumulative EV"].iloc[len(cty_df) - forecast_horizon - 1]
        forecasted_total = cty_df["Cumulative EV"].iloc[-1]

        if historical_total > 0:
            growth_pct = ((forecasted_total - historical_total) / historical_total) * 100
            growth_summaries.append(f"{cty}: {growth_pct:.2f}%")
        else:
            growth_summaries.append(f"{cty}: N/A (no historical data)")

    growth_sentence = " | ".join(growth_summaries)
    st.success(f"Forecasted EV adoption growth over next 3 years: {growth_sentence}")

st.success("Forecast complete")
st.markdown(
    '<div class="footer-note"> <strong>EV VEHICLE/CHARGING DEMAND PREDICTION</strong> by ANURAG SWAIN</div>',
    unsafe_allow_html=True,
)
