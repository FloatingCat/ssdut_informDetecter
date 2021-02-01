import requests
from bs4 import BeautifulSoup
from src.sender import sender

def GetPageInfo1():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 '
                      'Safari/537.36 '
    }
    page = requests.get('https://ssdut.dlut.edu.cn/index/bkstz.htm', headers)
    PageContent = BeautifulSoup(page.content, 'html.parser')
    newestHref = str(PageContent.find_all('a',class_='c56628',attrs={ 'target':"_blank"}))
    # newestHref = page.text
    # print(newestHref)
    with open('./data/0'+'last.txt','r',encoding='utf-8') as file:
        lastHref = file.read()
        # print(lastHref)
    file.close()
    if lastHref != newestHref :
        print('Detected!')
        sender('https://ssdut.dlut.edu.cn/index/bkstz.htm') #
        with open('./data/0'+'last.txt','w',encoding='utf-8') as file:
            file.write(newestHref)
            file.close()
    print( '0 Completed')

def GetPageInfo2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 '
                      'Safari/537.36 '
    }
    page = requests.get('http://dutdice.dlut.edu.cn/xszcq/jztz/jztz.htm', headers)
    PageContent = BeautifulSoup(page.content, 'html.parser')
    newestHref = str(PageContent.select('li > a'))
    # newestHref = page.text
    # print(newestHref)
    with open('./data/1'+'last.txt','r',encoding='utf-8') as file:
        lastHref = file.read()
        # print(lastHref)
    file.close()
    if lastHref != newestHref :
        print('Detected!')
        sender('http://dutdice.dlut.edu.cn/xszcq/jztz/jztz.htm')
        with open('./data/1'+'last.txt','w',encoding='utf-8') as file:
            file.write(newestHref)
            file.close()
    print( '1 Completed')


if __name__ == "__main__":
    GetPageInfo1()
    GetPageInfo2()
