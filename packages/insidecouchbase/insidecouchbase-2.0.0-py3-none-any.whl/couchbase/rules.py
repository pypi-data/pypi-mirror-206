def setRules():
    ruleList=[
    {
        "code": "configuration-01",
        "definition" : "Data Memory Quota Configuration",
        "result":"not_checked",
        "Recommendation" : "Data memory quota can not be greater than %70 of OS memory"
    },
    {
        "code": "configuration-02",
        "definition" : "SWAP Configuration",
        "result":"not_checked",
        "Recommendation" : "SWAP can not be used in production couchbase environments"
    },
    {
        "code": "configuration-03",
        "definition" : "All Nodes are Using Same Couchbase Version",
        "result":"not_checked",
        "Recommendation" : "Different versions of couchbase can not be used inside the same cluster."
    },
    {
        "code": "configuration-04",
        "definition" : "Cluster is Working Wtih MDS Model",
        "result":"not_checked",
        "Recommendation" : "1 Couchbase node has to be use 1 service only."
    },
    {
        "code": "configuration-05",
        "definition" : "Autofailover Enabled",
        "result":"not_checked",
        "Recommendation" : "Autofailover needs to be enabled to achive better HA"
    },
    {
        "code": "health-01",
        "definition" : "All Nodes Up and Running",
        "result":"not_checked",
        "Recommendation" : "All nodes have to be up and joined cluster."
    },
    {
        "code": "bucket-01",
        "definition" : "All Buckets Have Resident Ratio Greater Than %50",
        "result":"not_checked",
        "Recommendation" : "Bucket resident ratio needs to be greater than %50"
    },
    {
        "code": "bucket-02",
        "definition" : "All Buckets Have At Least 1 Replica",
        "result":"not_checked",
        "Recommendation" : "All buckets must have at least one replica to prevent data loss in case of emergency"
    },
    {
        "code": "bucket-03",
        "definition" : "All Buckets Have 1024 Primary Vbucket",
        "result":"not_checked",
        "Recommendation" : "All buckets must carry 1024 primary vbucket."
    }
]
    return ruleList