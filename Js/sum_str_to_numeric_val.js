/**
    Question
    given two string values, cacluate the sum and return
    as string without using any built in string to int
    conversion
*/

// Naming is terrible :) i know

//Test values

// Could have added check for instance of isNan or not

let value1 = "2001";
let value2 = "20";

// Handles getting integer repr of strings eg {['0']: 0, ['2']: 2}
let digits = {};

function updateDigits() {
  for (let i = 0; i < 10; i++) {
    digits[i.toString()] = i;
  }
}

updateDigits();

let convObj = {};

let conVal1;
let conVal2;

function conStrToDig(arg) {
  for (let i = 0; i < arg.length; i++) {
    convObj[i + 1] = digits[arg[i]];
  }
}

conStrToDig(value1);

//deepcopy

conVal1 = JSON.parse(JSON.stringify(convObj));

convObj = {};

conStrToDig(value2);

conVal2 = JSON.parse(JSON.stringify(convObj));

// Dealing with the actual addition per index

let large;
let small;

if (value1.length > value2.length) {
  large = conVal1;
  small = conVal2;
} else {
  large = conVal2;
  small = conVal1;
}

let sum_arr = [];

let largeValues = [...Object.values(large)];

let smallValues = [...Object.values(small)];

function finalArr(largeArr, smallArr) {
  for (let elem = 0; elem <= smallArr.length; elem++) {
    sum_arr.unshift(
      smallArr[smallArr.length - 1] + largeArr[largeArr.length - 1]
    );
    smallArr.pop();
    largeArr.pop();
  }
  for (let i = 0; i <= largeArr.length; i++) {
    sum_arr.unshift(largeArr[largeArr.length - 1]);
    largeArr.pop();
  }
}

finalArr(largeValues, smallValues);

// Dealing with conversion to base 10

let copyOfSum_Arr = JSON.parse(JSON.stringify(sum_arr));

let SumArr = [];

for (let i = 0; i < sum_arr.length; i++) {
  let lastIndxVal = copyOfSum_Arr[copyOfSum_Arr.length - 1];
  if (lastIndxVal >= 10) {
    let quotient = lastIndxVal % 10;
    let remainder = Math.floor(lastIndxVal / 10);
    SumArr.unshift(quotient);
    copyOfSum_Arr.pop();
    copyOfSum_Arr[copyOfSum_Arr.length - 1] += remainder;
  } else {
    if (copyOfSum_Arr.length == 1) {
      SumArr.unshift(copyOfSum_Arr[0]);
      copyOfSum_Arr.pop();
    } else {
      SumArr.unshift(copyOfSum_Arr[copyOfSum_Arr.length - 1]);
      copyOfSum_Arr.pop();
    }
  }
}

// Returns the final result

function getAnswer() {
  return SumArr.join("");
}

console.log(getAnswer());
