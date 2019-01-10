#!/usr/bin/env bash

#To be runned as sudo

npm install
npm run build
cp -r dist/* /var/www/html