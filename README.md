# Lambash
Run shell commands inside AWS lambda. Based on [lambdash][1]

## Why?
Yes.

Mainly for debugging purposes when someone needs to check how everything is inside there. You can test binaries included in lambda layers. Unfortunately, there is no state saved. Every time you press the `return/enter` key, the command is sent and executed from the original scrip location, `/var/task`.

## Deploy
We use [serverless][2] to deploy everything. You should change some of the configurations in it if you want to deploy it using your account.

## Usage
[![asciicast](https://asciinema.org/a/LCz8g4V9Wp9Mbqdq167XoSImN.svg)][3]

[1]: https://github.com/alestic/lambdash
[2]: https://www.serverless.com/
[3]: https://asciinema.org/a/LCz8g4V9Wp9Mbqdq167XoSImN
