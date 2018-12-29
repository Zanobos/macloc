#!/usr/bin/env bash

#To be runned as sudo

git pull                                            # Fetch the new code
supervisorctl stop maclocbe                         # Stop the application
source venv/bin/activate                            # Activate the venv
pip install -r webserver/app/doc/requirements.txt   # Install new dependencies
cd webserver                                        # Change folder
flask db upgrade                                    # Update db
supervisorctl start maclocbe                        # Start server