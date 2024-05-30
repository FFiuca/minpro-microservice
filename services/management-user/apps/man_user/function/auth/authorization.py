
class Authorization:

    def check_authorization(self, user, group, permission):
        return {
            'group': self.check_group(user, group),
            'permission': self.check_group(user, permission)
        }


    def check_group(self, user, group):
        check = isinstance(group, (str, list))
        if not check:
            return False

        data = []
        data.extend(group)

        res = {}
        for r in data:
            res[r] = user.groups.filter(name=r).exists()

        return res

    def check_permission(self, user, permission):
        check = isinstance(permission, (str, list))
        if not check:
            return False

        data = []
        data.extend(permission)

        res = {}
        for r in data:
            res[r] = user.has_perms(r)

        return res
