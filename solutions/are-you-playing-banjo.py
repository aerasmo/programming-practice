def are_you_playing_banjo(name):
    return ("{} plays banjo" if name[0] in "rR" else "{} does not play banjo").format(name)