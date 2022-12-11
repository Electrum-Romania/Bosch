let slider1 = document.getElementById("minVal");
let output1 = document.getElementById("minVal-value");
output1.innerHTML = slider1.value;
slider1.oninput = function() {
    output1.innerHTML = this.value;
}

let slider2 = document.getElementById("maxVal");
let output2 = document.getElementById("maxVal-value");
output2.innerHTML = slider2.value;
slider2.oninput = function() {
    output2.innerHTML = this.value;
}

