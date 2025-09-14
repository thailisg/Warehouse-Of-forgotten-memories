Well, I thought this project would be easy for me, but I must admit it was very hard, mostly because of the design part. I tried to look for videos to learn, but almost all the ones I found were using classes, so I decided to do it the same way as in those videos to organize the code better. I had to rewrite all the code I had when I decided to make the change. Besides the code, I spent a lot of time watching videos, asking the AI about classes and design, and reading documentation so the code would be more readable for you, the brother or sister who corrects my project, and for me in the future. I hope to improve this program over time to make it much more professional and visually better. I chose a design similar to Minecraft because I thought it fit the theme.

My application is divided into:

interface_main.py: This is the main design file; it contains the main window from where you can access other windows through buttons.

logic.py: Here is the logic of my program, where the functions documented in my proposal are, plus one more function to delete an object that I forgot to add before and a name change in one of the functions because I decided to change what the function would do. These are the functions:

read_findings_existing
save_find
delete_find (this is the new one)
search_by_field
read_alphabet_csv (this one I renamed; before it was read_dictionary, but I changed it to be more descriptive)
I left the main just as a run in a separate file.

main.py: This file contains the run for the program; from here the application opens.

Views: This folder contains the design of each button located in interface_main. Below I leave which function goes with each view:

read_findings_existing = findings_existing_view.py
save_find = save_find_view.py
delete_find = delete_view.py
search_by_field = search_by_field_view.py
read_alphabet_csv = alphabet_csv_view.py

Assets: This folder stores the image I use in interface_main, for decoration.

test_logic.py: This file is where I check the functioning of my functions from logic.py.

archivos_csv: This folder contains the .csv files I use in my program. I really didn’t realize the folder name was in Spanish until the end, but I didn’t see it as a problem. These are the files:

greek.csv: this contains the Greek alphabets
latin.csv: this contains the Latin alphabets
warehouse_object.csv: this contains the archaeological objects

I wanted to try customTkinter, but I didn’t know if it would be a problem, same with the PIL module, so I preferred to leave it normal because to run it I have to learn to walk first, hashdahsdh.

The modules I used were:

tkinter
pytest
os
csv

I wanted to use datetime, but I didn’t find where I could add it so it would fit well, so I finally didn’t use it. I tell you this because it was in my proposal.