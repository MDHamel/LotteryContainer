from LotteryContainer import LotteryContainer

def test(weights: list[int]):
    LC = LotteryContainer()

    for i, w in enumerate(weights):
        LC.insert(i, w)

    print(LC)

    print("value removed: ", LC.popRandom())

    print(LC)


print("Test 1, middle node removal")
test([1, 1, 1000, 1, 1, 1])

print("Test 2, leaf node removal")
test([1, 1, 1, 1, 1000, 1])

print("Test 3, root removal")
test([1000, 1, 1, 1, 1, 1])

print("Test 2, random")
test([10, 1, 5, 3, 8, 2, 10, 1, 5, 2, 11, 1, 3, 5 , 1])



