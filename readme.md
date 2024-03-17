# proglang.informatik.uni-freiburg.de

## usage

- `./publish "message"`
  - (1) all changes are pushed to `master`
  - (2) local build using the `bin/mdbook-{system}` binary into `book` directory
  - (3) build contents from `book` are pushed to `live` branch
- `./watch`: 
  - (1) local build using the `bin/mdbook-{system}` binary into `book` directory
  - (2) local web server is started with address `localhost:3000`