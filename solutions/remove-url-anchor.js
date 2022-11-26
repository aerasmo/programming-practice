// https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/javascript

// "www.codewars.com#about" --> "www.codewars.com"
// "www.codewars.com?page=1" -->"www.codewars.com?page=1"

function removeURLAnchor(url) {
    const regex = /\#([\s\S])*$/;
    // return url.replace(regex, '')
    return url.replace(/#.*/gi,"");
}


console.log(removeURLAnchor("www.codewars.com#about"))
console.log(removeURLAnchor("www.codewars.com/katas/?page=1#about"))
console.log(removeURLAnchor("www.codewars.com/katas/"))
