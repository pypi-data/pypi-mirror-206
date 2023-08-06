import typing_extensions

from iparapheur_provisioning.apis.tags import TagValues
from iparapheur_provisioning.apis.tags.admin_desk_api import AdminDeskApi
from iparapheur_provisioning.apis.tags.admin_tenant_api import AdminTenantApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADMINDESK: AdminDeskApi,
        TagValues.ADMINTENANT: AdminTenantApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADMINDESK: AdminDeskApi,
        TagValues.ADMINTENANT: AdminTenantApi,
    }
)
