const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/plain;charset=utf8'
  });
  const stream = fs.createReadStream(__dirname + '/README.md')
  stream.pipe(res)
})
server.listen(3000)
