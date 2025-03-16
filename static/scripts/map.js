var canvas = document.getElementById('rasterCanvas');
var ctx = canvas.getContext('2d');

var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
var data = imageData.data;

// получение данных от сервера
const url='http://127.0.0.1:5001';
let res_json = await fetch(url, {mode: "no-cors"});
let res = await res_json.json();

for (var i = 0; i < data.length; i++) {
  data[i] = res['maps'][i];
}
// -------------------------------------

ctx.putImageData(imageData, 0, 0);

var show_modules = document.getElementById("show_modules");
show_modules.addEventListener('change', function() {
    if (show_modules.checked) {
      console.log("show_modules");
    }
});

var show_bases = document.getElementById("show_bases");
show_bases.addEventListener('change', function() {
    if (show_bases.checked) {
      console.log("show_bases");
    }
});

var show_bases_cover = document.getElementById("show_bases_cover");
show_bases_cover.addEventListener('change', function() {
    if (show_bases_cover.checked) {
      console.log("show_bases_cover");
    }
});