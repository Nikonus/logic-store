// Auto logic 2025_11_30, token=6fcb3122
function logic(n) {
    let v = n;
    const t = "6fcb3122";
    for (let i = 0; i < t.length; i++) {
        v = (v * 5 + t.charCodeAt(i)) ^ i;
    }
    return v;
}

console.log(logic(10));
