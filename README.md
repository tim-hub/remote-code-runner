# Remote Code Runner

Remote Code Runner is a simple service for running code on remote server side.

# Usage

Using simple HTTP JSON API:

```
$ curl http://localhost:8080/run -H 'Content-Type: application/json' -d '{"lang":"python","code":"import math;print(math.pi)"}'
{"error": false, "timeout": false, "output": "3.141592653589793\n"}
```

API input:

- lang: language name, lowercase: `java`, `python`, `ruby`.
- code: language code as string: `import math;print(math.pi)`

API output:

- timeout: boolean, is timeout.
- error: boolean, is error output.
- output: string, the output of execution.

# Execution

How code are executed on the remote server side:

1. Http server `runner.py` got language name and code from API;
2. Write code into a temperary directory;
3. Execute command like `sudo docker run -v /tmp/dir:/app <image-tag> python3 main.py`;
4. Write output into API response.

# Limitation

- Multiple files are not supported.
- There is no way to read input from console. Any user input code will cause timeout.

# Extension

How to add a new language:

1. Install from `Dockerfile`:

```
# install node 13 at /opt/node-v13.12.0-linux-x64 and link to /usr/bin/node

RUN cd /opt \
  && wget https://nodejs.org/dist/v13.12.0/node-v13.12.0-linux-x64.tar.gz \
  && tar zxf node-v13.12.0-linux-x64.tar.gz \
  && rm node-v13.12.0-linux-x64.tar.gz \
  && ln -s /opt/node-v13.12.0-linux-x64/bin/node /usr/bin/node
```

2. Add configuration in `config.json`:

```
{
    ...
    "languages": {
        ...
        "node": {
            "file": "main.js",
            "command": "node main.js"
        }
    }
}
```
