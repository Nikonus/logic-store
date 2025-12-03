function logic(n) {
    let base3Representation = n.toString(3);

    let sumOfSquaredBase3Digits = 0;
    for (let i = 0; i < base3Representation.length; i++) {
        let digit = parseInt(base3Representation[i]);
        sumOfSquaredBase3Digits += digit * digit;
    }

    let intermediateProduct = sumOfSquaredBase3Digits * n;

    let nAsString = n.toString();
    let reversedNAsString = nAsString.split('').reverse().join('');
    let reversedNValue = parseInt(reversedNAsString);

    let firstComponent = n ^ intermediateProduct;
    let secondComponent = (reversedNValue % 7) * n;

    return firstComponent + secondComponent;
}

// Example usage to demonstrate the function
console.log(`logic(0) = ${logic(0)}`);
console.log(`logic(1) = ${logic(1)}`);
console.log(`logic(7) = ${logic(7)}`);
console.log(`logic(10) = ${logic(10)}`);
console.log(`logic(25) = ${logic(25)}`);
console.log(`logic(100) = ${logic(100)}`);
console.log(`logic(12345) = ${logic(12345)}`);