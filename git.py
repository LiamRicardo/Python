while True:
    user_input = input("Introduce una palabra o número (máximo 8 caracteres): ")
    if len(user_input) <= 8:
        print(f"Has introducido: {user_input}")
        break
    else:
        print("Error: El input excede los 8 caracteres. Inténtalo de nuevo.")
        