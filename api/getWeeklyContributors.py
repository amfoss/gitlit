import requests
from dateutil import parser, relativedelta


accessToken = "your_access_token"
headers = {"Authorization": "bearer "+ accessToken }


def getWeeklyContributors(repo, owner):
		query ="""
		{
		  repository(name: """ + '"' + str(repo) + '"' +  """, owner: """ + '"' + str(owner) + '"' +  """)
		  {
			pullRequests(last:100)
			{
				edges
				{
				  node
				  {
					createdAt
					author
					{
					  login
					}
				  }
				  cursor
				}
			}
			issues(last:100)
			{
					edges
				{
				  node
				  {
					createdAt
					author
					{
					  login
					}
				  }
				  cursor
				}
			}
		  }
		}
		"""
		request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

		if request.status_code == 200:
			result = request.json()

			clist = list()
			for contributor in result["data"]["repository"]["pullRequests"]["edges"]:
				created_at = parser.parse(contributor["node"]["createdAt"])
				timezone = created_at.tzinfo
				time_now = datetime.now(timezone)
				weekago = time_now - relativedelta.relativedelta(days=7)

				if(created_at>weekago):
					user = contributor["node"]["author"]["login"]
					if(user not in clist):
						clist.append(user)

			for contributor in result["data"]["repository"]["issues"]["edges"]:
				created_at = parser.parse(contributor["node"]["createdAt"])
				timezone = created_at.tzinfo
				time_now = datetime.now(timezone)
				weekago = time_now - relativedelta.relativedelta(days=7)

				if(created_at>weekago):
					user = contributor["node"]["author"]["login"]
					if(user not in clist):
						clist.append(user)



getWeeklyContributors("fosswebsite", "amfoss")
