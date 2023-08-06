pygopac
=======

A simple library for working with pac files.

## Examples

```python
import gopac

path = gopac.download_pac_file('https://host.com/proxy.pac')
proxy = gopac.find_proxy(path, 'https://www.some-site.com')
```

You can find other usage examples in the "examples" folder.

## Build wheel

Requirements:

- python
- golang >= 1.20 (The path to the executable file `go` should be in the PATH environment variable.
  If the `go version` command is executed without errors, then everything is correctly configured.)
- access to the internet

Build dist using standard tools:

```
make build-dist
```
