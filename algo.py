#Random arrow selector
import random
import numpy as np

def random_arrow():

    a = random.random()
    if a <= 0.25:
        b = 0
    elif a <= 0.5:
        b = 1
    elif a <= 0.75:
        b = 2
    else:
        b = 3
    return a, b

ans = []
for i in range(100):
    _, b = random_arrow()
    ans.append(b)

val, count = np.unique(ans, return_counts=True)
count_a = count/np.sum(count)


## Bubble sort implementation
def bubb(array):
    op = 0
    checks = 0
    arr_size = len(array)-1
    swapp = True
    while swapp:

        swapp = False
        for i in range(arr_size):
            checks += 1
            if array[i] > array[i+1]:
                temp = array[i] 
                array[i] = array[i+1]
                array[i+1] = temp
                swapp = True
                op += 1
                checks += 1
        arr_size -= 1
            
    return array, op, checks

import numpy as np

a = np.random.randint(50, size=(1,10))
a = a[0].tolist()
#print(a)
#print(bubb([100, 90,80, 70 ,60 ,50,40,30,20,10]))
#Worst case n * (n-1) = n**2 - n
#Best case n-1 = n


def selection_sort(array):
    #Selection sort algo: parses through array and finds lowest element, setting it to its position
    compar = 0
    swaps = 0
    print(array)
    #parse through list n times
    for j in range(len(array)-1):
        minimum = array[j]
        swapp = False
        #parse through list to check numbers
        for i in range(j+1, len(array)):
            #compares to min
            compar += 1
            if minimum > array[i]:
                minimum = array[i]
                index = i
                swapp = True

        #swaps values
        if swapp is True:
            swaps += 1
            tmp = array[index]
            array[index] = array[j]
            array[j] = tmp
        print(array)
    return array, compar, swaps
        
#print(selection_sort([70, 40, 69, 80, 12, 14, 34]))




def algo_nn(n):
    cont = 0
    for i in range(n):
        for i in range(2*i):
            cont += 1
    return cont

ans = []
x = []
for i in range(1,10):
    x.append(i)
    ans.append(algo_nn(i))

# import matplotlib.pyplot as plt

# plt.plot(x, ans)
# plt.show()

def algo_v(v):
    ## Given v, find the sequences of numbers that reaches its value
    seqs = []

    for i in range(1,v+1):
        seq = []
        sum = i
        seq.append(i)

        for j in range(1+i,v+2):

            if sum < v:
                sum += j
                seq.append(j)

            elif sum == v:
                seqs.append(seq)
                break              

    return seqs

#print(algo_v(15))


#Implement an array

class Arrayy():
    def __init__(self):
        self.data = []
        self.count = 0

    def add(self, el):
        self.data = self.data + [el]
        self.count += 1

        return self.data

    def get(self, idx:int):
        if idx <= count:
            return self.data[idx]
        else: 
            return IndexError

    def set(self, idx:int, el:int):
        self.data[idx] = el
        return self.data
    
    def remove(self, el:int):
        found = False
        idx = 0
        for idx in range(self.count):

            if self.data[idx] == el:
                found = True
                break

        if found:
            if idx != self.count-1:
        
                for _ in range(self.count - 1):
                    self.data[idx] = self.data[idx+1]
            self.data = self.data[:self.count-1]
            self.count -= 1

        return self.data

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def size(self):
        return self.count
    
    def contains(self, el:int):
        for elem in range(self.count):
            if self.data[elem] == el:
                return True
        
        return False

    def indexOf(self, el:int):

        for elem in range(self.count):

            if self.data[elem] == el:
                return elem

    def clear(self):
        self.data = []
        return self.data
    
    def add_idx(self, el:int, idx:int=None):

        self.data = self.data + [self.data[-1]]

        for elem in range(self.count-1, idx-1, -1):
            self.data[elem] = self.data[elem-1]

        self.data[idx] = el
            
        return self.data

# arr = Arrayy()

# print(arr.add(69))

# print(arr.add(68))

# print(arr.set(1, 6969))

# print(arr.add(696969))

# print(arr.remove(696969))

# print(arr.remove(69))

# print(arr.isEmpty())

# arrey = Arrayy()

# print(arrey.isEmpty())

# print(arr.size())

# print(arrey.size())

# print(arr.contains(6969))

# print(arr.contains(69))

# print(arr.indexOf(6969))

# #print(arr.clear())
# print(arr.add(69))

# print(arr.add(68))

# print(arr.add(696969))

# print(arr.add_idx(404, 0))

# import time
# import math

