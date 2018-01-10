'''
车次 出发站 到达站 出发时间 到达时间 历时	商务座 一等座	二等座	高级软卧 软卧	动卧 硬卧 软座 硬座 无座
G14 上海虹桥 北京南 10:00 14:28    04:28 无      无     无    --	   --	--	--	 --	  --   --	
'''
a="|预订|5l00000G1441|G14|AOH|VNP|AOH|VNP|10:00|14:28|04:28|N|usY%2BUl57hWKitIUp1d4m3n3e0ys4iJTdDfedKU6oXk7F3bAb|20180110|3|H6|01|04|1|0|||||||||||无|无|无||O0M090|OM9|0"
b=a.split('|')
# print(b)
# for index,value in enumerate(b):
#     print(index,'===>',value)
c=[]
info=c.extend(b[3:6])
info=c.extend(b[8:11])
info=c.extend(b[32:22:-1])
print(c)