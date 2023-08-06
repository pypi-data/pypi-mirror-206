from itertools import chain
from typing import Dict, Generic, List, TypeVar

from dcim.models import Device
from django.conf import settings
from rest_framework import serializers
from utilities.exceptions import AbortRequest
from virtualization.models import VirtualMachine

from .utils import get_attr, get_attr_str

T = TypeVar("T")


class BasePrometheusSerializer(serializers.Serializer, Generic[T]):
    targets = serializers.SerializerMethodField()
    labels = serializers.SerializerMethodField()

    def get_targets(self, device: T) -> List[str]:
        # Default to Name
        for attrs in chain(
            settings.PLUGINS_CONFIG["netbox_lists"][
                f"prometheus_{self.settings_type}_sd_target"
            ],
            (("name",),),
        ):
            print(f"Attr: {repr(attrs)}")
            target = get_attr(attrs, device)
            if target is not None:
                return [str(target)]

        # This shouldn't happen since Name is a required field
        raise AbortRequest(
            f"No target found for {repr(device)}. (this shouldn't happen)"
        )

    def get_labels(self, device: T) -> Dict[str, str]:
        labels = {
            k: get_attr_str(v, device)
            for k, v in settings.PLUGINS_CONFIG["netbox_lists"][
                f"prometheus_{self.settings_type}_sd_labels"
            ].items()
        }

        return labels


class PrometheusVMSerializer(BasePrometheusSerializer[VirtualMachine]):
    settings_type = "vm"


class PrometheusDeviceSerializer(BasePrometheusSerializer[Device]):
    settings_type = "device"
