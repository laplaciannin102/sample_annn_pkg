from os.path import dirname
import pandas as pd

module_path = dirname(__file__)

def load_sample_data0():
    df = pd.read_csv(
        module_path + '/sample_data/sample_data.csv',
        encoding='utf-8'
    )

    print('load sample data0')
    print('file format: {}'.format('csv'))
    print('sample pandas.DataFrame:')
    print(df)

    return df

def load_sample_data1():
    df = pd.read_excel(
        module_path + '/sample_data/sample_data.xlsx',
        index_col=0
    )

    print('load sample data1')
    print('file format: {}'.format('excel'))
    print('sample pandas.DataFrame:')
    print(df)

    return df