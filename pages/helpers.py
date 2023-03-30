

def dataToTemplate(q):
    
    data = []
    vis = {}
    
    for book in q:
        genre = book.genre
        if genre in vis:
            index = vis[genre]
            if len(data[index]['books1']) < 5:
                data[index]['books1'].append(book)
            else:
                data[index]['books2'].append(book)
        else:
            vis[genre]=len(data)
            obj = {'name':genre,'books1':[book],'books2':[]}
            data.append(obj)
    
    for genre in data:
        row=[]
        rows=[]
        for book in genre['books2']:
            row.append(book)
            if len(row)==5:
                rows.append(row)
                row=[]
        if len(row):
            rows.append(row)
        genre['books2']=rows

    return data