window.onload = function() {
  var cars = document.querySelectorAll("#cars img"), i = 1;
  Array.prototype.forEach.call(cars, function(car) {
	setTimeout(function(){ car.classList.add("visible") }, 700*i)
	i++;
})
};
