from fireREST76.defaults import API_RELEASE_660
from fireREST76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Timezone'
    CONTAINER_PATH = '/object/timezoneobjects/{uuid}'
    PATH = '/object/timezoneobjects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
