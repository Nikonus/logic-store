// Auto logic (2025_11_29) token=8e7448b3

function logic(n) {
    let v = n;
    const t = "8e7448b3";
    for (let i = 0; i < t.length; i++) {
        v = (v * 5 + t.charCodeAt(i)) ^ i;
    }
    return v;
}

console.log(logic(10));
