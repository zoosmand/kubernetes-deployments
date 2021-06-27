import pandas
import numpy as np
from elasticsearch import Elasticsearch
import json
from pprint import pprint
import time

import matplotlib.pyplot as plt
from sqlalchemy import create_engine

from pandas.io.json import json_normalize


# create a client instance of the library
es = Elasticsearch(hosts="http://localhost:9200", http_auth=('elastic', 'Fl5uHpBgPQRejghWwbVG'))
# es = Elasticsearch(hosts="http://localhost:9200", http_auth=('logstash_system', 'Em9huHceh64HKWKLmHMk'))
# total num of Elasticsearch documents to get with API call
# total_docs = 10
response = es.search(
    # index='logs-my_app-default',
    index='squid*',
    body={},
    size=10
)

print(response)

# Changed password for user apm_system
# PASSWORD apm_system = pcQqo0g5jWOJOX9WzobS

# Changed password for user kibana_system
# PASSWORD kibana_system = zvEZmbnqqw5qowQfhVP6

# Changed password for user kibana
# PASSWORD kibana = zvEZmbnqqw5qowQfhVP6

# Changed password for user logstash_system
# PASSWORD logstash_system = Em9huHceh64HKWKLmHMk

# Changed password for user beats_system
# PASSWORD beats_system = YPDqQh6tbFxSk1hoGI5n

# Changed password for user remote_monitoring_user
# PASSWORD remote_monitoring_user = R0hOIqhPEkwPhRcUf1D2

# Changed password for user elastic
# PASSWORD elastic = Fl5uHpBgPQRejghWwbVG

for key, val in response['hits'].items():
    if key == 'hits':
        for i, hit in enumerate(val):
            # pprint(hit['_id'])
            # pprint(hit['_source']['@timestamp'])
            # pprint(hit['_source']['event']['original'])
            pprint(hit)


# elastic_docs = response["hits"]["hits"]

# fields = {}
# for num, doc in enumerate(elastic_docs):
#     source_data = doc["_source"]

#     for key, val in source_data.items():
#         try:
#             fields[key] = np.append(fields[key], val)
#         except KeyError:
#             fields[key] = np.array([val])


# for key, val in fields.items():
    # print (key, "--->\n", val)
    # print ("NumPy array len:", len(val), "\n")



# create a Pandas DataFrame array from the fields dict
# elastic_df = pandas.DataFrame(fields)

# print ('elastic_df:', type(elastic_df), "\n")
# print (elastic_df) # print out the DF object's contents


# engine = create_engine("elasticsearch:///Server=127.0.0.1&Port=9200&User=elastic&Password=Fl5uHpBgPQRejghWwbVG")

# df = pandas.read_sql('SELECT * FROM logs WHERE', engine)

# print(df)

res = es.search(
    index="logs-my_app-default", 
    body={"query": {"match_all": {}}}, 
    size=10, 
    **{
        '_source': False, 
        'docvalue_fields': [
            '@timestamp', 
        ]
    })

pprint(res)




res = es.search(
    index="logs-my_app-default", 
    body={"query": {"range": { '@timestamp': {
        'gte': '2099-05-05',
        'lt': '2099-05-08',
    }}}}, 
    size=10, 
    **{
        '_source': False, 
        'docvalue_fields': [
            '@timestamp', 
        ]
    })

pprint(res)






res = es.search(
    index="logs-my_app-default", 
    body={"query": {"range": { '@timestamp': {
        'gte': 'now-1d/d',
        'lt': 'now/d',
    }}}}, 
    size=10, 
    **{
        '_source': False, 
        'docvalue_fields': [
            '@timestamp', 
        ]
    })

pprint(res)





res = es.search(
    index="logs-my_app-default", 
    body={
        "query": {"range": { '@timestamp': {
            'gte': '2099-05-05',
            'lt': '2099-05-08',
        }}},
        'runtime_mappings': {
            'source.ip': {
                'type': 'ip',
                'script': """
                String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ 'event.original' ].value)?.sourceip;
                if (sourceip != null) emit(sourceip);
                """
            }
        }
    }, 
    size=10, 
    **{
        '_source': False, 
        'docvalue_fields': [
            '@timestamp', 
            'source.ip'
        ]
    })

pprint(res)







res = es.search(
    index="logs-my_app-default", 
    body={
        "query": {"range": { '@timestamp': {
            'gte': '2099-05-05',
            'lt': '2099-05-08',
        }}},
        'runtime_mappings': {
            'source.ip': {
                'type': 'ip',
                'script': """
                String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ 'event.original' ].value)?.sourceip;
                if (sourceip != null) emit(sourceip);
                """
            }
        },
        'sort': [{ '@timestamp': 'desc' }]
    }, 
    size=10, 
    **{
        '_source': False, 
        'docvalue_fields': [
            '@timestamp', 
            'source.ip',
        ],
    })

pprint(res)






res = es.search(
    index="logs-my_app-default", 
    body={
        "query": {'match': {
            '_id': 'SCPnQ3oBDgNQ0HL1kQyx',
        }},
        'runtime_mappings': {
            'source.ip': {
                'type': 'ip',
                'script': """
                String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ 'event.original' ].value)?.sourceip;
                if (sourceip != null) emit(sourceip);
                """
            }
        },
    }, 
    size=10, 
    **{
        '_source': False, 
        'docvalue_fields': [
            '@timestamp', 
            'source.ip',
        ],
    })

pprint(res)
