# GitLit Algorithms


## Rating Algorithms
Each metric defined below has its own specific API query. The process is simple : we fetch the data from GitHub APIs which is already streamlined for a specific metric, cut down the data further (if needed) and then assign appropriate weights to these numbers to form a score of a User or a Repo.

-----------------------------------------------------------------------------------------

### User Rating
A total of 5 metrics have been designed to rate the user and the algorithms are designed according to the process mentioned above.

Each score is a boundless score calculated by summation of weighted sums of each of the following metric.

-----------------------------------------------------------------------------------------

### General traits
1. Contribution Count

*Motive : To get a base idea of a given user*

| Weight |    Formula                        |
| -------|---------------------------------- |
|  3     | Number of Commits                 |
|  3     | Number of PRs                     |
|  2     | Number of Issues                  |
|  2     | Number of User Repos              |
|  3     | Number of Repos contributed to     |

#### Base Score 

<a href="https://www.codecogs.com/eqnedit.php?latex=Base&space;Score&space;=&space;(0.3&space;*&space;Number&space;of&space;Commits)&space;&plus;&space;(0.3&space;*&space;Number&space;of&space;PRs)&space;&plus;&space;(0.2&space;*&space;Number&space;of&space;Issues)&space;&plus;&space;(0.2&space;*&space;Number&space;of&space;User&space;Repos)&space;&plus;&space;(0.3&space;*&space;Number&space;of&space;Repos&space;Contributed&space;To&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Base&space;Score&space;=&space;(0.3&space;*&space;Number&space;of&space;Commits)&space;&plus;&space;(0.3&space;*&space;Number&space;of&space;PRs)&space;&plus;&space;(0.2&space;*&space;Number&space;of&space;Issues)&space;&plus;&space;(0.2&space;*&space;Number&space;of&space;User&space;Repos)&space;&plus;&space;(0.3&space;*&space;Number&space;of&space;Repos&space;Contributed&space;To&space;)" title="Base Score = (0.3 * Number of Commits) + (0.3 * Number of PRs) + (0.2 * Number of Issues) + (0.2 * Number of User Repos) + (0.3 * Number of Repos Contributed To )" /></a>

-----------------------------------------------------------------------------------------

### Creation

1. Stars - Repo Ratio 

*Motive : To get the value of projects created*

| Weight |    Formula                        |
| -------|---------------------------------- |
| 1      |   <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{No.&space;of&space;Stars}{No.&space;of&space;Repos}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{No.&space;of&space;Stars}{No.&space;of&space;Repos}" title="\frac{No. of Stars}{No. of Repos}" /></a> |


#### Creation Score

<a href="https://www.codecogs.com/eqnedit.php?latex=Creation&space;Score&space;=&space;10*\frac{No.of&space;Stars}{No.&space;of&space;Repos}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Creation&space;Score&space;=&space;10*\frac{No.of&space;Stars}{No.&space;of&space;Repos}" title="Creation Score = 10*\frac{No.of Stars}{No. of Repos}" /></a> |

-----------------------------------------------------------------------------------------

### Contribution
1. PR Acceptance Ratio:

*Motive :  Value of Contribution*

| Weight |    Formula                        |
| -------|---------------------------------- |
| 3     | <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{(No.&space;of&space;Merged&space;PRs)^{2}}{Total&space;Number&space;of&space;PRs}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{(No.&space;of&space;Merged&space;PRs)^{2}}{Total&space;Number&space;of&space;PRs}" title="\frac{(No. of Merged PRs)^{2}}{Total Number of PRs}" /></a>   |


2. Issue Acceptance Ratio:

*Motive :  Value of Contribution*

| Weight |    Formula                        |
| -------|---------------------------------- |
| 2     | <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{(No.&space;of&space;Merged&space;PRs)^{2}}{Total&space;Number&space;of&space;PRs}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{(No.&space;of&space;Closed&space;Issues)^{2}}{Total&space;Number&space;of&space;Issues}" title="\frac{(No. of Closed Issues)^{2}}{Total Number of Issues}" /></a>   | 


