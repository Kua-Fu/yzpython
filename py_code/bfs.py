"""
广度优先搜索

算法步骤:

(1) 将根节点start放入队列中queue，定义检查列表为空列表explored

(2) 循环遍历队列queue，如果队列为空，停止循环

(3) 在每次循环中，

    从队列中取出第一个节点node，

    验证：

    a. 是否已经检查过，如果没有加入到判断检查列表explored中
    
    b. 是否是目标节点target，如果是目标节点，结束搜索，
    
       返回元组(True, explored)

       c. 否则将第一个节点的所有尚未检测过的直接子节点加入到队列中

(4) 若循环结束，表示整个图都已经检查过了，此时结果是没有找到目标，
    
    返回(False, explored)

"""


def bfs(graph, start, target):

    explored = [] # 遍历的路径
    queue = [start]  # (1)

    while queue: # (2)

        node = queue.pop(0) 
        if node not in explored: # (3) a
            explored.append(node)
            if node == target: # (3) b
                return True, explored
            neighbours = graph[node]
            for neighbour in neighbours: # (3) c
                queue.append(neighbour)

    return False, explored # (4)

