def humanify(name: str):
    import re
    return ' '.join(re.split('_+', name)).capitalize()


def humanify_class(name: str):
    new_name = [name[0]]
    for i in range(1, len(name)):
        if name[i].isupper():
            new_name.append(' ' + name[i].lower())
        else:
            new_name.append(name[i])
    return ''.join(new_name)
