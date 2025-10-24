from utils.openspace import OpenSpace

new_colleagues = [
    "Aleksei","Amine","Anna","Astha","Brigitta",
    "Bryan","Ena","Esra","Faranges","Frédéric",
    "Hamideh","Héloïse","Imran","Intan K.",
    "Jens","Kristin","Michiel","Nancy","Pierrick",
    "Sandrine","Tim","Viktor","Welederufeal","Živile"
]

openspace = OpenSpace(number_of_tables=6)
openspace.organize(new_colleagues)
openspace.display()
openspace.store("tables.txt")
