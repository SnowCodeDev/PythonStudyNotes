# 计算器 Calculator

def calculator():
    print("简易计算器 / Simple Calculator")
    print("=" * 30)
    print("操作符 / Operators:")
    print("+ : 加法 / Addition")
    print("- : 减法 / Subtraction")
    print("* : 乘法 / Multiplication")
    print("/ : 除法 / Division")
    print("q : 退出 / Quit")
    print("=" * 30)
    
    while True:
        try:
            num1 = float(input("输入第一个数字 / Enter first number: "))
            operator = input("输入操作符 / Enter operator (+, -, *, /): ")
            
            if operator == 'q':
                print("退出计算器 / Calculator exited.")
                break
                
            if operator not in ['+', '-', '*', '/']:
                print("错误: 无效操作符 / Error: Invalid operator")
                continue
                
            num2 = float(input("输入第二个数字 / Enter second number: "))
            
            if operator == '+':
                result = num1 + num2
                operation = "加法 / Addition"
            elif operator == '-':
                result = num1 - num2
                operation = "减法 / Subtraction"
            elif operator == '*':
                result = num1 * num2
                operation = "乘法 / Multiplication"
            elif operator == '/':
                if num2 == 0:
                    print("错误: 不能除以零 / Error: Cannot divide by zero")
                    continue
                result = num1 / num2
                operation = "除法 / Division"
            
            print(f"\n{operation}")
            print(f"结果 / Result: {num1} {operator} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("错误: 请输入有效数字 / Error: Please enter valid numbers")
        except KeyboardInterrupt:
            print("\n\n程序中断 / Program interrupted")
            break
        except Exception as e:
            print(f"发生错误 / Error occurred: {e}")

if __name__ == "__main__":
    calculator()
