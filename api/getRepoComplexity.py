import requests

accessToken = "your_access_token"
headers = {"Authorization": "bearer "+ accessToken }

def getRepoComplexity(repo, owner):
		query = """
		{
		  repository(name: """ + '"' + str(repo) + '"' +  """, owner: """ + '"' + str(owner) + '"' +  """) {
		    repositoryTopics(first: 100) {
		      nodes {
		        topic {
		          name
		        }
		      }
		    }
		  }
		}
		"""
		request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
		if request.status_code == 200:
			result = request.json()
			clist = list()
			for topic in result["data"]["repository"]["repositoryTopics"]["nodes"]:
				clist.append(topic["topic"]["name"])
		
			

		request = requests.get("https://api.github.com/repos/"+str(owner) + '/' + str(repo) + "/contributors?page=1&per_page=5&access_token="+accessToken)
		if request.status_code == 200:
			result = request.json()
			usernameList = list()
			for user in result:
				usernameList.append(user["login"])


getRepoComplexity("fosswebsite", "amfoss")

