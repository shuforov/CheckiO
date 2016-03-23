#/home/Dump/.git-credential-cache
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return None


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return None

print max(3, 2) == 3, "Simple case max"
print min(3, 2) == 2, "Simple case min"

# print max(3, 2) == 3, "Simple case max"
# print min(3, 2) == 2, "Simple case min"
# print max([1, 2, 0, 3, 4]) == 4, "From a list"
# print min("hello") == "e", "From string"
# print max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
# print min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"