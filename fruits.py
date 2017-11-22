prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }
    
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    }

for key_list in prices:
    print key_list
    print "prices: %s" % prices[key_list]
    print "stock: %s" % stock[key_list]
