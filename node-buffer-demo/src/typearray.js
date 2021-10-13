const { Buffer } = require('buffer');

// const buf = Buffer.alloc(4);
const buf = Buffer.from([1, 2, 3, 0]); // 将 Buffer 传给 TypedArray 构造函数将复制 Buffer 的内容，解释为整数数组，而不是目标类型的字节序列。
// console.log(buf, buf.buffer, buf.length, buf.byteLength)
// console.log('toString', buf.toString())
// const uint32array = new Uint32Array(buf.buffer);
const uint32array = new Uint32Array(buf);

console.log(uint32array, uint32array.length, uint32array.byteLength);



const arr = new Uint16Array(2);

arr[0] = 5000;
arr[1] = 4000;

// 复制 `arr` 的内容。
const buf1 = Buffer.from(arr);

// 与 `arr` 共享内存。
const buf2 = Buffer.from(arr.buffer);

console.log(buf1);
// 打印: <Buffer 88 a0>
console.log(buf2);
// 打印: <Buffer 88 13 a0 0f>

arr[1] = 6000;

console.log(buf1);
// 打印: <Buffer 88 a0>
console.log(buf2);
// 打印: <Buffer 88 13 70 17>
