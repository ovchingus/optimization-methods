const eps = 0.0001;

const f = x => x**3 - x;

function pr(x0, x1, h) {
  h = h * 2;
  x1 = x0 + h;
  console.log(x0, x1);
  if (f(x0) > f(x1)) {
    pr(x1, x1 + eps, h);
  } else {
    return;
  }
}

function run() {
  let a = 0,
    b = 1,
    x0 = a,
    x1 = 0,
    h = 0;

  if (f(x0) > f(x0 + eps)) {
    x1 = x0 + eps;
    h = eps;
  } else if (f(x0) > f(x0 - eps)) {
    x1 = x0 - eps;
    h = -eps;
  }

  pr(x0, x1, h);
}

run();
