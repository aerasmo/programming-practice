function nbYear(p0, percent, aug, p) {
    let pop = p0 + (p0 * percent / 100) + aug    
    let years = 1
    while (pop < p) {
      pop = pop + (pop * percent / 100) + aug
      years += 1
    } 
    return years
}