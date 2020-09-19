import requests
import UserAgent
import lxml.etree as le
import re

def spider_home():
    shop = input("请输入你要搜索的商品：")
    headers = UserAgent.get_headers()  # 随机获取一个headers
    url = 'https://search.jd.com/Search?keyword={shop}&enc=utf-8&wq=%E5%B0%8F&pvid=469d5d51a3184cc9a053124dc020b31f'.format(
        shop=shop
    )
    try:
        r = requests.get(
            url=url,
            headers=headers
        ).content
        content = le.HTML(r)
        href = content.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/@href')
        re_01 = re.compile(r'\d+')
        number = re_01.findall(str(href))
        for num in number:
            return num
        for index in href:
            print('http:' + index)
    except:
        print('爬取失败')


if __name__ == '__main__':
    spider_home()
