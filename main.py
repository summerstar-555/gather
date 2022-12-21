# 集合的特点：数据无法重复，下标无序。因此无法通过下标访问
# 虽然定义空集合也是使用花括号，但是在花括号前需使用set函数用来区分字典。
# 定义方式
# 1

"""
set1 = set()
set2 = {1,2,3} #这里必须写存放数据，否则类型为字典
print("set1是一个集合，它的类型是：",type(set1))
print("set2是一个集合，它的类型是：",type(set2))
"""

# 添加元素
"""
set1.add("code")
print(set1)
"""

# 移除
"""
set1.remove("code")
print(set1)
"""

# 随机取出一份元素
"""
set1 = {1,2,3,4}
ret = set1.pop()
print(set1)
"""

# 集合1.difference（集合2） — 取出集合1里集合2没有的元素
"""
set1 = {1,5,6}
set2 = {1,2,3}
print(set1.difference(set2))
"""

# 消除交集 - 集合1发生改变，2不会
"""
set1 = {1,5,6}
set2 = {1,2,3}
set1.difference_update(set2)
print(set1)
"""

# 集合合并
"""
set1 = {1,5,6}
set2 = {1,2,3}
print("合并后的结果为:",set1.union(set2))
"""
