#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
=================================================
作者：[郭磊]
手机：[15210720528]
Email：[174000902@qq.com]
Github：https://github.com/guolei19850528/guolei_py3_brhk
=================================================
"""
from typing import Callable

import requests
from addict import Dict
from jsonschema.validators import validate, Draft202012Validator


class ApiUrlSettings:
    URL__NOTIFY = "/notify.php"


class Api(object):
    """
    博瑞皓科 Speaker Api Class
    @see https://www.yuque.com/lingdutuandui/ugcpag/umbzsd#yG8IS
    """

    def __init__(
            self,
            base_url: str = "https://speaker.17laimai.cn/",
            token: str = "",
            id: str = "",
            version: str = "1"
    ):
        """
        @see https://www.yuque.com/lingdutuandui/ugcpag/umbzsd
        :param base_url:
        :param token:
        :param id:
        :param version:
        """
        self._base_url = base_url
        self._token = token
        self._id = id
        self._version = version

    @property
    def base_url(self):
        """
        base url
        :return:
        """
        return self._base_url[:-1] if self._base_url.endswith("/") else self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    def post(
            self,
            url: str = "",
            params: dict = None,
            data: dict = None,
            kwargs: dict = None,
            custom_callable: Callable = None
    ):
        """
        use requests.post
        :param url: requests.post(url=url,params=params,data=data,**kwargs) url=base_url+url if not pattern ^http else url
        :param params: requests.post(url=url,params=params,data=data,**kwargs)
        :param data: requests.post(url=url,params=params,data=data,**kwargs)
        :param kwargs: requests.post(url=url,params=params,data=data,**kwargs)
        :param custom_callable: custom_callable(response) if isinstance(custom_callable,Callable)
        :return:custom_callable(response) if isinstance(custom_callable,Callable) else addict.Dict instance
        """
        if not Draft202012Validator({"type": "string", "minLength": 1, "pattern": "^http"}).is_valid(url):
            url = f"/{url}" if not url.startswith("/") else url
            url = f"{self.base_url}{url}"
        kwargs = Dict(kwargs) if isinstance(kwargs, dict) else Dict()
        response = requests.post(
            url=url,
            params=params,
            data=data,
            **kwargs.to_dict()
        )
        if isinstance(custom_callable, Callable):
            return custom_callable(response)
        if response.status_code == 200:
            json_addict = Dict(response.json())
            if Draft202012Validator({
                "type": "object",
                "properties": {
                    "errcode": {
                        "oneOf": [
                            {"type": "integer", "const": 0},
                            {"type": "string", "const": "0"},
                        ],
                    },
                    "errmsg": {"type": "string", "enums": ["ok", "OK", "Ok", "oK"]}
                },
                "required": ["errcode", "errmsg"]
            }).is_valid(json_addict):
                return True
        return False

    def request(
            self,
            method: str = "GET",
            url: str = "",
            params: dict = None,
            data: dict = None,
            kwargs: dict = None,
            custom_callable: Callable = None
    ):
        """
        use requests.request
        :param method: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param url: requests.request(method=method,url=url,params=params,data=data,**kwargs) url=base_url+url if not pattern ^http else url
        :param params: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param data: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param kwargs: requests.request(method=method,url=url,params=params,data=data,**kwargs)
        :param custom_callable: custom_callable(response) if isinstance(custom_callable,Callable)
        :return:custom_callable(response) if isinstance(custom_callable,Callable) else addict.Dict instance
        """
        if not Draft202012Validator({"type": "string", "minLength": 1, "pattern": "^http"}).is_valid(url):
            url = f"/{url}" if not url.startswith("/") else url
            url = f"{self.base_url}{url}"
        kwargs = Dict(kwargs) if isinstance(kwargs, dict) else Dict()
        response = requests.request(
            method=method,
            url=url,
            params=params,
            data=data,
            **kwargs.to_dict()
        )
        if isinstance(custom_callable, Callable):
            return custom_callable(response)
        if response.status_code == 200:
            json_addict = Dict(response.json())
            if Draft202012Validator({
                "type": "object",
                "properties": {
                    "errcode": {
                        "oneOf": [
                            {"type": "integer", "const": 0},
                            {"type": "string", "const": "0"},
                        ],
                    },
                    "errmsg": {"type": "string", "enums": ["ok", "OK", "Ok", "oK"]}
                },
                "required": ["errcode", "errmsg"]
            }).is_valid(json_addict):
                return True
        return False

    def notify(
            self,
            message: str = None,
    ):
        validate(instance=message, schema={"type": "string", "minLength": 1})
        data = Dict({})
        data.setdefault("token", self.token)
        data.setdefault("id", self.id)
        data.setdefault("version", self.version)
        data.setdefault("message", message)
        return self.post(url=ApiUrlSettings.URL__NOTIFY, data=data.to_dict())
