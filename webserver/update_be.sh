#!/usr/bin/env bash

#To be runned as sudo

git pull                                            # Fetch the new code
supervisorctl stop maclocbe                         # Stop the application
source venv/bin/activate                            # Activate the venv
pip install -r app/doc/requirements.txt             # Install new dependencies
flask db upgrade                                    # Update db
supervisorctl start maclocbe                        # Start server