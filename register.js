const path = require("path");

const ProtocolRegistry = require("protocol-registry");

console.log("Registering...");
// Registers the Protocol
ProtocolRegistry.register({
  protocol: "gr", // sets protocol for your command , gr://**
  // command: `./run.sh $_URL_ && python ${path.join(__dirname, "./handle_url.py")}  `, // this will be executed with a extra argument %url from which it was initiated
  command: `${path.join(__dirname, "./run.sh")} $_URL_`, // this will be executed with a extra argument %url from which it was initiated
  override: true, // Use this with caution as it will destroy all previous Registrations on this protocol
  terminal: true, // Use this to run your command inside a terminal
  script: true,
}).then(async () => {
  console.log("Successfully registered");
});
