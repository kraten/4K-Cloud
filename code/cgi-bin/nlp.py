#!/usr/bin/python36

query="set up map  "


def check_staas_query(query):
    staas_list = ['cloud', 'drive', 'storage', 'Cloud', 'Storage', 'Drive'] 
    for i in staas_list:
        if i in query:
            size = [int(s) for s in query.split() if s.isdigit()]
            if len(size) != 0:
                return size[0]        
    return -1


def check_cluster_query(query):
    cluster_list = ['hadoop', 'cluster', 'Hadoop', 'Cluster'] 
    for i in cluster_list:
        if i in query:
            url = 'hadoop.py'
            return url
        
    return -1


def check_mr_query(query):
    mr_list = ['map', 'reduce', 'map reduce', 'Map', 'Reduce', 'Map reduce'] 
    for i in mr_list:
        if i in query:
            url = 'hadoop.py'
            return url
        
    return -1


def process_query(query):
    if check_staas_query(query) != -1:
        size = str(check_staas_query(query)) + 'G'
        url = 'staas.py?u=newuser&s={}'.format(size)
        return url
    elif check_cluster_query(query) != -1:
        url = check_cluster_query(query)
        return url
        
    elif check_mr_query(query) != -1:
        url = check_mr_query(query)
        return url
    else :
        return "No match found"


