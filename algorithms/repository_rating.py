"""

    annualActivityScoreSITORY RATING ALGORITHM

"""
import json
from datetime import timedelta, datetime
from dateutil import parser, relativedelta
from script import userTopicResult


import requests

class RepositoryMetrics:

    def __init__(self, name, owner, token):
        # initialize class variables
        self.name = str(name)
        self.owner = str(owner)
        self.reponame = self.name + '-' + self.owner

        # User Profile Details
        self.fullName = ''
        self.userID = ''  # used getting avatar

        self.topicsList = list()

        # Repo Statistics
        self.commitCount = 0
        self.prCount = 0
        self.prMergedCount = 0
        self.issueCount = 0
        self.branchCount = 0
        self.maintainersCount = 0

        self.weeklyContributorsCount = 0
        self.weeklyContributorsChange = 0
        self.firstTimeContributorsThisWeek = 0

        self.weeklyContributorNames = list()
        self.totalContributors = list()

        # Initializing User Points
        self.basePoints = 0
        self.activityPoints = 0
        self.popularityPoints = 0
        self.inclusivityPoints = 0
        self.meritPoints = 0
        self.repoPoints = 0

        # run class functions
        self.fetchBasicDetails()
        self.calcActivityScore()
        self.calcInclusivityScore()
        self.calcMeritScore()

        # calculate final score
        self.calcRepoScore()

    def fetchBasicDetails(self):
        query ="""
        {
          repository(name: """ + '"' + str(self.name) + '"' +  """, owner: """ + '"' + str(self.owner) + '"' +  """)
          {
            stargazers {
              totalCount
            }
            watchers {
              totalCount
            }
            forkCount

             pullRequests
                {
                    totalCount
                }

                issues
                {
                    totalCount
                }
          }
        }
        """

        request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

        if request.status_code == 200:
            result              = request.json()
            if(result is not None):
                stargazers          = result["data"]["repository"]["stargazers"]["totalCount"]
            else:
                stargazers = 0
            watchers            = result["data"]["repository"]["watchers"]["totalCount"]
            forkCount           = result["data"]["repository"]["forkCount"]
            self.prCount        = result["data"]["repository"]["pullRequests"]["totalCount"]
            issueCount          = result["data"]["repository"]["issues"]["totalCount"]

            self.basePoints = round(0.3 * watchers + 0.2 * stargazers + 0.15 * forkCount +0.5*self.prCount + 0.4*issueCount, 4) #phase 1 done






    def calcActivityScore(self):
        query = """
        {
            repository(name: """ + '"' + str(self.name) + '"' +  """, owner: """ + '"' +  str(self.owner) + '"' + """)
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
            total = timedelta(microseconds=1)
            count = 0

            if(result["data"]["repository"]["issues"]["edges"] is not None):

                for issue in result["data"]["repository"]["issues"]["edges"]:
                    count = count +1
                    created = parser.parse(issue["node"]["createdAt"])
                    closed = parser.parse(issue["node"]["closedAt"])
                    total = total + closed-created

            if(count>0):
                avgIssueResolutionTime = total/count
            else:
                avgIssueResolutionTime = -1

        else:
            avgIssueResolutionTime = -1




        query ="""
        {
          repository(name: """ + '"' + str(self.name) + '"' +  """, owner: """ + '"' + str(self.owner) + '"' +  """)
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

            # Add New Users
            for user in clist:
                if(user not in self.weeklyContributorNames):
                    self.weeklyContributorNames.append(user)

                if(user not in self.totalContributors):
                    self.totalContributors.append(user)

            # Remove Old Users
            for user in self.weeklyContributorNames:
                if(user not in clist):
                    self.weeklyContributorNames.remove(user)

            self.weeklyContributorsChange = len(clist) - self.weeklyContributorsCount
            self.weeklyContributorsCount = len(clist)  

            # -- ok

            numberOfDays = int(str(avgIssueResolutionTime)[0:2])
            if (numberOfDays) <= 20:
                avgIssueResolutionScore = 20
            elif (numberOfDays) <= 50:
                avgIssueResolutionScore = 10
            else:
                avgIssueResolutionScore = 5


            self.activityPoints = 8*avgIssueResolutionScore + 5*self.weeklyContributorsCount + 8*self.weeklyContributorsChange



    def calcInclusivityScore(self):
        merged_prs_query = """
        {
            repository(name: """ + '"' + str(self.name) + '"' +  """, owner: """ + '"' + str(self.owner) + '"' +  """)
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
            repository(name: """ + '"' + str(self.name) + '"' +  """, owner: """ + '"' + str(self.owner) + '"' +  """)
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
            PRmergedData    = mergedPR.json()
            PRtotalData     = totalPR.json()
            self.prMergedCount         = PRmergedData["data"]["repository"]["pullRequests"]["totalCount"]
            self.totalprCount   = PRtotalData["data"]["repository"]["pullRequests"]["totalCount"]

            if(self.totalprCount>0):
                PRacceptanceRatio = round( self.prMergedCount/self.totalprCount, 2)
            else:
                PRacceptanceRatio = -1

        else:
            PRacceptanceRatio = -1


        # new contributors below

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
                        rep_name    = prs["repository"]["nameWithOwner"]
                        created_at  = parser.parse(prs["createdAt"])
                        timezone    = created_at.tzinfo
                        time_now    = datetime.now(timezone)
                        weekago     = time_now - relativedelta.relativedelta(days=7)
                        if(created_at<weekago and rep_name == str(self.owner) + '/' + str(self.name)):
                            flag = 1

                    if(flag==0):
                        self.firstTimeContributorsThisWeek = self.firstTimeContributorsThisWeek + 1


        request = requests.get('https://api.github.com/repos/' + str(self.owner) + '/' + str(self.name) + '/contributors?page=1&per_page=100&access_token='+accessToken)

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
                request = requests.get('https://api.github.com/repos/' + str(self.owner) + '/' + str(self.name) + '/contributors?page='+ str(i) +'&per_page=100&access_token='+accessToken)

                if request.status_code == 200:

                    result = request.json()
                    c = 0
                    for user in result:
                        c = c + 1
                        self.totalContributors.append(user["login"])

                if(c<100):
                    flag=0

        self.inclusivityPoints = 0.8*PRacceptanceRatio + 0.4*self.firstTimeContributorsThisWeek



    def calcMeritScore(self):

    
        # repo complexity 

        query = """
        {
          repository(name: """ + '"' + str(self.name) + '"' +  """, owner: """ + '"' + str(self.owner) + '"' +  """) {
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
        
            to_delete = set()
            fileTopicList = open("topics.txt", "r").read().split('\n')
            for topic in clist:
                if topic not in fileTopicList:
                    to_delete.add(topic)
            clist = list(set(clist)-to_delete)

        request = requests.get("https://api.github.com/repos/"+str(self.owner) + '/' + str(self.name) + "/contributors?page=1&per_page=5&access_token="+accessToken)
        if request.status_code == 200:
            result = request.json()
            usernameList = list()
            for user in result:
                usernameList.append(user["login"])

            self.repoComplexity = 0
            for user in usernameList:
                uTR = userTopicResult(user, clist)
                self.repoComplexity = self.repoComplexity + uTR.userTopicSkill


        self.meritPoints = self.repoComplexity

    def calcRepoScore(self):
        self.repoPoints = self.basePoints + self.activityPoints + self.inclusivityPoints + self.meritPoints


    
accessToken = "<token-here>"
headers = {"Authorization": "bearer "+ accessToken }

username = input("Enter the owner name: ")
reponame = input("Enter the repository name: ")
r=RepositoryMetrics(str(reponame), str(username), accessToken)

print()
print("The Base Points: " + str(r.basePoints))
print("The Activity Points: " + str(r.activityPoints))
print("The Inclusivity Points: " + str(r.inclusivityPoints))
print("The Merit Points: " + str(r.meritPoints))
print()
print("The Repository Score is " + str(r.repoPoints))