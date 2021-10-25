# O(1)

def O1(numbers):
    return numbers[0]

# O(log(n))
def func(n):
    if n<= 1:
        return
    else:
        print(n)
        func(n/2)

# func(10)


# O(n)
def func2(numbers):
    for num in numbers:
        print(num)

# func2([1,2,3,4,5])

# O(n * log(n))
def func3(n):
    for i in range(int(n)):
        print(i, end=" ")
    print()
    if n <= 1:
        return
    else:
        func3(n/2)

# func3(10)

# O(n**)
def func5(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()

func5([1,2,3,4,5])

# O表記をみたらだいたいどんな構造化わかる
