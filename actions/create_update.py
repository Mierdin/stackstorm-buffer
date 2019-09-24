import requests
from st2common.runners.base_action import Action

__all__ = [
    'CreateUpdate'
]

class CreateUpdateAction(Action):

    def run(self, title, url):

        access_token = self.config.get('access_token')
        profile_ids = self.config.get('profile_ids')

        resp = requests.post("https://api.bufferapp.com/1/updates/create.json", headers = {
            "Authorization": "Bearer %s" % access_token,
            "Content-Type": "application/x-www-form-urlencoded"
        }, data={
            "profile_ids": profile_ids,
            "text": "%s %s" % (title, url),
            "shorten": False,
            "now": True
        })

        if resp.status_code == 200:
            return (True, {
                "post_id": resp.json().get['updates'],
                "status_code": resp.status_code
            })
        else:
            return (False, {
                "content": resp.content
            })
