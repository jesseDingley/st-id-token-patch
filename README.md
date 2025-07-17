# Streamlit ID Token Patch

Monkey Patch to return and include ID Token in the `user` object when calling `st.login()`.

On installation, this patch will make a modifiction to `streamlit/web/server/oauth_authlib_routes.py` in your current environment, so make sure you already have streamlit installed.

## Installation and Usage

To install and execute the patch, run `pip install .`

To install as an external package, add 

```streamlit-id-token-patch @ git+https://github.com/jesseDingley/streamlit-id-token-patch.git@main#egg=streamlit-id-token-patch``` 

to your `requirements.txt` 