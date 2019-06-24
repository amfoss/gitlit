import requests
import json
import collections

accessToken = "<access-token>"
headers = {"Authorization": "bearer "+ accessToken }

class userTopicResult:
	def __init__(self, username, userTopics):
		self.username = str(username)
		self.userTopics = list(userTopics)
		self.userTopicSkill = 0
		self.getTopicList()
		self.setSkillPoints()


	def getTopicList(self):
		selfTopicList = list() #topics of the user repos
		contributedTopicList = list() #topics of the user contributed repos
		starredTopicList = list() #topics which the user has starred

		topicOccurenceSelf		= dict() 
		topicOccurenceContributed = dict()
		topicOccurenceStarred = dict()

		self.topicInterestDict = dict() #final dict!!

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

		request = requests.post('https://api.github.com/graphql', json={'query': topic_query}, headers=headers)

		if request.status_code == 200:
			result = request.json()
			if result["data"]["user"]["starredRepositories"]["nodes"]:
				for i in result["data"]["user"]["starredRepositories"]["nodes"]:
					for j in i["repositoryTopics"]["nodes"]:
						starredTopicList.append(j["topic"]["name"])
			if result["data"]["user"]["repositories"]["nodes"]:
				for i in result["data"]["user"]["repositories"]["nodes"]:
					for j in i["repositoryTopics"]["nodes"]:
						selfTopicList.append(j["topic"]["name"])
			if result["data"]["user"]["repositoriesContributedTo"]["nodes"]:
				for i in result["data"]["user"]["repositoriesContributedTo"]["nodes"]:
					for j in i["repositoryTopics"]["nodes"]:
						contributedTopicList.append(j["topic"]["name"])


		fileTopicList = open("topics.txt", "r").read().split('\n')

		topicOccurenceSelf = dict(collections.Counter(x for x in selfTopicList if x))
		topicOccurenceContributed = dict(collections.Counter(x for x in contributedTopicList if x))
		topicOccurenceStarred = dict(collections.Counter(x for x in starredTopicList if x))

		self.skillSelf = topicOccurenceSelf # we are using this to calculate skill points down there
		#topicOccurenceSelf 4
		#topicOccurenceContributed 3
		#topicOccurenceStarred 1

		def removeIrrelevant(topicDict):
			to_delete = set(topicDict.keys()).difference(fileTopicList)  #removing A-B from A
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
						value = value + 4*topicOccurenceSelf[topic]
					if topic in topicOccurenceContributed.keys():
						value = value +3*topicOccurenceContributed[topic]
					if topic in topicOccurenceStarred.keys():
						value = value +1*topicOccurenceStarred[topic]
					self.topicInterestDict[topic]=value

		updateValue(topicOccurenceSelf)
		updateValue(topicOccurenceContributed)
		updateValue(topicOccurenceStarred)

		self.topicInterestDict = dict(sorted(self.topicInterestDict.items(), key=lambda x: x[1], reverse=True))

	def setSkillPoints(self):

		topicSkillDict = dict()

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

		request = requests.post('https://api.github.com/graphql', json={'query': prm_query}, headers=headers)

		PRtopicList = list()
		PRtopicDict = dict()

		issueTopicList = list()
		issueTopicDict = dict()

		topicPRs 	= dict()

		if request.status_code == 200:
			result = request.json()

			for i in result["data"]["user"]["pullRequests"]["nodes"]:
				for j in i["repository"]["repositoryTopics"]["nodes"]:
					PRtopicList.append( j["topic"]["name"])

			for i in result["data"]["user"]["issues"]["nodes"]:
				for j in i["repository"]["repositoryTopics"]["nodes"]:
					issueTopicList.append( j["topic"]["name"])

			PRtopicDict = dict(collections.Counter(x for x in PRtopicList if x))
			issueTopicDict = dict(collections.Counter(x for x in issueTopicList if x))

		def updateSkillsetValue(topicDict):
			for topic in topicDict.keys():
				if topic not in topicSkillDict.keys() and topic in self.topicInterestDict.keys():
					value = 0
					if topic in PRtopicDict.keys():
						value = value + PRtopicDict[topic]
					if topic in issueTopicDict.keys():
						value = value +issueTopicDict[topic]
					if topic in self.skillSelf.keys():
						value = value + 0.5*self.skillSelf[topic]
					topicSkillDict[topic]=value

		updateSkillsetValue(PRtopicDict)
		updateSkillsetValue(issueTopicDict)
		updateSkillsetValue(self.skillSelf)
		for topic in self.userTopics:
			if topic in topicSkillDict.keys():
				self.userTopicSkill = self.userTopicSkill + topicSkillDict[topic]
