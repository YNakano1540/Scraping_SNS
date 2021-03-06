import requests
from pyquery import PyQuery as pq
import re

#イラスト関連SNSのフォロワーとかのデータを抽出します。

class scraping_SNS:
    #YouTubeから再生回数取得
    def youtube(self, url):
        
        response = requests.get(url)
        py_response = []
        py_response.append(pq(response.text))
        
        """
        フォロワー数,再生回数の取得
        """
        follower_text = ""
        play_text = ""
        
        for py_response in py_response:
            response_list = re.split('"',str(py_response))
            follower_text = [s for s in response_list if "subscriberCountText" in s]
            
            play_text = [s for s in response_list if "回視聴" in s]

            follower_text = re.sub("\\D", "", str(follower_text))
            play_text = re.sub("\\D", "", str(play_text))
        
        return play_text
    
    #Instagramのフォロワー取得
    def Instagram(self, url):

        response = requests.get(url)
        py_response = []
        py_response.append(pq(response.text))


        """
        フォロワー数の取得
        """
        follower_text = ""

        for py_response in py_response:
            response_list = re.split('"',str(py_response))
            follower_list = re.split(",",str([s for s in response_list if "Followers" in s]))
            follower_text = re.sub("\\D", "", str(follower_list[0]))

        return follower_text

    #deviantartのフォロワー取得
    def deviant(self, url):
        
        response = requests.get(url)
        py_response = []
        py_response.append(pq(response.text))
        
        
        """
        フォロワー数の取得
        """
        follower_text = ""
        
        for py_response in py_response:
            response_list = re.split(",",str(py_response))
            
            #print(response_list)
            
            follower_text = [s for s in response_list if 'watchers' in s]
            view_text = [s for s in response_list if 'pageviews' in s]
            
            follower_text = re.sub("\\D", "", str(follower_text[-3]))
            view_text = re.sub("\\D", "", str(view_text[-1]))
            
        return follower_text,view_text

    #Artstationのフォロワー取得
    def artstation(self, url):
        
        response = requests.get(url)
        py_response = []
        py_response.append(pq(response.text))
        
        
        """
        フォロワー数の取得
        """
        follower_text = ""
        
        for py_response in py_response:
            response_list = re.split(",",str(py_response))

            follower_text = [s for s in response_list if 'followers_count' in s]
            follower_text = re.sub("\\D", "", str(follower_text))
        
        return follower_text

    def twitter(self, url):
        
        response = requests.get(url)
        py_response = []
        py_response.append(pq(response.text))
        
        
        """
        フォロワー数の取得
        """
        follower_list = []
        
        for py_response in py_response:
            follower = py_response("p[style='padding-top:6px; color:#0066CC; font-weight: bold; line-height:1.3']").text()
            follower_list = re.split("\xa0\xa0",str(follower))
        
        follower_text = re.sub("\\D", "", str(follower_list[1]))

        return follower_text