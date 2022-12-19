# import os
import requests
from bs4 import BeautifulSoup
# from dotenv import load_dotenv


################# For preload of the login website ##########################

# s = requests.Session()
# headers = {
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
# }
# # load_dotenv()
# # login_data = os.getenv('login_data')

# login_data = {
# 'username':'bishalbashyal33@gmail.com',
# 'password':'hultprize12!!',
# }

# base_url = "https://admin-oncampus.hultprize.org"
# log_url = "/Account/Login"
# home_url = base_url+log_url
# # urlopen(home_url, context=ssl.create_default_context(cafile=certifi.where()))
# # print(home_url)
# res = s.get(home_url, headers=headers, verify=False)
# soup = BeautifulSoup(res.content, 'html5lib')
# value = soup.find('input', attrs={'name':'__RequestVerificationToken'})['value']
# login_data['__RequestVerificationToken'] = value

# page = s.post(home_url, data=login_data, headers=headers)



def fetch_data():

    s = requests.Session()
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    # load_dotenv()
    # login_data = os.getenv('login_data')

    login_data = {
    'username':'bishalbashyal33@gmail.com',
    'password':'hultprize12!!',
    }

    base_url = "https://admin-oncampus.hultprize.org"
    log_url = "/Account/Login"
    home_url = base_url+log_url
    # urlopen(home_url, context=ssl.create_default_context(cafile=certifi.where()))
    # print(home_url)
    res = s.get(home_url, headers=headers, verify=False)
    soup = BeautifulSoup(res.content, 'html5lib')
    value = soup.find('input', attrs={'name':'__RequestVerificationToken'})['value']
    login_data['__RequestVerificationToken'] = value

    page = s.post(home_url, data=login_data, headers=headers)
    registerBar_soup = BeautifulSoup(page.content, "html.parser")
    results = registerBar_soup.find("div", id="mySidenav")
    link_html = results.find_all("a", href=True)
    link_list = []
    for item in link_html:
        link_list.append(item['href'])


        
    # registration page
    reg_url = "https://admin-oncampus.hultprize.org/registration"
    reg_res = s.get(reg_url, headers=headers)
    reg_soup = BeautifulSoup(reg_res.content, 'html5lib')
    reg_page = reg_soup.find("div", id="registrations")
    reg_table = reg_page.find('tbody')
    table_row = reg_table.find_all('tr')
    total_list = []
    for item in table_row:
        each_team = item.find_all('td')
        team = []
        for each in each_team:
            for i in each:
                val = (i.text).strip()
                # print(val)
                if (val != "Edit") and (val != "Team Details") and (val !='\n') and (val!=''):
                    # print(val)
                    team.append(val)
                
        total_list.append(team)
            
    return total_list