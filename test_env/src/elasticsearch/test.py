
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(
        "http://elasticsearch:9200"
    )

for i in range(30):
    body = {
        "test": [
            {
                "test_value":str(i//3)
            }
        ]
    }
    
    es.index(
        index="test_index",
        doc_type="_doc",
        body=body,
        id=i
    )