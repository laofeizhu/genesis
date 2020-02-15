import pandas as pd

if __name__ == "__main__":
  bug1 = pd.DataFrame(data={"size": [1], "age": [0], "point": [(0, 1)]})
  bug2 = pd.DataFrame(data={"size": [2], "age": [1], "point": [(1, 2)]})
  bug1.to_csv('./tmp.csv', mode='a', header=True)
  bug2.to_csv('./tmp.csv', mode='a', header=False)
