#!/usr/bin/env python3

import requests
import json

# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       

query = """
{
  viewer {
    login	# details about the user
    company
    bio
    email
    repository (name:"<REPO NAME>"){	# details about the repository, name should be given beforehand 
      name
      forkCount
      stargazers {
        totalCount
      }
      licenseInfo {
        name
      }
    }  
  }
  rateLimit {	# details of the user api token requests limit
    limit
    cost
    remaining
    resetAt
  }
}
"""

headers = {"Authorization": "Bearer <YOUR ACCESS TOKEN>"}

# Simple function to use requests.post to make the API call. Note the json= section.

def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:          # 200 is successful whereas 404 gives not found error
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

# Execute the query

result = run_query(query) 
#print(result)
print(json.dumps(result, indent=4))

# Drill down the dictionary to get the remaining number of requests for that hour 

remaining_rate_limit = result["data"]["rateLimit"]["remaining"] 
print("\n\nRemaining rate limit - {}".format(remaining_rate_limit))