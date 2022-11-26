let fire = {'fire': 0.5, 'water': 0.5, 'grass': 2, 'electric': 1}
let water = {'fire': 2, 'water': 0.5, 'grass': 0.5, 'electric': 0.5}
let grass = {'fire': 0.5, 'water': 2, 'grass': 0.5, 'electric': 1}
let electric = {'fire': 1, 'water': 2, 'grass': 1, 'electric': 0.5}

let effectivity = {'fire': fire,
                'water': water,
                'grass': grass,
                'electric': electric}
                
const calculateDamage = (yourType, opponentType, attack, defense) => {
    console.log(yourType)
    console.log(opponentType)
    effectiveness = effectivity[yourType][opponentType]
    damage = 50 * (attack / defense) * effectiveness
    console.log(damage)
    return damage
}