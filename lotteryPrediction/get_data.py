import pandas as pd
import csv

def get_one_page(page):
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (str(page))
    tb = pd.read_html(url, skiprows=[0, 1])[0]  # 跳过前两行
    return tb.drop([len(tb)-1])  # 去掉最后一行

save_csv = r'/home/ubuntu/PycharmProjects/ML_PY/lotteryPrediction/data/lottery_data.csv'

with open(save_csv, 'w', encoding='utf-8-sig', newline='') as f:
    csv.writer(f).writerow(['开奖日期', '期号', '中奖号码', '销售额(元)', '中奖注数一等奖', '中奖注数二等奖', '详细'])

for i in range(1,123):  # 2019-06-03 17:29:15 目前122页数据
    get_one_page(i).to_csv(save_csv, mode='a', encoding='utf_8_sig', header=0, index=0)
    print('第'+str(i)+'页抓取完成')
