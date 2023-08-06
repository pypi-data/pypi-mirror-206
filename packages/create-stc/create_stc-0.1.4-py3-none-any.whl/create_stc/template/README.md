## Prerequisites

Streamlit

You should create virtual environment

``` bash
python -m venv .venv
```

Then base on your distribution, you can activate the virtual environment by:

``` bash
. .venv/bin/activate
```

Now you need to install streamlit in your virtual environment

``` bash
pip install streamlit
```

Install **wheel** package if you want to build your component

``` bash
pip install wheel
```

## Development mode

Open a new terminal to display frontend stream component

``` bash
cd your_component_name/frontend
npm install
npm start
```

Open a new terminal to run streamlit

``` bash
streamlit run main.py
```

## Production mode

**Important**: Go to `/your_component_name/__init__.py` and set the `_RELEASE` flag to True

First go to `/your_component_name/frontend` to build the frontend stream component

``` bash
npm run build
```

Now you can build your component by:

``` bash
python setup.py sdist bdist_wheel
```

Now install your component in your environment

``` bash
pip install dist/your_component_name-version-py3-none-any.whl
```

Then change your `main.py` a little bit

``` python
import streamlit as st
from my_component import my_component

component_name, component_value = my_component()
st.write(component_name)
```
