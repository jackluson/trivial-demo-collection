struct User{  
    1: string id,  
    2: string name,  
    3: i16 age,
}

service UserService{
 void addUser(1: User user),
 User getUser(1: string id),
}
