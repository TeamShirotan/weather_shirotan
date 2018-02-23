#encoding:utf-8

# ***********************
# *** Python 3.x only ***
# ***********************

import urllib.request
import json

def getWeather():
	citycode = '270000' #大阪府　大阪
	html = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode)

	# 読み込んだJSONデータをディクショナリ型に変換
	resp_dict = json.loads(html.read().decode('utf-8'))

#	print (resp_dict['title'])
#	print (u'今日の天気は{}だよ'.format(resp_dict['forecasts'][0]['telop']))

	#for forecast in resp['forecasts']:
	#    print '**************************'
	#    print forecast['dateLabel']+'('+forecast['date']+')'
	#    print forecast['telop']
	#print '**************************'

	return resp_dict['forecasts'][0]['telop']

if __name__ == "__main__" :
	weather = getWeather()
	print (u'今日の天気は{}だよ'.format(weather))
