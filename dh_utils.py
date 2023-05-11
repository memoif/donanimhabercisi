import requests
from bs4 import BeautifulSoup
def get_id(link):
    linkler = []
    soup = BeautifulSoup(requests.get(link).content,"html.parser").find_all("div", class_="kl-icerik-satir yenikonu")
    for i in range(1, len(soup)):
        x = soup[i].find("div", class_="kl-konu").findChildren()[0].get("href")
        linkler.append("https://forum.donanimhaber.com" + x)
    linkler = [(int(link[link.rfind("-")+1::]),link) for link in linkler]
    return linkler
def get_max(link):
    ids = get_id(link)
    return max(ids, key=lambda x : x[0])
def get_details(link : str):
    URL = link
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    forum = soup.find("nav", class_="forumdizin").find_all("a")[-1].text
    konu_ismi = soup.find("h1", class_="kl-basligi upInfinite").text.strip()
    konu_sahibi = soup.find("div", class_="ki-kullaniciadi member-info").text.strip()
    lis = [forum, konu_ismi, konu_sahibi]
    return lis