'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''


class Exercice20:
    def divisible_by_7(self, n):
        for i in range(0, n + 1):
            if i % 7 == 0:
                yield i


ex = Exercice20()
for i in ex.divisible_by_7(100):
    print(i)
