```javascript
function logic(n) {
    let val = n;

    // Initial bitwise scramble
    val = val ^ (val >>> 7);
    val = val * 0x1A85EB51; // Large prime multiplier
    val = val ^ (val << 13);

    // Introduce some modular arithmetic and constants
    val = val + (n % 29) * (n % 37);
    val = Math.floor(val * Math.PI);

    // Add another layer of bitwise operations, incorporating a string-based value
    let s = Math.abs(n).toString();
    let stringInfluence = 0;
    for (let i = 0; i < s.length; i++) {
        stringInfluence += parseInt(s[i], 10) * (i + 1);
    }
    val = val ^ (stringInfluence << 5);

    // Final chaotic blend using Math functions and another bitwise twist
    val = Math.floor(val * Math.abs(Math.sin(val / 1000 + n / 50))) ^ (n | 0xCAFEBABE);

    // Ensure it's an integer and not too large for consistent output, though not strictly required by prompt
    return val | 0;
}

// Example usage:
console.log("logic(0):", logic(0));
console.log("logic(1):", logic(1));
console.log("logic(10):", logic(10));
console.log("logic(42):", logic(42));
console.log("logic(12345):", logic(12345));
console.log("logic(-50):", logic(-50));
console.log("logic(987654321):", logic(987654321));
console.log("logic(Math.random() * 1000000 | 0):", logic(Math.random() * 1000000 | 0));
```