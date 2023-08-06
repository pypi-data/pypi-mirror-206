r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Retrieving storage shelf information
The storage shelf GET API retrieves all of the shelves in the cluster.
<br/>
---
## Examples
### 1) Retrieve a list of shelves from the cluster
#### The following example shows the response with a list of shelves in the cluster:
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Shelf

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(Shelf.get_collection()))

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
[
    Shelf({"uid": "3109174803597886800"}),
    Shelf({"uid": "9237728366621690448"}),
    Shelf({"uid": "9946762738829886800"}),
    Shelf({"uid": "10318311901725526608"}),
    Shelf({"uid": "13477584846688355664"}),
]

```
</div>
</div>

---
### 2) Retrieve a specific shelf from the cluster
#### The following example shows the response of the requested shelf. If there is no shelf with the requested uid, an error is returned.
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Shelf

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Shelf(uid=3109174803597886800)
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
Shelf(
    {
        "voltage_sensors": [
            {
                "id": 1,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "voltage": 5.11,
                "state": "ok",
            },
            {
                "id": 2,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "voltage": 12.38,
                "state": "ok",
            },
            {
                "id": 3,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "voltage": 5.11,
                "state": "ok",
            },
            {
                "id": 4,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "voltage": 12.26,
                "state": "ok",
            },
            {
                "id": 5,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "voltage": 5.7,
                "state": "ok",
            },
            {
                "id": 6,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "voltage": 12.26,
                "state": "ok",
            },
            {
                "id": 7,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "voltage": 5.15,
                "state": "ok",
            },
            {
                "id": 8,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "voltage": 12.3,
                "state": "ok",
            },
        ],
        "module_type": "iom6",
        "state": "ok",
        "paths": [
            {
                "name": "0e",
                "node": {
                    "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
                    "name": "node-1",
                    "_links": {
                        "self": {
                            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
                        }
                    },
                },
            },
            {
                "name": "0g",
                "node": {
                    "uuid": "0530d6c1-8c6d-11e8-907f-00a0985a72ee",
                    "name": "node-1",
                    "_links": {
                        "self": {
                            "href": "/api/cluster/nodes/0530d6c1-8c6d-11e8-907f-00a0985a72ee"
                        }
                    },
                },
            },
        ],
        "id": "10",
        "internal": False,
        "local": True,
        "manufacturer": {"name": "NETAPP"},
        "serial_number": "SHU0954292N0HAH",
        "disk_count": 24,
        "ports": [
            {
                "designator": "square",
                "id": 0,
                "cable": {
                    "part_number": "112-00430+A0",
                    "length": "2m",
                    "identifier": "5001086000702488-500a098000c9edbf",
                    "serial_number": "APF16510229807",
                },
                "internal": False,
                "module_id": "a",
                "wwn": "500A098000C9EDBF",
                "state": "connected",
                "remote": {"phy": "08", "wwn": "5001086000702488"},
            },
            {
                "designator": "circle",
                "id": 1,
                "cable": {
                    "part_number": "112-00176+A0",
                    "length": "0.5-1.0m",
                    "identifier": "500a098000d5c4bf-500a098000c9edbf",
                    "serial_number": "APF133917610YT",
                },
                "internal": False,
                "module_id": "a",
                "wwn": "500A098000C9EDBF",
                "state": "connected",
                "remote": {"phy": "00", "wwn": "500A098000D5C4BF"},
            },
            {
                "designator": "square",
                "id": 2,
                "cable": {
                    "part_number": "112-00430+A0",
                    "length": "2m",
                    "identifier": "5001086000702648-500a098004f208bf",
                    "serial_number": "APF16510229540",
                },
                "internal": False,
                "module_id": "b",
                "wwn": "500A098004F208BF",
                "state": "connected",
                "remote": {"phy": "08", "wwn": "5001086000702648"},
            },
            {
                "designator": "circle",
                "id": 3,
                "cable": {
                    "part_number": "112-00176+20",
                    "length": "0.5-1.0m",
                    "identifier": "500a0980062ba33f-500a098004f208bf",
                    "serial_number": "832210017",
                },
                "internal": False,
                "module_id": "b",
                "wwn": "500A098004F208BF",
                "state": "connected",
                "remote": {"phy": "00", "wwn": "500A0980062BA33F"},
            },
        ],
        "uid": "3109174803597886800",
        "acps": [
            {
                "channel": "in_band",
                "enabled": True,
                "connection_state": "active",
                "node": {
                    "uuid": "cf62d23c-6100-11eb-9852-00a098fd725d",
                    "name": "cat33-01",
                    "_links": {
                        "self": {
                            "href": "/api/cluster/nodes/cf62d23c-6100-11eb-9852-00a098fd725d"
                        }
                    },
                },
            },
            {
                "channel": "in_band",
                "enabled": True,
                "connection_state": "active",
                "node": {
                    "uuid": "d0892dd7-6100-11eb-9cdb-d039ea010238",
                    "name": "cat33-02",
                    "_links": {
                        "self": {
                            "href": "/api/cluster/nodes/d0892dd7-6100-11eb-9cdb-d039ea010238"
                        }
                    },
                },
            },
        ],
        "temperature_sensors": [
            {
                "id": 1,
                "location": "front of the shelf on the left, on the OPS panel",
                "installed": True,
                "threshold": {
                    "high": {"warning": 40, "critical": 42},
                    "low": {"warning": 5, "critical": 0},
                },
                "temperature": 20,
                "ambient": True,
                "state": "ok",
            },
            {
                "id": 2,
                "location": "inside of the shelf on the midplane",
                "installed": True,
                "threshold": {
                    "high": {"warning": 50, "critical": 55},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 29,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 3,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 50, "critical": 55},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 33,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 4,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 65, "critical": 70},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 41,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 5,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 50, "critical": 55},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 32,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 6,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 65, "critical": 70},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 41,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 7,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 50, "critical": 55},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 34,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 8,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 65, "critical": 70},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 45,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 9,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 50, "critical": 55},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 30,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 10,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "threshold": {
                    "high": {"warning": 65, "critical": 70},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 40,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 11,
                "location": "rear of the shelf at the top left, on shelf module A",
                "installed": True,
                "threshold": {
                    "high": {"warning": 55, "critical": 60},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 30,
                "ambient": False,
                "state": "ok",
            },
            {
                "id": 12,
                "location": "rear of the shelf at the top right, on shelf module B",
                "installed": True,
                "threshold": {
                    "high": {"warning": 55, "critical": 60},
                    "low": {"warning": 10, "critical": 5},
                },
                "temperature": 33,
                "ambient": False,
                "state": "ok",
            },
        ],
        "name": "6.10",
        "connection_type": "sas",
        "fans": [
            {
                "id": 1,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "rpm": 3150,
                "state": "ok",
            },
            {
                "id": 2,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "rpm": 3000,
                "state": "ok",
            },
            {
                "id": 3,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "rpm": 3220,
                "state": "ok",
            },
            {
                "id": 4,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "rpm": 3000,
                "state": "ok",
            },
            {
                "id": 5,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "rpm": 3000,
                "state": "ok",
            },
            {
                "id": 6,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "rpm": 3150,
                "state": "ok",
            },
            {
                "id": 7,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "rpm": 3150,
                "state": "ok",
            },
            {
                "id": 8,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "rpm": 3000,
                "state": "ok",
            },
        ],
        "bays": [
            {"id": 0, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 1, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 2, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 3, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 4, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 5, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 6, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 7, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 8, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 9, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 10, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 11, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 12, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 13, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 14, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 15, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 16, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 17, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 18, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 19, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 20, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 21, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 22, "has_disk": True, "state": "ok", "type": "single_disk"},
            {"id": 23, "has_disk": True, "state": "ok", "type": "single_disk"},
        ],
        "current_sensors": [
            {
                "id": 1,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "current": 6990,
                "state": "ok",
            },
            {
                "id": 2,
                "location": "rear of the shelf on the upper left power supply",
                "installed": True,
                "current": 5150,
                "state": "ok",
            },
            {
                "id": 3,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "current": 4600,
                "state": "ok",
            },
            {
                "id": 4,
                "location": "rear of the shelf on the upper right power supply",
                "installed": True,
                "current": 4800,
                "state": "ok",
            },
            {
                "id": 5,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "current": 4140,
                "state": "ok",
            },
            {
                "id": 6,
                "location": "rear of the shelf on the lower left power supply",
                "installed": True,
                "current": 7770,
                "state": "ok",
            },
            {
                "id": 7,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "current": 4140,
                "state": "ok",
            },
            {
                "id": 8,
                "location": "rear of the shelf on the lower right power supply",
                "installed": True,
                "current": 4720,
                "state": "ok",
            },
        ],
        "frus": [
            {
                "id": 0,
                "installed": True,
                "firmware_version": "0191",
                "part_number": "111-00690+B2",
                "type": "module",
                "state": "ok",
                "serial_number": "8001900099",
            },
            {
                "id": 1,
                "installed": True,
                "firmware_version": "0191",
                "part_number": "111-00190+B0",
                "type": "module",
                "state": "ok",
                "serial_number": "7903785183",
            },
            {
                "id": 1,
                "installed": True,
                "firmware_version": "0311",
                "part_number": "0082562-12",
                "type": "psu",
                "state": "ok",
                "serial_number": "PMW82562007513E",
                "psu": {"model": "9C"},
            },
            {
                "id": 2,
                "installed": True,
                "firmware_version": "0311",
                "part_number": "0082562-12",
                "type": "psu",
                "state": "ok",
                "serial_number": "PMW825620075138",
                "psu": {"model": "9C"},
            },
            {
                "id": 3,
                "installed": True,
                "firmware_version": "0311",
                "part_number": "0082562-12",
                "type": "psu",
                "state": "ok",
                "serial_number": "PMW8256200750BA",
                "psu": {"model": "9C"},
            },
            {
                "id": 4,
                "installed": True,
                "firmware_version": "0311",
                "part_number": "0082562-12",
                "type": "psu",
                "state": "ok",
                "serial_number": "PMW8256200750A2",
                "psu": {"model": "9C"},
            },
        ],
        "model": "DS4246",
        "location_led": "off",
    }
)

```
</div>
</div>

