import requests
import json
import urllib
import sys
import shlex
import subprocess
import os

repos = []
AuthToken = "7e9bcbb256d146a76bcac3dc6542ab4e571166f2"

def getUrlConfig(page):
	prefix = "https://" + AuthToken + ":x-oauth-basic@" + "api.github.com/search/repositories"
	query = "q=stars:>=1000"
	sort = "sort=stars"
	order = "order=desc"
	url = prefix + '?' + query + '&' + sort + '&' + order + '&page=' + str(page)
	return url

def getIssueUrl(orgs, org , page):
	prefix = "https://" + AuthToken + ":x-oauth-basic@" +  "api.github.com/repos/"
	url = prefix + orgs + "/" + org + "/issues" + "?&page=" + str(page)
	return url
	
def processData(rawData):
	allData = json.load(rawData)
	items = allData["items"]
#	repos = []
	for item in items:
		repos.append(item["html_url"])
	print len(repos)
	return

def writeToFile():
	print "writing repository names to file..."
	f = open("repositories.txt","w")
	for item in repos:
		f.write(item + "\n")
	f.close()

def collectAllInfo():
	for page in range(1,10):
		url = getUrlConfig(page)
		print url
		print "retrieving data on page " + str(page) + "..."
		req = urllib.urlopen(url)
		processData(req)
	writeToFile()

def readFromFile():
	f = open("repositories.txt","r")
	for line in f:
		repos.append(line)
	f.close()
	
def collectSingleRepo():
	readFromFile()
	print len(repos)
	for repo in repos:
		cmd = "git clone " + repo
		cmdList = shlex.split(cmd)
		print cmdList
		subprocess.call(cmdList)
		
		tmp = repo[:-1].split('/')
		orgs = tmp[3]
		org = tmp[4]
		if not os.path.exists(org + "/issues"):
			os.mkdir(org + "/issues")
		page = 1
		
		while True:
			url = getIssueUrl(orgs, org , page)
			print url
			req = urllib.urlopen(url)
			issues = json.load(req)
			print str(page) + ":" + str(len(issues))
			if (len(issues) == 0): 
				break
			page += 1
			for issue in issues:
				id = issue["number"]
				commentsNum = issue["comments"]
				all = [issue]
				if (commentsNum > 0):
					req = urllib.urlopen(issue["comments_url"])
					comments = json.load(req)
					for comment in comments:
						all.append(comment)
				f = open(org + "/issues/" + str(id) + ".txt", "w")
				json.dump(all,f)		
			
	
def main(argv):
	option = argv[0]
	if option in ("all","single"):
		if option == "all":
			collectAllInfo()
		else:
			collectSingleRepo()
	else: 
		print "Argument Error!"
		print "Please use 'all' to collect all the information or 'single' to collect a single repositories"
		return 

	
if __name__ == '__main__':
	main(sys.argv[1:])
