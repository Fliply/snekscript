import snekscript

while True:
    text = input('snekscript > ')
    result, error = snekscript.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)