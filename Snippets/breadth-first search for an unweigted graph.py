from collections import deque #to be able to use a queue (FIFO data structure)

graph={}                     #with hash map/table creat a graph
graph['you']=['alice','rob','claire']
graph['rob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire']=['bob','jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['bob']=[]
graph['jonny']=[]

def poli_name(name):         #just a function to determine the requested item/target
    return name[0]==name[len(name)-1]

def breadth_first_search(name):
    search_queue =  deque()      #creat a queue
    search_queue += graph[name]     #add all the name's neighbours to the queue
    searched=[]
    while search_queue:         #while the queue isn't empty
        person = search_queue.popleft()      #grab the first person of the queue
        if not person in searched:       #Only search this person if you haven’t already searched them
            if poli_name(person):
                print(person+' has a name that starts and \
ends with the same letter')
                return True
            else:                              #it's not the proper one so...
                search_queue += graph[person]  #...  add its neighbours to the queue
                searched.append(person)       #mark the item as checked
    return False
breadth_first_search('you')
