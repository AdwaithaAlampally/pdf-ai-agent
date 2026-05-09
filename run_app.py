from streamlit.web import cli as stcli
import sys

sys.argv = [
    "streamlit",
    "run",
    "app.py",
    "--global.developmentMode=false",
]

sys.exit(stcli.main())