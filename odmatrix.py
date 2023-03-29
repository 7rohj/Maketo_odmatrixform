filename = input("파일명을 입력해주세요:")

def odmatrix(filename):
    import os
    import pandas as pd

    path = os.getcwd()
    print(path,'\\',filename)

    df = pd.read_csv(f'./{filename}.txt', delimiter = '\t')

    od_matrix = df.groupby(['Origin', 'Destination'])['Auto'].sum().unstack().fillna(0)
    od_matrix

    return od_matrix.to_csv('./odmatrix 생성완료.csv')
    print('파일생성완료!')
   
if __name__ == "__main__":
    odmatrix(filename)