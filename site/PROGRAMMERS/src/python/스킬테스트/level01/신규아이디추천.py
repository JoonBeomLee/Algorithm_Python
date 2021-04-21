def lower(string):
    return string.lower()

def remove_special(string):
    special = ["-", "_", "."]
    result = ""
    
    for st in string:
        if not st.isalpha() and not st.isdigit():
            if st not in special: continue
            else: result += st
        else:
            result += st
        
    return result

def replace_dot(string):
    dot_idxs = []
    result_idxs = []
    for idxs, st in enumerate(string):
        if st == ".":
            dot_idxs.append(idxs)
            
        else:
            if len(dot_idxs) <= 1:
                dot_idxs = []
            else:
                st = dot_idxs[0]
                ed = dot_idxs[-1]
                
                result_idxs.append([st, ed])
                dot_idxs = []
    
    if len(dot_idxs) <= 1:
        dot_idxs = []
    else:
        st = dot_idxs[0]
        ed = dot_idxs[-1]

        result_idxs.append([st, ed])
        dot_idxs = []

    remove_dots = 0
    lst_string = list(string)
    for dots in result_idxs:
        st = dots[0] - remove_dots
        ed = dots[1] - remove_dots
        
        lst_string[st:ed+1] = "."
        remove_dots += (ed - st)
    
    string = "".join(lst_string)
    return string

def remove_fst_ed_dots(string):
    lst_string = list(string)
    
    
    if lst_string[0] == ".":
        lst_string[0] = ""
    
    if lst_string[-1] == ".":
        lst_string[-1] = ""
        
    return "".join(lst_string)

def insert_new_id(string):
    if len(string) == 0:
        return "a"
    
    return string

def cut_15len(string):
    result = ""
    if len(string) >= 16:
        result = string[:15]
        
        if result[-1] == ".":
            result = result[:14]
        
        return result
    else:
        return string
    
def add_last_st(string):
    if len(string) <= 2:
        while len(string) <= 2:
            string += string[-1]
            
    return string
        
def solution(new_id):
    answer = ''
    
    answer = lower(new_id)
    answer = remove_special(answer)
    answer = replace_dot(answer)
    answer = remove_fst_ed_dots(answer)
    answer = insert_new_id(answer)
    answer = cut_15len(answer)
    answer = add_last_st(answer)
    print(answer)
    
    return answer