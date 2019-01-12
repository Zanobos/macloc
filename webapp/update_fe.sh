#!/usr/bin/env bash

npm install
npm run build
cp -r dist/* /var/www/html
