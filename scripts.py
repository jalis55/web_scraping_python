import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import time

total_dataset=[]
def scraper(year,gender,page):
    
    data={}
    url=f'https://www.swimcloud.com/recruiting/rankings/{year}/{gender}/?page={page}'
    response=requests.get(url)
    page_content=BeautifulSoup(response.content,'html.parser')
    all_names=page_content.findAll('a',attrs={'class':'u-text-semi'})
    individual_profile='https://www.swimcloud.com'+all_names[0]['href']
    individual_profile_content=requests.get(individual_profile).content
    individual_profile_data=BeautifulSoup(individual_profile_content,'html.parser')
    individual_profile_data_year=individual_profile_data.find('p',attrs={'class':'c-list-bar__description'}).text
    data['year']=individual_profile_data_year
    individual_profile_data_name=individual_profile_data.find('span',attrs={'class':'u-mr-'}).text
    name=individual_profile_data_name.split(' ')
    data['first name']=name[0]
    data['last name']=''.join(name[1:])
    individual_profile_data_country=individual_profile_data.find('h5',attrs={'class':'c-link-boxes-item__primary-text'}).text
    data['country']=individual_profile_data_country.replace('  ','').replace('\n','')
    individual_profile_data_details=individual_profile_data.select('ul[class="o-list-inline o-list-inline--dotted"] li')
    individual_profile_data_location=individual_profile_data_details[0].text
    location=individual_profile_data_location.split(',')
    data['city']=location[0]
    data['state']=location[1]
    individual_profile_data_club=individual_profile_data_details[1].text
    data['club']=individual_profile_data_club.replace('\n','')
    try:
        individual_profile_data_instagram=individual_profile_data_details[3].find('a')['href']
        data['instagram']=individual_profile_data_instagram
    except:
        data['instagram']=None
    #data['instagram']=individual_profile_data_instagram
    individual_powerindex=individual_profile +'/powerindex'
    individual_powerindex=requests.get(individual_powerindex).content
    individual_powerindex_details=BeautifulSoup(individual_powerindex,'html.parser')
    event_tds=individual_powerindex_details.select('tr td[class="u-text-truncate u-text-semi"]')[:3]
    time_tds=individual_powerindex_details.select('tr td[class="c-table-clean__time u-text-semi"]')[:3]
    data['event-1']=event_tds[0].text
    data['event-1 time']=time_tds[0].text
    data['event-2']=event_tds[1].text
    data['event-2 time']=time_tds[1].text
    data['event-3']=event_tds[2].text
    data['event-3 time']=time_tds[2].text
    
    
    total_dataset.append(data)

if __name__=="__main__":
    import multiprocessing as mp
    start=time.time()
    p1=mp.Process(target=scraper,args=(2025,'M',1,))
    p2=mp.Process(target=scraper,args=(2025,'M',2,))
    p3=mp.Process(target=scraper,args=(2025,'M',3,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end=time.time()
    
    print(total_dataset)
    print(end-start)
    