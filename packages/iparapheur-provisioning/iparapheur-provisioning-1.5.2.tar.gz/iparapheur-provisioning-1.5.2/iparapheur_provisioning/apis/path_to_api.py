import typing_extensions

from iparapheur_provisioning.paths import PathValues
from iparapheur_provisioning.apis.paths.api_provisioning_v1_admin_tenant_tenant_id import ApiProvisioningV1AdminTenantTenantId
from iparapheur_provisioning.apis.paths.api_provisioning_v1_admin_tenant_tenant_id_desk_desk_id import ApiProvisioningV1AdminTenantTenantIdDeskDeskId
from iparapheur_provisioning.apis.paths.api_provisioning_v1_admin_tenant import ApiProvisioningV1AdminTenant
from iparapheur_provisioning.apis.paths.api_provisioning_v1_admin_tenant_tenant_id_desk import ApiProvisioningV1AdminTenantTenantIdDesk

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID: ApiProvisioningV1AdminTenantTenantId,
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK_DESK_ID: ApiProvisioningV1AdminTenantTenantIdDeskDeskId,
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT: ApiProvisioningV1AdminTenant,
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK: ApiProvisioningV1AdminTenantTenantIdDesk,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID: ApiProvisioningV1AdminTenantTenantId,
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK_DESK_ID: ApiProvisioningV1AdminTenantTenantIdDeskDeskId,
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT: ApiProvisioningV1AdminTenant,
        PathValues.API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK: ApiProvisioningV1AdminTenantTenantIdDesk,
    }
)
