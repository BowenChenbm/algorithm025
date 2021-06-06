学习总结和笔记:

这周内容主要以熟悉实例为主，准备结课了，加油！！

布隆过滤器 Python 实例
# Python
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
    def __init__(self, size, hash_num):
        self.size = size 		
        self.hash_num = hash_num 		
        self.bit_array = bitarray(size) 		
        self.bit_array.setall(0) 

    def add(self, s): 		
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size 			
            self.bit_array[result] = 1 

    def lookup(self, s): 		
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size 			
                if self.bit_array[result] == 0: 				
                return "Nope" 		
        return "Probably" 

bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 

LRU Cache 实例:
class LRUCache(object):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict() 		
        self.remain = capacity

    def get(self, key): 		
        if key not in self.dic: 			
            return -1 		
        v = self.dic.pop(key) 		
        self.dic[key] = v   # key as the newest one 		
        return v 

    def put(self, key, value): 		
        if key in self.dic: 			
            self.dic.pop(key) 		
        else: 			
            if self.remain > 0: 				
                self.remain -= 1 			
            else:   # self.dic is full				
                self.dic.popitem(last=False) 		
            self.dic[key] = value

排序：
排序分类，比较类排序 和 非比较类排序， 重点掌握快速排序，归并排序，以及堆排序。

快排：
#Python
def quick_sort(begin, end, nums):    
    if begin >= end: return    
    pivot_index = partition(begin, end, nums)    
    quick_sort(begin, pivot_index-1, nums)    
    quick_sort(pivot_index+1, end, nums)    

def partition(begin, end, nums):    
    pivot = nums[begin]    
    mark = begin    
    for i in range(begin+1, end+1):        
        if nums[i] < pivot:            
            mark +=1            
            nums[mark], nums[i] = nums[i], nums[mark]    
    nums[begin], nums[mark] = nums[mark], nums[begin]    
    return mark

归并：
#Python
def mergesort(nums, left, right):    
    if right <= left: return    
    mid = (left+right) >> 1    
    mergesort(nums, left, mid)    
    mergesort(nums, mid+1, right)    
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):    
    temp = []    
    i, j = left,  mid+1   
    while i <= mid and j <= right:        
        if nums[i] <= nums[j]:            
            temp.append(nums[i])            
            i +=1        
        else:            
            temp.append(nums[j])            
            j +=1    
    while i<=mid:        
        temp.append(nums[i])        
        i +=1   
    while j<=right:        
        temp.append(nums[j])        
        j +=1    
    nums[left:right+1] = temp

堆排：
#Python
def heapify(parent_index, length, nums):    
    temp = nums[parent_index]    
    child_index = 2*parent_index+1    
    while child_index < length:        
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:            
            child_index = child_index+1        
        if temp > nums[child_index]:            
            break        
        nums[parent_index] = nums[child_index]        
        parent_index = child_index        
        child_index = 2*parent_index + 1    
    nums[parent_index] = temp

def heapsort(nums):    
    for i in range((len(nums)-2)//2, -1, -1):        
        heapify(i, len(nums), nums)    
    for j in range(len(nums)-1, 0, -1):        
        nums[j], nums[0] = nums[0], nums[j]        
        heapify(0, j, nums)

动规总结：
动规和递归/分治 没有本质的区别，关键看有无最优子结构，都是要找重复子问题，差异性为最优子结构，中途淘汰次优解。
动态方程经验：一维困难一般升二维，二维困难升三维，以此类推
