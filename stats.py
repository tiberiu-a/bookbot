def get_num_words(text):
    return len(text.split())

def get_num_lethers(text):
    lethers_counter = {}
    for i in range(0, len(text)):
        lether = text[i].lower()
        if lether in lethers_counter:
            num = lethers_counter[lether] + 1
            lethers_counter[lether] = num
        else:
            lethers_counter[lether] = 1
    return lethers_counter

def get_report(lethers_count):
    unsorted_lethers_list = []
    for key in lethers_count:
        unsorted_lethers_list.append({'char': key, 'count': lethers_count[key]})
    unsorted_lethers_list.sort(reverse=True, key=sort_on)
    return unsorted_lethers_list

def sort_on(dict):
    return dict["count"]
    
