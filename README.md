# GitLit :fire:
![Status](https://img.shields.io/badge/Status-Under_Development-Red.svg) 
![Version 0.1](https://img.shields.io/badge/Version-0.1_(Alpha)-green.svg) 
[![GNU][license-badge]][license]
[![Open Issues][issues-badge]][issues]
[![PRs][pr-badge]][prs]
[![Contributors][contributors-badge]][contributors]


[![Watchers][watchers-badge]][watchers]
[![Star Gazers][stars-badge]][stargazers]
[![Forks][forks-badge]][forks]


GitLit is a social network exclusively for Open-Source developers. It works by connecting enthusiastic developers to the most interesting and relevant projects to them and forming new communities of like-minded and passionate developers.   

## :thinking: Why GitLit? 

1. **It is difficult to find contributable projects** - What if you can get a dashboard full of project and issues suggestions, which are relevant to you - both skill and interest wise?

## :star2: Top Features
1. Adavanced Rating System for Contributor's & Repositories on GitHub
2. Intelligent Identification of Contributor's Interest & Skills
3. Smart & Relevant Mapping of Repositories & Contributor's based on shared interests and skill-level. 
4. Suggestion feed of contributable repositories, and notifications for fixable issues
5. View similar repositories and users
6. Intelligent Insights with actionable feedbacks & checklist for contributors and repositories

## :bowtie: Target Users  
There are two primary use-cases for GitLit, one for the developers to discover interesting projects and the other is for 
people in the industry to find talented and enthusiastic developers. 

**Project Discovery**

* **Students & Beginners:** GitLit can be used by students and beginners to get started into the world of Open Source.
It helps them to break-the-ice, and kick-start their FOSS journey without essentially going into deeper level.

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

## :bookmark_tabs: Documentation
* **Algorithms**
  * **Documentation**
  * [**Working Code**](/algorithms/README.MD) 
* **Data Sourcing & Processing**
  * [**GitHub API**](https://github.com/teamdeadlock/GitLit/wiki/GitHub-API)
  * **Limitations in Sourcing & Processing**
* **Rating Metrics**
  * [**User Metrics**](https://github.com/teamdeadlock/GitLit/wiki/Metrics:-Repository-Metrics)
  * [**Repository Metrics**](https://github.com/teamdeadlock/GitLit/wiki/Metrics:-Repository-Metrics)
* **Interest Identification**
  * **Using GitHub Topics as basis for Interest Classfication**
  * [**Finding User's Topics of Interest**](https://github.com/teamdeadlock/GitLit/wiki/Topics:-Identifying-Project-Topics)
  * [**Weighting Topics of Interest**](https://github.com/teamdeadlock/GitLit/wiki/Topics:-Weighting-Topics-of-Interest)
  * [**Identification of Project Topics**](https://github.com/teamdeadlock/GitLit/wiki/Topics:-Identifying-Project-Topics)
* **Matching & Mapping**

## :electric_plug: How it Works?  

### Suggestion Panel to help developers
1. Fetches all data about a developer, once a developer signs-up.
2. After analysing his previous contribution pattern, an complex algorithm rates the developer using smart metrics, and classifies him into interest groups.
3. Based on his interests, and his skill in the given topic of interest, an ML-based matching algorithm matches it with most relevant projects
4. The developer recieves relevant and interesting suggestions for projects, and issues.  

### Discovery Panel to help projects


## :nut_and_bolt: Tech Stack  

* **Language:** Python 3.6
* **Framework (full-stack):** Django
* **API:** GraphQL (Github API 4), Rest API (Github API 3)
* **Frontend Frameworks:** Bootstrap 4
* **Javascript Libraries:** jQuery
* **Stylesheet Pre-processors:** Sass 


##  :busts_in_silhouette: Creators

1. [Venu Vardhan Reddy](https://github.com/vchrombie)
2. [Akhil K Gangadharan](https://github.com/akhilam512)
3. [Ashwin S Shenoy](https://github.com/aswinshenoy)

Contributions are welcome! <3

## :black_nib: License 
[GNU General Public License v3.0](/LICENSE)

[contributors-badge]:https://img.shields.io/github/contributors/amfoss/gitlit.svg
[contributors]: https://github.com/amfoss/GitLit/graphs/contributors
[watchers-badge]:https://img.shields.io/github/watchers/amfoss/gitlit.svg?style=social
[watchers]: https://github.com/amfoss/GitLit/watchers
[stars-badge]:https://img.shields.io/github/stars/amfoss/gitlit.svg?style=social
[stargazers]:https://github.com/amfoss/GitLit/stargazers
[forks-badge]: https://img.shields.io/github/forks/amfoss/gitlit.svg?style=social
[forks]: https://github.com/amfoss/GitLit/network/members
[license-badge]: https://img.shields.io/github/license/amfoss/gitlit.svg
[license]: https://github.com/amfoss/gitlit/blob/master/LICENSE
[issues-badge]: https://img.shields.io/github/issues/amfoss/gitlit.svg
[issues]: https://github.com/amfoss/gitlit/issues
[pr-badge]:https://img.shields.io/github/issues-pr/amfoss/gitlit.svg
[prs]: https://github.com/amfoss/gitlit/pulls

