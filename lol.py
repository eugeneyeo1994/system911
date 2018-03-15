import json

s_config= {

"host" : '127.0.0.1',
"port" : '3306',
"user" : 'root',
"password" : 'Jiachin123',
"database" : 'cnberdynedb',

}

data=json.dumps(s_config)
with open("server_config.json","w") as file:
    file.write(data)


