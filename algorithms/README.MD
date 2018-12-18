# GitLit Algorithms


## Rating Algorithms 
Each metric defined below has its own specific API query. The process is simple : we fetch the data from GitHub APIs which is already streamlined for a specific metric, cut down the data further (if needed) and then assign appropriate weights to these numbers to form a score of a User or a Repo.

-----------------------------------------------------------------------------------------

## User Rating
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

## Repository Rating

### General Traits

1. General activity and relevance of repo

*Motive : To get a basic idea*

| Weight  | Trait              |
|-------- | ------------------ |
| 3       | Number of watchers |
| 2       | Numer of stars     |
| 5       | Number of PRs      |
| 1.5     | Number of forks    |
|  4      | Number of issues   |

#### Base Score

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathbf{Base&space;Score}&space;=&space;(0.3&space;*&space;Watchers)&space;&plus;&space;(0.2&space;*&space;Stars)&space;&plus;&space;(0.15&space;*&space;Forks)&space;&plus;&space;(0.5&space;*&space;PRs)&space;&plus;&space;(0.4&space;*&space;Issues)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbf{Base&space;Score}&space;=&space;(0.3&space;*&space;Watchers)&space;&plus;&space;(0.2&space;*&space;Stars)&space;&plus;&space;(0.15&space;*&space;Forks)&space;&plus;&space;(0.5&space;*&space;PRs)&space;&plus;&space;(0.4&space;*&space;Issues)" title="\mathbf{Base Score} = (0.3 * Watchers) + (0.2 * Stars) + (0.15 * Forks) + (0.5 * PRs) + (0.4 * Issues)" /></a>
-----------------------------------------------------------------------------------------

### Actvity

1. Average Issue Resolution Time

*Motive : To weigh the response time*

| Weight  | Formula            |
|-------- | ------------------ |
|  8      | <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{TimeTakenToCloseIssues}{TotalNuberOfIssues}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{TimeTakenToCloseIssues}{TotalNuberOfIssues}" title="\frac{TimeTakenToCloseIssues}{TotalNuberOfIssues}" /></a> |

Average Issue Resolution Score is calculated from the above formula based on the following conditions : 

| Average Issue Resolution Time  ( in days )  |  Score  |
| ------------------------------------------- | ------- |
|     less than or equal to 20                |  20     |
|     less than or equal to 50                |  10     |
|     greater than 50                         |   5     |

2. Weekly Contributor Count

*Motive : To acount for contributor activity*

(*Note : A contributor,here, means anyone who has created an Issue or a PR*)


| Weight  | Formula            |
|-------- | ------------------ |
| 5       |  <a href="https://www.codecogs.com/eqnedit.php?latex=No.OfWeeklyContributor" target="_blank"><img src="https://latex.codecogs.com/gif.latex?No.OfWeeklyContributor" title="No.OfWeeklyContributor" /></a> |

3. Weekly Contributor Change

*Motive : To acount for contributor activity*

| Weight  | Formula            |
|-------- | ------------------ |
|  8      |  <a href="https://www.codecogs.com/eqnedit.php?latex=TotalContributorCount&space;-&space;WeeklyContributorCount" target="_blank"><img src="https://latex.codecogs.com/gif.latex?TotalContributorCount&space;-&space;WeeklyContributorCount" title="TotalContributorCount - WeeklyContributorCount" /></a> |


#### Activity Score

<a href="https://www.codecogs.com/eqnedit.php?latex=ActivityScore&space;=&space;(8*AvgIssueResolutionScore)&space;&plus;&space;(5*WeeklyContributorCount)&space;&plus;&space;(8*WeeklyContributorChange)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ActivityScore&space;=&space;(8*AvgIssueResolutionScore)&space;&plus;&space;(5*WeeklyContributorCount)&space;&plus;&space;(8*WeeklyContributorChange)" title="ActivityScore = (8*AvgIssueResolutionScore) + (5*WeeklyContributorCount) + (8*WeeklyContributorChange)" /></a>


-----------------------------------------------------------------------------------------

### Inclusivity 

1. PR Acceptance Ratio

*Motive : To account for new code submitted w.r.t old code*

| Weight  | Formula            |
|-------- | ------------------ |
|    8    |  <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{MergedPRs}{TotalNumberOfPRs}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{MergedPRs}{TotalNumberOfPRs}" title="\frac{MergedPRs}{TotalNumberOfPRs}" /></a> |

2.  New Contributor Count

*Motive : To account for first time contributors to repo in the week* 

| Weight  | Formula            |
|-------- | ------------------ |
|    4    | <a href="https://www.codecogs.com/eqnedit.php?latex=No.OfFirstTimeContributorToRepo" target="_blank"><img src="https://latex.codecogs.com/gif.latex?No.OfFirstTimeContributorToRepo" title="No.OfFirstTimeContributorToRepo" /></a> |

#### Inclusivity Score

<a href="https://www.codecogs.com/eqnedit.php?latex=InclusivityScore&space;=&space;(0.8&space;*&space;PRacceptanceRatio&space;)&space;&plus;&space;(&space;0.4*No.OfNewContributors&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?InclusivityScore&space;=&space;(0.8&space;*&space;PRacceptanceRatio&space;)&space;&plus;&space;(&space;0.4*No.OfNewContributors&space;)" title="InclusivityScore = (0.8 * PRacceptanceRatio ) + ( 0.4*No.OfNewContributors )" /></a>

-----------------------------------------------------------------------------------------


### Merit 

1. Complexity of Repo

It is estimated by calcuating the Skill Points of the top 10 contributors of the repo in the topics the Repo and the Contributors both share.

<a href="https://www.codecogs.com/eqnedit.php?latex=RepoComplexity&space;=&space;(SkillPointsOfTopTenContributors)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?RepoComplexity&space;=&space;(SkillPointsOfTopTenContributors)" title="RepoComplexity = (SkillPointsOfTopTenContributors)" /></a>

#### Merit Score

<a href="https://www.codecogs.com/eqnedit.php?latex=Merit&space;Score&space;=&space;Repo&space;Complexity" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Merit&space;Score&space;=&space;Repo&space;Complexity" title="Merit Score = Repo Complexity" /></a>

-----------------------------------------------------------------------------------------


### Total Repo Score

<a href="https://www.codecogs.com/eqnedit.php?latex=Total&space;Repo&space;Score&space;=&space;BaseScore&space;&plus;&space;ActivityScore&space;&plus;InclusivityScore&space;&plus;&space;MeritScore" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Total&space;Repo&space;Score&space;=&space;BaseScore&space;&plus;&space;ActivityScore&space;&plus;InclusivityScore&space;&plus;&space;MeritScore" title="Total Repo Score = BaseScore + ActivityScore +InclusivityScore + MeritScore" /></a>



 -----------------------------------------------------------------------------------------




