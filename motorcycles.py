#修改列表中元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#列表中添加元素
motorcycles.append('ducati2')
print(motorcycles)
#列表中插入元素
motorcycles.insert(0,"benchi")
print(motorcycles)
#从列表中删除元素
#使用del 删除指定位置元素
del motorcycles[0]
print(motorcycles)
#使用pop并返回被删除的元素（默认弹出最后一个） 先进后出
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#使用pop删除指定元素
first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)
#remove根据值删除元素(只根据值删除一次)
remove_element=motorcycles.remove("yamaha")
print(remove_element)
print(motorcycles)