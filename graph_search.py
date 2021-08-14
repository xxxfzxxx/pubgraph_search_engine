from py2neo import Graph, Node, Relationship

def associate_author(graph, name, org):
    instruction = '''match (:author{name:"%s", org:"%s"})-[*2..2]-(p:author)
return  p.name, p.org ''' % (name, org)
    result = graph.run(instruction).data()
    res = []
    for i in result:
        res.append((i["p.name"],i["p.org"]))
    res = list(set(res))
    return res

def associate_paper(graph, title):
    instruction = '''match (:paper{title:"%s"})-[*1..1]-(p:paper)
return  p.title ''' % (title)
    result = graph.run(instruction).data()
    res = []
    for i in result:
        res.append((i["p.title"]))
    res = list(set(res))
    return res

def shortest_path(graph, name1, org1, name2, org2):
    instruction= '''match (a:author{name:"%s", org:"%s"}), (b:author{name:"%s", org:"%s"}),
p = shortestPath((a)-[*..15]-(b))
return p ''' %(name1, org1, name2, org2)
    result = graph.run(instruction).data()
    return result

def find_authors(graph, title):
    instruction = '''match ((p:author)-[*1..1]-(b:paper{title:"%s"}))
return  p.name, p.org ''' % (title)
    result = graph.run(instruction).data()
    res = []
    for i in result:
        res.append((i["p.name"],i["p.org"]))
    res = list(set(res))
    return res    

def common_paper(graph, name1, org1, name2, org2):
    instruction = '''match ((:author{name:"%s", org:"%s"})-[*1..1]-(b:paper))
return  b.title ''' % (name1, org1)
    result1 = graph.run(instruction).data()
    res1 = [i["b.title"] for i in result1]
    instruction = '''match ((:author{name:"%s", org:"%s"})-[*1..1]-(b:paper))
return  b.title ''' % (name2, org2)
    result1 = graph.run(instruction).data()
    res2 = [i["b.title"] for i in result1]
    res = list(set(res1).intersection(set(res2)))
    return res

def pagerank(graph, title):
    instruction = '''match (p:paper{title:"%s"})
return  p.pagerank ''' % (title)
    result = graph.run(instruction).data()
    return result[0]["p.pagerank"]

if __name__ == '__main__':
    graph = Graph('bolt://40.114.125.234:7687',username='neo4j',password='123456aa')
    # Find Related Author
    Author_name, Author_org = "Nestor Garay-Vitoria", "-1"
    print("Relevant Authors:")
    print(associate_author(graph, Author_name, Author_org))
    print("-------------------")
    # Find Relate Paper
    Paper_title = "Rothko's Negative Theology"
    print("Relevant Papers:")
    print(associate_paper(graph, Paper_title))
    print("-------------------")
    # Find the shortest path between two authors
    author1_name, author1_org = "Nestor Garay-Vitoria", "-1"
    author2_name, author2_org = "Julio Abascal", "-1"
    print("shortest path:")
    print(shortest_path(graph, author1_name, author1_org, author2_name, author2_org))
    print("-------------------")
    # Coauthorship:
    # Find all authors of a paper
    Paper_title = "Evaluation of Prediction Methods Applied to an Inflected Language."
    print("all authors of a paper:")
    print(find_authors(graph, Paper_title))
    print("-------------------")
    # Find papers that two authors coauthor on 
    print("papers that two authors coauthor on:")
    author1_name, author1_org = "Nestor Garay-Vitoria", "-1"
    author2_name, author2_org = "Julio Abascal", "-1"
    print(common_paper(graph, author1_name, author1_org, author2_name, author2_org))
    print("-------------------")
    print("Pagerank score of a paper")
    Paper_title = "Action of diethylstilboestrol on mouse vaginal sialic acids. I."
    print(pagerank(graph, Paper_title))
