import functions

def unified(data):
    onedatalist = []
    datalist = []
    for i in data:
        if i == " ":
            datalist.append(''.join(onedatalist))
            onedatalist = []
        else:
            onedatalist.append(i)
    del onedatalist
    onefunction = datalist[0]
    del datalist[0]
    return functions.functiondict[f'{onefunction}'](*datalist)
