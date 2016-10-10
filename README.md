Thin Python wrapper for Solve360 API.

_optional_ Django integration.


```
from solve_threesixty.api import Solve360

solve = Solve360(user=SOLVE360_USER, password=SOLVE360_PASSWORD,
                 owner=DEFAULT_OWNER_SOLVE360_ID)
```


To avoid adding your credentials to the code base you can add a
`local_settings.py` file somewhere on your `PYTHONPATH` or add as part
of your `django.settings`.
