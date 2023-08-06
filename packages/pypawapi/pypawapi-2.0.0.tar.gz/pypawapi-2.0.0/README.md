## pawapi
`pawapi` is a Python package providing access to the PythonAnywhere API.

## Install
Use `pip` to install the latest version:

```bash
 $ pip install --upgrade pypawapi --user
```

## Usage
[Get your token](https://www.pythonanywhere.com/account/#api_token)

```python
from pawapi import Pawapi, Python3

TOKEN = "<your_token>"
USER = "<your_username>"

api = Pawapi(USER, TOKEN)
cpu_usage = api.cpu.get_info()
print(cpu_usage)

domain = f"{USER}.pythonanywhere.com"
api.webapp.create(domain, Python3.PYTHON39)
app = api.webapp.list()[-1]
print(app["id"])
```

### Docs
```shell
$ python -c "import pawapi; help(pawapi.Pawapi)"
```

## LICENSE
 The MIT License (MIT)    

 Copyright (c) 2019 Maraudeur    

 Permission is hereby granted, free of charge, to any person obtaining    
 a copy of this software and associated documentation files (the    
 "Software"), to deal in the Software without restriction, including    
 without limitation the rights to use, copy, modify, merge, publish,    
 distribute, sublicense, and/or sell copies of the Software, and to    
 permit persons to whom the Software is furnished to do so, subject to    
 the following conditions:    

 The above copyright notice and this permission notice shall be included    
 in all copies or substantial portions of the Software.    

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,    
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.    
 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY    
 CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,    
 TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE    
 SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.    
