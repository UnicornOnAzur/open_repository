import pandas as pd


def make_dataframe(col):
    df = pd.DataFrame(columns=["a", "b", "c"])
    col.dataframe(data=df, use_container_width=True)


if __name__ == "__main__":
    print("This is the open repository")
