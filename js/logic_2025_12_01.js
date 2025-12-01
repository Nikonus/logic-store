```javascript
function logic(n) {
    let n_abs = Math.abs(n);
    let n_str = String(n_abs);
    let accumulator = 0;

    for (let i = 0; i < n_str.length; i++) {
        let digit = parseInt(n_str[i], 10);
        if (i % 2 === 0) {
            accumulator = (accumulator + (digit * (i + 1))) ^ (digit | i);
        } else {
            accumulator = (accumulator * digit + i) & (digit ^ i);
        }
        accumulator = Math.abs(accumulator);
        accumulator = accumulator % 65537;
    }

    let result = accumulator;

    let shiftAmount = n_abs % 10;
    if (shiftAmount === 0) {
        shiftAmount = 1;
    }

    result = (result << shiftAmount) | (result >>> shiftAmount);
    result = Math.abs(result);
    result = Math.floor(Math.sqrt(result + n_str.length));

    if (n < 0) {
        result = -result;
    }

    if (n % 3 === 0) {
        result = result + (n % 5);
    } else {
        result = result ^ (n_str.length + 1);
    }
    
    return result;
}
```