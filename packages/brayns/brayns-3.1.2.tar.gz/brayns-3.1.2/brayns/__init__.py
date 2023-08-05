# Copyright (c) 2015-2023 EPFL/Blue Brain Project
# All rights reserved. Do not distribute without permission.
#
# Responsible Author: adrien.fleury@epfl.ch
#
# This file is part of Brayns <https://github.com/BlueBrain/Brayns>
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License version 3.0 as published
# by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Brayns Python package.

This package provides a high level API to interact with an instance of Brayns
instance through websockets.

The low level JSON-RPC API is also available using the instance directly.
"""

from .core import (
    AmbientLight,
    Application,
    BoundedPlane,
    Box,
    Camera,
    CameraController,
    Capsule,
    CarPaintMaterial,
    ColorMethod,
    ColorRamp,
    ControlPoint,
    DirectionalLight,
    EmissiveMaterial,
    Entrypoint,
    Fovy,
    Framebuffer,
    GBufferChannel,
    GBufferExporter,
    Geometry,
    GlassMaterial,
    Image,
    ImageInfo,
    InteractiveRenderer,
    Light,
    Loader,
    LoaderInfo,
    Material,
    MatteMaterial,
    MeshLoader,
    MetalMaterial,
    MhdVolumeLoader,
    Model,
    OpacityCurve,
    OrthographicProjection,
    PerspectiveProjection,
    PhongMaterial,
    PickResult,
    Plane,
    PlasticMaterial,
    ProductionRenderer,
    ProgressiveFramebuffer,
    Projection,
    QuadLight,
    RawVolumeLoader,
    Renderer,
    Scene,
    Simulation,
    Snapshot,
    Sphere,
    StaticFramebuffer,
    TimeUnit,
    ValueRange,
    Version,
    VersionError,
    View,
    VolumeDataType,
    add_clipping_geometries,
    add_geometries,
    add_light,
    check_version,
    clear_clipping_geometries,
    clear_lights,
    clear_models,
    clear_renderables,
    color_model,
    enable_simulation,
    get_application,
    get_bounds,
    get_camera,
    get_camera_name,
    get_camera_projection,
    get_camera_view,
    get_color_methods,
    get_color_ramp,
    get_color_values,
    get_entrypoint,
    get_entrypoints,
    get_loaders,
    get_material,
    get_material_name,
    get_methods,
    get_model,
    get_models,
    get_renderer,
    get_renderer_name,
    get_scene,
    get_simulation,
    get_version,
    instantiate_model,
    pick,
    remove_models,
    set_camera,
    set_camera_projection,
    set_camera_view,
    set_color_ramp,
    set_framebuffer,
    set_material,
    set_model_color,
    set_renderer,
    set_resolution,
    set_simulation_frame,
    stop,
    update_model,
)
from .movie import Movie, MovieError, MovieFrames
from .network import (
    ConnectionClosedError,
    Connector,
    Future,
    Instance,
    InvalidServerCertificateError,
    JsonRpcError,
    JsonRpcFuture,
    JsonRpcProgress,
    JsonRpcReply,
    JsonRpcRequest,
    Logger,
    ProtocolError,
    ServiceUnavailableError,
    SslClientContext,
    WebSocketError,
)
from .plugins import (
    AtlasColumnHighlight,
    AtlasDensity,
    AtlasDistanceType,
    AtlasFlatmapAreas,
    AtlasLayerDistance,
    AtlasOrientationField,
    AtlasShellOutline,
    AtlasUsecase,
    BbpCells,
    BbpLoader,
    BbpReport,
    BbpReportType,
    CellPlacementLoader,
    CircuitColorMethod,
    ColumnNeighbor,
    ColumnPosition,
    CylindricProjection,
    DtiLoader,
    GeometryType,
    Morphology,
    MorphologyLoader,
    NrrdLoader,
    ProteinColorScheme,
    ProteinLoader,
    SonataEdgePopulation,
    SonataLoader,
    SonataNodePopulation,
    SonataNodes,
    SonataReport,
    SonataReportType,
    VoxelType,
    XyzLoader,
    get_atlas_usecases,
    get_circuit_ids,
    set_circuit_thickness,
)
from .service import (
    LogLevel,
    Manager,
    Plugin,
    Process,
    Service,
    SslServerContext,
    start,
)
from .utils import (
    Axis,
    Bounds,
    CameraRotation,
    Color3,
    Color4,
    Error,
    ImageFormat,
    JsonSchema,
    JsonType,
    ModelRotation,
    PlaneEquation,
    Quaternion,
    Resolution,
    Rotation,
    Transform,
    Vector2,
    Vector3,
    componentwise_max,
    componentwise_min,
    deserialize_schema,
    euler,
    merge_bounds,
    parse_hex_color,
    parse_image_format,
    serialize_schema,
)
from .version import VERSION

__version__ = VERSION
"""Version tag of brayns Python package (major.minor.patch)."""

__all__ = [
    "add_clipping_geometries",
    "add_geometries",
    "add_light",
    "AmbientLight",
    "Application",
    "AtlasColumnHighlight",
    "AtlasDensity",
    "AtlasDistanceType",
    "AtlasFlatmapAreas",
    "AtlasLayerDistance",
    "AtlasOrientationField",
    "AtlasShellOutline",
    "AtlasUsecase",
    "Axis",
    "BbpCells",
    "BbpLoader",
    "BbpReport",
    "BbpReportType",
    "BoundedPlane",
    "Bounds",
    "Box",
    "Camera",
    "CameraController",
    "CameraRotation",
    "Capsule",
    "CarPaintMaterial",
    "CellPlacementLoader",
    "check_version",
    "CircuitColorMethod",
    "clear_clipping_geometries",
    "clear_lights",
    "clear_models",
    "clear_renderables",
    "color_model",
    "Color3",
    "Color4",
    "ColorMethod",
    "ColorRamp",
    "ColumnNeighbor",
    "ColumnPosition",
    "componentwise_max",
    "componentwise_min",
    "ConnectionClosedError",
    "Connector",
    "ControlPoint",
    "CylindricProjection",
    "deserialize_schema",
    "DirectionalLight",
    "DtiLoader",
    "EmissiveMaterial",
    "enable_simulation",
    "Entrypoint",
    "Error",
    "euler",
    "Fovy",
    "Framebuffer",
    "Future",
    "GBufferChannel",
    "GBufferExporter",
    "Geometry",
    "GeometryType",
    "get_application",
    "get_atlas_usecases",
    "get_bounds",
    "get_camera_name",
    "get_camera_projection",
    "get_camera_view",
    "get_camera",
    "get_circuit_ids",
    "get_color_methods",
    "get_color_ramp",
    "get_color_values",
    "get_entrypoint",
    "get_entrypoints",
    "get_loaders",
    "get_material_name",
    "get_material",
    "get_methods",
    "get_model",
    "get_models",
    "get_renderer_name",
    "get_renderer",
    "get_scene",
    "get_simulation",
    "get_version",
    "GlassMaterial",
    "Image",
    "ImageFormat",
    "ImageInfo",
    "Instance",
    "instantiate_model",
    "InteractiveRenderer",
    "InvalidServerCertificateError",
    "JsonRpcError",
    "JsonRpcFuture",
    "JsonRpcProgress",
    "JsonRpcReply",
    "JsonRpcRequest",
    "JsonSchema",
    "JsonType",
    "Light",
    "Loader",
    "LoaderInfo",
    "Logger",
    "LogLevel",
    "Manager",
    "Material",
    "MatteMaterial",
    "merge_bounds",
    "MeshLoader",
    "MetalMaterial",
    "MhdVolumeLoader",
    "Model",
    "ModelRotation",
    "Morphology",
    "MorphologyLoader",
    "Movie",
    "MovieError",
    "MovieFrames",
    "NrrdLoader",
    "OpacityCurve",
    "OrthographicProjection",
    "parse_hex_color",
    "parse_image_format",
    "PerspectiveProjection",
    "PhongMaterial",
    "pick",
    "PickResult",
    "Plane",
    "PlaneEquation",
    "PlasticMaterial",
    "Plugin",
    "Process",
    "ProductionRenderer",
    "ProgressiveFramebuffer",
    "Projection",
    "ProteinColorScheme",
    "ProteinLoader",
    "ProtocolError",
    "QuadLight",
    "Quaternion",
    "RawVolumeLoader",
    "remove_models",
    "Renderer",
    "Resolution",
    "Rotation",
    "Scene",
    "serialize_schema",
    "Service",
    "ServiceUnavailableError",
    "set_camera_projection",
    "set_camera_view",
    "set_camera",
    "set_circuit_thickness",
    "set_color_ramp",
    "set_framebuffer",
    "set_material",
    "set_model_color",
    "set_renderer",
    "set_resolution",
    "set_simulation_frame",
    "Simulation",
    "Snapshot",
    "SonataEdgePopulation",
    "SonataLoader",
    "SonataNodePopulation",
    "SonataNodes",
    "SonataReport",
    "SonataReportType",
    "Sphere",
    "SslClientContext",
    "SslServerContext",
    "start",
    "StaticFramebuffer",
    "stop",
    "TimeUnit",
    "Transform",
    "update_model",
    "ValueRange",
    "Vector2",
    "Vector3",
    "Version",
    "VersionError",
    "View",
    "VolumeDataType",
    "VoxelType",
    "WebSocketError",
    "XyzLoader",
]
