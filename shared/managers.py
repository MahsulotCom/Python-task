from django.db import models


class BaseManager(models.Manager):
    """
    A base manager class for Django models.

    This class can be used as a base class for custom managers in Django models.
    It provides a basic implementation of a manager without any additional functionality.

    Example usage:
    ```
    class MyManager(BaseManager):
        pass
    ```

    Note: This class is intended to be subclassed and extended with custom functionality.
    """

    pass
