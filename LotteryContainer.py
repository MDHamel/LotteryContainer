'''
part two:

have container be a tree data structure.
get random number between 1 and self.root.subtree_sum
go through binary tree, selecting item via weighted binary tree method
keep item stored,
update tree: find the leaf on the most weighted tree, keeping track of the path (binary for left and right might be the best method)
place it where item was
update subtree weight and children weight (those effected)

'''
#TODO: adjust weights after insertion, popping, adjusting after pop, adjusting weight after swap

from random import randint
from collections import deque

class WeightedNode:
    def __init__(self, value: any, weight: int):
        self.value = value
        self.weight = weight

        self.left = None
        self.right = None
        
        self.subtree_weight = weight

    def __str__(self):
        return "(Value: {0}, Weight: {1}, Subtree_Weight:{2})".format(self.value, str(self.weight), str(self.subtree_weight))


class LotteryContainer:
    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def insert(self, item: any, weight: int):
        new_node = WeightedNode(item, weight)

        if not self.root:
            self.root = new_node
        else:
            self._insert_balance(self.root, new_node)

        self.count += 1

    def _insert_balance(self, curr_node, new_node):
        left_weight = curr_node.left.subtree_weight if curr_node.left else 0
        right_weight = curr_node.right.subtree_weight if curr_node.right else 0

        curr_node.subtree_weight += new_node.weight

        if left_weight <= right_weight:
            if not curr_node.left:
                curr_node.left = new_node
            else:
                self._insert_balance(curr_node.left, new_node)
        else:
            if not curr_node.right:
                curr_node.right = new_node
            else:
                self._insert_balance(curr_node.right, new_node)

    def popRandom(self):
        rand_num = randint(1, self.root.subtree_weight)
        path = []
        selected_node = self._select_node_by_weight(rand_num, self.root, path)

        value = selected_node.value

        # pop last item which is the selected node as it will be appended
        # again during _
        path.pop()
        self._remove_node(selected_node, path)

        self.count -= 1

        return value

    def _remove_node(self, node, path):
        value_to_remove = node.weight
        node_swapped = False

        leaf = self._get_leaf_node(node, path)

        for i, n in enumerate(path):
            cur_node = n
            if i == len(path) - 1:
                if cur_node.left == leaf:
                    cur_node.left = None
                elif cur_node.right == leaf:
                    cur_node.right = None

            if cur_node == node and cur_node != leaf:
                leaf.left = cur_node.left
                leaf.right = cur_node.right

                if i > 0:
                    parent = path[i - 1]
                    if parent.left == cur_node:
                        parent.left = leaf
                    else:
                        parent.right = leaf
                else:
                    cur_node.value = leaf.value
                    cur_node.weight = leaf.weight
                node_swapped = True
                cur_node.subtree_weight = node.subtree_weight - value_to_remove
            else:
                cur_node.subtree_weight -= leaf.weight if node_swapped else value_to_remove

        del node 

    def _get_leaf_node(self, curr_node:WeightedNode, path: list[WeightedNode]):
        if not curr_node.left and not curr_node.right:
            return curr_node
        path.append(curr_node)
        left_weight = curr_node.left.subtree_weight if curr_node.left else 0
        right_weight = curr_node.right.subtree_weight if curr_node.right else 0
        
        if left_weight <= right_weight or (curr_node.left and not curr_node.right):
            return self._get_leaf_node(curr_node.left, path)
        else:
            return self._get_leaf_node(curr_node.right, path)

    def pickRandom(self):
        rand_num = randint(1, self.root.subtree_weight)

        path = []
        selected_node = self._select_node_by_weight(rand_num, self.root, path)

        return selected_node.value
    
    def _select_node_by_weight(self, target: int, node: WeightedNode, path: list[WeightedNode] | None = None):
        if isinstance(path, list):
            path.append(node)

        left_weight = node.left.subtree_weight if node.left else 1

        if target <= left_weight and node.left:
            return self._select_node_by_weight(target, node.left, path)
        elif target <= left_weight + node.weight:
            return node
        elif node.right: 
            return self._select_node_by_weight(target - left_weight - node.weight, node.right, path)

    def __str__(self):
        queue = deque([self.root])
        result = []
        height = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(str(node))
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append("\n")
            height += 1
        
        return ''.join(result)
    
