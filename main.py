import random, time
import tabulate

def ssort(L):
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L

def qsort(a, pivot_fn):
    ## TO DO
    if len(a) == 0:
        return a
    
    piv_point = pivot_fn(a)
    left = []
    right = []
    for i in a:
        if i < piv_point:
            left.append(i)
        elif i > piv_point:
            right.append(i)
    
    l_sort = qsort(left, pivot_fn)
    r_sort = qsort(right, pivot_fn)
    
    return l_sort + [piv_point] * a.count(piv_point) + r_sort
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[1, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda a: a[0]
    qsort_random_pivot = lambda a: random.choice(a)
    tim_sort = lambda a: sorted(a)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist),
            time_search(ssort, mylist),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim_sort', 'ssort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()

