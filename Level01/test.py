import pandas as pd

url = 'https://ds-lecture-data.s3.ap-northeast-2.amazonaws.com/kt%26g/kt%26g_0.csv'
headers = ['분기', '매출액', '영업이익', '영업이익(발표기준)', '세전계속사업이익',
           '당기순이익', '당기순이익(지배)', '당기순이익(비지배)', '자산총계', '부채총계',
           '자본총계', '자본총계(지배)', '자본총계(비지배)', '자본금', '영업활동현금흐름',
           '투자활동현금흐름', '재무활동현금흐름', '영업이익률', '순이익률', 'ROE(%)',
           'ROA(%)', '부채비율', '자본유보율', 'EPS(원)', 'PER(배)']

df = pd.read_csv(url,names=headers)


# hey = df['영업이익']

# for i in range(len(hey)):
#     hey[i] = hey[i].replace(',', '')

# boy = hey.astype(str).astype(int)
# print(boy+100000, type(boy))

def toInt(string):
    return int(string.replace(',',''))

def margin(sales, profit):
    return profit/sales*100


df['영업이익']=df['영업이익'].apply(toInt)
df['매출액']=df['매출액'].apply(toInt)

df['영업이익률2'] = margin(df['영업이익'], df['매출액'])
#print(result)
# pandas => axis=1
# lambda => axis=0
df['영업이익']


df['영업이익률2'] = df.apply(lambda x: margin(x['영업이익'], x['매출액']), axis=1)
print(df['영업이익률2'])