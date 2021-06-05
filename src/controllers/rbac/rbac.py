import functools
from ..errors import errors


class RBAC:
    @classmethod
    def permissions_required(self, *required_perms):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                current_user = args[1]
                user_perms = current_user.get("permissions",[])
                if set(required_perms).issubset(set(user_perms)):
                    return func(*args, **kwargs)
                else:
                    raise errors.HTTPPermissionDenied
            return wrapper
        return decorator
