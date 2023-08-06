# Copyright (C) 2022 Cochise Ruhulessin # type: ignore
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import decimal
from datetime import datetime

from canonical import EmailAddress
from canonical import Phonenumber

from ..resource import ShopifyResource
from .customeraddress import CustomerAddress
from .customeremailmarketingconsent import CustomerEmailMarketingConsent
from .customersmsmarketingconsent import CustomerSmsMarketingConsent
from .partialcustomeraddress import PartialCustomerAddress


class Customer(ShopifyResource):
    accepts_marketing: bool = False
    accepts_marketing_updated_at: datetime
    addresses: list[CustomerAddress | PartialCustomerAddress] = []
    currency: str
    created_at: datetime
    default_address: CustomerAddress | PartialCustomerAddress | None = None
    email: EmailAddress | None = None
    email_marketing_consent: CustomerEmailMarketingConsent | None = None
    first_name: str | None
    id: int
    last_name: str | None
    last_order_id: int | None = None
    last_order_name: str | None = None
    # metafield
    marketing_opt_in_level: str | None = None
    multipass_identifier: str | None = None
    name: str | None = None
    note: str | None = None
    orders_count: int = 0
    password: str | None = None
    password_confirmation: str | None = None
    phone: Phonenumber | None = None
    sms_marketing_consent: CustomerSmsMarketingConsent | None = None
    state: str  = 'enabled'
    tags: str
    tax_exemptions: list[str] = []
    total_spent: decimal.Decimal | None = None
    updated_at: datetime
    verified_email: bool = False

    class Meta:
        base_endpoint: str = '/2023-01/customers'