from croto import croto


def crotorun():
    while True:
        text = input('croto > ')
        result, error = croto.run('<stdin>', text)
        if error:
            print(error.as_string())
        else:
            print(result)
