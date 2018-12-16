import requests

headers = {"Authorization": "Bearer <TOKEN>"}

def getBaseRating(username):
	query = """
	{
		user(login:""" + '"' + username + '"' + """)
		{
			repositories(isFork:false)
			{
			  totalCount
			}
			followers
			{
			  totalCount
			}
			following
			{
			  totalCount
			}
			repositoriesContributedTo
			{
			  totalCount
			}
			organizations
			{
			  totalCount
			}
			pullRequests
			{
			  totalCount
			}
			issues
			{
			  totalCount
			}
			contributionsCollection
			{
			  totalCommitContributions
			  totalPullRequestContributions
			  totalRepositoryContributions
			  totalIssueContributions
			  totalPullRequestReviewContributions
			}
		  }

	}
	"""
	request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
	if request.status_code == 200:
		result = request.json()

		print(result)

		PRcount 		= result["data"]["user"]["pullRequests"]["totalCount"]
		repoTotalCount = result["data"]["user"]["repositories"]["totalCount"]
		issueCount 	= result["data"]["user"]["issues"]["totalCount"]
		organizationsCount 	= result["data"]["user"]["organizations"]["totalCount"]
		followersCount		= result["data"]["user"]["followers"]["totalCount"]
		followingCount 		= result["data"]["user"]["following"]["totalCount"]

		# ContributorCollection data is contributions over last year
		
		commits = result["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
		prs = result["data"]["user"]["contributionsCollection"]["totalPullRequestContributions"]
		reps = result["data"]["user"]["contributionsCollection"]["totalRepositoryContributions"]
		issue = result["data"]["user"]["contributionsCollection"]["totalIssueContributions"]
		review = result["data"]["user"]["contributionsCollection"]["totalPullRequestReviewContributions"]

username = input("Enter username: ")
getBaseRating(username)
