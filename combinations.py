#Iswarya (13-10-2023) parenthasis combinations
def form_parenthesis(n):
    def backtrack(combination, left, right):
        if len(combination) == 2 * n:
            valid_combinations.append(combination)
            return
        if left < n:
            backtrack(combination + '(', left + 1, right)
        if right < left:
            backtrack(combination + ')', left, right + 1)

    valid_combinations = []
    backtrack('', 0, 0)
    return valid_combinations

n = int(input("Ente n value: "))
valid_combinations = form_parenthesis(n)
for combination in valid_combinations:
    print(combination)

