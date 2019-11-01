f = x => x ** 3 - x
let [a,b] =[0.4094, 0.819]

function calcFib(n) {
  let f,
    f1 = 1,
    f2 = 1,
    m = 0;
  while (m < n - 1) {
    f = f1 + f2;
    f1 = f2;
    f2 = f;
    ++m;
  }
  return f1;
}

function fib(x1, x2, a, b, y1, y2, n) {
  if (n > 1) {
    n--;
    if (y1 > y2) {
      a = x1;
      x1 = x2;
      x2 = b - (x1 - a);
      y1 = y2;
      y2 = f(x2);
    } else {
      b = x2;
      x2 = x1;
      x1 = a + (b - x2);
      y2 = y1;
      y1 = f(x1);
    }
    // console.log(x1, x2, a, b, n);
    console.log('N = ' + n + ' x1 = ' + x1 + ' x2 = ' + x2 + ' a= ' + a + ' b= ' + b)
  }
  if (n == 1) {
    console.log((x1 + x2) / 2);
    return;
  } else {
    fib(x1, x2, a, b, y1, y2, n);
  }
}

function main() {

    n = 18;
  let x1 = a + ((b - a) * calcFib(n - 2)) / calcFib(n),
    x2 = a + ((b - a) * calcFib(n - 1)) / calcFib(n);
  let y1 = f(x1),
    y2 = f(x2);
  console.log(x1, x2, a, b, n);
  fib(x1, x2, a, b, y1, y2, n);
  return 0;
}
main();
