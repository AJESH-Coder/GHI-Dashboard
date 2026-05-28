import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

GHI_Data=pd.read_csv("C:/Users/jhaan/OneDrive/Desktop/GHI.CSV")
GHI_Data.index=GHI_Data["Country"]

class Graphs:
    def individual_graph(self):
        Year_For_Graph = GHI_Data[Select_Box_Individual]
        st.bar_chart(Year_For_Graph)

    def comparison_graph_bar(self):
        Year_For_Comparison = GHI_Data[Select_Box_comparison]
        Avg_Of_2025 = sum(GHI_Data["2025"]) / 6
        Avg_Of_Selected_Year = sum(Year_For_Comparison) / 6
        fig, ax = plt.subplots()
        ax.bar([Select_Box_comparison, "2025"], [Avg_Of_Selected_Year, Avg_Of_2025], width=0.3, color=["#E74C3C", "#27AE60"])
        ax.set_ylabel("Avg GHI Score")
        ax.set_title("Year Comparison")
        st.pyplot(fig)

    def comparison_graph_scatter(self):
        Year_For_Comparison = GHI_Data[Select_Box_comparison]
        Avg_Of_2025 = sum(GHI_Data["2025"]) / 6
        Avg_Of_Selected_Year = sum(Year_For_Comparison) / 6
        fig, ax = plt.subplots()
        ax.scatter([Select_Box_comparison, "2025"], [Avg_Of_Selected_Year, Avg_Of_2025])
        ax.set_ylabel("Avg GHI Score")
        ax.set_title("Year Comparison")
        st.pyplot(fig)

    def comparison_graph_pie(self):
        Year_For_Comparison = GHI_Data[Select_Box_comparison]
        Avg_Of_2025 = sum(GHI_Data["2025"]) / 6
        Avg_Of_Selected_Year = sum(Year_For_Comparison) / 6
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie([Avg_Of_Selected_Year, Avg_Of_2025], labels=[Select_Box_comparison, "2025"], colors=["#E74C3C", "#27AE60"], autopct="%1.1f%%")
        ax.set_ylabel("Avg GHI Score")
        ax.set_title("Year Comparison")
        st.pyplot(fig)

Select_Box_Individual = st.selectbox("Select year to see stats in graph:", ['2000', '2008', '2016', '2025'])
st.success(f"Data of year: {Select_Box_Individual}")
Graph=Graphs()
Graph.individual_graph()
st.divider()

Select_Box_comparison = st.selectbox("Select year to compare stats with 2025:", ['2000', '2008', '2016'])
Select_Box_Graph = st.selectbox("Select the graph to see the comparison:", ['Scatter Graph', 'Bar Graph', 'Pie Chart'])

if Select_Box_Graph == 'Scatter Graph':
    Graph.comparison_graph_scatter()

elif Select_Box_Graph == 'Bar Graph':
    Graph.comparison_graph_bar()

elif Select_Box_Graph == 'Pie Chart':
    Graph.comparison_graph_pie()