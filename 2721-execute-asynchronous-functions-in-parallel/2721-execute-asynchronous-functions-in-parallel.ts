type Fn<T> = () => Promise<T>;

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
  return new Promise((resolve, reject) => {
    const results: T[] = new Array(functions.length);
    let remaining = functions.length;

    functions.forEach((fn, index) => {
      fn()
        .then(value => {
          results[index] = value;
          remaining -= 1;
          if (remaining === 0) {
            resolve(results);
          }
        })
        .catch(error => {
          reject(error);
        });
    });

    // Edge case: empty input
    if (functions.length === 0) {
      resolve([]);
    }
  });
}


/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */