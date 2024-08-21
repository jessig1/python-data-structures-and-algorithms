all elements represented hierarchically
parent node greater than children and descendants
right/left don't mater
use arrays to represent parent/child relationship with indexes
left_child_index = 2 * parent_index + 1
right_child_index = 2 * parent_index + 2
parent_index = (child_index -1)/2
