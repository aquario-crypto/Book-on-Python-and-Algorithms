## sorting and searching

<br>

* **inversions** in a sequence is a pair of elements that are out of order with respect to the ordering relation. a sorting algorithm is a sequence of operations that reduces inversions to zero.
* a **topological sort** of a diretect graph is a way of ordering the list of nodes such that if `(a, b)` is a edge of the graph, then `a` appears before `b`. it does not work if a graph has cycles or is not directed.


<br>

----

### `sorting_algorithms.py`

<br>

```python
> python3 sorting_algorithms.py


Array: [3, 5, 1, 2, 10, 6]
Testing merge sort: [1, 2, 3, 5, 6, 10]
Testing quick sort: [1, 2, 3, 5, 6, 10]
```

<br>

### `binary_search.py`

<br>

```python
> python binary_search.py
Recursive:  6
Iterative:  6
```
