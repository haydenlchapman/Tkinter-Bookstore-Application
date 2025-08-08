from .book import Book

book_list = [
    # Fantasy
    Book("The Hobbit", "Fantasy", "J.R.R. Tolkien", 1937, "George Allen & Unwin", "books/covers/the_hobbit.jpg"),
    Book("A Game of Thrones", "Fantasy", "George R. R. Martin", 1996, "Bantam Spectra", "books/covers/a_game_of_thrones.jpg"),
    Book("World of Warcraft: Illidan", "Fantasy", "William King", 2016, "Del Rey Books", "books/covers/world_of_warcraft_illidan.jpg"),
    Book("Mistborn: The Final Empire", "Fantasy", "Brandon Sanderson", 2006, "Tor Books", "books/covers/mistborn_final_empire.jpg"),
    Book("The Way of Kings", "Fantasy", "Brandon Sanderson", 2010, "Tor Books", "books/covers/the_way_of_kings.jpg"),
    Book("Eragon", "Fantasy", "Christopher Paolini", 2002, "Paolini LLC", "books/covers/eragon.jpg"),
    Book("The Lies of Locke Lamora", "Fantasy", "Scott Lynch", 2006, "Gollancz", "books/covers/the_lies_of_locke_lamora.jpg"),
    Book("The Eye of the World", "Fantasy", "Robert Jordan", 1990, "Tor Books", "books/covers/the_eye_of_the_world.jpg"),
    Book("Sabriel", "Fantasy", "Garth Nix", 1995, "HarperCollins", "books/covers/sabriel.jpg"),
    Book("Harry Potter and the Half-Blood Prince", "Fantasy", "J. K. Rowling", 2005, "Scholastic Corporation", "books/covers/harry_potter_and_the_half_blood_prince.jpg"),

    # Historical fiction
    Book("The Book Thief", "Historical Fiction", "Markus Zusak", 2005, "Knopf", "books/covers/the_book_thief.jpg"),
    Book("All the Light We Cannot See", "Historical Fiction", "Anthony Doerr", 2014, "Scribner", "books/covers/all_the_light_we_cannot_see.jpg"),
    Book("The Pillars of the Earth", "Historical Fiction", "Ken Follett", 1989, "Macmillan", "books/covers/the_pillars_of_the_earth.jpg"),
    Book("The Nightingale", "Historical Fiction", "Kristin Hannah", 2015, "St. Martin's Press", "books/covers/the_nightingale.jpg"),
    Book("A Gentleman in Moscow", "Historical Fiction", "Amor Towles", 2016, "Viking", "books/covers/a_gentleman_in_moscow.jpg"),
    Book("The Paris Library", "Historical Fiction", "Janet Skeslien Charles", 2021, "Atria Books", "books/covers/the_paris_library.jpg"),
    Book("Beneath a Scarlet Sky", "Historical Fiction", "Mark Sullivan", 2017, "Lake Union Publishing", "books/covers/beneath_a_scarlet_sky.jpg"),
    Book("The Tattooist of Auschwitz", "Historical Fiction", "Heather Morris", 2018, "Echo Publishing", "books/covers/the_tattooist_of_auschwitz.jpg"),
    Book("The Alice Network", "Historical Fiction", "Kate Quinn", 2017, "William Morrow", "books/covers/the_alice_network.jpg"),
    Book("The Coffin Quilt", "Historical Fiction", "Yaa Gyasi", 1999, "Harcourt Children's Books", "books/covers/the_coffin_quilt.jpg"),

    # Science Fiction
    Book("Dune", "Science Fiction", "Frank Herbert", 1965, "Chilton Books", "books/covers/dune.jpg"),
    Book("Neuromancer", "Science Fiction", "William Gibson", 1984, "Ace Books", "books/covers/neuromancer.jpg"),
    Book("Foundation", "Science Fiction", "Isaac Asimov", 1951, "Gnome Press", "books/covers/foundation.jpg"),
    Book("Ender's Game", "Science Fiction", "Orson Scott Card", 1985, "Tor Books", "books/covers/enders_game.jpg"),
    Book("Snow Crash", "Science Fiction", "Neal Stephenson", 1992, "Bantam Books", "books/covers/snow_crash.jpg"),
    Book("Hyperion", "Science Fiction", "Dan Simmons", 1989, "Doubleday", "books/covers/hyperion.jpg"),
    Book("The Left Hand of Darkness", "Science Fiction", "Ursula K. Le Guin", 1969, "Ace Books", "books/covers/left_hand_of_darkness.jpg"),
    Book("The Martian", "Science Fiction", "Andy Weir", 2011, "Crown Publishing", "books/covers/the_martian.jpg"),
    Book("Red Mars", "Science Fiction", "Kim Stanley Robinson", 1992, "Bantam Books", "books/covers/red_mars.jpg"),
    Book("Old Man's War", "Science Fiction", "John Scalzi", 2005, "Tor Books", "books/covers/old_mans_war.jpg"),

    # Mystery
    Book("The Girl with the Dragon Tattoo", "Mystery", "Stieg Larsson", 2005, "Norstedts Förlag", "books/covers/girl_with_dragon_tattoo.jpg"),
    Book("Gone Girl", "Mystery", "Gillian Flynn", 2012, "Crown Publishing", "books/covers/gone_girl.jpg"),
    Book("The Da Vinci Code", "Mystery", "Dan Brown", 2003, "Doubleday", "books/covers/da_vinci_code.jpg"),
    Book("And Then There Were None", "Mystery", "Agatha Christie", 1939, "Collins Crime Club", "books/covers/and_then_there_were_none.jpg"),
    Book("The Hound of the Baskervilles", "Mystery", "Arthur Conan Doyle", 1902, "George Newnes", "books/covers/hound_of_baskervilles.jpg"),
    Book("In the Woods", "Mystery", "Tana French", 2007, "Viking Press", "books/covers/in_the_woods.jpg"),
    Book("Big Little Lies", "Mystery", "Liane Moriarty", 2014, "Penguin Publishing", "books/covers/big_little_lies.jpg"),
    Book("Rebecca", "Mystery", "Daphne du Maurier", 1938, "Victor Gollancz", "books/covers/rebecca.jpg"),
    Book("The Cuckoo's Calling", "Mystery", "Robert Galbraith", 2013, "Sphere Books", "books/covers/cuckoos_calling.jpg"),
    Book("Still Life", "Mystery", "Louise Penny", 2005, "St. Martin's Press", "books/covers/still_life.jpg"),

    # Thriller / Suspense
    Book("The Silence of the Lambs", "Thriller / Suspense", "Thomas Harris", 1988, "St. Martin's Press", "books/covers/silence_of_lambs.jpg"),
    Book("The Girl on the Train", "Thriller / Suspense", "Paula Hawkins", 2015, "Riverhead Books", "books/covers/girl_on_train.jpg"),
    Book("Shutter Island", "Thriller / Suspense", "Dennis Lehane", 2003, "William Morrow", "books/covers/shutter_island.jpg"),
    Book("The Firm", "Thriller / Suspense", "John Grisham", 1991, "Doubleday", "books/covers/the_firm.jpg"),
    Book("Before I Go to Sleep", "Thriller / Suspense", "S.J. Watson", 2011, "HarperCollins", "books/covers/before_i_go_to_sleep.jpg"),
    Book("I Am Watching You", "Thriller / Suspense", "Teresa Driscoll", 2017, "Thomas & Mercer", "books/covers/i_am_watching_you.jpg"),
    Book("The Reversal", "Thriller / Suspense", "Michael Connelly", 2010, "Little, Brown", "books/covers/the_reversal.jpg"),
    Book("Behind Closed Doors", "Thriller / Suspense", "B.A. Paris", 2016, "St. Martin's Press", "books/covers/behind_closed_doors.jpg"),
    Book("The Woman in Cabin 10", "Thriller / Suspense", "Ruth Ware", 2016, "Gallery Books", "books/covers/woman_in_cabin_10.jpg"),
    Book("Into the Water", "Thriller / Suspense", "Paula Hawkins", 2017, "Riverhead Books", "books/covers/into_the_water.jpg"),

    # Biography / Autobiography / Memoir
    Book("The Diary of a Young Girl", "Biography / Autobiography / Memoir", "Anne Frank", 1947, "Contact Publishing", "books/covers/anne_frank.jpg"),
    Book("Becoming", "Biography / Autobiography / Memoir", "Michelle Obama", 2018, "Crown Publishing", "books/covers/becoming.jpg"),
    Book("Educated", "Biography / Autobiography / Memoir", "Tara Westover", 2018, "Random House", "books/covers/educated.jpg"),
    Book("The Glass Castle", "Biography / Autobiography / Memoir", "Jeannette Walls", 2005, "Scribner", "books/covers/glass_castle.jpg"),
    Book("Steve Jobs", "Biography / Autobiography / Memoir", "Walter Isaacson", 2011, "Simon & Schuster", "books/covers/steve_jobs.jpg"),
    Book("Born a Crime", "Biography / Autobiography / Memoir", "Trevor Noah", 2016, "Spiegel & Grau", "books/covers/born_a_crime.jpg"),
    Book("When Breath Becomes Air", "Biography / Autobiography / Memoir", "Paul Kalanithi", 2016, "Random House", "books/covers/when_breath_becomes_air.jpg"),
    Book("Bossypants", "Biography / Autobiography / Memoir", "Tina Fey", 2011, "Little, Brown", "books/covers/bossypants.jpg"),
    Book("Long Walk to Freedom", "Biography / Autobiography / Memoir", "Nelson Mandela", 1994, "Little, Brown", "books/covers/long_walk_to_freedom.jpg"),
    Book("I Know Why the Caged Bird Sings", "Biography / Autobiography / Memoir", "Maya Angelou", 1969, "Random House", "books/covers/caged_bird_sings.jpg"),

    # Horror
    Book("It", "Horror", "Stephen King", 1986, "Viking", "books/covers/it.jpg"),
    Book("The Shining", "Horror", "Stephen King", 1977, "Doubleday", "books/covers/the_shining.jpg"),
    Book("Dracula", "Horror", "Bram Stoker", 1897, "Archibald Constable", "books/covers/dracula.jpg"),
    Book("The Haunting of Hill House", "Horror", "Shirley Jackson", 1959, "Viking", "books/covers/haunting_of_hill_house.jpg"),
    Book("Bird Box", "Horror", "Josh Malerman", 2014, "Ecco Press", "books/covers/bird_box.jpg"),
    Book("House of Leaves", "Horror", "Mark Z. Danielewski", 2000, "Pantheon Books", "books/covers/house_of_leaves.jpg"),
    Book("The Exorcist", "Horror", "William Peter Blatty", 1971, "Harper & Row", "books/covers/exorcist.jpg"),
    Book("Mexican Gothic", "Horror", "Silvia Moreno-Garcia", 2020, "Del Rey", "books/covers/mexican_gothic.jpg"),
    Book("The Silent Patient", "Horror", "Alex Michaelides", 2019, "Celadon Books", "books/covers/silent_patient.jpg"),
    Book("Hell House", "Horror", "Richard Matheson", 1971, "Viking", "books/covers/hell_house.jpg"),

    # Romance
    Book("Pride and Prejudice", "Romance", "Jane Austen", 1813, "T. Egerton", "books/covers/pride_and_prejudice.jpg"),
    Book("Outlander", "Romance", "Diana Gabaldon", 1991, "Delacorte Press", "books/covers/outlander.jpg"),
    Book("Me Before You", "Romance", "Jojo Moyes", 2012, "Penguin Books", "books/covers/me_before_you.jpg"),
    Book("The Notebook", "Romance", "Nicholas Sparks", 1996, "Warner Books", "books/covers/the_notebook.jpg"),
    Book("Twilight", "Romance", "Stephenie Meyer", 2005, "Little, Brown", "books/covers/twilight.jpg"),
    Book("The Time Traveler's Wife", "Romance", "Audrey Niffenegger", 2003, "MacAdam/Cage", "books/covers/time_travelers_wife.jpg"),
    Book("The Rosie Project", "Romance", "Graeme Simsion", 2013, "Text Publishing", "books/covers/rosie_project.jpg"),
    Book("Beautiful Disaster", "Romance", "Jamie McGuire", 2011, "Atria Books", "books/covers/beautiful_disaster.jpg"),
    Book("Red, White & Royal Blue", "Romance", "Casey McQuiston", 2019, "St. Martin's Griffin", "books/covers/red_white_royal_blue.jpg"),
    Book("Beach Read", "Romance", "Emily Henry", 2020, "Berkley", "books/covers/beach_read.jpg"),

    # Adventure
    Book("The Call of the Wild", "Adventure", "Jack London", 1903, "Macmillan", "books/covers/call_of_the_wild.jpg"),
    Book("The Lost World", "Adventure", "Arthur Conan Doyle", 1912, "Hodder & Stoughton", "books/covers/lost_world.jpg"),
    Book("The Sea Wolf", "Adventure", "Jack London", 1904, "Macmillan", "books/covers/sea_wolf.jpg"),
    Book("Life of Pi", "Adventure", "Yann Martel", 2001, "Knopf Canada", "books/covers/life_of_pi.jpg"),
    Book("Treasure Island", "Adventure", "Robert Louis Stevenson", 1883, "Cassell and Company", "books/covers/treasure_island.jpg"),
    Book("The Three Musketeers", "Adventure", "Alexandre Dumas", 1844, "Baudry's European Library", "books/covers/three_musketeers.jpg"),
    Book("Around the World in 80 Days", "Adventure", "Jules Verne", 1873, "Pierre-Jules Hetzel", "books/covers/around_the_world.jpg"),
    Book("Hatchet", "Adventure", "Gary Paulsen", 1986, "Macmillan", "books/covers/hatchet.jpg"),
    Book("King Solomon's Mines", "Adventure", "H. Rider Haggard", 1885, "Cassell & Co", "books/covers/king_solomons_mines.jpg"),
    Book("The Alchemist", "Adventure", "Paulo Coelho", 1988, "HarperTorch", "books/covers/the_alchemist.jpg"),

    # Dystopian / Utopian
    Book("1984", "Dystopian / Utopian", "George Orwell", 1949, "Secker & Warburg", "books/covers/1984.jpg"),
    Book("Brave New World", "Dystopian / Utopian", "Aldous Huxley", 1932, "Chatto & Windus", "books/covers/brave_new_world.jpg"),
    Book("Fahrenheit 451", "Dystopian / Utopian", "Ray Bradbury", 1953, "Ballantine Books", "books/covers/fahrenheit_451.jpg"),
    Book("The Giver", "Dystopian / Utopian", "Lois Lowry", 1993, "Houghton Mifflin", "books/covers/the_giver.jpg"),
    Book("The Hunger Games", "Dystopian / Utopian", "Suzanne Collins", 2008, "Scholastic Press", "books/covers/hunger_games.jpg"),
    Book("Divergent", "Dystopian / Utopian", "Veronica Roth", 2011, "Katherine Tegen Books", "books/covers/divergent.jpg"),
    Book("The Handmaid's Tale", "Dystopian / Utopian", "Margaret Atwood", 1985, "McClelland and Stewart", "books/covers/handmaids_tale.jpg"),
    Book("Never Let Me Go", "Dystopian / Utopian", "Kazuo Ishiguro", 2005, "Faber and Faber", "books/covers/never_let_me_go.jpg"),
    Book("Oryx and Crake", "Dystopian / Utopian", "Margaret Atwood", 2003, "McClelland and Stewart", "books/covers/oryx_and_crake.jpg"),
    Book("We", "Dystopian / Utopian", "Yevgeny Zamyatin", 1924, "E.P. Dutton", "books/covers/we.jpg")
]