"""Support for cameras from Starling Home Hub."""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass
from homeassistant.const import Platform
from homeassistant.helpers.entity import EntityCategory

from custom_components.starling_home_hub.entities.binary_sensor import StarlingHomeHubBinarySensorEntityDescription
from custom_components.starling_home_hub.entities.switch import StarlingHomeHubSwitchEntityDescription
from custom_components.starling_home_hub.integrations.base import from_base_entities


CAMERA_PLATFORMS = from_base_entities({
    Platform.BINARY_SENSOR: [
        StarlingHomeHubBinarySensorEntityDescription(
            key="animal_detected",
            name="Animal Detected",
            relevant_fn=lambda device: "animalDetected" in device,
            value_fn=lambda device: device["animalDetected"],
            device_class=BinarySensorDeviceClass.MOTION,
            icon="mdi:dog-side"
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="doorbell_pushed",
            name="Doorbell Pushed",
            relevant_fn=lambda device: "doorbellPushed" in device,
            value_fn=lambda device: device["doorbellPushed"],
            device_class=BinarySensorDeviceClass.OCCUPANCY
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="garage_door_state",
            name="Garage Door",
            relevant_fn=lambda device: "garageDoorState" in device,
            value_fn=lambda device: device["garageDoorState"] == "open",
            device_class=BinarySensorDeviceClass.GARAGE_DOOR
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="motion_detected",
            name="Motion Detected",
            relevant_fn=lambda device: "motionDetected" in device,
            value_fn=lambda device: device["motionDetected"],
            device_class=BinarySensorDeviceClass.MOTION
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="package_delivered",
            name="Package Delivered",
            relevant_fn=lambda device: "packageDelivered" in device,
            value_fn=lambda device: device["packageDelivered"],
            icon="mdi:package-variant-closed"
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="package_retrieved",
            name="Package Retrieved",
            relevant_fn=lambda device: "packageRetrieved" in device,
            value_fn=lambda device: device["packageRetrieved"],
            icon="mdi:package-variant"
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="person_detected",
            name="Person Detected",
            relevant_fn=lambda device: "personDetected" in device,
            value_fn=lambda device: device["personDetected"],
            device_class=BinarySensorDeviceClass.MOTION
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="sound_detected",
            name="Sound Detected",
            relevant_fn=lambda device: "soundDetected" in device,
            value_fn=lambda device: device["soundDetected"],
            device_class=BinarySensorDeviceClass.SOUND
        ),
        StarlingHomeHubBinarySensorEntityDescription(
            key="vehicle_detected",
            name="Vehicle Detected",
            relevant_fn=lambda device: "vehicleDetected" in device,
            value_fn=lambda device: device["vehicleDetected"],
            device_class=BinarySensorDeviceClass.MOTION,
            icon="mdi:car-estate"
        ),
    ],
    Platform.SWITCH: [
        StarlingHomeHubSwitchEntityDescription(
            key="camera_enabled",
            name="Camera Enabled",
            relevant_fn=lambda device: "cameraEnabled" in device,
            value_fn=lambda device: device["cameraEnabled"],
            icon="mdi:camera",
            entity_category=EntityCategory.CONFIG,
            update_field="cameraEnabled",
            device_class=SwitchDeviceClass.SWITCH
        ),
        StarlingHomeHubSwitchEntityDescription(
            key="quiet_time",
            name="Quiet Time",
            relevant_fn=lambda device: "quietTime" in device,
            value_fn=lambda device: device["quietTime"],
            icon="mdi:sleep",
            entity_category=EntityCategory.CONFIG,
            update_field="quietTime",
            device_class=SwitchDeviceClass.SWITCH
        ),
        StarlingHomeHubSwitchEntityDescription(
            key="flood_light",
            name="Flood Light",
            relevant_fn=lambda device: "floodLightOn" in device,
            value_fn=lambda device: device["floodLightOn"],
            icon="mdi:light-flood-down",
            update_field="floodLightOn",
            device_class=SwitchDeviceClass.SWITCH
        ),
    ]
})
