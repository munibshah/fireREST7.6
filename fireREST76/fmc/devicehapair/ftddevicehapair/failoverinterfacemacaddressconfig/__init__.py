from fireREST76.defaults import API_RELEASE_630
from fireREST76.fmc import ChildResource


class FailoverInterfaceMacAddressConfig(ChildResource):
    CONTAINER_NAME = 'FtdDeviceHAPair'
    CONTAINER_PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    PATH = '/devicehapairs/ftddevicehapairs/{container_uuid}/failoverinterfacemacaddressconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
