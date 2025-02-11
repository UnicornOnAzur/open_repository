import numpy as np
import pandas as pd
import plotly.express as px


def make_dataframe(col):
    df = pd.DataFrame(columns=["a", "b", "c"])
    col.dataframe(data=df, use_container_width=True)


def make_graph(col):
    df = px.data.gapminder().query("year == 2007")
    fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                    color='lifeExp', hover_data=['iso_alpha'],
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    col.plotly_graph(fig)


if __name__ == "__main__":
    print("This is the open repository")