#### Contribution Score
<a href="https://www.codecogs.com/eqnedit.php?latex=ContributionScore&space;=(0.3*PRratio)&space;&plus;&space;(0.2*IssueRatio)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ContributionScore&space;=(0.3*PRratio)&space;&plus;&space;(0.2*IssueRatio)" title="ContributionScore =(0.3*PRratio) + (0.2*IssueRatio)" /></a>

-----------------------------------------------------------------------------------------

### Community 
1. Number of followers/following/organisations involved in.
*Motive : to get impact in community*

| Weight |    Formula                        |
| -------|---------------------------------- |
|  10    | Number of Organisations           |
|  2     | Number of Followers               |
|  1     | Number of Following               |

#### Community Score
<a href="https://www.codecogs.com/eqnedit.php?latex=Community&space;Score&space;=&space;(1*OrganisationCount)&space;&plus;&space;(0.2*FollowersCount)&space;&plus;&space;(0.2*FollowingCount)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Community&space;Score&space;=&space;(1*OrganisationCount)&space;&plus;&space;(0.2*FollowersCount)&space;&plus;&space;(0.2*FollowingCount)" title="Community Score = (1*OrganisationCount) + (0.2*FollowersCount) + (0.2*FollowingCount)" /></a>

-----------------------------------------------------------------------------------------

### Activity
1. Annual merged PRs 
*Motive : to get to know how active the user is*

| Weight |    Formula                        |
| -------|---------------------------------- |
|   3    |  Number of PRs merged in an year  |

2. Annual raised Issues
*Motive : to get to know how active the user is*

| Weight |    Formula                        |
| -------|---------------------------------- |
|   2    |  Number of PRs merged in an year  |


#### Activity Score
<a href="https://www.codecogs.com/eqnedit.php?latex=Activity&space;Score&space;=&space;(3*No.ofPRmergedinLastYear)&space;&plus;&space;(2*No.ofIssuesRaisedinLastYear)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Activity&space;Score&space;=&space;(3*No.ofPRmergedinLastYear)&space;&plus;&space;(2*No.ofIssuesRaisedinLastYear)" title="Activity Score = (3*No.ofPRmergedinLastYear) + (2*No.ofIssuesRaisedinLastYear)" /></a>
-----------------------------------------------------------------------------------------

### User Score 
<a href="https://www.codecogs.com/eqnedit.php?latex=User&space;Score&space;=&space;(0.5&space;*&space;BasePoints)&space;&plus;&space;(2&space;*&space;CreationPoints)&space;&plus;&space;(1*ActivityPoints)&space;&plus;&space;(2&space;*&space;ContributionPoints)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?User&space;Score&space;=&space;(0.5&space;*&space;BasePoints)&space;&plus;&space;(2&space;*&space;CreationPoints)&space;&plus;&space;(1*ActivityPoints)&space;&plus;&space;(2&space;*&space;ContributionPoints)" title="User Score = (0.5 * BasePoints) + (2 * CreationPoints) + (1*ActivityPoints) + (2 * ContributionPoints)" /></a>
-----------------------------------------------------------------------------------------


### Skill Score

First, skill score is calculated for each topic the User is interested in :

| Weight  | Contribution     |
|-------- | -----------------|
|   1     |   Number of PRs  |
|   1     |  Number of Issues|

SKill score for a topic is finally calculated as :

<a href="https://www.codecogs.com/eqnedit.php?latex=Skill&space;Score&space;=&space;(Number&space;of&space;PR&space;in&space;the&space;Topic)&space;&plus;&space;(Number&space;of&space;Issue&space;in&space;the&space;Topic)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Skill&space;Score&space;=&space;(Number&space;of&space;PR&space;in&space;the&space;Topic)&space;&plus;&space;(Number&space;of&space;Issue&space;in&space;the&space;Topic)" title="Skill Score = (Number of PR in the Topic) + (Number of Issue in the Topic)" /></a>

-----------------------------------------------------------------------------------------


