学习笔记
Trie：
在python 的模板中，一开始没理解这里：
for char in word:
    node = node.setdefault(char, {})

尝试把node和root打印出来后，才发现存储的形式为：{'a': {'b': {'s': {'#': True}}}}， 原因是在setdefault返回的是第二个参数的{}，这里刚好是个字典，node接收到这个字典的地址就等于在里面重新开启一个储存位置紧接着检查下一个，直到遇到end_of_word. 中间不存实际单词，每一层key串起来才是我们要的单词。
总结：每个函数或者方法返回的东东，都要看清楚返回的是值还是其他东西。

并查集：
听超哥讲的有点懵，找到了B站这个视频讲的比较好https://www.bilibili.com/video/BV13t411v7Fs?p=1， 更容易理解。

红黑树和AVL树：
只需要记住概念和重点：
Lookup: AVL > RedBlackTrees
Inter insertion and removal: AVL < RedBlackTrees
store: AVL > RedBlackTrees
AVL used in database where faster retrievals required

位运算常见计算：
XOR - 异或
异或： 相同为0，不同为1. 不进位加法
异或 常见操作特点：
x^0 = x
x^1s = ~x //1s = ~0
x^(~x) = 1s
x^x = 0
c = a^b => a^c = b, b^c = a //交换两个数
a^b^c = a^(b^c) = (a^b)^c //associative

指定位置的位运算
1.将x最右边的n位清零：x & (~0<<n)
2.获取x的第n位值（0或者1）：(x>>n) & 1
3.获取x的第n位的幂值：x & (1<<n)
4.仅将第n位置为1：x | (1<<n)
5.仅将第n位置为0：x & (~(1<<n))
6. 将x最高位至第n位(含)清零：x & ((1<<n)-1)
