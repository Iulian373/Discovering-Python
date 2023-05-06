#
graph={}

graph['start']={}
graph['start']['a']=6
graph['start']['b']=2
                        #              B
graph['a']={}           #           2/ | \5
graph['a']['fin']=1     #       start  |3 fin
                        #           6\ | /1
graph['b']={}           #              A 
graph['b']['a']=3
graph['b']['fin']=5

graph['fin']={}

#
infinity=float('inf')
costs={}
costs['a']=6
costs['b']=2
costs['fin']=infinity

#
parents={}
parents['a']='start'
parents['b']='start'
parents['fin']=None

#
processed=[]

#
def find_lowest_cost_node(costs):
    lowest_cost=float('inf')
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

#
node=find_lowest_cost_node(costs) #Find the lowest-cost node that you haven’t processed yet
while node is not None: # If you’ve processed all the nodes, this while loop is done
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():    #Go through all the neighbors of this node
        new_cost=cost+neighbors[n]
        if new_cost<costs[n]:#If it's cheaper to get to this neighbor by going through this node
            costs[n]=new_cost#...update the cost of this node
            parents[n]=node#This node becomes the new parent for this neighbor
    processed.append(node)
    node=find_lowest_cost_node(costs)

print(costs['fin'])
print(parents)
