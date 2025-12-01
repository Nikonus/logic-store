function logic(n) {
    if (typeof n !== 'number' || !Number.isInteger(n) || n < 0) {
        return 0; 
    }

    let intermediate = n * 7 + 3; 

    let binaryIntermediate = intermediate.toString(2);
    
    const targetLength = Math.ceil(binaryIntermediate.length / 4) * 4;
    const paddedBinaryIntermediate = binaryIntermediate.padStart(targetLength, '0');

    let transformedBinaryChunks = '';
    for (let i = 0; i < paddedBinaryIntermediate.length; i += 4) {
        const chunk = paddedBinaryIntermediate.substring(i, i + 4);
        transformedBinaryChunks += chunk.split('').reverse().join('');
    }

    const finalIntermediateValue = parseInt(transformedBinaryChunks, 2);

    return (finalIntermediateValue ^ (n * 3)) + (finalIntermediateValue & n);
}

console.log(`logic(0): ${logic(0)}`);
console.log(`logic(1): ${logic(1)}`);
console.log(`logic(2): ${logic(2)}`);
console.log(`logic(3): ${logic(3)}`);
console.log(`logic(10): ${logic(10)}`);
console.log(`logic(15): ${logic(15)}`);
console.log(`logic(16): ${logic(16)}`);
console.log(`logic(12345): ${logic(12345)}`);
console.log(`logic(-5): ${logic(-5)}`); 
console.log(`logic(3.14): ${logic(3.14)}`);
console.log(`logic("hello"): ${logic("hello")}`);