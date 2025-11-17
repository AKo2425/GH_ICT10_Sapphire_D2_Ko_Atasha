from pyscript import display


band_club = {"Presley", "Phoebe", "Cali", "Erin"}
dance_club = {"Piper", "Cali", "Heidi", "Nola"}

# Students in at least one club 
at_least_one = band_club | dance_club

# Students in both clubs 
both_clubs = band_club & dance_club

# Students only in Band
only_band = band_club - dance_club

# Students only in Dance
only_dance = dance_club - band_club

# Students in exactly one club 
exactly_one = band_club ^ dance_club

# Display results in HTML divs
display(f"Band Club: {band_club}", target="band-club")
display(f"Dance Club: {dance_club}", target="dance-club")
display(f"Students in at least one club: {at_least_one}", target="at-least-one")
display(f"Students in both clubs: {both_clubs}", target="both-clubs")
display(f"Students only in Band Club: {only_band}", target="only-band")
display(f"Students only in Dance Club: {only_dance}", target="only-dance")
display(f"Students in exactly one club: {exactly_one}", target="exactly-one")
