# action-setup-python-poetry

GitHub action for setting up Python and Poetry

# Usage

See [action.yml](action.yml).

Basic:

```yaml
steps:
    - uses: moneymeets/action-setup-python-poetry@master
```

With specific versions:

```yaml
steps:
    - uses: moneymeets/action-setup-python-poetry@master
      with:
        python_version: 3.10.0
        poetry_version: 1.1.11
```

With private git repository dependencies:

```yaml
steps:
    - uses: moneymeets/action-setup-python-poetry@master
      with:
        ssh_key: ${{ secrets.SSH_KEY }}
```
