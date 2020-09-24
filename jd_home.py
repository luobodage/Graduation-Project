import requests
import UserAgent
import lxml.etree as le
import re
import os


def spider_home():
    """
    获取物品的url以及标题价格
    :return: 返回物品编码
    """
    shop = input("请输入你要搜索的商品：")

    global headers

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

        price = content.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div/strong/i/text()')

        title_01 = content.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div/a/em/text()')

        title = [x.strip() for x in title_01 if x.strip() != ''] # 提取标题 将多余空格和\n去除

        re_01 = re.compile(r'\d+')

        number = re_01.findall(str(href))

        shop_price_01 = "".join(price)
        print("商品价格：" + shop_price_01)
        # for shop_price in price:
        #
        #     print("商品价格：" + shop_price)

        global shop_title  # 全局定义商品题目 进行文件改标题
        shop_title_01 = "".join(title)
        print("商品标题：" + shop_title_01)
        # for shop_title in title:
        #     print("商品标题：" + shop_title)

        for index in href:
            global href_shop
            href_shop = 'http:' + index
            # print(href_shop)

        for num in number:
            # print(num)
            return num

    except:
        print('爬取失败')


def file_rename():

    file_srcFile = 'id.txt'

    file_dstFile = shop_title + '.txt'

    os.rename(file_srcFile, file_dstFile)  # 改标题

    img_srcFile = 'ciyun.png'

    img_dstFile = shop_title + '.png'

    os.rename(img_srcFile, img_dstFile)


if __name__ == '__main__':

    spider_home()