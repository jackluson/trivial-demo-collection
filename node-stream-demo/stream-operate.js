const Stream = require('stream')

const readableStream = new Stream.Readable({
  read() {}
})
const writableStream = new Stream.Writable()

writableStream._write = (chunk, encoding, next) => {
  console.log("🚀 ~ chunk", chunk)
  console.log(chunk.toString())
  next()
}

readableStream.on('readable', () => {
  console.log(readableStream.read())
})

readableStream.pipe(writableStream)

const res = readableStream.push('hi!')
console.log("🚀 ~ res", res)
readableStream.push('ho!你好')

const res1 = writableStream.write('hey!\n')
console.log("🚀 ~ res1", res1)
