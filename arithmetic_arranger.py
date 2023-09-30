def arithmetic_arranger(problems, bln=False):
    arranged_problems = ""
    upper_row = ""
    lower_row = ""
    lines = ""
    final_row = ""
    # Checking if the problems exceed the limit
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    operator = list(map(lambda x: x.split()[1], problems))
    # Checking for input errors
    if set(operator) != {"-", "+"} and len(set(operator)) != 1:
        equations = "Error: Operator must be '+' or '-'."
        return equations

    numbers = []
    for number in problems:
        number = number.split()
        numbers.extend([number[0], number[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems    
    
    result = list(map(lambda x: eval(x), problems))
    for i in range(0, len(numbers), 2):
        distance = max(len(numbers[i]), len(numbers[i + 1])) + 2
        upper_row += numbers[i].rjust(distance)
        lines += '-' * distance
        final_row += str(result[i // 2]).rjust(distance)
        if i != len(numbers) - 2:
            upper_row += " " * 4
            lines += " " * 4
            final_row += " " * 4
    for i in range(1, len(numbers), 2):
        distance = max(len(numbers[i - 1]), len(numbers[i])) + 1
        lower_row += operator[i // 2]
        lower_row += numbers[i].rjust(distance)
        if i != len(numbers) - 1:
            lower_row += ' ' * 4

    if bln:
        arranged_problems = "\n".join((upper_row, lower_row, lines, final_row))
    else:
        arranged_problems = "\n".join((upper_row, lower_row, lines))
    return arranged_problems