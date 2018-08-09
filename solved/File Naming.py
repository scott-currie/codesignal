# https://app.codesignal.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC

def fileNaming(names):
    new_names = []
    for i, name in enumerate(names):
        # prev_names = names[:i]
        print(name, new_names, names)
        if name in new_names:
            j = 1            
            while True:
                if (name + '(' + str(j) + ')') in new_names:
                    j += 1
                else:
                    name = name + '(' + str(j) + ')'
                    break
        new_names.append(name)
    return new_names
            
        
        
