# Lottery Container

## Part I

Create a container object that can store items and provide two methods: `insert(item)` and `popRandom()`.

- **`insert(item)`** - Takes in one item of any type. If your language supports any data type, you can accept items of any type; otherwise, use a Template/Generic type.

- **`popRandom()`** - Removes an item from a random index in the array and returns its value.

### Follow-Up

What is the time complexity of these two methods? Is it possible to achieve O(1) complexity for both methods?

### Notes

- Duplicate values are allowed.



**Example:**
```python
LC = LottoContainer()  
LC.insert("apple")  
LC.insert("orange")  
LC.insert("banana")  
print(LC.popRandom())   => "orange"
print(LC.popRandom())   => "apple"
```

The item to be printed could be any of the items in the list as they all have an equal chance.


## Part II

Similar to Part I, but now items have weights for the `popRandom()` method. The methods are updated as follows:

- **`insert(item, weight)`** - Takes an item along with an integer `weight`. The `weight` influences the likelihood of the item being selected by `popRandom()`.

- **`popRandom()`** - Pops a random item based on its `weight`, removes it from the array, and returns its `value`.

### Follow-Up
What is the time complexity of these two methods?

### Notes

- Duplicate values and/or weights are allowed.
- Weights are always greater than 0.


**Example:**
```python
LC = LottoContainer()  
LC.insert("apple", 15)  
LC.insert("orange", 1)  
LC.insert("banana", 4)  
print(LC.popRandom())   => "apple"  
print(LC.popRandom())   => "banana" 
```
The items in the list are now weighted, this means that on the first popRandom(), each item has the following chances:

* "apple"   - 15 out of 20 => 75%
* "orange"  - 1 out of 20 => 5%
* "banana"  - 4 out of 20 => 20%

and on the second:

* "orange"  - 1 out of 5 => 20%
* "banana"  - 4 out of 5 => 80%

Note that these are still random, so while it is possible to get orange on your first try, it is unlikely.
