def fashionably_late(arrivals,name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(arrivals,'Adela'))
