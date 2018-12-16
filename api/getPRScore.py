import requests

headers = {"Authorization": "Bearer <TOKEN>"}

def getPRscore(username):
	merged_prs = """
	{
	   user(login:""" + '"' + username + '"' + """)
	  {
		pullRequests(states:MERGED)
		{
			totalCount
		}
	  }
	}
	"""
	merged = requests.post('https://api.github.com/graphql', json={'query': merged_prs}, headers=headers)
	if merged.status_code == 200:
		result = merged.json()
		print(result)
		PRmergedCount = result["data"]["user"]["pullRequests"]["totalCount"]

username = input("Enter username: ")
getPRscore(username)
