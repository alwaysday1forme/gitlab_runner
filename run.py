import requests
from urllib.parse import urlparse

print('give version to download. example "16.7.1"')
VERSION = ("v" + input())
print(VERSION)

#VERSION = 'v16.7.1'


#url = f"https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/binaries/gitlab-runner-linux-386"



#parsing last part of url for file name
#parsed_url = urlparse(url)
#filename = parsed_url.path.split("/")[-1]
#print(filename)


#pulling url from interwebs and saving file
#r = requests.get(url)
#with open(filename, 'wb') as f:
#	f.write(r.content)

	


#list of url dictionary with links, (name:url)

url = {'Linux_386':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/binaries/gitlab-runner-linux-386',
       'Linux_AMD64':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/binaries/gitlab-runner-linux-amd64',
       'Windows_386':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/binaries/gitlab-runner-windows-386.exe',
       'Windows_AMD64':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}binaries/gitlab-runner-windows-amd64.exe',
       'Debian_386':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/deb/gitlab-runner_i386.deb',
       'Debian_AMD64':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/deb/gitlab-runner_amd64.deb'}

#for k,v in url.items():
#	print(k,v)

for v in url.values():
	parsed_url = urlparse(v)
	filename = parsed_url.path.split("/")[-1]
	print(filename)
	r = requests.get(v)
	with open(filename, 'wb') as f:
		f.write(r.content)
	print(str(url.keys))



#FROM REVISION WITH RICHMOND
import requests
from urllib.parse import urlparse

print('give version to download. example "16.7.1"')
VERSION = ("v" + input())
print(VERSION)


#VERSION = 'v16.7.1'
#url = f"https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/{VERSION}/binaries/gitlab-runner-linux-386"

#parsing last part of url for file name
#parsed_url = urlparse(url)
#filename = parsed_url.path.split("/")[-1]
#print(filename)

#pulling url from interwebs and saving file
#r = requests.get(url)
#with open(filename, 'wb') as f:
#   f.write(r.content)

    
#PUTTING IT ALL TOGETHER BELOW. 

#list of url dictionary with links, (name:url)
url = {'Linux_386':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/'+VERSION+'/binaries/gitlab-runner-linux-386',
       'Linux_AMD64':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/'+VERSION+'/binaries/gitlab-runner-linux-amd64',
       'Windows_386':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/'+VERSION+'/binaries/gitlab-runner-windows-386.exe',
       'Windows_AMD64':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/'+VERSION+'/binaries/gitlab-runner-windows-amd64.exe',
       'Debian_386':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/'+VERSION+'/deb/gitlab-runner_i386.deb',
       'Debian_AMD64':'https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/'+VERSION+'/deb/gitlab-runner_amd64.deb'}


#loop is breaking it. 

for v in url.values():
    parsed_url = urlparse(v)
    filename = parsed_url.path.split("/")[-1]
    print(filename)
    r = requests.get(v)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(str(url.keys))

