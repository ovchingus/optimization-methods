f = x => x ** 3 - x
let [a, b] = [0.4094, 0.819]
l = 0.001

function dichotomies(a0, b0, accuracy) {
  let x;
  let step = 1
  while (Math.abs(b0 - a0) > accuracy) {
    console.log('Шаг ' + step++ + ' x = ' + x + ' a0 = ' + a0 + ' b0 = ' + b0)
    x = (a0 + b0) / 2;
    f(x - accuracy / 2) > f(x + accuracy / 2) ? (a0 = x) : (b0 = x);
  }
  console.log((a0 + b0) / 2);
}

dichotomies(a,b,l)
