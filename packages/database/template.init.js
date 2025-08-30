// Switch to the "bimbimclick" database
db = db.getSiblingDB("bimbimclick");

// Create a user with readWrite access to that database
db.createUser({
  user: "{username}",
  pwd: "{password}",
  roles: [
    {
      role: "readWrite",
      db: "bimbimclick"
    }
  ]
});
