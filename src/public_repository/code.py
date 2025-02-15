# -*- coding: utf-8 -*-
"""
@author: UnicornOnAzur

This module provides functionalities to create and display a DataFrame
and a treemap graph using Streamlit and Plotly.
"""

# Third party
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


def create_empty_dataframe(column: st.delta_generator.DeltaGenerator) -> None:
    """
    Creates an empty DataFrame with specified columns and displays it in the
    provided column.

    Args:
        column: The column object where the DataFrame will be displayed.
    """
    df: pd.DataFrame = pd.DataFrame(columns=["a", "b", "c"])
    column.dataframe(data=df, use_container_width=True)


def display_treemap(column: st.delta_generator.DeltaGenerator) -> None:
    """
    Generates a treemap graph using the Gapminder dataset for the year 2007
    and displays it in the provided column.

    Args:
        column: The column object where the graph will be displayed.
    """
    df: pd.DataFrame = px.data.gapminder().query("year == 2007")
    fig: go.Figure = px.treemap(df,
                                path=[px.Constant("world"),
                                      "continent",
                                      "country"],
                                values="pop",
                                color="lifeExp",
                                hover_data=["iso_alpha"],
                                color_continuous_scale="RdBu",
                                color_continuous_midpoint=np.average(
                                    df["lifeExp"], weights=df["pop"]),
                                title="Chart from public repository")
    column.plotly_chart(fig, key="public")


if __name__ == "__main__":
    print("This is the open repository")
