def export_data():
    with open('db.csv', 'r') as file:
        data = []
        f = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    f.append(line.strip())
                else:
                    data.append(f)
                    f = []
    return data