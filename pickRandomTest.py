from LotteryContainer import LotteryContainer

def Testing(test_weights, sample_size = 5000000):
    LC = LotteryContainer()
    s = sum(test_weights)

    for i, n in enumerate(test_weights):
        LC.insert(i, n)

    count = [0] * len(LC)

    for i in range(sample_size):
        count[LC.pickRandom()] += 1

    print("\n".join(["{2}: Deviation: {3:.4f} Tested: {0:.4f}, Expected: {1:.4f}".format((x/sample_size) * 100, (test_weights[i]/s) * 100, i, abs((x/sample_size) - (test_weights[i]/s)) * 100) for i, x in enumerate(count)]))

# Testing 1
print("Test 1")
Testing([2, 4, 1, 7, 18, 2, 3, 15, 7, 12])

# Testing 2
print("\nTest 2")
Testing([1, 2, 3, 4, 5, 6, 4, 2, 1])

# Testing 3
print("\nTest 3")
Testing([3, 3, 3])

# Testing 4
print("\nTest 4")
Testing([9, 8, 1, 1, 1])

# Testing 5
print("\nTest 5")
Testing([1, 1, 1, 1, 1, 1, 1, 5])

# Testing 6
print("\nTest 6")
Testing([1])

# Testing 6
print("\nTest 6")
Testing([200, 1])