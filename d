#!/bin/bash
rm -rfv $1
curl https://raw.githubusercontent.com/saebaxyz/v/master/$1 -o $1
chmod +x $1
