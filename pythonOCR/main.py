from aip import AipOcr
import os,shutil
import re as formatr

dir = r''
dirs = r''


def read_image(path):
    dir_i = dir + '\\'
    print(dir_i + path)
    with open(dir_i + path, 'rb') as f:
        image = f.read()
    return image


api_key = ''
app_id = ''
secret_key = ''
client = AipOcr(app_id, api_key, secret_key)
fs = os.listdir(dir)
import pandas as pd
df = pd.read_excel(r"D:\work\code\pythonProject1\test.xls")  
print(df)
df_li = df.values.tolist()
nameList = []
for s_li in df_li:
    nameList.append(s_li[1])
print(nameList)
for image in fs:
    i = read_image(image)
    path = dir + '\\' + image
    print(path)
    inf = client.basicGeneral(i)
    str = ''
    for response in inf['words_result']:
        for words in response['words']:
            str = str + words

        
    print(str)
    res = ''.join(formatr.findall('[\u4e00-\u9fa5]', str))
    for name in nameList:
        print(name)
        print(res)
        if (res.__contains__(name)):
            print('小石头在这')
            file = os.path.splitext(image)
            filename, type = file
            print(type)
            filename =dirs+'\\' +name+'\\' + res +type
            dstpath =dirs+'\\' +name
            print(dstpath)
            if not os.path.exists(dstpath):
               os.makedirs(dstpath)
            shutil.copy(path,filename)

    print(inf)
