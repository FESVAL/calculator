if __name__ == "__main__":
  text=int(input("Введи дію, використовуючи відповідно число: 1 - Додавання, 2 - Віднімання, 3 - Множення, 4 - Ділення\n"))
print(text)  
number1=float(input("Введи перше число:")) 
number2=float(input("Введи друге число:"))
if text==1:
  result=number1+number2
  print(f"Сума чисел {number1} та {number2} дорівнює: {result}")
elif text==2:
  result=number1-number2
  print(f"Різниця числа {number1} та числа {number2} дорівнює: {result}")
elif text==3:
  result=number1*number2
  print(f"Множина чисел {number1} та {number2} дорівнює: {result}")
elif text==4:
  result=number1/number2
  print(f"Частка числа {number1} та числа {number2} дорівнює: {result}")
else:
  print('Перевір,яку дію ввів, я таку не знаю')