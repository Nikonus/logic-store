// Auto logic 2025_11_30, token=8e54135
function logic(n) {
    let v = n;
    const t = "8e54135";
    for (let i = 0; i < t.length; i++) {
        v = (v * 5 + t.charCodeAt(i)) ^ i;
    }
    return v;
}

console.log(logic(10));
