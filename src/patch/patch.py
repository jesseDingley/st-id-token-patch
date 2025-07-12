import re
import importlib.util

def mod_authcallbackhandler() -> None:
    """
    Hack to return ID Token from st.login()
    """

    spec = importlib.util.find_spec("streamlit.web.server.oauth_authlib_routes")
    if not spec or not spec.origin:
        raise ImportError("Could not locate streamlit.web.server.oauth_authlib_routes")

    oauth_fpath = spec.origin

    with open(oauth_fpath, "r") as f:
        content = f.read()

    if "user.update" in content:
        return

    pattern = r'user = cast\("dict\[str, Any\]", token\.get\("userinfo"\)\)'

    replacement = (
        'user = cast("dict[str, Any]", token.get("userinfo"))\n'
        '        user.update({\n'
        '            "id_token": token["access_token"]\n'
        '        })\n'
    )

    new_content = re.sub(pattern, replacement, content)

    with open(oauth_fpath, "w") as f:
        f.write(new_content)


mod_authcallbackhandler()