
import requests

accessToken = "your_access_token"
headers = {"Authorization": "bearer "+ accessToken }



def getNewContributors(self):
		for user in self.weeklyContributorNames:
			query = """
				{
				  user(login:""" + user +"""){

					pullRequests(first:100)
					{
						nodes
						{
						  createdAt
						  repository {
							nameWithOwner
						  }
					  }
					}
				  }
				}
			"""
			request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

			if request.status_code == 200:
				flag = 0
				result = request.json()
				if(result["data"]):
					for prs in result["data"]["user"]["pullRequests"]["nodes"]:
						rep_name 	= prs["repository"]["nameWithOwner"]
						created_at 	= parser.parse(prs["createdAt"])
						timezone 	= created_at.tzinfo
						time_now 	= datetime.now(timezone)
						weekago 	= time_now - relativedelta.relativedelta(days=7)
						if(created_at<weekago and rep_name == str(self.owner) + '/' + str(self.repo)):
							flag = 1

					if(flag==0):
						self.newContributors = self.newContributors + 1


		request = requests.get('https://api.github.com/repos/' + str(self.owner) + '/' + str(self.repo) + '/contributors?page=1&per_page=100&access_token='+accessToken)

		if request.status_code == 200:
			result = request.json()
			c = 0

			for user in result:
				c = c +1
				self.totalContributors.append(user["login"])

			if(c<100):
				flag = 0

			else:
				flag = 1
				i = 1

			while(flag!=0):
				i = i+1
				request = requests.get('https://api.github.com/repos/' + str(self.owner) + '/' + str(self.repo) + '/contributors?page='+ str(i) +'&per_page=100&access_token='+accessToken)

				if request.status_code == 200:

					result = request.json()
					c = 0
					for user in result:
						c = c + 1
						self.totalContributors.append(user["login"])

				if(c<100):
					flag=0