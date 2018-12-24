# Using APIs for fetching data - Github GraphQL v4 


##  GitHub GraphQL v4 API 

GitHub v4 GraphQL is a shift from the traditional v3 REST API structure of GitHub, as it is a specification which offers an elegant way of data retrieval, offers more efficient queries and more stablitiy to the backend. 

It offers a much easier and comfortable way to understand, write and send queries and that is the reason why almost all the queries used here will be in GraphQL. Although some specific data is not available via GraphQL, REST v3 API is used wherever v4 failed.


### Examples
 
1. To extract the topic names assigned for a given input repository 
```
query
{
  repository(owner:"amfoss", name:"fosswebsite")
  {
  	repositoryTopics
    {
      nodes
      {
        topic
      	{
          name 
        }
      }
    }
  }
}
```

This query returns a list of topic names in JSON format.


One may use the [GitHub v4 Explorer](https://developer.github.com/v4/explorer/) to test constructing and sending queries.

### Documentation and References

- [Documentation](https://developer.github.com/v4/guides/intro-to-graphql/)
- [Implementing and Using GraphQL at GitHub - YouTube](https://www.youtube.com/watch?v=wPPFhcqGcvk)





