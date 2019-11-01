f = x => x ** 3 - x
let [a,b] =[0.4094, 0.819]
l = 0.001

const phi = 0.5 * (1.0 + Math.sqrt(5.0));
let count = 0;

function minimize(eps, a, b) {
  if (Math.abs(b - a) < eps) {
    console.log((a + b) / 2);
  } else {
    count++;
    t = (b - a) / phi;
    x1 = b - t;
    x2 = a + t;
    console.log('шаг ' + count + ' x1= ' + x1 + ' x2= ' + x2 + ' a= ' + a + ' b= ' + b);
    if (f(x1) >= f(x2)) {
      minimize(eps, x1, b);
    } else {
      minimize(eps, a, x2);
    }
  }
}

minimize(l, a, b);
