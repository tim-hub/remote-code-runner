# Remote Code Runner

Remote Code Runner is a simple service for running code on remote server side.

# Install

Environment:

- Ubuntu Linux 18.04
- Docker
- Python3

```
$ sudo apt install git docker.io python3
```

Get source:

```
$ git clone https://github.com/michaelliao/remote-code-runner.git 
```

Download required docker images:

```
$ python3 list_images.py
sudo docker run -t --rm openjdk:14-slim ls
sudo docker run -t --rm python:3.8-slim ls
sudo docker run -t --rm ruby:2.7-slim ls
sudo docker run -t --rm node:13.12-slim ls
sudo docker run -t --rm gcc:9.3 ls
```

Copy and execute the output commands to force docker download required images to local. This may take a long time.

Start server:

```
$ sudo nohup runner.py >> ./output.log 2>&1 &
```

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
3. Execute command like `sudo docker run -t --rm -w /app -v /tmp/dir:/app <image-tag> python3 main.py`;
4. Write output into API response.

# Limitation

- Multiple files are not supported.
- There is no way to read input from console. Any user input code will cause timeout.

# Extension

How to add a new language:

1. Add configuration in `config.json`:

```
{
    ...
    "languages": {
        ...
        "node": {
            "file": "main.js",
            "image": "node:13.12-slim",
            "command": "node main.js"
        }
    }
}
```

The key `node` is the language name.

2. Make sure image is downloaded on local:

```
$ sudo docker run -t --rm node:13.12-slim ls
```

3. Restart `runner.py`.
