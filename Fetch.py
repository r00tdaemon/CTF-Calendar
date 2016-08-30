import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def dateTimeFormat(dateTime):
    pass
    dateTime=dateTime[:4]+'-'+dateTime[4:6]+'-'+dateTime[6:8]+dateTime[8:11]+':'+dateTime[11:13]+':'+dateTime[13:]
    return (dateTime)
def fetch():
    url='https://ctftime.org/event/list/upcoming/rss/'
    resp=urllib.request.urlopen(url)
    soup=BeautifulSoup(resp.read(),'html.parser')
    events=[]
    event={}
    for value in soup.find_all(['title','url','start_date','finish_date'])[1:]:

        if (value.name=='title'):
            event['summary']=value.string
        elif(value.name=='start_date'):
            event['start']={'dateTime':dateTimeFormat(value.string),'timeZone': 'Asia/Kolkata'}
        elif(value.name=='finish_date'):
            event['end']={'dateTime':dateTimeFormat(value.string),'timeZone': 'Asia/Kolkata'}
        elif(value.name=='url'):
            event['location']=value.string
        if set(event.keys())== {'location', 'end', 'summary', 'start'}:
            events.append(event)
            event={}
    return events

if __name__=='__main__':
    print(fetch())