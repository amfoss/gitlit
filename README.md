# GitLit :fire:
[ALPHA VERSION]

GitLit is a social network exclusively for Open-Source developers.

It works by connecting enthusiastic developers to the most interesting and relevant projects to them and forming new communities of like-minded and passionate developers.   

## :thinking: Why GitLit? 

1. **Its hard to find contributable projects** - What if you can get a dashboard full of project and issues suggestions, which are relevant to you - both skill and interest wise?


## :bowtie: Target Users  
There are two primary use-cases for GitLit, one for the developers to discover interesting projects and the other is for 
people in the industry to find talented and enthusiastic developers. 

**Project Discovery**

* **Students & Beginners:** GitLit can be used by students and beginners to get started into the world of Open Source.
It helps them to break-the-ice, and kick-start their FOSS journey without essentially going into deeper level they can.

* **Developers** GitLit can also be used by amateur as well as professional developers to discover innovative, interesting
and relevant projects to contribute to - based on their skill level.

**Developer Discovery**

* **Developer Advocates:** GitLit can be used by developer advocates to identify enthusiastic and talented 
contributors, who are interested in their organization, and connect with them. It can be also used by them to analyse 
their projects, and monitor community members. 

* **College Clubs:** College based computer clubs like [amFOSS](http://amfoss.in/), can use GitLit to identify enthusiastic and talented 
 students out of a large pool and effectively monitor and check their progress.
 
 * **Corporate Recruiters:** Corporate companies can discover developers, with the required talent and passion using
 credible metrics of GitLit. 


## :electric_plug: How it Works?  

### Suggestion Panel to help developers
1. Fetches all data about a developer, once a developer signs-up.
2. After analysing his previous contribution pattern, an complex algorithm rates the developer using smart metrics, and classifies him into interest groups.
3. Based on his interests, and his skill in the given topic of interest, an ML-based matching algorithm matches it with most relevant projects
4. The developer recieves relevant and interesting suggestions for projects and issues.  

### Discovery Panel to help projects


### Some Screenshots
<img src="/dashboard.jpg" alt="User Dashboard"> 
<img src="/repo.jpg" alt="Repository Profile">

## Technical Details

### Rating Metrics

**User Metrics:**

- Base Score : General cliche metrics
- Creation : How good the developer’s own projects are?
- Contribution : How active is the developer in contributing to other repositories?
- Community : How large is the network of the repository?
- Activity : How frequently does the user contribute?
- Topic-wise Metrics -
  - Skill Score : represents the skill a user has for a topic?
  - Interest Score: how interested the user is in the topic?

**Repo Metrics:**

- Merit: How valuable is the community to FOSS?
- Activity: How engaging and active is the community?
- Popularity: How popular is the community?
- Inclusivity : How likely is the community open to new contributors? 

Scores for each of the above mentioned trait for user and repo are calculated, and matching is performed. 

### Data Sourcing 

View GitHub API-related documentation at [/api](/api/README.md)


### :computer: Algorithms  

View algorithm documentation at [/algorithms](/algorithms/README.MD) 

## :nut_and_bolt: Tech Stack  

* **Language:** Python 3.6
* **Framework (full-stack):** Django
* **API:** GraphQL (Github API 4), Rest API (Github API 3)
* **Frontend Frameworks:** Bootstrap 4
* **Javascript Libraries:** jQuery
* **Stylesheet Pre-processors:** Sass 


##  :busts_in_silhouette: Contributors

1. [Venu Vardhan Reddy](https://github.com/vchrombie)
2. [Akhil K Gangadharan](https://github.com/akhilam512)
3. [Ashwin S Shenoy](https://github.com/aswinshenoy)

Contributions are welcome! <3

## :black_nib: License 
GNU General Public License v3.0
