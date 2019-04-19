Getting Started
---
1. Install dependencies

    ```
    pip install -r requirements.txt
    ```
    
Add user or update password
---
* If the user exists, this will update the password.  Otherwise, it will create the user

* You will be prompted to enter the password twice

    ```
    htpasswd .htpasswd username
    ```
    
Starting the server locally
---
    pypi-server -P .htpasswd -p 8080 --welcome index.html  packages
    

Upload to private PyPI server
---
1. Add to .pypirc file
    ```
    [distutils]
    index-servers =
      pypi
      mypypiserver
    
    [pypi]
    repository: ....
    username: ....
    password: ....
    
    [mypypiserver]
    repository: http://pypi.server.address
    username: <user_here>
    password: <password_here>
    ```
    
2. Run the following command:
    ```
    python setup.py sdist upload -r mypypiserver
    ```

Installing from requirements.txt
---
*Add the following lines to the top of requirements.txt*
    
    --trusted-host pypi.server.com \
    --extra-index-url http://username:password@pypi.server.com \