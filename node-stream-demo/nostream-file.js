const http = require('http')
const fs = require('fs')

const server = http.createServer(function(req, res) {
  fs.readFile(__dirname + '/README.md', 'utf8', (err, data) => {
    console.log("🚀 ~ fs.readFile ~ data", data)
    res.writeHead(200, {
      'Content-Type': 'text/plain;charset=utf8'
    });
    res.end(data)
  })
})
server.listen(3000)
