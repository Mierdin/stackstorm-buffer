import requests
from st2common.runners.base_action import Action

__all__ = [
    'CreateUpdate'
]

class CreateUpdateAction(Action):

    def run(self, title, url, post_image=None):

        access_token = self.config.get('access_token')
        profile_ids = self.config.get('profile_ids')

        data = {
            "profile_ids": profile_ids,
            "text": "%s %s" % (title, url),
            "shorten": False,
            "now": True,
        }

        if post_image:
            data["media[photo]"] = post_image
            data["media[link]"] = url
            data["media[picture]"] = post_image
            data["media[title]"] = title

        resp = requests.post("https://api.bufferapp.com/1/updates/create.json", headers = {
            "Authorization": "Bearer %s" % access_token,
            "Content-Type": "application/x-www-form-urlencoded"
        }, data=data)

        if resp.status_code == 200:
            return (True, {
                "updates": resp.json()['updates'],
                "status_code": resp.status_code,
                "post_image": post_image
            })
        else:
            return (False, {
                "content": resp.content
            })
