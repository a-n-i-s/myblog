from .models import UserSetting
def usersettings(self):
  if self.user.is_authenticated:
    setting=self.user.usersetting
    return {
      'settings':setting,
    }
  return {'settings':{}}