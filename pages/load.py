def start():   
    
    import csv
    import glob

    from .models import Book

    filename = "pages/books.csv"

    rows = []
    l = glob.glob("**/books.csv",recursive=True)
    print(l)
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            # print("*(#@RFNO#@(#*)#!()#I)JFNU#F!I)")
            print(row)
            book = Book(title = row['Title'] , author=row['Author'] , genre=row['Genre'] , length = row['Height'] , publisher=row['Publisher'])
            book.save()
    