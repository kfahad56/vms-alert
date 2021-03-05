db = db.getSiblingDB('admin');
db.createUser({user:"trudesk",pwd:"TruDesk1",roles:[{role:"root",db:"admin"}],passwordDigestor:"server"})
db = db.getSiblingDB('trudesk');
db.createUser({user:"trudesk",pwd:"TruDesk1",roles:[{role:"dbAdmin",db:"trudesk"},{role:"readWrite",db:"trudesk"}],passwordDigestor:"server"})