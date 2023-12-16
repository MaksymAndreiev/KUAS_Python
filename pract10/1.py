def total(numbers):
    return sum(numbers)


def cumulative(numbers):
    return [total(numbers[:i + 1]) for i in range(len(numbers))]


def nested_sum(n):
    return n if isinstance(n, int) else total(
        [nested_sum(i) for i in n if isinstance(i, int) or isinstance(i, list)]) if isinstance(n, list) else 0


print(total([1, 1, 1, 1, 1]))
print(total([1, 2, 3, 4, 5]))
print(total(range(10)))
print('-' * 30)

print(cumulative([]))
print(cumulative([1]))
print(cumulative([1, 2, 3, 4, 5]))
print(cumulative(range(10)))
print('-' * 30)

print(nested_sum([None, 1, [2, "two", [[[[3, False, 4]]]], []], 5]))
print('-' * 30)


def isordered(l):
    return l == sorted(l)


print(isordered([]))  # True
print(isordered([1, 1, 1]))  # True
print(isordered([1, 2, 3]))  # True
print(isordered([1, 3, 2]))  # False
print(isordered([2, 1, 3]))  # False
print(isordered([[1], [2]]))  # True
print(isordered([[2], [1]]))  # False
print(isordered(["any", "body", "can", "dance", "even", "fred"]))  # True
print('-' * 30)


def is_anagram(string1, string2):
    return all([char in string2 for char in string1])


print(is_anagram("tone", "note"))
print(is_anagram("chemical", "alchemic"))
print(is_anagram("detail", "dilate"))  # True
print(is_anagram("angered", "enraged"))  # True
print(is_anagram("tangled", "tingled"))  # False
print(is_anagram("goat", "boat"))
