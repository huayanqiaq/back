from lxml import etree
import requests
import re
import time

header={
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, sdch, br',
'Accept-Language': 'zh-CN,zh;q=0.8'
}

def gethtml(url):
	content=requests.get(url=url,headers=header,timeout=6)
	if content.status_code == requests.codes.ok:
		return content.text
	else:
		pass

def getxpath(html):
	x_content=etree.HTML(html)
	return x_content

def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    r = requests.get(imgUrl, stream=True,headers=header,timeout=6)
    with open("D:\\images\\"+str(int(time.time()))+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename

repace=re.compile(r'\(1\/(.*?)\)')
#repace1=re.compile(r'script\>var\s+id=\'/(.*?)\'')

if __name__== '__main__':
	for i in range(4818,4819):
		content=gethtml("http://www.jj20.com/bz/nxxz/nxmt/"+str(i)+".html")
		content1=getxpath(content)
		content2=content1.xpath('//h1/span/text()')
		content3=repace.findall(content2[0])
		number = int(content3[0])
		for iii in range(2,number):
			imghtml="http://www.jj20.com/bz/nxxz/nxmt/"+str(i)+"_"+str(iii)+".html"
			#print imghtml
			time.sleep(1)
			imgcontent=gethtml(imghtml)
			imgcontentxpath=getxpath(imgcontent)
			imgurl=imgcontentxpath.xpath('//img[@id="bigImg"]/@src')
			imgurl1="http://sjbz.jj20.com/d/down01.php?p="+imgurl[0].split('com')[1]
			print imgurl1
			#downloadImageFile(imgurl1)
