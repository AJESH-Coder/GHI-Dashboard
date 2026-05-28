import streamlit as st
import pandas as pd

GHI_Data=pd.read_csv("C:/Users/jhaan/OneDrive/Desktop/GHI.CSV")
GHI_Data.index=GHI_Data.index+1

st.title("Stats Of The Countries")

class Stats:
    def table(self):
        st.write(GHI_Data)

    def country_rank(self):
        Highest_rank=GHI_Data["Rank"].min()
        Highest_country = GHI_Data.loc[GHI_Data["Rank"] == Highest_rank, "Country"].values[0]
        Lowest_rank=GHI_Data["Rank"].max()
        Lowest_country = GHI_Data.loc[GHI_Data["Rank"] == Lowest_rank, "Country"].values[0]
        st.subheader(f"Country with highest rank in GHI (In 2025): \n {Highest_country}, Rank: {Highest_rank}")
        st.subheader(f"Country with lowest rank in GHI (In 2025): \n {Lowest_country}, Rank: {Lowest_rank}")

    def average_data(self):

        GHI_Data["Avg"] = round((GHI_Data["2000"] + GHI_Data["2008"] + GHI_Data["2016"] + GHI_Data["2025"]) / 4, 2)

        lowest = GHI_Data.loc[GHI_Data["Avg"].idxmin(), "Country"]
        highest = GHI_Data.loc[GHI_Data["Avg"].idxmax(), "Country"]
        lowest_avg = GHI_Data["Avg"].min()
        highest_avg = GHI_Data["Avg"].max()

        st.subheader(f"Country with highest average in GHI across 4 years is: \n {highest}, Average: {highest_avg}")
        st.subheader(f"Country with lowest average in GHI across 4 years is: \n {lowest}, Average: {lowest_avg}")

    def improvement(self):
        GHI_Data["Improvement"] = round(GHI_Data["2000"] - GHI_Data["2025"], 2)
        Most_improved = GHI_Data.loc[GHI_Data["Improvement"].idxmax(), "Country"]
        Least_improved = GHI_Data.loc[GHI_Data["Improvement"].idxmin(), "Country"] 
        Most_Improved_By = GHI_Data["Improvement"].max()
        Least_Improved_By = GHI_Data["Improvement"].min()

        st.subheader(f"Country which has most improved in GHI from 2000 to 2025 is: \n {Most_improved}, Improved by: {Most_Improved_By}")
        st.subheader(f"Country which has less improved in GHI from 2000 to 2025 is: \n {Least_improved}, Improved by: {Least_Improved_By}")

    def nepal_journey(self):
        st.subheader("Nepal's Journey")
        st.write("Nepal has improved very significantly from 37.0 in 2000 to 14.8 in 2025." \
        " This country has the most improvement in South Asia because of it substantial reductions in child stunting, " \
        "targeted health interventions, and strong policy commitments.")

    def advice(self):
        st.subheader("Improvement Advice")

        advice = {
            "Nepal": "Continue investing in agriculture and maternal nutrition programs.",
            "India": "Focus on reducing child stunting and improving food distribution.",
            "Bangladesh": "Strengthen social protection programs and flood resilience.",
            "Pakistan": "Improve political stability and access to clean water.",
            "Sri Lanka": "Maintain current progress and focus on economic recovery.",
            "Afghanistan": "Urgent need for conflict resolution and humanitarian aid."
        }

        for country, tip in advice.items():
            st.write(f"{country}: {tip}")

Stat=Stats()
Stat.table()
st.divider()
Stat.country_rank()
Stat.average_data()
Stat.improvement()
st.divider()
Stat.nepal_journey()
st.divider()
Stat.advice()