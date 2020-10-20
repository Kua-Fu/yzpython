"""
深度优先搜索 (递归实现)

步骤:

(1) 定义已经检查节点列表visited为空列表，

(2) 对于一个节点node，调用dfs

    如果没有被检查，则添加到检查列表中，
       
       a. 判断是否是目标节点，如果是目标节点, 返回(True, visited)

       b. 如果不是目标节点，则对于节点node的所有子节点，递归调用dfs
          
          判断dfs的返回值，如果是True, 则返回检查列表

(3) 最终遍历所有的节点，没有找到，则返回 (False, visited)

"""

visited = [] # (1)

def dfs(visited, graph, node, target): # (2)

    if node not in visited:
        
        visited.append(node)

        if node == target: # (2) a
            return True, visited

        for neighbour in graph[node]: # (3) b
            if dfs(visited, graph, neighbour, target)[0]:
                return True, visited

    return False, visited
