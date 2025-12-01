```javascript
function logic(n) {
    if (typeof n !== 'number' || !Number.isInteger(n)) {
        throw new Error("Input must be an integer.");
    }

    n = Math.abs(n);

    if (n === 0) {
        return 0;
    }

    let nAsString = n.toString();
    let sumOfSquaresOfDigits = 0;
    for (let i = 0; i < nAsString.length; i++) {
        const digit = parseInt(nAsString[i], 10);
        sumOfSquaresOfDigits += digit * digit;
    }

    const binaryString = n.toString(2);
    let numberOfSetBits = 0;
    for (let i = 0; i < binaryString.length; i++) {
        if (binaryString[i] === '1') {
            numberOfSetBits++;
        }
    }

    const primeModulo1 = 1009;
    const primeModulo2 = 991;

    let intermediateTransformation = (sumOfSquaresOfDigits * numberOfSetBits) % primeModulo1;

    let integerSquareRoot = Math.floor(Math.sqrt(n));
    if (integerSquareRoot === 0) {
        integerSquareRoot = 1;
    }

    let finalResult = (intermediateTransformation * integerSquareRoot + n) % (primeModulo1 * primeModulo2);

    return finalResult;
}

console.log(logic(0));
console.log(logic(1));
console.log(logic(7));
console.log(logic(42));
console.log(logic(123));
console.log(logic(1000));
console.log(logic(987654321));
console.log(logic(-42));
```