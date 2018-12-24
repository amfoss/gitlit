# GitLit :fire:
GitLit is a web app that rates repositories and contributors through an algorithm which takes into consideration a range of metrics, from standard metrics like Stars, Forks, and PRs to accounting for factors like Activity in the Community (eg: Issue Resolution, PR Resolution time, Feature Addition),  backgrounds of the contributors, Inclusivity and Value.  Gitlit gives you the best and most appropriate projects to contribute to by analysing your skills and interest. 

## :thinking: Why GitLit? 
Open Source is, by large, hard to adjust into. Whenever one enters the world of Open Source, he/she is, in most of the cases, greeted by large organizations where new contributors may find difficult to contribute something worthy - it can be their lack of patience or simply the lack of enough skills or it might be what we think it is - simply the lack of finding the correct projects. Contributions, in general,  have largely been limited to some popular organizations since it has been difficult for new innovative projects to gain attention and acquire a group of interested and skilled contributors. 
Furthermore, the same is the case for contributors to discover interesting and contributable communities and then to find workable issues and cool features - all in all - a complicated and a time-taking task, often leading many beginners to drop out of Open Source as they lack the know-how to get started.  



----------------------------------------------------------------------------------------------------------------------
## :bowtie: Target Customers  
GitLit has two primary use-cases, one for the developers to discover interesting projects and the other is for 
people in the industry to find talented and enthusiastic developers. 

**Project Discovery**

* **Students & Beginners:** GitLit can be used by students and beginners to get started into the world of Open Source.
It helps them to break-the-ice, and kick-start their FOSS journey without essentially going into deeper level they can.

* **Developers** GitLit can also be used by amateur as well as professional developers to discover innovate, interesting
and relevant projects to contribute to, based on their skill level.

**Developer Discovery**

* **Developer Advocates:** GitLit can be used by developer advocates to identify enthusiastic and talented 
contributors, who are interested in their organization, and connect with them. It can be also used by them to analyse 
their projects, and monitor community members. 

* **College Clubs:** College based computer clubs like amFOSS, can use GitLit to identify enthusiastic and talented 
 students out of a large pool, effectively monitor them and check their progress.
 
 * **Corporate Recruiters:** Corporate companies can discover developers, with the required talent and passion using
 credible metrics of GitLit 

----------------------------------------------------------------------------------------------------------------------

## :electric_plug: How it Works?  

A set of scores are calculated for the user and based on these scores, appropriate repositories (of whose scores are also calculated) are matched.

### User Dashboard
<img src="/dashboard.jpg" alt="Dashboard.jpg"> 

### Repository Rating
<img src="/repo.jpg" alt="SampleRepo.jpg">

### Rating

**User Analysis:**

- Base Score : General cliche’ metrics
- Creation : How good the developer’s own project are?
- Contribution : How active is the developer in contributing to other repositories?
- Community : How large is the network of the repository?
- Activity : How frequently does the user contribute?
- Topic-wise Metrics -
  - Skill Score : represents the skill a user has for a topic?
  - Interest Score: how interested the user is in the topic?

**Repo Analysis:**

- Merit: How valuable is the community to FOSS?
- Activity: How engaging and active is the community?
- Popularity: How popular is the community?
- Inclusivity : How likely is the community open to new contributors? 

Scores for each of the above mentioned trait for user and repo are calculated, and matching is performed. 

### Data collection 

For API and query working details - please refer to [/api](/api/README.md)

----------------------------------------------------------------------------------------------------------------------

## :computer: Algorithms  
Please refer to the README file in [/algorithms](/algorithms/README.MD) 

----------------------------------------------------------------------------------------------------------------------

## :nut_and_bolt: Tech Stack  

* **Language:** Python 3.6
* **Framework (full-stack):** Django
* **API:** GraphQL (Github API 4), Rest API (Github API 3)
* **Frontend Frameworks:** Bootstrap 4
* **Javascript Libraries:** jQuery
* **Stylesheet Pre-processors:** Sass 

----------------------------------------------------------------------------------------------------------------------

##  :busts_in_silhouette: Contributors

1. [Venu Vardhan Reddy](https://github.com/vchrombie)
2. [Akhil K Gangadharan](https://github.com/akhilam512)
3. [Ashwin S Shenoy](https://github.com/aswinshenoy)

Contributors are welcome! <3

----------------------------------------------------------------------------------------------------------------------

## :black_nib: License 
GNU General Public License v3.0
