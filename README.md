# Lottery Container

## Part I: 

Make a container object that stores items. have two methods: insert(item) and popRandom().

**insert(type item)** -   Should take in one item of <type>. Lets say this can be of any type if your language allows otherwise use a Template/Generic.

**popRandom()** - This method should take an item at a random index, remove the item from the array, and return it's value.


**Follow up**:  
What is the time complexity for these two methods? Is it possible to get both methods to 
O(1) complexity?

**Notes:**
There can be duplicate values.


**Example:**

LC = LottoContainer()  
LC.insert("apple")  
LC.insert("orange")  
LC.insert("banana")  
print(LC.popRandom())   # > orange  
print(LC.popRandom())   # > apple  

The item to be printed could be any of the items in the list as they all have an equal chance.


## Part II:

Same as part one, however, now the items are to be weighted for the randomPop() method. The methods\
will change to the following:

insert(Type item, int weight) -  The object will now take in an item with a 'weight'. The weight
will contribute to how likely it is to be selected for popRandom().

popRandom() - Using the weights to skew results, pop a random item, remove the item from the array, and return it's value. 


**Follow up**:  
What is the time complexity for these two methods? 

**Notes:**
There can be duplicate values and weights.


**Example:**

LC = LottoContainer()  
LC.insert("apple", 15)  
LC.insert("orange", 1)  
LC.insert("banana", 4)  
print(LC.popRandom())   # > apple  
print(LC.popRandom())   # > banana  

The items in the list are now weighted, this means that on the firs popRandom() each item has the following chances:

* "apple"   - 15 out of 20 -> 75%
* "orange"  - 1 out of 20 -> 5%
* "banana"  - 4 out of 20 -> 20%

and on the second:

* "orange"  - 1 out of 5 -> 20%
* "banana"  - 4 out of 5 -> 80%

Note that these are still random, so while it is possible to get orange on your first try, it is unlikely.
