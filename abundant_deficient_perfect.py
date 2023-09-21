def sum_of_divisors(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i) == 0:
            divisors.append(i)
    return sum(divisors)

def decide(number):
    div_sum = sum_of_divisors(number)
    if div_sum == number:
        return f"{number} is a perfect number."
    elif div_sum > number:
        return f"{number} is abundant."
    elif div_sum < number:
        return f"{number} is deficient."