# num_of_homes = int(input(""))
# secs = time.time()
# cities = []
# home_round_cons = []
# city = 0

# while num_of_homes > 0:

#     city += 1
#     homes = {}
#     cons_tot = 0
#     num_people_city = 0
    
#     for _ in range(num_of_homes):

#         peop_cons = str(input("")).split()
#         num_people, consumption = int(peop_cons[0]), int(peop_cons[1])
#         round_consump = consumption // num_people
#         cons_tot += consumption
#         num_people_city += num_people

#         if homes.get(round_consump):
#             homes[round_consump] +=  num_people
#         else: 
#             homes[round_consump] =  num_people
    
#     sorted_homes = dict(sorted(homes.items()))
#     cons_med = cons_tot / num_people_city
#     cities.append([city, cons_med])
#     home_round_cons.append(sorted_homes)
#     num_of_homes = int(input(""))

# for i in range(len(home_round_cons)):
#     print(f"Cidade# {cities[i][0]}:")

#     for k, v in home_round_cons[i].items():
#         print(f"{v}-{k}", end=" ")

#     if i < len(home_round_cons)-1:
#         print(f"\nConsumo medio: {math.floor(cities[i][1]*100)/100.0:.2f} m3.\n")
#     else:
#         print(f"\nConsumo medio: {math.floor(cities[i][1]*100)/100.0:.2f} m3.")

# secs2 = time.time()
# print(f"Tempo total em segundos: {secs2-secs:.2f}")

# class Node:
#     def __init__(self, el):
#         self.el = el
#         self.next = None
    
#     def __repr__(self):
#         return self.el 

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0

#     def add_first(self, node):
#         node.next = self.head
#         self.head = node
#         self.tail = node.next
#         print(f"tail: {self.tail}")
    
#     def add_last(self, node):
#         #We must iter
#         return 


#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.el)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)

# link_list = LinkedList()
# print(link_list)

# link_list.add_first(Node("A"))
# print(link_list)

# link_list.add_first(Node("B"))
# print(link_list)


# import sys 

# num_part = []
# part = []
# for line in sys.stdin:
#     try:
#         temp = int(line.rstrip())
#         if 0 == temp:
#             break
#         num_part.append(temp)

#     except ValueError:
#         name, n = line.split()
#         part.append([name, n])

# winners = []
# game_num = 0
# for i in range(len(num_part)):
#     num_players = num_part[i]
#     players = part[game_num:game_num+num_players]
#     game_num += num_players

#     game = []
#     names = []
#     for j in range(len(players)):
#         game.append(players[j][1])
#         names.append(players[j][0])


#     new_runs = None
#     for _ in range(len(game)):
#         if len(game) == 1:
#             winners.append(names[0])
#             break
#         if new_runs is None:
#             runs = int(game[0])
#         else:
#             runs = int(new_runs)

#         if runs % 2 == 0:

#             lost = runs % len(game)
#             new_runs = game[lost]
#             print(names)
#             del game[lost]
#             del names[lost]
#             print(names)

#         else:

#             new_g = game[::-1]

#             lost = (runs % len(new_g)) 
#             real_lost = len(game) - lost
#             new_runs = game[real_lost]

#             print(names)
#             del game[real_lost]
#             del names[real_lost]
#             print(names)


# print(winners)




# par = impar = 0
# for i in range(5):
#     if i%2 == 0:
#         par += i
#     else:
#         impar += i
# print(par, impar)



class Node():
    def __init__(self, el):
        self.el = el
        self.next = None
    
    def __repr__(self) -> str:
        return self.el



class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0
    

    def add_first(self, node):
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.counter += 1

    def add_last(self, node):
        last_node = self.tail
        last_node.next = node
        self.tail = node
        node.next = None
        self.counter += 1


    def get_idx(self, idx):
        if idx == 0:
            return self.head
        elif idx == self.counter - 1:
            return self.tail
        else:
            i = 0
            node = self.head
    
            while node is not None:
                print(f"idx: {idx}, node: {node}, next: {node.next}, i: {i}")
                if i == idx:
                    return node #, node.next
                node = node.next
                i += 1
            
    def get_idx_aft(self, idx):
        if idx == 0:
            return self.head
        elif idx == self.counter - 1:
            return self.tail
        else:
            i = 0
            node = self.head
    
            while node is not None:
                print(f"idx: {idx}, node: {node}, next: {node.next}, i: {i}")
                if i == idx-1:
                    return node
                node = node.next
                i += 1

    def add_mid_after(self, node, idx):
        if idx < 0 or idx >= self.counter - 1:
            raise IndexError
        else:
            node_before = self.get_idx(idx)
            node.next = node_before.next
            node_before.next = node
            self.counter += 1

    def add_mid_bef(self, node, idx):
        if idx <= 0 or idx >= self.counter:
            return IndexError
        else:
            node_aft = self.get_idx_aft(idx)
            node.next = node_aft.next
            node_aft.next = node
            self.counter += 1
            

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.el)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    

