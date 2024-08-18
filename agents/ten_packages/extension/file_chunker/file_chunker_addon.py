from ten import (
    Addon,
    register_addon_as_extension,
    TenEnv,
)
from .log import logger
from .file_chunker_extension import FileChunkerExtension


@register_addon_as_extension("file_chunker")
class FileChunkerExtensionAddon(Addon):
    def on_create_instance(self, ten: TenEnv, addon_name: str, context) -> None:
        logger.info("on_create_instance")
        ten.on_create_instance_done(FileChunkerExtension(addon_name), context)
