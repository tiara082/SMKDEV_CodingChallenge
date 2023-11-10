class HappyNumberChecker:
    def __init__(self, n):
        self.n = n
        self.seen_numbers = set()
        self.explanation = f"{n}"

    def check_happiness(self):
        while self.n != 1 and self.n not in self.seen_numbers:
            self.seen_numbers.add(self.n)
            self.n = sum(int(i) ** 2 for i in str(self.n))
            self.explanation += f" + {self.n}"

        return self.n == 1, self.explanation + f" = 1" if self.n == 1 else self.explanation + f" (siklus tidak mencakup 1)"

#  input dari pengguna
input_number = int(input("Input: "))

# mengecek angka bahagia
checker = HappyNumberChecker(input_number)
result, explanation = checker.check_happiness()

#  output 
print(f"Output: {str(result).lower()}")
print(f"Penjelasan : {explanation}")
