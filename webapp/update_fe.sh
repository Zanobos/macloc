#!/usr/bin/env bash

#To be runned as sudo

git pull                                            # Fetch the new code
npm install
npm run build
cp dist/* /var/www/html