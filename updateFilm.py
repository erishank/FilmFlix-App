from link import *

def update_Films():
    
    filmIdField = input("Enter the FilmID to be updated:")
    
    titleField= input ("Enter the Title of the New Film:").title()
    yearField= input ("Enter the YearReleased of the Film:").title()
    ratingField= input ("Enter the Rating of the Film:").title()
    durationField= input ("Enter the Duration of the Film:").title()
    genreField= input ("Enter the Genre of the Film:").title()
    
    
    titleField= "'" + titleField + "'"
    yearField= "'" + yearField + "'"
    ratingField= "'" + ratingField + "'"
    durationField= "'" + durationField + "'"
    genreField= "'" + genreField + "'"
    
    

    
    dbCursor.execute(f"UPDATE tblfilms SET Title ={titleField},YearReleased ={yearField},Rating ={ratingField}, Duration ={durationField},Genre ={genreField} WHERE FilmID = {filmIdField}")
    dbLink.commit()
    
    print(f"{filmIdField} updated in the Film table tblfilm.")
    
if __name__ == "__main__":
    update_Films()
    