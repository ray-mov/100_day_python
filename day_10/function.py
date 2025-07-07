#function chaining

def func1(text):
    return text +" "+ text


def func2(text):
    return text.title()


texts= func1(func2("mello"))

print(texts)