"""

    USER RATING ALGORITHM

"""

# importing libraries
import requests


class UserMetrics:

    def __init__(self, username,token):
        #initialize class variables
        self.username = str(username)
        self.token = str(token)

        #User Profile Details
        self.fullName = ''
        self.userID = '' #used getting avatar

        #User Statistics
        self.repoOwnCount = 0
        self.followersCount = 0
        self.followingCount = 0
        self.prCount = 0
        self.issueCount = 0
        self.repoContributionCount = 0

        #Initializing User Points
        self.basePoints = 0
        self.creationPoints = 0
        self.contributionPoints = 0
        self.activityPoints = 0
        self.communityPoints = 0

        #run class functions
        self.fetchBasicDetails()
        #self.calcBaseScore()
        #self.calcCreationScore()
        #self.calcContributionScore()
        #self.calcActivityScore()
        #self.calcCommunityScore()

        #calculate final score
        #self.calcUserScore()

    def fetchBasicDetails(self):
        query = """
        {
            user(login:""" + '"' + self.username + '"' + """)
            {
                name
                databaseId
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
        header = {"Authorization": "bearer " + self.token}
        request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=header)
        if request.status_code == 200:
            result = request.json()
            self.fullName =  result["data"]["user"]["name"]
            self.userID =  result["data"]["user"]["databaseId"]

            self.followersCount = result["data"]["user"]["followers"]["totalCount"]
            self.followingCount = result["data"]["user"]["following"]["totalCount"]
            self.prCount = result["data"]["user"]["pullRequests"]["totalCount"]
            self.issueCount = result["data"]["user"]["issues"]["totalCount"]
            self.repoOwnCount = result["data"]["user"]["repositories"]["totalCount"]
            self.repoContributionCount = result["data"]["user"]["repositoriesContributedTo"]["totalCount"]


username = str(input("Enter Username: "))
token = str(input("Enter Token: "))

user = UserMetrics(username, token)

print("PROFILE ANALYSIS")
print("Username: " + str(user.username))
print("Full Name: " + str(user.fullName))
print("\n \nSTATISTICS")
print("Full Name: " + str(user.followersCount))
print("PR Count: " + str(user.prCount))
print("Issue Count:" + str(user.issueCount))
print("Repos Owned Count:" + str(user.repoOwnCount))
print("Repos Contributed Count:" + str(user.repoContributionCount))
