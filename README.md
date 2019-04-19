Getting Started
---
Install dependencies

    ```
    pip install -r requirements.txt
    ```
    
Starting the Server
---
    pypi-server -P .htpasswd -p 8080 packages
    

Upload to private PyPI server
---
Add to .pypirc file
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
    
Run the following command:
        ```
        python setup.py sdist upload -r mypypiserver
        ```
