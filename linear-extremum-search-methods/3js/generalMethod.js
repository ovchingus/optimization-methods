f = x => x ** 3 - x
let [a,b] =[0.4094, 0.819]
l = 0.01

function generalMethod(a0, b0, accuracy) {
  let x1 = a0 + accuracy;
  let x2 = b0 - accuracy;
  let step = 1
  while (b0 - a0 > accuracy) {
    console.log('Шаг ' + step++ + ' x1 = ' + x1 + ' x2 = ' + x2)
    if (f(x1) < f(x2)) {
      b0 = x2;
      x2 = x2 - accuracy;
    } else if (f(x1) > f(x2)) {
      a0 = x1;
      x1 = x1 + accuracy;
    } else if (f(x1) == f(x2)) {
      a0 = x1;
      b0 = x2;
      x1 = x1 + accuracy;
      x2 = x2 - accuracy;
    }
  }
  console.log('ответ:' + (a0 + b0) / 2);
}

generalMethod(a,b,l)
