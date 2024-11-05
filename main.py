from pass_generator import generate_password, Complexity

passwd = generate_password(12, Complexity.MEDIUM)
print(passwd)
