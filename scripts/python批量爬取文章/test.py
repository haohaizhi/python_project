# coding=utf-8

import requests
import re
import xlwt
from bs4 import BeautifulSoup
import pdfkit

def save_div_content_as_pdf(url, output_file):
    try:
        # 发起请求获取网页内容
        r = requests.get(url)
        r.raise_for_status()

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(r.text, 'html.parser')

        # 定位到<div class="content">下的内容
        div_content = soup.find('div', class_='content')
        #print(div_content) 
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(div_content))
       
    except requests.exceptions.RequestException as e:
        print(f'请求失败: {e}')
    except Exception as e:
        print(f'发生错误: {e}')

def get_msg():
    number = 0
    for i in range(1, 5):  # 页数自己随便改
        print("正在爬取第" + str(i) + "页数据...")
        url_start = 'https://stock.finance.sina.com.cn/stock/go.php/vReport_List/kind/search/index.phtml?symbol=sz300682&t1=all&p=' + str(i)
        
        r = requests.get(url_start)
        #print(r.text)
        reg = re.compile(r'<td class="tal f14">.*?title="(.*?)" href="(.*?)">.*?</td>',re.S)            
        items = reg.findall(r.text)
        if not items:
            return
        for item in items:
            url_end = 'https:' + item[1]
            title = item[0]
            print(title + " 网址:" + url_end)
            filename = title + '.html'
            save_div_content_as_pdf(url_end, filename)
            #r2 = requests.get(url_end)
            #print(r2.text)
def test():
    url = "https://stock.finance.sina.com.cn/stock/go.php/vReport_Show/kind/search/rptid/746707369274/index.phtml"
    output_pdf = "test.html"
    save_div_content_as_pdf(url, output_pdf)

def main():
	get_msg()


if __name__ == '__main__':
	main()
