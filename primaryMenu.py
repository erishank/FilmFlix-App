# CRUD : Create   Read         Upadte      Delete
import   addFilm, displayFilm, updateFilm, deleteFilms,filmReport

def obtain_menu_file():# creating function to read .txt file
    with open("python project2/filmflex.txt","r") as primeMenu:
        readMenuContents = primeMenu.read()
    return readMenuContents
# creating function for film menu
def films_menu():
    option = 0
    optionList =["1","2","3","4","5","6"]
    menuChoice = obtain_menu_file()
    while option not in optionList:
        print(menuChoice)
        option = input(" Choose a valid option from the list above:")
        if option not in optionList:
            print(f"{option}  is an invalid choice not in the above list!")
        return option
mainProgram = True
while mainProgram:
    primeFilmMenu = films_menu()
    
    if primeFilmMenu == "1":
       displayFilm.get_films()
    elif primeFilmMenu == "2":
        addFilm.insert_film()
    elif primeFilmMenu =="3":
        updateFilm.update_Films()
    elif primeFilmMenu == "4":
        deleteFilms.delete_film()
    elif primeFilmMenu == "5":
        filmReport.get_Report()
    else:
        mainProgram = False
input(" Press Enter Key to Exit/Quit this App:")
    
    
    
