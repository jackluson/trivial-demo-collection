// 创建buffer
// 1. 字符串
// const buf = Buffer.from('Hey!')

// 2. ArrayBuffer instance
let buffer = new ArrayBuffer(4);
// 主要new ArrayBuffer不是一个迭代器, TypeArray才是一个迭代器
// const buf = Buffer.from(buffer)
// buf[0] = 72

// 3. TypeArray instance
let view = new Uint8Array(buffer)
view[0] = 72
// console.log('view toString', view.toString())
// const buf = Buffer.from(view)
// 4. Array
// const buf = Buffer.from([0x48, 101, 121, 33]) 

// 5. Array Object
// const payload = {
//   [0]: 'a', // 无效
//   [1]: 'b',
//   [2]: 'c',
//   length: 3
// }

// 迭代buffer内容
// const buf = Buffer.from('您好a')
// console.log("🚀 ~ buf", buf, buf.length) // <Buffer 48 65 79 21> 对应十六进制
// for (const item of buf) {
//   console.log('item', item)
// }

// 更改 buffer 的内容

// const buf = Buffer.alloc(4)
// const buf = Buffer.allocUnsafe(4)
//虽然 alloc 和 allocUnsafe 均分配指定大小的 Buffer（以字节为单位），但是 alloc 创建的 Buffer 会被使用零进行初始化，而 allocUnsafe 创建的 Buffer 不会被初始化。 这意味着，尽管 allocUnsafe 比 alloc 要快得多，但是分配的内存片段可能包含可能敏感的旧数据。
// console.log(buf.toString())
// buf.write('Hey!')
// console.log(buf.toString())
// buf[1] = 111 //o
// console.log(buf.toString()) //Hoy!

// 复制 buffer

const buf = Buffer.from('Hey!')
// let bufcopy = Buffer.alloc(4) //分配 4 个字节。
// buf.copy(bufcopy)
// console.log(buf.toString())

let bufcopy = Buffer.alloc(2) //分配 2 个字节。
buf.copy(bufcopy, 0, 0, 2)
console.log(bufcopy.toString())

// 切片 buffer
/* 
如果要创建 buffer 的局部视图，则可以创建切片。 切片不是副本：原始 buffer 仍然是真正的来源。 如果那改变了，则切片也会改变。

使用 slice() 方法创建它。 第一个参数是起始位置，可以指定第二个参数作为结束位置：
*/
const buf = Buffer.from('Hey!')
buf.slice(0).toString() //Hey!
const slice = buf.slice(0, 2)
console.log(slice.toString()) //He
buf[1] = 111 //o
console.log(slice.toString()) //Ho

