// Switch to the "localbulk" database
db = db.getSiblingDB("localbulk");

// Create a user with readWrite access to that database
db.createUser({
  user: "{username}",
  pwd: "{password}",
  roles: [
    {
      role: "readWrite",
      db: "localbulk"
    }
  ]
});
