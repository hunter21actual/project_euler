n = 100

def sos(n):
    return int(n * (n + 1) * (2*n + 1) / 6)

def sqs(n):
    return (int(n * (n + 1) / 2)) ** 2

print(sqs(10)-sos(10))
