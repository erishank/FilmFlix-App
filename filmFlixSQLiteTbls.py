from link import *




dbCursor.execute("""
CREATE TABLE "tblfilms" (
	"FilmID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"YearReleased"	INTEGER,
	"Rating"	TEXT,
    "Duration" INTEGER,
    "Genre" TEXT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)""")
