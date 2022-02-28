"""
This question is designed to help you get a better understanding of basic heap operations.

There are  types of query:

" " - Add an element  to the heap.
" " - Delete the element  from the heap.
"" - Print the minimum of all the elements in the heap.
NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

Input Format

The first line contains the number of queries, .
Each of the next  lines contains one of the  types of query.

Constraints


Output Format

For each query of type , print the minimum value on a single line.

Sample Input

STDIN       Function
-----       --------
5           Q = 5
1 4         insert 4
1 9         insert 9
3           print minimum
2 4         delete 4
3           print minimum
Sample Output

4  
9 
Explanation

After the first  queries, the heap contains {}. Printing the minimum gives  as the output. Then, the  query deletes  from the heap, and the  query gives  as the output.
"""

import heapq

def add(listt,dic, val):
    if val in dic and dic[val]>0:
        dic[val]-=1
    else:
        heapq.heappush(listt,val)
    
def delete(dic,val):
    if val in dic:
        dic[val]+=1
    else:
        dic[val] = 1
            
def display(listt,dic):
    
    while len(listt)>0 and listt[0] in dic and dic[listt[0]] >0:
        dic[listt[0]]-=1
        heapq.heappop(listt)
        
    print(listt[0])


def queryfun(dic, listt, lst):
    
    if lst[0] == 1:
        add(listt,dic,lst[1])
    elif lst[0] == 2:
        delete(dic,lst[1])
    elif lst[0] == 3:
        display(listt,dic)

listt = []
dic = {}
heapq.heapify(listt)
q = int(input())
for i in range(q):
    accept  = input()
    quer = accept.split()
    quer[0] = int(quer[0])
    if len(quer)>1:
        quer[1]=int(quer[1])
    queryfun(dic,listt,quer)