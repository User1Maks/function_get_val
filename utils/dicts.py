def get_val(collection, key, default='git'):
    """
    Возвращает значение из словаря по переданному ключу.
    :param collection: исходный словарь.
    :param key: ключ, по которому начинается извлечение. Если ключ не существует,
    возвращается default.
    :param default: если ключа не существует, возвращает default, по умолчанию 'git'.
    :return: значение словаря.
    """
    # collection = {"vcs": "mercurial", "program": "python", "university": "Skypro"}

    if key in collection.keys():
        return collection[key]
    else:
        return default
