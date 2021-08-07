from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")


def search(query, start_year=1950, end_year=2021, title_only=True):
    if title_only:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "title": query
                            }
                        },
                        {
                            "range": {
                                "n_citation": {
                                    "gte": 100,
                                    "boost": 2
                                }
                            }
                        }
                    ],
                    "filter": [
                        {
                            "range": {
                                "year": {
                                    "gte": start_year,
                                    "lte": end_year
                                }
                            }
                        }
                    ]
                }
            }
        }
    else:
        body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "fields": ["title","abstract","indexed_abstract","keywords","fos.name"],
                                "query": query,
                                "analyzer":"snowball"
                            }
                        },
                        {
                            "range": {
                                "n_citation": {
                                    "gte": 100,
                                    "boost": 2
                                }
                            }
                        }
                    ],
                    "filter": [
                        {
                            "range": {
                                "year": {
                                    "gte": start_year,
                                    "lte": end_year
                                }
                            }
                        }
                    ]
                }
            }
        }
    results = es.search(index=["aminer_*", "mag_*"], body=body, size=100)
    return results

if __name__ == '__main__':
    # change params in line 77 to search
    search = search("algorithm", start_year=2000, title_only=True)
    
    title = [str(hit['_source']['title']) for hit in search['hits']['hits']]
    scores = [hit['_score'] for hit in search['hits']['hits']]
    index = [hit['_index'] for hit in search['hits']['hits']]
    year = [hit['_source']['year'] for hit in search['hits']['hits']]
    n_citation = [hit['_source']['n_citation'] for hit in search['hits']['hits']]
    # authors = [str(hit['_source']['authors']) for hit in search['hits']['hits']]
    
    # increase the range in line 87 to see more results
    for i in range(10):
        print('result',i+1,':','score:',scores[i])
        print('index: ', index[i])
        print('title:',title[i])
        print('year: ', year[i])
        print('n_citation: ', n_citation[i])
        # print('authors:',authors[i])
        print('--------------------------------------------------------------')