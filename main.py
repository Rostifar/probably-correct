import matplotlib.pyplot as plt
import math

class ProbabilityError(Exception):
    pass

def binomial_c(n, k):
    prod = 1.0
    for i in range(1, k + 1):
        prod *= ((n + 1 - i) / i)
    return prod

def factorial(n):
    prod = 1.0
    for i in range(n + 1):
        prod *= (n - i)
    return prod

def approx_factorial(n):
    prod = 1.0
    for i in range(n + 1):
        prod *= ((n / math.exp(1)) ** n) 
    return prod * (math.sqrt(2 * n * math.pi))

class Geometric:
    def __init__(self, p):
        self.p = p
        if p < 0 or p > 1:
                raise ProbabilityError("Probability can only be between 0 and 1.")

    def get_distribution(self):
        return lambda n: ((1 - p) ** n) * p if n >= 0 else \
                    exec('raise(ProbabilityError("Probability can only be between 0 and 1."))')
    def exp(self):
        return 1.0 / p
    def var(self):
        return (1.0 - p) / (p ** 2)


class Binomial:
    def __init__(self, p, n):
        self.p = p
        self.n = n
    
    def get_distribution(self):
        lazy_binomial = lambda k: binomial_c(self.n, k) * (self.p ** k) * \
                ((1 - self.p) ** (self.n - k))
        return lambda k: lazy_binomial(k) if k >= 0 else \
                    exec('raise(ProbabilityError("Probability can only be between 0 and 1."))')

    def exp(self):
        return self.n * self.p
    
    def var(self):
        return self.exp() * (1 - self.p)


class Poisson(self):
    def __init__(self, lam):
        self.lam = lam
    
    def get_distribution(self):
        return lambda k: lazy_binomial(k) if k >= 0 else \
                    exec('raise(ProbabilityError("Probability can only be between 0 and 1."))')

    def exp(self):
        return self.n * self.p
    
    def var(self):
        return self.exp() * (1 - self.p)


# example
N = 100
x = range(N)
y = []

b = Binomial(0.5, 100)
G = b.get_distribution()

#G = geometric(1.0 / 6)
for i in range(100):
    y.append(G(i))
    print("trial: " + str(i))
    print("probability: " + str(G(i)))

plt.plot(x, y)
plt.xlabel("trial")
plt.ylabel("probability")
plt.show()