#encoding:utf-8

# ***********************
# *** Python 2.x only ***
# ***********************

import urllib2, sys
import sys
import json

def getWeather():
	try: citycode = sys.argv[1]
	except: citycode = '270000' #大阪府　大阪

	resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

	# 読み込んだJSONデータをディクショナリ型に変換
	resp_dict = json.loads(resp)
	print (resp_dict['title'])

	print (u'今日の天気は{}だよ'.format(resp_dict['forecasts'][0]['telop']))

	#for forecast in resp['forecasts']:
	#    print '**************************'
	#    print forecast['dateLabel']+'('+forecast['date']+')'
	#    print forecast['telop']
	#print '**************************'

if __name__ == "__main__" :
	getWeather()
