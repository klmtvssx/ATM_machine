
balance = 10000

print("Саламатсызбы!")
print(f"Балансыңызда {balance} сом бар.")

amount = int(input("Канча сумма аласыз? "))

if amount > balance:
    print("Кечиресиз, балансыңызда жетишсиз сумма.")
else:
    balance -= amount
    print(f"Сиз {amount} сом алдыңыз.")
    print(f"Калган балансыңыз: {balance} сом.")

print("Саламатта калыңыз!")
