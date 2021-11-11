import pandas as pd
df = pd.read_excel(r"D:\work\code\pythonProject1\test.xls")  # 读取项目名称列,不要列名
print(df)
df_li = df.values.tolist()
result = []
for s_li in df_li:
    result.append(s_li[1])
print(result)