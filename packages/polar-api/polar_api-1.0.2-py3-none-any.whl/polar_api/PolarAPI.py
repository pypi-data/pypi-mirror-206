# %%
import base64
import json
import os
import time
import webbrowser
from typing import Union
from urllib.parse import parse_qs, urlencode, urlparse

import requests


class PolarTeamproAPI:
    BASE_URL = "https://teampro.api.polar.com"
    AUTH_URL = "https://auth.polar.com/"
    AUTH_ENDPOINT = "oauth/authorize?"
    TOKEN_ENDPOINT = "oauth/token?"

    def __init__(
        self, client_id: str, client_secret: str, redirect_uri: str, version: str = "v1"
    ) -> None:
        self.VERSION = version
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri
        self.REFRESH_TOKEN = None

        # Token init
        self.HOME_DIR = (
            os.getenv("HOME") or os.getenv("HOMEPATH") or os.getenv("USERPROFILE")
        )
        self.TOKEN_CACHE_DIR = os.getenv("SSI_TOKEN_CACHE") or "."

    # Helpers
    ## ----- OLD SEMI AUTOMATED FETCHING ----- ##
    # def _cache_token(self, id: str) -> str:
    #     return f"polar_auth_token_{id}"

    # def _get_cached_tokens(self, token_file: str) -> str:
    #     if os.path.exists(token_file):
    #         with open(token_file, "r") as f:
    #             token = json.load(f)
    #             return token

    def _get_auth_header(self):
        auth_string = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        auth_string_encoded = auth_string.encode("ascii")
        auth_string_decoded = base64.b64encode(auth_string_encoded).decode("ascii")
        return auth_string_decoded

    # def _retrieve_access_token_manual(self, auth_url: str) -> str:
    #     webbrowser.open(auth_url, new=2)
    #     auth_code = input("Authorization Code: ")

    #     return auth_code

    # def _get_access_token(self):
    #     cached_token = self._cache_token(id=self.CLIENT_ID)
    #     token_file = f"{self.TOKEN_CACHE_DIR}/{cached_token}.json"

    #     access_token = self._get_cached_tokens(token_file=token_file)

    #     if access_token != None and time.time() <= access_token["expires"]:
    #         return access_token["access_token"]

    #     new_tokens = self._fetch_tokens()

    #     with open(token_file, "w+") as f:
    #         new_tokens_out = json.dumps(new_tokens)
    #         f.write(new_tokens_out)
    #     return new_tokens["access_token"]

    # def _get_refresh_token(self, refresh_token: str):
    #     headers = {
    #         "Authorization": f"Basic {self._get_auth_header()}",
    #         "Content-Type": "application/x-www-form-urlencoded",
    #     }
    #     data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    #     response = requests.post(
    #         self.AUTH_URL + self.TOKEN_ENDPOINT, headers=headers, data=data
    #     )
    #     token_data = response.json()
    #     self._set_tokens(token_data)

    ## ----- NEW MANUAL FETCHING ----- ##
    def create_authorization_url(self, state: str = None) -> str:
        params = {
            "client_id": self.CLIENT_ID,
            "response_type": "code",
            "scope": "team_read",
            "redirect_uri": self.REDIRECT_URI,
        }
        if state:
            params["state"] = state
        return self.AUTH_URL + self.AUTH_ENDPOINT + urlencode(params)

    def fetch_authorization_code(self, url: str) -> str:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        code = query_params.get("code", [None])[0]
        return code

    def _fetch_tokens(self, authorization_code: str) -> None:
        headers = {
            "Authorization": f"Basic {self._get_auth_header()}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": self.REDIRECT_URI,
        }

        response = requests.post(
            self.AUTH_URL + self.TOKEN_ENDPOINT, headers=headers, data=data
        )
        token_data = response.json()
        # token_data["expires"] = time.time() + token_data["expires_in"]

        return token_data

    def set_access_token(self, authorization_code: str) -> None:
        tokens = self._fetch_tokens(authorization_code=authorization_code)
        self.ACCESS_TOKEN = tokens["access_token"]
        self.HEADERS = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.ACCESS_TOKEN,
        }

    # Request helpers

    def _url(self, *route) -> str:
        return "{base}/{version}/{route}".format(
            base=self.BASE_URL,
            version=self.VERSION,
            route="/".join(str(r) for r in route),
        )

    def _get_route_json(self, *route, **params) -> dict:
        for param, val in params.items():
            if isinstance(param, bool):
                params[param] = json.dumps(val)  # So that True -> 'true'
        r = requests.get(self._url(*route), headers=self.HEADERS, params=params)
        return r.json()

    # Team

    def get_team(self, page: int = None, per_page: int = None) -> dict:
        return self._get_route_json("teams", page=page, per_page=per_page)

    def get_team_details(self, team_id: str) -> dict:
        return self._get_route_json("teams", team_id)

    # Team training sessions

    def get_team_training_session(
        self,
        team_id: str,
        since: str = None,
        until: str = None,
        page: int = None,
        per_page: int = None,
    ) -> dict:
        return self._get_route_json(
            "teams",
            team_id,
            "training_sessions",
            since=since,
            until=until,
            page=page,
            per_page=per_page,
        )

    def get_team_training_session_detail(self, training_session_id: str) -> dict:
        return self._get_route_json("teams", "training_sessions", training_session_id)

    # Player training sessions

    def get_player_training_session(
        self,
        player_id: str,
        since: str = None,
        until: str = None,
        type: str = None,
        page: int = None,
        per_page: int = None,
    ) -> dict:
        return self._get_route_json(
            "players",
            player_id,
            "training_sessions",
            since=since,
            until=until,
            type=type,
            page=page,
            per_page=per_page,
        )

    def get_player_training_session_detail(
        self, player_session_id: str, samples: Union[str, list[str]] = "all"
    ) -> dict:
        """_summary_

        Args:
            player_session_id (str): _description_
            samples (str | list[str]): Include requested samples in response.
                                       Possible values are "all" or comma-separated list from
                                       "distance", "location", "hr", "speed", "cadence", "altitude", "forward_acceleration", "rr".

        Returns:
            dict: _description_
        """
        return self._get_route_json(
            "training_sessions", player_session_id, samples=samples
        )

    def get_player_training_session_trimmed(self, player_session_id: str) -> dict:
        return self._get_route_json(
            "training_sessions", player_session_id, "session_summary"
        )
