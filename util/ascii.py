def acceptable_values():
    res = []
    res.extend(range(32, 34))  # SPACE!
    res.append(39)  # '
    res.extend(range(44, 47))  # ,-.
    res.extend(range(48, 60))  # 0-9:;
    res.append(63)  # ?
    res.extend(range(65, 91))  # A-Z
    res.extend(range(97, 123))  # a-z
    return res
