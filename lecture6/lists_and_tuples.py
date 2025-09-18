from email_utils import send_email

# A person is defined by their name, email address and city of residence
ulrika = ("Ulrika", "uu@uu.uu", "Uddevalla")
markus = ("Markus", "mm@mm.mm", "Mölndal")
karl = ("Karl", "kk@kk.kk", "Kungälv")
pia = ("Pia", "pp@pp.pp", "Partille")
inari = ("Inari", "inari@chalmers.se", "Göteborg")

# Loop over the people, send email to people who live in Göteborg
people = [ulrika, markus, karl, pia, inari]

for person in people:
    name, email_address, city = person
    if city == "Göteborg":
        subject = f"Exciting opportunities in {city}"
        msg = f"Hello {name}! This is legit not spam."
        send_email(subject, msg, email_address)