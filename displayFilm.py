from link import *

def get_films():
    
    dbCursor.execute(" SELECT * FROM tblfilms")
    allFilms = dbCursor.fetchall()
    
    for aFilm in allFilms:
        print(aFilm)
        
if __name__ == "__main__":
    get_films()
    
    
    
"""from link import *
    
def show_Films():
        
    dbCursor.execute("SELECT * FROM tblfilms")
    films = dbCursor.fetchall()
       
    for aFilm in films:
         print(f"{aFilm} showing all the films in the film table: ")
        """