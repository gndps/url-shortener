# Local url shortener
Features:
- generates url with custom://url_schema (For example: https://google.com --> myprotocol://98sh32jksf)
- local file system as storage (all shortened urls will be written to json files in url dir)

# Pre-requisites
1. nodejs must be installed on the system
2. `npm i protocol-registry`
3. python3

# How to use
## Initialize
1. Update `protocol: "myprotocol", // sets protocol for your command , myprotocol://**` in `register.js` to whatever you want your protocol to be. If you keep `myprotocol`, then the shortener urls will look like: myprotocol://98sh32jksf)
2. `node ./register.js` (This registers the protocol system wide, now the `run.sh` will handle all such urls)

## Shorten Urls
`./short https://google.com`

## Open Urls
Just open the short urls in any browser and it should be redirected to original link