---
## Modifying storage shelf
The storage shelf PATCH API modifies the shelf location LED.
---
## Example
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Shelf

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Shelf(uid=3109174803597886800)
    resource.location_led = "on"
    resource.patch()

```

---"""

import asyncio
from datetime import datetime
import inspect
from typing import Callable, Iterable, List, Optional, Union

try:
    RECLINE_INSTALLED = False
    import recline
    from recline.arg_types.choices import Choices
    from recline.commands import ReclineCommandError
    from netapp_ontap.resource_table import ResourceTable
    RECLINE_INSTALLED = True
except ImportError:
    pass

from marshmallow import fields, EXCLUDE  # type: ignore

import netapp_ontap
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Shelf", "ShelfSchema"]
__pdoc__ = {
    "ShelfSchema.resource": False,
    "ShelfSchema.opts": False,
    "Shelf.shelf_show": False,
    "Shelf.shelf_create": False,
    "Shelf.shelf_modify": False,
    "Shelf.shelf_delete": False,
}


class ShelfSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Shelf object"""

    acps = fields.List(fields.Nested("netapp_ontap.models.shelf_acps.ShelfAcpsSchema", unknown=EXCLUDE), data_key="acps")
    r""" Alternate Control Paths to ACP processors/functions in shelf modules and expanders"""

    bays = fields.List(fields.Nested("netapp_ontap.models.shelf_bays.ShelfBaysSchema", unknown=EXCLUDE), data_key="bays")
    r""" The bays field of the shelf."""

    connection_type = fields.Str(
        data_key="connection_type",
        validate=enum_validation(['unknown', 'fc', 'sas', 'nvme']),
    )
    r""" The connection_type field of the shelf.

Valid choices:

* unknown
* fc
* sas
* nvme"""

    current_sensors = fields.List(fields.Nested("netapp_ontap.models.shelf_current_sensors.ShelfCurrentSensorsSchema", unknown=EXCLUDE), data_key="current_sensors")
    r""" The current_sensors field of the shelf."""

    disk_count = Size(
        data_key="disk_count",
    )
    r""" The disk_count field of the shelf.

Example: 12"""

    drawers = fields.List(fields.Nested("netapp_ontap.models.shelf_drawers.ShelfDrawersSchema", unknown=EXCLUDE), data_key="drawers")
    r""" The drawers field of the shelf."""

    errors = fields.List(fields.Nested("netapp_ontap.models.shelf_errors.ShelfErrorsSchema", unknown=EXCLUDE), data_key="errors")
    r""" The errors field of the shelf."""

    fans = fields.List(fields.Nested("netapp_ontap.models.shelf_fans.ShelfFansSchema", unknown=EXCLUDE), data_key="fans")
    r""" The fans field of the shelf."""

    frus = fields.List(fields.Nested("netapp_ontap.models.shelf_frus.ShelfFrusSchema", unknown=EXCLUDE), data_key="frus")
    r""" The frus field of the shelf."""

    id = fields.Str(
        data_key="id",
    )
    r""" The id field of the shelf.

Example: 1"""

    internal = fields.Boolean(
        data_key="internal",
    )
    r""" The internal field of the shelf."""

    local = fields.Boolean(
        data_key="local",
    )
    r""" The local field of the shelf."""

    location_led = fields.Str(
        data_key="location_led",
        validate=enum_validation(['off', 'on', 'unsupported']),
    )
    r""" The location_led field of the shelf.

Valid choices:

* off
* on
* unsupported"""

    manufacturer = fields.Nested("netapp_ontap.models.shelf_manufacturer.ShelfManufacturerSchema", data_key="manufacturer", unknown=EXCLUDE)
    r""" The manufacturer field of the shelf."""

    model = fields.Str(
        data_key="model",
    )
    r""" The model field of the shelf.

Example: DS2246"""

    module_type = fields.Str(
        data_key="module_type",
        validate=enum_validation(['unknown', 'iom6', 'iom6e', 'iom12', 'iom12b', 'iom12e', 'iom12f', 'iom12g', 'nsm100', 'nsm8e', 'psm3e', 'nsm16e']),
    )
    r""" The module_type field of the shelf.

Valid choices:

* unknown
* iom6
* iom6e
* iom12
* iom12b
* iom12e
* iom12f
* iom12g
* nsm100
* nsm8e
* psm3e
* nsm16e"""

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the shelf.

Example: 1.1"""

    paths = fields.List(fields.Nested("netapp_ontap.resources.storage_port.StoragePortSchema", unknown=EXCLUDE), data_key="paths")
    r""" The paths field of the shelf."""

    ports = fields.List(fields.Nested("netapp_ontap.models.shelf_ports.ShelfPortsSchema", unknown=EXCLUDE), data_key="ports")
    r""" The ports field of the shelf."""

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" The serial_number field of the shelf.

Example: SHFMS1514000895"""

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['unknown', 'ok', 'error']),
    )
    r""" The state field of the shelf.

Valid choices:

* unknown
* ok
* error"""

    temperature_sensors = fields.List(fields.Nested("netapp_ontap.models.shelf_temperature_sensors.ShelfTemperatureSensorsSchema", unknown=EXCLUDE), data_key="temperature_sensors")
    r""" The temperature_sensors field of the shelf."""

    uid = fields.Str(
        data_key="uid",
    )
    r""" The uid field of the shelf.

Example: 7777841915827391056"""

    vendor = fields.Nested("netapp_ontap.models.shelf_vendor.ShelfVendorSchema", data_key="vendor", unknown=EXCLUDE)
    r""" The vendor field of the shelf."""

    voltage_sensors = fields.List(fields.Nested("netapp_ontap.models.shelf_voltage_sensors.ShelfVoltageSensorsSchema", unknown=EXCLUDE), data_key="voltage_sensors")
    r""" The voltage_sensors field of the shelf."""

    @property
    def resource(self):
        return Shelf

    gettable_fields = [
        "acps",
        "bays",
        "connection_type",
        "current_sensors",
        "disk_count",
        "drawers",
        "errors",
        "fans",
        "frus",
        "id",
        "internal",
        "local",
        "location_led",
        "manufacturer",
        "model",
        "module_type",
        "name",
        "paths.links",
        "paths.name",
        "paths.node",
        "ports",
        "serial_number",
        "state",
        "temperature_sensors",
        "uid",
        "vendor",
        "voltage_sensors",
    ]
    """acps,bays,connection_type,current_sensors,disk_count,drawers,errors,fans,frus,id,internal,local,location_led,manufacturer,model,module_type,name,paths.links,paths.name,paths.node,ports,serial_number,state,temperature_sensors,uid,vendor,voltage_sensors,"""

    patchable_fields = [
        "location_led",
    ]
    """location_led,"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Shelf.get_collection(fields=field)]
    return getter

async def _wait_for_job(response: NetAppResponse) -> None:
    """Examine the given response. If it is a job, asynchronously wait for it to
    complete. While polling, prints the current status message of the job.
    """

    if not response.is_job:
        return
    from netapp_ontap.resources import Job
    job = Job(**response.http_response.json()["job"])
    while True:
        job.get(fields="state,message")
        if hasattr(job, "message"):
            print("[%s]: %s" % (job.state, job.message))
        if job.state == "failure":
            raise NetAppRestError("Shelf modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Shelf(Resource):
    """Allows interaction with Shelf objects on the host"""

    _schema = ShelfSchema
    _path = "/api/storage/shelves"
    _keys = ["uid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a collection of shelves.
### Related ONTAP commands
* `storage shelf show`
* `storage shelf port show`
* `storage shelf drawer show`
* `storage shelf drawer show-slot`
* `storage shelf acp show`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="shelf show")
        def shelf_show(
            fields: List[Choices.define(["connection_type", "disk_count", "id", "internal", "local", "location_led", "model", "module_type", "name", "serial_number", "state", "uid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Shelf resources

            Args:
                connection_type: 
                disk_count: 
                id: 
                internal: 
                local: 
                location_led: 
                model: 
                module_type: 
                name: 
                serial_number: 
                state: 
                uid: 
            """

            kwargs = {}
            if connection_type is not None:
                kwargs["connection_type"] = connection_type
            if disk_count is not None:
                kwargs["disk_count"] = disk_count
            if id is not None:
                kwargs["id"] = id
            if internal is not None:
                kwargs["internal"] = internal
            if local is not None:
                kwargs["local"] = local
            if location_led is not None:
                kwargs["location_led"] = location_led
            if model is not None:
                kwargs["model"] = model
            if module_type is not None:
                kwargs["module_type"] = module_type
            if name is not None:
                kwargs["name"] = name
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if state is not None:
                kwargs["state"] = state
            if uid is not None:
                kwargs["uid"] = uid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Shelf.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Shelf resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Shelf"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a shelf location LED.
### Related ONTAP commands
* `storage shelf location-led modify`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)



    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of shelves.
### Related ONTAP commands
* `storage shelf show`
* `storage shelf port show`
* `storage shelf drawer show`
* `storage shelf drawer show-slot`
* `storage shelf acp show`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific shelf.
### Related ONTAP commands
* `storage shelf show`
* `storage shelf port show`
* `storage shelf drawer show`
* `storage shelf drawer show-slot`
* `storage shelf acp show`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)


    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a shelf location LED.
### Related ONTAP commands
* `storage shelf location-led modify`
### Learn more
* [`DOC /storage/shelves`](#docs-storage-storage_shelves)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="shelf modify")
        async def shelf_modify(
        ) -> ResourceTable:
            """Modify an instance of a Shelf resource

            Args:
                connection_type: 
                query_connection_type: 
                disk_count: 
                query_disk_count: 
                id: 
                query_id: 
                internal: 
                query_internal: 
                local: 
                query_local: 
                location_led: 
                query_location_led: 
                model: 
                query_model: 
                module_type: 
                query_module_type: 
                name: 
                query_name: 
                serial_number: 
                query_serial_number: 
                state: 
                query_state: 
                uid: 
                query_uid: 
            """

            kwargs = {}
            changes = {}
            if query_connection_type is not None:
                kwargs["connection_type"] = query_connection_type
            if query_disk_count is not None:
                kwargs["disk_count"] = query_disk_count
            if query_id is not None:
                kwargs["id"] = query_id
            if query_internal is not None:
                kwargs["internal"] = query_internal
            if query_local is not None:
                kwargs["local"] = query_local
            if query_location_led is not None:
                kwargs["location_led"] = query_location_led
            if query_model is not None:
                kwargs["model"] = query_model
            if query_module_type is not None:
                kwargs["module_type"] = query_module_type
            if query_name is not None:
                kwargs["name"] = query_name
            if query_serial_number is not None:
                kwargs["serial_number"] = query_serial_number
            if query_state is not None:
                kwargs["state"] = query_state
            if query_uid is not None:
                kwargs["uid"] = query_uid

            if connection_type is not None:
                changes["connection_type"] = connection_type
            if disk_count is not None:
                changes["disk_count"] = disk_count
            if id is not None:
                changes["id"] = id
            if internal is not None:
                changes["internal"] = internal
            if local is not None:
                changes["local"] = local
            if location_led is not None:
                changes["location_led"] = location_led
            if model is not None:
                changes["model"] = model
            if module_type is not None:
                changes["module_type"] = module_type
            if name is not None:
                changes["name"] = name
            if serial_number is not None:
                changes["serial_number"] = serial_number
            if state is not None:
                changes["state"] = state
            if uid is not None:
                changes["uid"] = uid

            if hasattr(Shelf, "find"):
                resource = Shelf.find(
                    **kwargs
                )
            else:
                resource = Shelf()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Shelf: %s" % err)



