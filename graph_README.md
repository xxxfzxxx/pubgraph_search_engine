## How to use graph search:
# Support Following Functions:
- **Find Associate Author**: associate_author(graph, name, org)
  
- **Find Associate Paper**: associate_paper(graph, title)
  
- **Shortest path**: shortest_path(graph, name1, org1, name2, org2)
  
- **Return Pagerank Score**: pagerank(graph, title)
  
- **find all authors of a paper:** find_authors(graph, title)
  
- **find papers that two authors collaborate on**: common_paper(graph, name1, org1, name2, org2)

- *graph* parameter refers to connect to the neo4j database, with command: *graph = Graph('bolt://40.114.125.234:7687',username='neo4j',password='123456aa')*

- Sample usage begins from **line 59**