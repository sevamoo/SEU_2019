import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


if __name__ == '__main__':
    init = True
    t0 = time.time()
    cities = pd.read_csv('./data/AQI_cities.csv').values[:,0]
    print len(cities)
    while init:
        cols = ['cityname','min_o3','max_o3','min_pm25','max_pm25','min_pm10','max_pm10','min_so2','max_so2','min_no2','max_no2','min_co','max_co']
        DF = pd.DataFrame(data= np.empty((len(cities),len(cols)),dtype=str),columns=cols)
        
        for i,city in enumerate(cities[:]):
            url = 'http://aqicn.org/city/'+ city
            try:
                r = requests.get(url, timeout=1200)
                soup = BeautifulSoup(r.content, 'html.parser')
        
                try:
                    min_o3 = soup.find("td", {"id": "min_o3"})
                    min_o3 = int(str(min_o3).split(">")[1].split("<")[0])
                except:
                    min_o3 = np.nan
                try:
                    max_o3 = soup.find("td", {"id": "max_o3"})
                    max_o3 = int(str(max_o3).split(">")[1].split("<")[0])
                except:
                    max_o3 = np.nan
                try:
                    min_pm25 = soup.find("td", {"id": "min_pm25"})
                    min_pm25 = int(str(min_pm25).split(">")[1].split("<")[0])
                except:
                    min_pm25 = np.nan
                try:
                    max_pm25 = soup.find("td", {"id": "max_pm25"})
                    max_pm25 = int(str(max_pm25).split(">")[1].split("<")[0])
                except:
                    max_pm25 = np.nan
                try:
                    min_pm10 = soup.find("td", {"id": "min_pm10"})
                    min_pm10 = int(str(min_pm10).split(">")[1].split("<")[0])
                except:
                    min_pm10 = np.nan
                try:
                    max_pm10 = soup.find("td", {"id": "max_pm10"})
                    max_pm10 = int(str(max_pm10).split(">")[1].split("<")[0])
                except:
                    max_pm10 = np.nan
        
                try:
                    min_so2 = soup.find("td", {"id": "min_so2"})
                    min_so2 = int(str(min_so2).split(">")[1].split("<")[0])
                except:
                    min_so2 = np.nan
                try:
                    max_so2 = soup.find("td", {"id": "max_so2"})
                    max_so2 = int(str(max_so2).split(">")[1].split("<")[0])
                except:
                    max_so2 = np.nan
                try:
                    min_no2 = soup.find("td", {"id": "min_no2"})
                    min_no2 = int(str(min_no2).split(">")[1].split("<")[0])
                except:
                    min_no2 = np.nan
                try:
                    max_no2 = soup.find("td", {"id": "max_no2"})
                    max_no2 = int(str(max_no2).split(">")[1].split("<")[0])
                except:
                    max_no2 = np.nan
                try:
                    min_co = soup.find("td", {"id": "min_co"})
                    min_co = int(str(min_co).split(">")[1].split("<")[0])
                except:
                    min_co = np.nan
                try:
                    max_co = soup.find("td", {"id": "max_co"})
                    max_co = int(str(max_co).split(">")[1].split("<")[0])
                except:
                    max_co = np.nan
            
                vec = [city,min_o3,max_o3,min_pm25,max_pm25,min_pm10,max_pm10,min_so2,max_so2,min_no2,max_no2,min_co,max_co]
                DF.ix[i].values[:] = vec
                if i%10==0:
                    print i, city
                
            except:
                pass
            try:
                del r
            except:
                pass
            

        t = time.localtime()
        date = str(t.tm_year)+"_"+str(t.tm_mon)+"_"+str(t.tm_mday)
        print date
        DF.to_csv('./data/AQI_{}.csv'.format(date),index=False)
        sleep_time = 10*3600
        alarm_steps = sleep_time/30
        print 'going to sleep for a while (to be exact for {} hours!)....'.format(sleep_time/3600)
        for t in range(0,sleep_time+1,alarm_steps):
            print 'now time is {}. The crawler will wake up in {} minutes'.format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),(sleep_time-t)/60.)
            time.sleep(alarm_steps)
        
 
     
   
        
        
    
        