import requests
from bs4 import BeautifulSoup
# url = 'https://book.douban.com/tag/?icn=index-nav'
# down_data = requests.get(url)
# soup = BeautifulSoup(down_data.text, 'lxml')
# #tags=soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
# tags = soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
# catogries_list = []
# for tag in tags:
#     tag = tag.get_text()
#     helf="https://book.douban.com/tag/"
#     url = helf + str(tag)
#     print(url)
    #catogries_list.append(url)

def get_details(url):
    #url="https://book.douban.com/tag/程序"
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text.encode('utf-8'),'lxml')
    tag = url.split('?')[0].split('/')[-1]
    details = soup.select("#subject_list > ul > li > div.info > div.pub")
    scores = soup.select("#subject_list > ul > li > div.info > div.star.clearfix > span.rating_nums")
    persons = soup.select("#subject_list > ul > li > div.info > div.star.clearfix > span.pl")
    titles = soup.select("#subject_list > ul > li > div.info > h2 > a")
    list = []
    print('=======================')
    print(len(details))
    for detail, score, person, title in zip(details,scores,persons,titles):
        list = []
        list.append(detail)
        list.append(score)
        list.append(person)
        list.append(title)
        print(list)

url = "https://book.douban.com/tag/程序"
get_details(url)


for page in range(7):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    #把这个放到get_details函数中解决，get_details返回一个new_link进行拼装
    new_link = soup.select("#subject_list > div.paginator > span.next > link")
    #new-link是一个list可能为空
    new_link_part = str(new_link[0]).split('?')[1].split("\"")[0]
    l = new_link_part.split('amp;')[0] + new_link_part.split('amp;')[1]
    url = url + '/?' + l
    get_details(url)
    print('=======================')
    print(page)
    print('=======================')
