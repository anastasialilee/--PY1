def get_random_password(n=8) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    import random
    password = random.sample(alphabet, n)
    return password


print(get_random_password())
