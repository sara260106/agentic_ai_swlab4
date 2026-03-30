# -------------------------------
# TOOLS
# -------------------------------

def extract_numbers(text):
    words = text.split()
    numbers = [int(word) for word in words if word.isdigit()]
    return numbers


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def summarize_result(result):
    return f"The average value is {result}."
