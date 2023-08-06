import configparser
import os
import requests


class BlackListListChecker():

    def load_config(self,config_file:str):
        if not os.path.exists(config_file):
            raise Exception("The provided configuration file does not exists")
        config = configparser.ConfigParser()
        config.read(config_file)

        if(self.mockup):
            provider=config["mockup-1"]
        else:
            provider=config["provider-1"]
        if "provider_name" not in provider:
            self.name="mockup-1"
        else:
            self.name=provider["provider_name"]

        if provider["user"] is None:
            raise Exception("The username is mandatory. Let empty if not required")
        else:
            self.user = provider["user"]

        if provider["password"] is None:
            raise Exception("The password is mandatory. Let empty if not required")
        else:
            self.password = provider["password"]

        if provider["base_url"] is None:
            raise Exception ("The URL is mandatory")
        else:
            self.base_url=provider["base_url"]

        if provider["type_request"] is None:
           self.type_request="get"
        else:
            self.type_request=provider["type_request"]


    def __init__(self,config_file:str,mockup=False):
        self.mockup=mockup
        self.load_config(config_file)

    def handleGetRequest(self,domain):
        url=self.base_url+domain
        r=requests.get(url,auth=(self.user, self.password))
        if(r.status_code != 200):
            raise Exception("Error requesting remote url="+url+";status_Code="+str(r.status_code))
        return r.json()

    def check(self,domain:str):
        output_dict=None
        if domain is None:
            raise Exception("A domain must be provided")
        result=None

        if self.mockup:
            result=self.load_mockup(self.name)
        else:
            if str.lower(self.type_request)=="get":
                result=self.handleGetRequest(domain)
        if result is not None:
            blacklists=result["blacklists"]
            output_dict = [x for x in blacklists if x['detected'] == True]
        return output_dict




