def check_num(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def first_n_primes(n=10):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum_100():
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1
    return total

def test_check_num():
    assert check_num(1) == "Positive"
    assert check_num(-1) == "Negative"
    assert check_num(0) == "Zero"

def test_first_n_primes():
    assert first_n_primes(5) == [2, 3, 5, 7, 11]
    assert first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_100():
    assert sum_100() == 5050