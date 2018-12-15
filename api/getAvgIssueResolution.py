import requests
from dateutil import parser, relativedelta


accessToken = "your_access_token"
headers = {"Authorization": "bearer "+ accessToken }

def getAvgIssueResolution(owner, repo):
		query = """
		{
			repository(name: """ + '"' + str(repo) + '"' +  """, owner: """ + '"' +  str(owner) + '"' + """)
			{
				issues(last:100, states: CLOSED)
				{
				  edges{
					node
					{
					  createdAt
					  closedAt
					}

				  }

				}
			  }
		}
		"""
		request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

		if request.status_code == 200:
			result = request.json()
			

			if(result["data"]["repository"]["issues"]["edges"] is not None):

				for issue in result["data"]["repository"]["issues"]["edges"]:
					created = parser.parse(issue["node"]["createdAt"])
					closed = parser.parse(issue["node"]["closedAt"])


getAvgIssueResolution("amfoss","fosswebsite")
			
