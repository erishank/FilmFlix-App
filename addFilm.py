from link import *

def insert_film():
    filmTitle = input("Enter the Film Title:")
    filmYearReleased = int(input("Enter the year film released:"))
    filmRating = input("Enter the Rating of the Film:")
    filmDuration = int(input("Duration of the Film in minutes:"))
    filmGenre = input("Enter the Genre of Film:")
    
    
    dbCursor.execute("INSERT INTO tblfilms(Title,YearReleased,Rating,Duration,Genre)VALUES(?,?,?,?,?)",(filmTitle,filmYearReleased,filmRating,filmDuration,filmGenre))
    dbLink.commit()
    
    print(f"{filmTitle} inserted into the FilmFlix Table. ")
    
if __name__ == "__main__":
    insert_film()
    
"""from link import *

def add_Films():
    filmTitle = input("Enter the title of the film:")
    filmYearReleased = input("Enter the Year of the film:")
    filmRating = input("Enter the Rating of the film:")
    filmDuration = input("Enter the Duration of the film:")
    filmGenre = input("Enter the Genre of the film:")
    
    dbCursor.execute(" INSERT INTO tblfilms (Title, Year, Rating,Duration,genre)VALUES(?,?,?,?,?)",(filmTitle,filmYearReleased,filmRating,filmDuration,filmGenre))
    dbLink.commit()
    
    print(f"{filmTitle} is added to the film table.")
    
if __name__ == "__main__":
    add_Films()
    """
    
    