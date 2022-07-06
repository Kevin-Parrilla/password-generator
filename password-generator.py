from enum import auto
import string, random

auto_gen_pass = []

for i in range(5):
    auto_gen_pass.append(random.choice(string.ascii_letters))
    auto_gen_pass.append(random.choice(string.punctuation))
    auto_gen_pass.append(random.choice(string.digits))

print(''.join(auto_gen_pass))