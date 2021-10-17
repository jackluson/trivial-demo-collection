const thrift = require("thrift");
const UserService = require("./gen-nodejs/UserService.js");

const users = {};
const opts = {
  transport: thrift.TBufferedTransport,
  protocol: thrift.TBinaryProtocol,
};
console.log("opts", opts);
const server = thrift.createServer(
  UserService,
  {
    addUser: function (user, result) {
      console.log("user", user);
      users[user.id] = user;
      console.log("[ADD_USER] add:", user, " current:", users);
      result(null);
    },
    getUser: function (id, result) {
      console.log("[GET_USER] get:", id);
      result(null, users[id]);
    },
  },
  opts
);

server.listen(7911);
console.log("server start");
