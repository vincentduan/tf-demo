import csv
import pandas

# csvfile = open('./test.csv', 'r')
# data = mycsv.reader(csvfile)

# for raw in data:
#     print(raw[1])


# with open('./test.csv', 'r') as incsv, open('./test-out.csv','w') as outcsv:
#     r = csv.reader(incsv, delimiter=',')
#     w = csv.writer(outcsv, delimiter='\t')
#     for raw in r:
#         print(raw)
#         w.writerow(raw)

#显示所有列
pandas.set_option('display.max_columns', None)
#显示所有行
pandas.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50

df_chunk = pandas.read_csv('D:/test/internet_ip_daily_hk-20190731-20190810/000000_0',
                           sep='\t',
                           quotechar='"',
                           names=["ip", "timestamp", "desc_info", "related_identity", "record_num", "type", "date"],
                           chunksize=10000,
                           dtype={'desc_info': str})
# quotechar=' '表示当数据中出现"时, 使用空格进行包裹, 默认使用"包裹，用作标识开始和解释的字符，引号内的分割符将被忽略
df_chunk.get_chunk(5).to_csv('./result.csv', quotechar=' ')
