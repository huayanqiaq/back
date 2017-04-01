__author__ = 'cike'
import requests
from lxml import etree
import time

def gethtml(url):
	header={
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, sdch, br',
'Accept-Language': 'zh-CN,zh;q=0.8'
}
	m=requests.get(url=url,headers=header).text
	return m

def xpath(xpathcontent):
	xf1=etree.HTML(xpathcontent)
	xf2=xf1.xpath('//a/img/@lazysrc')
	return xf2

def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    r = requests.get(imgUrl, stream=True)
    with open("D:\\images\\"+str(int(time.time()))+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename

if __name__== '__main__':
	for list in range(19800,19906):
		page="https://5imm.me/detail/"+str(list)
		html=gethtml(page)
		xf2=xpath(html)
		for i in xf2:
			time.sleep(1)
			downloadImageFile(i)