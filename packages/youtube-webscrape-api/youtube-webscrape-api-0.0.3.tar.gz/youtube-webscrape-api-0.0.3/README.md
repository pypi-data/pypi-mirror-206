
# Youtube-Scraper

Youtube Scraper is a simple webscraping based replacement to Youtube api v3, to get
youtube results, channel details, and channels videos, **Fast**, this project is for non-commercial use only,
 
this library ships 3 main functions: 
  *  _channels_videos_ 
  * _youtube_results_
  * _channels_about_

## Installation
***
```sh
pip install youtube-webscrape-api==0.0.2
```
## Usage
***
channels_videos()
```python
>>> from yt_scrape import channels_videos   
>>> videos = channels_videos("@TheThinkersOfficial")
>>> for video in videos:
...     print(video)
{'vid_id': '8Q80l3j5x0E', 'thumbnail': 'https://i.ytimg.com/vi/8Q80l3j5x0E/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLApcmw1_uXXAY5wXOmDTCSGQgAH-g', 'title':
 'Dopamine, Oxytocin, Serotonin and Melatonin Explained by Sahil Adeem - @TheThinkersOfficial', 'description_snippet': 'Dopamine, oxytocin, serotonin, and melatonin are important neurotransmitters a
nd hormones that play various roles in the human body. Dopamine is a neurotransmitter that is associated with pleasure...', 'length': '7:30', 'publish_time': '5 hours ago', 'view_count': '786 views'
}
{'vid_id': 'X77PaK-dfFg', 'thumbnail': 'https://i.ytimg.com/vi/X77PaK-dfFg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBfeXwTZfzPYoXijy8kTyC85kSLwQ', 'title':
 'This Video Will Change Your Perception About Imran Khan - Sahil Adeem - New Video 2023', 'description_snippet': 'In this video Sahil Adeem is going to talk about the system of Islam. The system of
 Islam is built around the belief in one God, Allah, and following the teachings of the Quran, the holy book...', 'length': '21:42', 'publish_time': '1 day ago', 'view_count': '8,809 views'}        
...
...
{'vid_id': 'ui4s-5SpgZw', 'thumbnail': 'https://i.ytimg.com/vi/ui4s-5SpgZw/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLChKjCqljy4xUyGwPKLnf8GoAgEUA', 'title':
 'Joint Family System Say B Bara Masla - Explained by SAhil Adeem - @TheThinkersOfficial', 'description_snippet': 'Why the arrogance of of our last generation is so big? How to tackle that arrogance
 and what steps youth should must take to handle and tackle that arrogance? Why our youth in IT industry must...', 'length': '15:22', 'publish_time': '3 weeks ago', 'view_count': '3,772 views'} 
```
***

youtube_results()
```python
>>> results = youtube_results("dota 2")
>>> print(len(results))
20
>>> print(results[:3]) 
[{'vid_id': 'KguZit1F8bk', 'thumbnail': 'https://i.ytimg.com/vi/KguZit1F8bk/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDvQCUEpe_u4QJp2NAIbJA7FZzy9w', 'title': 'O
G vs GAIMIN GLADIATORS - MAJOR CHAMPIONS - DPC WEU SPRING 2023 DOTA 2', 'publish_time': '4 hours ago', 'vid_length': '10:39', 'views': '19,856 views', 'channel_url': '/@NoobFromUA', 'channel_name': 
'NoobFromUA'}, {'vid_id': 'TQjdmrOXquk', 'thumbnail': 'https://i.ytimg.com/vi/TQjdmrOXquk/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLADEOBPzu54sdqwq2Uklm6Kg-UQ0Q
', 'title': 'OLD G vs BETRAYED - QUALIFIER FINAL - DPC WEU SPRING 2023 DOTA 2', 'publish_time': '8 hours ago', 'vid_length': '16:54', 'views': '80,996 views', 'channel_url': '/@NoobFromUA', 'channel
_name': 'NoobFromUA'}, {'vid_id': '', 'thumbnail': '', 'title': '', 'publish_time': '', 'vid_length': '', 'views': '', 'channel_url': '', 'channel_name': ''}]
```
***
channels_about()
```python
>>> from yt_scrape import channels_about
>>> details = channels_about("@RightSpeaking")
>>> print(details) 
{'channel_name': 'Right Speaking', 'views_count': '3,380,715 views', 'channel_thumbnail': 'https://yt3.googleusercontent.com/KGWLOEnAtGewyZllYfZenEDgsJI3j2AQ7fJpIwO9JBB0KamQbA-D0VL6oHKkK0zHKjggTHzkL
w=s200-c-k-c0x00ffffff-no-rj?days_since_epoch=19438', 'channel_url': 'http://www.youtube.com/@RightSpeaking', 'description': "Speak for Right - True Islamic Argument - Sahil Adeem\nLet's bring Islam
ic System into the country.\n", 'banner': 'https://yt3.googleusercontent.com/1a-KQDvr6-JyGjEB0gEJ4edQ1G3CePSIA7T47U-TGmfs-FXu7IMe7Mk1bSqkIg3bVkwpDmNxFA=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff
-no-nd-rj', 'channel_id': 'UC7LdpA6FnHj6wfVwvcHApPw', 'videos_count': '367', 'subscribers': '23K subscribers', 'joined': 'Joined  Dec 4, 2021', 'country': 'Pakistan'}
```
***

## Features
- Get Search Youtube results (max 20)
- get Channels about section data
- get Channels Videos (max 30)

## Fields

data available in each function.
* youtube_results:
   * title
   * publish_time
   * thumbnail_link
   * video_length
   * views
   * vid_id
   * channel_url
   * channel_name


* channels_about: 
   * channel_name
   * views_count
   * channel_thumbnail
   * channel_url
   * description
   * banner
   * channel_id
   * videos_count
   * subscribers
   * joined
   * country


* channels_videos:
   * vid_id
   * thumbnail
   * title
   * description_snippet
   * length
   * view_count
   * publish_time

## Exception
possible exception are:
```python
>>> from yt_scrape.exceptions import TooManyRequests, ChannelDeleted, NoVideoFound
```


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Contributions are always welcome!
