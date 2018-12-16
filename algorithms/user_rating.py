"""

    USER RATING ALGORITHM

"""

# importing libraries
import requests
import collections
from datetime import datetime
from dateutil import parser, relativedelta
import os
module_dir = os.path.dirname(__file__)  # get current directory

def runquery(token, query):
    header = {"Authorization": "bearer " + token}
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=header)
    if request.status_code == 200:
        return request.json()
    else:
        return 0


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
        self.userPoints = 0

        #run class functions
        self.fetchBasicDetails()
        self.calcCreationScore()
        self.calcContributionScore()
        self.calcActivityScore()

        #calculate final score
        self.calcUserScore()
        self.getTopicList()
        self.setSkillPoints()

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
        response = runquery(self.token,query)
        if response:
            self.fullName = response["data"]["user"]["name"]
            self.userID = response["data"]["user"]["databaseId"]

            self.followersCount = response["data"]["user"]["followers"]["totalCount"]
            self.followingCount = response["data"]["user"]["following"]["totalCount"]
            self.prCount = response["data"]["user"]["pullRequests"]["totalCount"]
            self.issueCount = response["data"]["user"]["issues"]["totalCount"]
            self.organizationCount = response["data"]["user"]["organizations"]["totalCount"]
            self.repoOwnCount = response["data"]["user"]["repositories"]["totalCount"]
            self.repoContributionCount = response["data"]["user"]["repositoriesContributedTo"]["totalCount"]

            self.yCommitsCount = response["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
            self.yPRCount = response["data"]["user"]["contributionsCollection"]["totalPullRequestContributions"]
            self.yReposCount = response["data"]["user"]["contributionsCollection"]["totalRepositoryContributions"]
            self.yIssueCount = response["data"]["user"]["contributionsCollection"]["totalIssueContributions"]
            self.yReviewCount = response["data"]["user"]["contributionsCollection"]["totalPullRequestReviewContributions"]

            self.basePoints = round(0.3 * self.yCommitsCount + 0.3 * self.yPRCount + 0.3 * self.yReposCount + 0.2 * self.yIssueCount + 0.2 * self.yReviewCount, 2)
            self.communityPoints = round(self.organizationCount + 0.2 * self.followersCount + 0.1 * self.followingCount, 2)

    def calcCreationScore(self):
        query = """
        {
            user(login:""" + '"' + self.username + '"' + """)
            {
              repositories(isFork:false,last:100)
              {
                edges
                {
                  node
                  {
                    stargazers
                    {
                      totalCount
                    }
                  }
                }
              }
            }
        }       
        """
        response = runquery(self.token,query)
        if response:
            repoStarsCount = 0
            if response["data"]["user"]["repositories"]["edges"]:
                for repo in response["data"]["user"]["repositories"]["edges"]:
                    repoStarsCount = repoStarsCount + repo["node"]["stargazers"]["totalCount"]
                if repoStarsCount>0:
                    self.creationPoints =  (10 * repoStarsCount/self.repoOwnCount) 
                else:
                    self.creationPoints = 0.5 * self.repoOwnCount
            else:
                self.creationPoints = self.repoOwnCount

    def calcActivityScore(self):
        pr_query = """
        {
          user(login:""" + '"' + self.username + '"' + """)
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
        response = runquery(self.token, pr_query)
        if response:
            count = 0
            if (response["data"]["user"]["pullRequests"]["edges"]):
                for pr in response["data"]["user"]["pullRequests"]["edges"]:
                    created = parser.parse(pr["node"]["createdAt"])
                    timezone = created.tzinfo
                    time_now = datetime.now(timezone)
                    yearago = time_now - relativedelta.relativedelta(year=1)

                    if (created > yearago):
                        count = count + 1

            annualPRmergedCount = count

        issue_query = """
              {
                user(login:""" + '"' + self.username + '"' + """)
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
        response = runquery(self.token, issue_query)
        if response:
            count = 0
            if (response["data"]["user"]["issues"]["edges"]):
                for pr in response["data"]["user"]["issues"]["edges"]:
                    created = parser.parse(pr["node"]["createdAt"])
                    timezone = created.tzinfo
                    time_now = datetime.now(timezone)
                    yearago = time_now - relativedelta.relativedelta(year=1)

                    if (created > yearago):
                        count = count + 1

            annualIssuesRaised = count

        self.activityPoints = 3 * annualPRmergedCount + 2 * annualIssuesRaised

    def calcContributionScore(self):
        query = """
        {
           user(login:""" + '"' + self.username + '"' + """)
          {
            pullRequests(states:MERGED)
            {
                totalCount
            }
            issues(states:CLOSED)
            {
                totalCount
            }
          }
        }
        """
        response = runquery(self.token, query)
        if response:
            self.PRmergedCount = response["data"]["user"]["pullRequests"]["totalCount"]
            self.IssuesMergedCount = response["data"]["user"]["pullRequests"]["totalCount"]

        if self.prCount > 0:
            PRscore = ((self.PRmergedCount) ** 2) / self.prCount
        else:
            PRscore = 0

        if self.issueCount > 0:
            IssueScore = ((self.IssuesMergedCount) ** 2) / self.issueCount
        else:
            IssueScore = 0

        self.contributionPoints = round(0.3 * PRscore + 0.2 * IssueScore,2)

    def calcUserScore(self):
        self.userPoints = round(0.5 * self.basePoints + 2 * self.creationPoints + self.activityPoints + 2 * self.contributionPoints,2)

    def getTopicList(self):
        selfTopicList = list()  # topics of the user repos
        contributedTopicList = list()  # topics of the user contributed repos
        starredTopicList = list()  # topics which the user has starred

        topicOccurenceSelf = dict()
        topicOccurenceContributed = dict()
        topicOccurenceStarred = dict()

        self.topicInterestDict = dict()  # final dict!!

        topic_query = """
        {
            user(login:""" + '"' + self.username + '"' + """)
           {
            starredRepositories(last: 100) {
                  nodes {
                    repositoryTopics(first: 100) {
                      nodes {
                        topic {
                          name
                        }
                      }
                    }
                  }
                }
                repositories(last: 100) {
                  nodes {
                    languages(first: 3)
                    {
                      nodes
                      {
                        name
                      }
                    }
                    repositoryTopics(first: 100) {
                      nodes {
                        topic {
                          name
                        }
                      }
                    }
                  }
                }
                repositoriesContributedTo(last: 100) {
                  nodes {
                    languages(first: 3)
                    {
                        nodes
                        {
                            name
                        }
                    }
                    repositoryTopics(first: 100) {
                      nodes {
                        topic {
                          name
                        }
                      }
                    }
                  }
                }
             }
        }
        """

        result = runquery(self.token, topic_query)
        if result:
            for i in result["data"]["user"]["starredRepositories"]["nodes"]:
                for j in i["repositoryTopics"]["nodes"]:
                    starredTopicList.append(j["topic"]["name"])

            for i in result["data"]["user"]["repositories"]["nodes"]:
                for j in i["repositoryTopics"]["nodes"]:
                    selfTopicList.append(j["topic"]["name"])

            for i in result["data"]["user"]["repositoriesContributedTo"]["nodes"]:
                for j in i["repositoryTopics"]["nodes"]:
                    contributedTopicList.append(j["topic"]["name"])


        fileTopicList = open(os.path.join(module_dir, 'topics.txt'), "r").read().split('\n')

        topicOccurenceSelf = dict(collections.Counter(x for x in selfTopicList if x))
        topicOccurenceContributed = dict(collections.Counter(x for x in contributedTopicList if x))
        topicOccurenceStarred = dict(collections.Counter(x for x in starredTopicList if x))

        self.topicSkill = topicOccurenceSelf  # we are using this to calculate skill points down there

        # topicOccurenceSelf 4
        # topicOccurenceContributed 3
        # topicOccurenceStarred 1

        def removeIrrelevant(topicDict):
            to_delete = set(topicDict.keys()).difference(fileTopicList)  # removing A-B from A
            for d in to_delete:
                del topicDict[d]

        removeIrrelevant(topicOccurenceSelf)
        removeIrrelevant(topicOccurenceContributed)
        removeIrrelevant(topicOccurenceStarred)

        def updateValue(topicDict):
            for topic in topicDict.keys():
                if topic not in self.topicInterestDict.keys():
                    value = 0
                    if topic in topicOccurenceSelf.keys():
                        value = value + 4 * topicOccurenceSelf[topic]
                    if topic in topicOccurenceContributed.keys():
                        value = value + 3 * topicOccurenceContributed[topic]
                    if topic in topicOccurenceStarred.keys():
                        value = value + 1 * topicOccurenceStarred[topic]
                    self.topicInterestDict[topic] = value

        updateValue(topicOccurenceSelf)
        updateValue(topicOccurenceContributed)
        updateValue(topicOccurenceStarred)

        self.topicInterestDict = dict(sorted(self.topicInterestDict.items(), key=lambda x: x[1], reverse=True))

    def setSkillPoints(self):
        self.topicSkillDict = dict()

        prm_query = """
        {
            user(login:""" + '"' + self.username + '"' + """)
            {
              pullRequests(last: 100, states: MERGED) {
                  nodes {
                    repository {
                      repositoryTopics(first: 100) {
                        nodes {
                          topic {		
                            name
                          }
                        }
                      }
                    }
                  }
                }
                issues(last: 100, states: CLOSED) {
                  nodes {
                    repository {
                      repositoryTopics(first: 100) {
                        nodes {
                          topic {		
                            name
                          }
                        }
                      }
                    }
                  }
                }
             }
        }
        """

        PRtopicList = list()
        PRtopicDict = dict()

        issueTopicList = list()
        issueTopicDict = dict()

        result = runquery(self.token, prm_query)
        if result:

            for i in result["data"]["user"]["pullRequests"]["nodes"]:
                for j in i["repository"]["repositoryTopics"]["nodes"]:
                    PRtopicList.append(j["topic"]["name"])

            for i in result["data"]["user"]["issues"]["nodes"]:
                for j in i["repository"]["repositoryTopics"]["nodes"]:
                    issueTopicList.append(j["topic"]["name"])

            PRtopicDict = dict(collections.Counter(x for x in PRtopicList if x))
            issueTopicDict = dict(collections.Counter(x for x in issueTopicList if x))

        def updateSkillsetValue(topicDict):
            for topic in topicDict.keys():
                if topic not in self.topicSkillDict.keys() and topic in self.topicInterestDict.keys():
                    value = 0
                    if topic in PRtopicDict.keys():
                        value = value + PRtopicDict[topic]
                    if topic in issueTopicDict.keys():
                        value = value + issueTopicDict[topic]
                    if topic in self.topicSkill.keys():
                        value = value + 0.5 * self.topicSkill[topic]
                    self.topicSkillDict[topic] = value

        updateSkillsetValue(PRtopicDict)
        updateSkillsetValue(issueTopicDict)
        updateSkillsetValue(self.topicSkill)
        self.topicSkill = dict(sorted(self.topicSkill.items(), key=lambda x: x[1], reverse=True))
