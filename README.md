# KLeaner
Keep you system tidy. Schedule automatic cleaning jobs for you linux files and folder.

```
,--. ,--.,--.
|  .'   /|  |    ,---.  ,--,--.,--,--,  ,---. ,--.--.
|  .   ' |  |   | .-. :' ,-.  ||      \| .-. :|  .--'
|  |\   \|  '--.\   --.\ '-'  ||  ||  |\   --.|  |
`--' '--'`-----' `----' `--`--'`--''--' `----'`--'
```

## Setup Instructions

### Make environment
```shell
virtualenv -p python3 venv
```

### Install Requirements
```shell
pip3 install -r requirements.txt
```

## Run Instructions

### Modify `config.yml`

Modify `config.yml` according to you need. More details [link](README.md#more-about-config).

### Run `kleaner.py`

```shell
python kleaner.py
```

---

## More about config

In config Kleaner jobs uses tags which are very much similar to linux `find`. You can find more about `find` options [here](https://linux.die.net/man/1/find).

```yaml
Job1:
    directory: '/full/path/to/dir1'          # directory to clean
    mtime: -1                                # operate on files & folders modified at most 1 hours ago
    repeat: 10                               # repeat every 10 seconds
    type: 'f'                                # operate only on files
    dry_run: True

Job2:
    directory: '/full/path/to/dir2'
    repeat: 10
    type: 'd'                                # operate only on directories
    mtime: -1
```

---

## Roadmap

- [x] Basic implementation of Kleaner
- [x] Add README.md
- [ ] Give repeat more flexibility. Should be able to put cronjob like syntax.
- [ ] Package Kleaner
