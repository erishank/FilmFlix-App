"""from link import *

def obtain_Report():
    
    
    dbCursor.execute(f"SELECT  FilmID,Title,YearReleased FROM tblfilms ")
    #dbCursor.execute(f"SELECT * FROM tblfilms WHERE title like '%o' ")
    dbCursor.execute(f"SELECT Title,Genre FROM tblfilms ORDER BY filmID desc ")
    
    allRecords = dbCursor.fetchall()
    
    for aRecord in allRecords:
      print(aRecord)

if __name__ == "__main__":
    obtain_Report()"""
    
    
from link import *

def get_Report():
    
    #dbCursor.execute(" SELECT * FROM tblfilms WHERE Title like '%n'")
    dbCursor.execute(" SELECT * FROM tblfilms WHERE Title like 't%'")
    dbCursor.execute(f"SELECT  FilmID,Title,YearReleased FROM tblfilms ")
    allRecords = dbCursor.fetchall()
    
    for eachRecord in allRecords:
        print(eachRecord)
        
if __name__ == "__main__":
    get_Report()