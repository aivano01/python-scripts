#!/usr/bin/env python3
from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.email())
print(fake.date())
print(fake.company())
print(fake.country())
print(fake.city())
print(fake.job())
print(fake.phone_number())
print(fake.text())
print(fake.url())