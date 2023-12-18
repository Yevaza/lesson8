def summa(N, prices):
    sorted_prices = sorted(prices, reverse=True)
    payment = sum(sorted_prices[i] + sorted_prices[i+1] for i in range(0, N, 3) if i + 2 < N)
    return payment

N = int(input("Количество товаров: "))
prices = list(map(int, input("Стоимости выбранных товаров: ").split()))

result = summa(N,prices)
print("Минимальная сумма денег:",result)