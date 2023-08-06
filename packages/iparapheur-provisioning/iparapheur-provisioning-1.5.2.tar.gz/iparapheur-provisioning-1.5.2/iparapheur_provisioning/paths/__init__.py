# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iparapheur_provisioning.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID = "/api/provisioning/v1/admin/tenant/{tenantId}"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK_DESK_ID = "/api/provisioning/v1/admin/tenant/{tenantId}/desk/{deskId}"
    API_PROVISIONING_V1_ADMIN_TENANT = "/api/provisioning/v1/admin/tenant"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK = "/api/provisioning/v1/admin/tenant/{tenantId}/desk"
