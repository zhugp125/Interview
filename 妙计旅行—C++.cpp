1.vector resize 和 reserve 的区别
resize 设置vector的长度，调用resize函数之后，所有的空间都已经初始化，可以直接访问
reserve 预分配vector的存储空间，调用reserve函数，预分配出的空间没有被初始化，不可访问

2.map unordered_map实现机制和区别
实现机制：
  map              红黑树
  unordered_map    哈希表
  
区别：
  map              有序
  unordered_map    无序
  
优缺点：
  map
    优点：1.有序性 2.高效性
	缺点：1.空间占用率高
  unordered_map
    优点：1.查找速度快
	缺点：1.哈希表的建立比较费时间s