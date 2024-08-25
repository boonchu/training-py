#### codesmelling with pylint/black:

- [example](https://raw.githubusercontent.com/saminarp/rwar/main/.pylintrc)

```
pylint --generate-rcfile > .pylintrc
```

#### reformatting with pre-commit:

- https://dev.to/emmo00/how-to-setup-black-and-pre-commit-in-python-for-auto-text-formatting-on-commit-4kka

```
pip install -r requirements.txt
cat <<- ECHO >|.pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        args: [--line-length=88]
        language_version: python3.10
ECHO
pre-commit install
# testing with cli prior to posting with git.
pre-commit run --all-files
```

#### notes:

https://stackoverflow.com/search?tab=votes&q=user%3a229602%20%5bpython%5d&searchOn=3
https://stackoverflow.com/users/125382/mak

```

```
