function points(games) {
    score = 0;
    for (i= 0; i < games.length; i++) {
        arr = games[i].split(':');
        x = arr[0]; y = arr[1];
        if (x > y) {
            score += 3
        }
        else if (x == y) {
            score += 1
        }
    }
    return score
}