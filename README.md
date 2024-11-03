#### Customize VsCode settings

- [vs-code-settings](https://dev.to/softwaredotcom/vs-code-settings-you-should-customize-5e75)
- [top-10s-vscode-settings](https://dev.to/bhagatparwinder/top-10-vs-code-settings-1bkm)
- [set windows terminal as default one](https://offering.solutions/blog/articles/2020/03/24/setting-windows-terminal-as-default-external-terminal-in-visual-studio-code/)
- [customize fonts](https://dev.to/solexy79/installing-a-new-font-for-vs-code-in-three-3-simple-steps-13a5)
- copy settings to local drive.

```
cp settings.json /mnt/<drive_replace_me>/Users/<userId_replace_me_here>/AppData/Roaming/Code/User/settings.json
```

#### I choose `Carmel Case`

- [effective-variable-naming-in-programming-camelcase-vs-snake-case](https://medium.com/@eusdima/effective-variable-naming-in-programming-camelcase-vs-snake-case-a026e3037792#:~:text=For%20example%2C%20JavaScript%20and%20Java%20developers%20typically,use%20CamelCase%2C%20while%20Python%20developers%20prefer%20snake_case.)

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

#### tips:

https://github.com/guettli/python-tips

#### notes:

https://stackoverflow.com/search?tab=votes&q=user%3a229602%20%5bpython%5d&searchOn=3
https://stackoverflow.com/users/125382/mak
https://stackoverflow.com/users/633961/guettli
