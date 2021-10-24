//
// Autogenerated by Thrift Compiler (0.14.2)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//

import thrift = require('thrift');
import Thrift = thrift.Thrift;
import Q = thrift.Q;
import Int64 = require('node-int64');

import ttypes = require('./user_types');
import User = ttypes.User

declare class Client {
    private output: thrift.TTransport;
    private pClass: thrift.TProtocol;
    private _seqid: number;

    constructor(output: thrift.TTransport, pClass: { new(trans: thrift.TTransport): thrift.TProtocol });

    addUser(user: User): Promise<void>;

    addUser(user: User, callback?: (error: void, response: void)=>void): void;

    getUser(id: string): Promise<User>;

    getUser(id: string, callback?: (error: void, response: User)=>void): void;
  }

declare class Processor {
  private _handler: object;

  constructor(handler: object);
  process(input: thrift.TProtocol, output: thrift.TProtocol): void;
    process_addUser(seqid: number, input: thrift.TProtocol, output: thrift.TProtocol): void;
    process_getUser(seqid: number, input: thrift.TProtocol, output: thrift.TProtocol): void;
}