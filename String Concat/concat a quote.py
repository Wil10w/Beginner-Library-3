def quote_this(quote, name):
    return '"' + quote + '"' + ' -' + name

a = quote_this("Try and fail, but never fail to try.", "Jared Leto")
print(a)
b = quote_this(a, "Michael Scott")
print(b)
