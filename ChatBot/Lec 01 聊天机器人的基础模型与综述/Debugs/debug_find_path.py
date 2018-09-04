# -*- coding:utf-8 -*-
graph = {'上海': ['苏州', '常州'],
         '苏州': ['常州', '镇江'],
         '常州': ['镇江'],
         '镇江': ['常州'],
         '盐城': ['南通'],
         '南通': ['常州']}

# 明确如何找到从A到B的路径
def find_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(node, end, path)
            if newpath:
                return newpath
    return None

if __name__=='__main__':
    print(find_path('上海','镇江'))