# ll = LinkedList()
# print(ll)

# ll.add_first(Node('B5'))
# print(ll)

# ll.add_first(Node('A'))
# print(ll)

# ll.add_last(Node('C'))
# print(ll)

# ll.add_mid_after(Node('B1'), 0)
# print(ll)

# ll.add_mid_after(Node('B2'), 1)
# print(ll)

# ll.add_mid_bef(Node('B3'), 3)
# print(ll)

# ll.add_mid_bef(Node('B4'), 4)
# print(ll)


class DoubleLinkedList:
    def __init__(self) -> None:
        self.header = None
        self.trailer = None
        self.count = 0

    def add_last(self, node):
        
        if self.count == 0:
            self.header = node
            self.trailer = node

        else:
            temp = self.trailer
            self.trailer = node
            temp.next = node

        self.count += 1
        

    def add_first(self, node):
    
        if self.count == 0:
            self.header = node
            self.trailer = node

        else:
            temp = self.header
            self.header = node
            node.next = temp
            
        self.count += 1

    def __repr__(self):

        if self.count > 0:
            nodes = []
            node = self.header
            while node != self.trailer:
                nodes.append(node.el)
                node = node.next 
            nodes.append(node.el)
            nodes.append("None")
            return " -> ".join(nodes) + " ||| header is: " + str(self.header.el) + " trailer is: " + str(self.trailer.el) + " count is: " + str(self.count)
 
        else:
            return "DLL is empty"


# dll = DoubleLinkedList()
# print(dll)
# dll.add_last(Node('A'))
# print(dll)
# dll.add_last(Node('B'))
# print(dll)

# dll.add_first(Node('A1'))
# print(dll)
# dll.add_first(Node('A0'))
# print(dll)

## -------------------------
# Stack (pilha)
class Stack:
    def __init__(self):
        self.top = None
        self.__size = 0

    def push(self, Node):
        Node.next = self.top
        self.top = Node
        self.__size = self.__size + 1

    def pop(self):
        if self.__size > 0:
            node = self.top
            self.top = self.top.next
            self.__size = self.__size - 1
        else:
            raise IndexError
        return node

    def peek(self):
        if self.__size > 0:
            return self.top.el
        else:
            raise IndexError
        
    def __repr__(self):
        pointer = self.top
        r = ""
        while(pointer):
            r = r + str(pointer.el) + '\n'
            pointer = pointer.next
        
        return r

# pilha = Stack()
# print(pilha)
# pilha.push(Node(69))
# #print(pilha)
# pilha.push(Node('mAH OI'))
# pilha.push(Node('AAAAOI'))
# pilha.pop()
# print(pilha)

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.__size = 0

    def push(self, node):
        if self.last:
            self.last.next = node
            self.last = node

        else:
            self.last = node

        self.__size = self.__size + 1

        if self.first is None:
            self.first = node

    def pop(self):
        if self.__size > 0:
            self.first = self.first.next
            self.__size = self.__size - 1
            return self.first.el
        else:
            raise IndexError
    
    def peek(self):
        if self.__size > 0:
            return self.first.el
        else:
            raise IndexError
        
    def __repr__(self) -> str:
        if self.__size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.el) + " "
                pointer = pointer.next
            return r
        
        raise IndexError

# fila = Queue()
# fila.push(Node(1))
# fila.push(Node('69'))
# fila.push(Node('oI'))
# print(fila)
# fila.pop()
# print(fila)


# def remove(list, el):
#     cap = list.capacity
#     found = -1
#     if list.size > 4:
#         for i in range(list.size):
#             if el == list[i]:
#                 found = i
            
#         if found != -1:
#             for j in range(found, list.size-1):
#                 list[j] = list[j+1]
            
#             list = list[:list.size-1]
#             list.size -= 1

#             if list.size / cap < 0.25:
#                 if list.capacity / 2 < 4:
#                     list.capacity = 4
#                 else:
#                     list.capacity = list.capacity / 2
    
#     else:
#         raise IndexError
def add(self, el):
    self.data = self.data + [el]
    self.count += 1   


def toarray(llist):
    arr = []
    arr.size = 0
    pointer = llist.head
    while(pointer):
        arr.add(pointer.data)

    return arr
