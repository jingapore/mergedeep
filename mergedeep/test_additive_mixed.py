import mergedeep

def run_test():

    dict_1 = {'a':{'b':[{'c':None}]}, 'd':None} 
    dict_2 = {'a':{'b':None}, 'd':'foo'}

    return mergedeep.merge(dict_1, dict_2, strategy=mergedeep.Strategy.ADDITIVE_MIXED)

if __name__=="__main__":
    print(run_test())