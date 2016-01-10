#coding:UTF-8
lst = [1,23,45]
lst.append(456)
print lst
print lst.count(1)
lst2 = [4,5,6,7]
#注意和+法有区别，加法不会改变lst本身
print lst+lst2
print lst
#记住这个地方没有返回值
lst.extend(lst2)
print lst
lst[len(lst):] = lst2
print lst
print lst.index(45)
lst.insert(3,'four')
print lst
lst.reverse()
print lst
lst.sort()
print lst
