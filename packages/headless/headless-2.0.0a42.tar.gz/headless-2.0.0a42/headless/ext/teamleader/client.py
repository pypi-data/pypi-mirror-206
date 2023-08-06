# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any
from typing import AsyncGenerator
from typing import TypeVar

from headless.core.httpx import Client
from headless.types import ICredential, IResource


M = TypeVar('M', bound=IResource)


class TeamleaderClient(Client):
    __module__: str = 'headless.ext.teamleader'
    base_url: str = "https://api.focus.teamleader.eu"

    def __init__(self, *, credential: ICredential | None = None, **kwargs: Any):
        super().__init__(base_url=self.base_url, credential=credential, **kwargs)

    async def retrieve(
        self,
        model: type[M],
        resource_id: int | str | None = None
    ) -> M:
        meta = model.get_meta()
        response = await self.post(
            url=model.get_retrieve_url(resource_id),
            json={'id': str(resource_id)},
            headers=meta.headers
        )
        response.raise_for_status()
        self.check_json(response.headers)
        data = self.process_response('retrieve', await response.json())
        return self.resource_factory(model, 'retrieve', data)
    
    async def listall(
        self,
        model: type[M],
        *params: Any,
        url: str | None = None,
        iteration: int = 0
    ) -> AsyncGenerator[M, None]:
        iteration += 1
        page_size: int = 100
        meta = model.get_meta()
        response = await self.request(
            method='POST',
            url=url or model.get_list_url(*params),
            json={
                'page': {
                    'size': page_size,
                    'number': iteration
                },
                #'sort': [
                #    {
                #        'field': 'added_at',
                #        'order': 'asc'
                #    }
                #]
            },
            headers=meta.headers
        )
        print(response.content)
        response.raise_for_status()
        self.check_json(response.headers)
        data = self.process_response('list', await response.json())
        data = model.process_response('list', data)
        resources = [
            self.resource_factory(model, None, x)
            for x in data
        ]
        if not resources:
            return
        while resources:
            yield resources.pop(0)
        async for resource in self.listall(model, *params, iteration=iteration):
            yield resource