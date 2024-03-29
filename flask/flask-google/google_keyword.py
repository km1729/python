import requests
from bs4 import BeautifulSoup

def get_search_count(keyword):
    url = "https://www.google.com/search?q={}".format(keyword)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    res = requests.get(url, headers=headers)

    #구문분석
    # soup text 결과안에서 result-stats tag부분 찾기
    soup = BeautifulSoup(res.text, 'lxml')
    number = soup.select_one('#result-stats').text
    # print(number) # 검색결과 약 7,320,000개 (0.47초) 
    number = number[number.find('About')+6:number.rfind(' results')] # 7,320,000
    number = float(number.replace(',','')) # 7320000
    return number

if __name__ == '__main__':
    # python3 google_keyword.py를 실행할 때 침착맨에 관한 검색 결과 갯수 보여짐
    print(get_search_count("2022 fifa"))
