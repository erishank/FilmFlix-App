from link import *

def delete_film():
    try:
     filmIdField = input(" Enter the filmID to be deleted:")
    
     dbCursor.execute(f"SELECT * FROM tblfilms WHERE FilmID ={filmIdField}")
     aRecord =dbCursor.fetchone()
    
     if aRecord == None:
        print(f" No record found.{filmIdField}")
        
     else:
        dbCursor.execute(f"DELETE FROM tblfilms WHERE FilmID ={filmIdField}")
        dbLink.commit()
        print(f"{filmIdField} is deleted from the Film Table tblfilms")
    except sql.OperationalError as e:
        print(f" No database or table exists.")
    
if __name__ == "__main__":
    delete_film()
"""    
from link import *

def delete_film():
    
     filmIdField = input(" Enter the filmId to be deleted:")
     
     dbCursor.execute(f"SELECT * FROM tblfilms WHERE FilmID ={filmIdField}")
     aRecord = dbCursor.fetchone()
     if aRecord == None:
         print(f" No record found.{filmIdField}")
         
     else:
         dbCursor.execute(f"DELETE FROM tblfilms WHERE FilmID ={filmIdField}")
         dbLink.commit()
         
         print(f"{filmIdField} is deleted from the table tblfilms")
         
if __name__ == "__main__":
    delete_film()"""
        
        