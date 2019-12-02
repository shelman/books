#!/usr/bin/env bash

pushd .git/hooks
rm pre-commit
ln -s ../../hooks/pre-commit pre-commit
popd
