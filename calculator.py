#!/usr/bin/env python3
"""
Командный калькулятор
Каждый участник добавляет свою функцию
"""

def main():
    print("Добро пожаловать в командный калькулятор!")
    print("Доступные операции:")
    print("1. Сложение (add)")
    print("2. Вычитание (subtract)")
    print("3. Умножение (multiply)")
    print("4. Деление (divide)")
    print("5. Выход")
    
    while True:
        try:
            choice = input("\nВыберите операцию (1-5): ")
            
            if choice == '5':
                print("До свидания!")
                break
                
            if choice in ['1', '2', '3', '4']:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                
                if choice == '1':
                    from operations import add
                    result = add(a, b)
                    print(f"Результат: {a} + {b} = {result}")
                elif choice == '2':
                    from operations import subtract
                    result = subtract(a, b)
                    print(f"Результат: {a} - {b} = {result}")
                elif choice == '3':
                    from operations import multiply
                    result = multiply(a, b)
                    print(f"Результат: {a} * {b} = {result}")
                elif choice == '4':
                    from operations import divide
                    result = divide(a, b)
                    print(f"Результат: {a} / {b} = {result}")
            else:
                print("Неверный выбор. Попробуйте снова.")
                
        except ValueError:
            print("Ошибка: введите число!")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()