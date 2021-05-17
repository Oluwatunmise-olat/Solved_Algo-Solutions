/**
    Given a roman nmeral convert it to an integer
*/

/**
    Should Know before Attempt

Constraints are values that make use of subtraction to get their values
e.g xii = is simply (x + ii) = 12 same with everyother except constraints that
are going to val2 - val1 eg xc [x = 10, c =100] xc=100-10 = 90

*/

let lookups = {
    'i': 1, 'v': 5, 'x': 10,
    'l': 50, 'c': 100, 'd': 500,
    'm': 1000
};

let constraint = {
    'iv': 4, 'ix':9,'xl':40,
    'xc': 90, 'cd':100, 'cm':900
};

// let text = 'mcmxciv';
let text = 'ix';

text = text.toLowerCase();

let text_len = text.length;

let arr = text.split("");

let obj = {};

let divide = Math.ceil(text_len/ 2)

let all = []


for (let i = 0; i < text.length ; i++){
    let slice = (arr.slice(i, i+ 2));
    all.push(slice.join(''));
};

// console.log(all, 'all')

for (let i =0; i< all.length; i++){
    if (Object.keys(constraint).includes(all[i])){
        obj[i] = constraint[all[i]]
        delete all[i + 1]
    }else{
        if (all[i] != undefined){
            let item = all[i].split('')
            obj[i] = lookups[item[0]]
        };
    };
};

// console.log(obj)

let sum = 0;

function addArray(arr){
    for (let i=0; i<arr.length; i++){
        if (arr[i] == undefined){
            continue
        }else{
            sum += arr[i];
        };
    };
    return sum;
};

let objArray = Object.values(obj);

console.log(addArray(objArray));
