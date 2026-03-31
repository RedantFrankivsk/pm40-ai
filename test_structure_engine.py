import random
from description_builder import DescriptionBuilder


prices = [100]

for i in range(50):
    prices.append(prices[-1] + random.uniform(-1, 1))

volumes = [random.uniform(100, 200) for _ in range(50)]


builder = DescriptionBuilder()

description = builder.build(prices, volumes)

print("DESCRIPTION:")
print(description)