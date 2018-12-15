import requests
from dateutil import parser, relativedelta
from datetime import timedelta, datetime
import json

headers = {"Authorization": "Bearer <TOKEN>"}

def getAnnualActivityScore(username):
	count = 0
	pr_query = """
	{
	  user(login:""" + '"' + username + '"' + """)
	  {
		  pullRequests(last:100,states:MERGED)
		  {
			edges{
			  node
			  {
				createdAt
			  }
			}
		  }

	  }
	}
	"""
	request = requests.post('https://api.github.com/graphql', json={'query': pr_query}, headers=headers)
	if request.status_code == 200:
		result = request.json()
		print(result)
		count = 0
		if(result["data"]["user"]["pullRequests"]["edges"]):
			for pr in result["data"]["user"]["pullRequests"]["edges"]:
				created = parser.parse(pr["node"]["createdAt"])
				timezone = created.tzinfo
				time_now = datetime.now(timezone)
				yearago = time_now - relativedelta.relativedelta(year=1)

				if(created>yearago):
					count = count+1

	annualPRmergedCount = count

	issue_query = """
	{
	  user(login:""" + '"' + username + '"' + """)
	  {
		  issues(last:100,states:CLOSED)
		  {
			edges{
			  node
			  {
				createdAt
			  }
			}
		  }

	  }
	}
	"""
	request = requests.post('https://api.github.com/graphql', json={'query': issue_query}, headers=headers)
	if request.status_code == 200:
		result = request.json()
		print(result)
		count = 0
		if(result["data"]["user"]["issues"]["edges"]):
			for pr in result["data"]["user"]["issues"]["edges"]:
				created = parser.parse(pr["node"]["createdAt"])
				timezone = created.tzinfo
				time_now = datetime.now(timezone)
				yearago = time_now - relativedelta.relativedelta(year=1)

				if(created>yearago):
					count = count+1

	annualIssuesRaised = count
	annualActivityScore = 3 *  annualPRmergedCount + 2 * annualIssuesRaised

username = input("Enter username: ")
getAnnualActivityScore(username)

