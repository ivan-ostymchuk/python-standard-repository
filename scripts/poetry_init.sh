#!/usr/bin/env bash

install_poetry() {
  if [[ "$OSTYPE" =~ ^darwin ]]; then
      brew install poetry && pip install poetry-plugin-export
  fi

  if [[ "$OSTYPE" =~ ^linux ]]; then
      sudo apt-get install poetry && pip install poetry-plugin-export
  fi
}

install_dependencies() {
  poetry install --sync
}

update_dependencies() {
  poetry update
}

show_dependencies() {
  echo -en '\n Showing installed dependencies . . . \n'
  poetry show
}

pre_commit_hooks() {
  echo -en '\n Installing pre-commit and pre-push hooks . . . \n'

  if [[ "$OSTYPE" =~ ^darwin ]]; then
      brew install pre-commit && pre-commit install
  fi

  if [[ "$OSTYPE" =~ ^linux ]]; then
      sudo apt-get install pre-commit && pre-commit install
  fi
}

pre_commit_autoupdate() {
  echo -en '\n pre-commit autoupdate . . . \n'
  poetry run pre-commit autoupdate
}

setup_environment() {
  install_poetry
  install_dependencies
  update_dependencies
  show_dependencies
  pre_commit_hooks
  pre_commit_autoupdate
}

setup_environment

$SHELL
