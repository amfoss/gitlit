import requests


accessToken = "your_access_token"
headers = {"Authorization": "bearer "+ accessToken }


def getPRacceptance(repo, owner):
		merged_prs_query = """
		{
			repository(name: """ + '"' + str(repo) + '"' +  """, owner: """ + '"' + str(owner) + '"' +  """)
			{
				pullRequests(states: MERGED)
				{
					totalCount
				}

			}
		}
		"""
		total_prs_query = """
		{
			repository(name: """ + '"' + str(repo) + '"' +  """, owner: """ + '"' + str(owner) + '"' +  """)
			{
				pullRequests
				{
					totalCount
				}

			}
		}
		"""
		mergedPR = requests.post('https://api.github.com/graphql', json={'query': merged_prs_query}, headers=headers)
		totalPR  = requests.post('https://api.github.com/graphql', json={'query': total_prs_query}, headers=headers)

		if totalPR.status_code == 200 and mergedPR.status_code ==200:
			PRmergedData 	= mergedPR.json()
			PRtotalData  	= totalPR.json()

			mergedCount 		= PRmergedData["data"]["repository"]["pullRequests"]["totalCount"]
			totalPRcount 	= PRtotalData["data"]["repository"]["pullRequests"]["totalCount"]

			

getPRacceptance("fosswebsite", "amfoss")