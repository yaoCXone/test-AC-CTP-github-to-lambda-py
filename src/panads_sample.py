import pandas as pd


def print_sample_2x2():   
    d={'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1')