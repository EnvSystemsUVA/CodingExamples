import pandas as pd

def reshape(filename):
    df = pd.read_csv(filename, index_col=[0,1], skipinitialspace=True)
    df = df.unstack()
    df = df.transpose()
    df.to_csv(filename)
    return None

reshape("Start_Julia.csv")
reshape("Shut_Julia.csv")
reshape("Commit_Julia.csv")
reshape("Generation_Julia.csv")