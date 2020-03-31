import mergedeep

def run_test_none_type():

    dict_1 = {'a':{'b':[{'c':None}]}, 'd':None} 
    dict_2 = {'a':{'b':None}, 'd':'foo'}

    return mergedeep.merge(dict_1, dict_2, strategy=mergedeep.Strategy.ADDITIVE_MIXED)

def run_test_dict_to_list():

    dict_1 = {'a':{'b':[{'c':{'d':None}}]}, 'e':None} 
    dict_2 = {'a':{'b':{'c':{'d':'foo'}}}, 'e':'bar'}

    return mergedeep.merge(dict_1, dict_2, strategy=mergedeep.Strategy.ADDITIVE_MIXED)

def source_has_more_fields():

    dict_1 = {'a':{'b':[{'c':{'d':None}}]}, 'e':None} 
    dict_2 = {'a':{'b':{'c':{'d':'foo', 'g':'barbar'}}}, 'e':'bar', 'f':'foofoo'}

    return mergedeep.merge(dict_1, dict_2, strategy=mergedeep.Strategy.ADDITIVE_MIXED)

def twice_nested_list():

    dict_1 = {'a': [{'b':[{'c':None}]}], 'f':None}
    dict_2 = {'a': {'b':{'c':'foo'}}, 'f':'bar'}
    
    return mergedeep.merge(dict_1, dict_2, strategy=mergedeep.Strategy.ADDITIVE_MIXED)

if __name__=="__main__":
    print('result for none_type')
    print(run_test_none_type())

    print('result for dict_to_list')
    print(run_test_dict_to_list())

    print('result for source_has_more_fields')
    print(source_has_more_fields())

    print('result for twice nested list')
    print(twice_nested_list())