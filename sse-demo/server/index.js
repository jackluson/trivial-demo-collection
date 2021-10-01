var http = require("http");

http
  .createServer(function (req, res) {
    var fileName = "." + req.url;
    let now = Date.now();
    if (fileName === "./stream") {
      console.log("now", now);
      res.writeHead(200, {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
        "Access-Control-Allow-Origin": "*",
      });
      res.write("retry: 10000\n");
      res.write("event: connecttime\n");
      res.write("data: " + new Date() + "\n\n");
      res.write("data: " + new Date() + "\n\n");

      interval = setInterval(function () {
        res.write("data: " + new Date() + "\n\n");
        console.log("Date.now() - now", Date.now() - now);
        // if (Date.now() - now > 5000) {
        //   clearInterval(interval);
        // }
      }, 1000);
      // 重新建立连接,会先触发close事件
      req.connection.addListener(
        "close",
        function () {
          console.log("close", Date.now());
          clearInterval(interval);
        },
        false
      );
    }
  })
  .listen(8844, "127.0.0.1");
