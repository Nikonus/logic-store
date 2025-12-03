```javascript
function _countPrimeFactors(num) {
    if (num <= 1) return 0;
    let count = 0;
    let tempNum = num;

    while (tempNum % 2 === 0) {
        count++;
        tempNum /= 2;
    }

    for (let i = 3; i * i <= tempNum; i += 2) {
        while (tempNum % i === 0) {
            count++;
            tempNum /= i;
        }
    }

    if (tempNum > 1) {
        count++;
    }
    return count;
}

function logic(n) {
    let inputNum = n;

    if (typeof inputNum !== 'number') {
        inputNum = 0;
    } else if (!Number.isFinite(inputNum)) {
        inputNum = 0;
    } else {
        inputNum = Math.floor(Math.abs(inputNum));
    }

    let sumSquaresOfDigits = 0;
    let tempStr = String(inputNum);
    for (let i = 0; i < tempStr.length; i++) {
        const digit = parseInt(tempStr[i], 10);
        sumSquaresOfDigits += digit * digit;
    }

    const totalPrimeFactorsCount = _countPrimeFactors(inputNum);

    const magicConstantA = 739;
    const magicConstantB = 1297;
    const magicConstantC = 997;

    let intermediateResultX = (sumSquaresOfDigits * totalPrimeFactorsCount) + magicConstantA;
    let intermediateResultY = Math.floor(inputNum / magicConstantB);

    let finalValue = (intermediateResultX ^ intermediateResultY) + (inputNum % magicConstantC);

    return finalValue;
}

console.log(logic(0));
console.log(logic(1));
console.log(logic(7));
console.log(logic(13));
console.log(logic(42));
console.log(logic(1234));
console.log(logic(98765));
console.log(logic(-5));
console.log(logic(3.14));
console.log(logic(Infinity));
console.log(logic(NaN));
```