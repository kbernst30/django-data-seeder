workflow "Publish" {
  resolves = ["publish-to-pypi"]
  on = "release"
}

action "publish-to-pypi" {
  needs = "Master"
  uses = "mariamrf/py-package-publish-action@master"
  secrets = [
    "TWINE_USERNAME",
    "TWINE_PASSWORD",
  ]
  env = {
    BRANCH = "master"
    PYTHON_VERSION = "3.6.0"
  }
}

# Filter for master branch
action "Master" {
  uses = "actions/bin/filter@master"
  args = "branch master"
}
