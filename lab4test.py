def min_banknotes(n):
    # Номінали купюр, від найбільшої до найменшої
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}

    for d in denominations:
        if n >= d:
            count = n // d     # скільки купюр цього номіналу потрібно
            n = n % d          # залишок суми
            result[d] = count  # записуємо у словник

    return result


# Приклад
n = int(input("Введіть суму премії (грн): "))
res = min_banknotes(n)

print("\nМінімальна кількість купюр:")
total_bills = 0
for denom, count in res.items():
    print(f"{denom} грн — {count} шт.")
    total_bills += count

print(f"\nЗагальна кількість купюр: {total_bills}")
