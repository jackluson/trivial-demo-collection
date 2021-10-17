const thrift = require("thrift");
const UserService = require("./gen-nodejs/UserService.js");
const ttypes = require("./gen-nodejs/user_types");

const connection = thrift.createConnection("localhost", 7911, {});
const client = thrift.createClient(UserService, connection);

connection.on("error", function (err) {
  console.error(err);
});

function addUser(user) {
  client.addUser(user, function (err) {
    console.log("err", err);
    if (err) {
      console.error(err);
    } else {
      console.log("user added", user.id);
    }
  });
}

function getUser(userId) {
  client.getUser(userId, function (err, response) {
    console.log("response", response);
    if (err) {
      console.error(err);
    } else {
      console.log("get user", response);
    }
  });
}

const user = new ttypes.User({
  id: "2",
  name: "shadowingszy",
  age: 22,
});
addUser(user);

getUser("2");
