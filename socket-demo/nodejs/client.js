/*
 * Desc:
 * File: /client.js
 * Project: nodejs
 * File Created: Saturday, 13th August 2022 6:40:11 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2022 Camel Lu
 */
var net = require('net');
var port = 8080;
var host = '127.0.0.1';
var client = new net.Socket();
//创建socket客户端
client.setEncoding('binary');
//连接到服务端
client.connect(port, host, function () {
  client.write('hello server');
  //向端口写入数据到达服务端
});
client.on('data', function (data) {
  console.log('from server:' + data);
  //得到服务端返回来的数据
});
client.on('error', function (error) {
  //错误出现之后关闭连接
  console.log('error:' + error);
  client.destory();
});
client.on('close', function () {
  //正常关闭连接
  console.log('Connection closed');
});
