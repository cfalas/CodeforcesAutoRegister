# Codeforces Auto-Registration
This is a simple script that can register you to the next [Codeforces](http://codeforces.com) round. It will open a Chrome browser, find the next contest and register the account provided.

# Usage
## Configure
After cloning this repository, it is quite simple to use this script. 
Open the file register.py with your favorite text editor. Change the contents of lines 3, 4 and 5 to match your details. For example, I would change line 3 from 

    username =  "USERNAME"
to

    username =  "cfalas"
Don't remove the quotes!
Line 4 should contain in a similar way your password and line 5 should contain the path to the chromedriver path, which is needed for the script to run. You can download it from [here](https://chromedriver.chromium.org/downloads)

## Run
After completing the changes required to the script, you are ready to run it. You can do that either by running the command

    python register.py
   from a terminal, or by running
   

    chmod +x register.py
    ./register.py