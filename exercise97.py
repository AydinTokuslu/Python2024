def clear_numbers(str):
    text = []
    for i in str:
        if i.isdigit():
            continue
        else:
            text.append(i)
    return "".join(text)


print(clear_numbers("kflkfla53j513 lk35jjk3 2j5 22 mrr"))