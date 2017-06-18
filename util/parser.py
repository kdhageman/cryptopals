def parse_kv(inp):
    splitted = inp.split("&")
    res = {}
    for s in splitted:
        res[s.split("=")[0]] = s.split("=")[1]
    return res
