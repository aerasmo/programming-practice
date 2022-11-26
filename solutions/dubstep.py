import re
def song_decoder(song):
    return re.sub(r"(WUB)+", " ", song).strip(" ")

# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
# =>  WE ARE THE CHAMPIONS MY FRIEND