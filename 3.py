def second_index(text, symbol):
    find_symbol = text.find(symbol)

    if find_symbol != -1:
        second_symbol = text.find(symbol, find_symbol + 1)
        if second_symbol != -1:
            return second_symbol
    return None

print(second_index("hi", "h"))  # Виведе: None, оскільки другого входження "h" немає
print(second_index("sims", "s"))  # Виведе: 3, оскільки друге входження "s" на індексі 3
print(second_index("find the river", "e"))  # Виведе: 12, оскільки друге входження "e" на індексі 12
print(second_index("Hello, hello", "lo"))  # Виведе: 10, оскільки друге входження "lo" на індексі 10

