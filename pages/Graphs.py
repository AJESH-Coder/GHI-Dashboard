import streamlit as st
import pandas as pd
import plotly.express as px

GHI_Data = pd.read_csv("ghi.csv")
GHI_Data.index = GHI_Data["Country"]

class Graphs:
    def individual_graph(self):
        Year_For_Graph = GHI_Data[["Country", Select_Box_Individual]]
        fig = px.bar(Year_For_Graph, x="Country", y=Select_Box_Individual)
        st.plotly_chart(fig)

    def comparison_graph_bar(self):
        Year_For_Comparison = GHI_Data[Select_Box_comparison]
        Avg_Of_2025 = sum(GHI_Data["2025"]) / 6
        Avg_Of_Selected_Year = sum(Year_For_Comparison) / 6
        fig = px.bar(x=[Select_Box_comparison, "2025"], y=[Avg_Of_Selected_Year, Avg_Of_2025], color=[Select_Box_comparison, "2025"], labels={"x": "Year", "y": "Avg GHI Score"})
        st.plotly_chart(fig)

    def comparison_graph_scatter(self):
        Year_For_Comparison = GHI_Data[Select_Box_comparison]
        Avg_Of_2025 = sum(GHI_Data["2025"]) / 6
        Avg_Of_Selected_Year = sum(Year_For_Comparison) / 6
        fig = px.scatter(x=[Select_Box_comparison, "2025"], y=[Avg_Of_Selected_Year, Avg_Of_2025], labels={"x": "Year", "y": "Avg GHI Score"})
        st.plotly_chart(fig)

    def comparison_graph_pie(self):
        Year_For_Comparison = GHI_Data[Select_Box_comparison]
        Avg_Of_2025 = sum(GHI_Data["2025"]) / 6
        Avg_Of_Selected_Year = sum(Year_For_Comparison) / 6
        fig = px.pie(values=[Avg_Of_Selected_Year, Avg_Of_2025], names=[Select_Box_comparison, "2025"], color_discrete_sequence=["#E74C3C", "#27AE60"])
        st.plotly_chart(fig)

Select_Box_Individual = st.selectbox("Select year to see stats in graph:", ['2000', '2008', '2016', '2025'])
st.success(f"Data of year: {Select_Box_Individual}")
Graph = Graphs()
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
