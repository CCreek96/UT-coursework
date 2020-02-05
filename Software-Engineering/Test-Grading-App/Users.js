var Users=[{
  username:"Carlos",
  password:"OUsucks"
},
{
  username:"Isai",
  password:"40acres"
},
{
  username:"Robert",
  password:"hookem16"
}]

var Admins=[{
  username:"Sam",
  password:"longhorn69"
},
{
  username: "Connor",
  password:"vyoung05"
},
{
  username:"Evan",
  password:"bevo420"
}]

var Requests =[]

function addUser(userName1, password1){
    var temp = false;
    for (i=0; i<Users.length; i++){
        if (userName1 == Users[i].username){
            temp = true;
        }

    }
    if (temp != true){
    Users.push({username:userName1, password: password1})
    }
}

function removeUser(username){
    for (i=0; i<Users.length; i++){
        if (username== Users[i].username){
            delete Users[i]
        }
    }
}
function adminCheck(username,password)
{
    for (i=0; i<Admins.length;i++){
        if(username == Admins[i].username && password == Admins[i].password){
            found = true;
            document.location= "admin-main.html";

        }

    }
}
function userCheck(username, password){
    for (i=0; i<Users.length;i++){
        if(username == Users[i].username && password == Users[i].password){
            found = true;
            document.location = "user-main.html";
        }
    }
}

function requestChecker(username,password) {
    var found = false;
    for (j=0; j<Requests.length; j++){
        for (i=0; i<Users.length; i++){
            if(Users[i].usernmane ==Requests[j].username){
                found= true;

            }
        }
    }
    for (j=0; j<Requests.length; j++){
        for (i=0; i<Admins.length; i++){
            if(Admins[i].usernmane ==Requests[j].username){
                found = true;
            }
        }
    }
    if (found ==false){
        addRequest(username, password)
    } else {
        window.alert('Username already exists')
    }
}

function removeRequest(username, password){
    for (i=0; i<Requests.length; i++){
        if (username== Request[i].username){
            delete Requests[i]
        }
    }
}
function addRequest(userName1,password1){
    var temp = false;
    for (i=0; i<Requests.length; i++){
        if (userName1 == Requests[i].username){
            temp = true;
        }

    }
    if (temp != true){
    Requests.push({username:userName1, password: password1})
}
}
function displayRequests(){
        console.log(Requests)
    }
function displayUsers(){
    console.log(Users)
}
