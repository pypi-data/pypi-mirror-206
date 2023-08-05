"""create CLI command implementation."""
# dem/cli/command/create_cmd.py

import typer
import dem.core.container_engine as container_engine
import dem.core.registry as registry
import dem.core.data_management as data_management
from dem.core.dev_env_setup import DevEnv, DevEnvLocal, DevEnvLocalSetup
from dem.cli.menu import ToolTypeMenu, ToolImageMenu
from dem.core.tool_images import ToolImages

tool_image_statuses = {
    ToolImages.LOCAL_ONLY: "local",
    ToolImages.REGISTRY_ONLY: "registry",
    ToolImages.LOCAL_AND_REGISTRY: "local and registry"
}

def get_tool_images() -> list[list[str]]:
    tool_images = ToolImages()
    return [[name, tool_image_statuses[status]] for name, status in tool_images.elements.items()]

def get_dev_env_descriptor_from_user(dev_env_name: str) -> dict:
    tool_type_menu = ToolTypeMenu(list(DevEnv.supported_tool_types))
    # Wait until the user finishes the tool type selection.
    tool_type_menu.wait_for_user()
    selected_tool_types = tool_type_menu.get_selected_tool_types()

    tool_image_menu = ToolImageMenu(get_tool_images())
    dev_env_descriptor = {
        "name": dev_env_name,
        "tools": []
    }
    for tool_type in selected_tool_types:
        tool_image_menu.set_title("Select tool image for type " + tool_type)
        tool_image_menu.wait_for_user()
        selected_tool_image = tool_image_menu.get_selected_tool_image()
        tool_descriptor = {
            "type": tool_type,
            "image_name": selected_tool_image[0],
            "image_version": selected_tool_image[1]
        }
        dev_env_descriptor["tools"].append(tool_descriptor)
    return dev_env_descriptor

def execute(dev_env_name: str) -> None:
    derserialized_local_dev_nev = data_management.read_deserialized_dev_env_json()
    dev_env_local_setup = DevEnvLocalSetup(derserialized_local_dev_nev)
    dev_env_original = dev_env_local_setup.get_dev_env_by_name(dev_env_name)
    if dev_env_original is not None:
        typer.confirm("The input name is already used by a Development Environment. Overwrite it?", 
                      abort=True)

    dev_env_descriptor = get_dev_env_descriptor_from_user(dev_env_name)
    
    if dev_env_original is not None:
        dev_env_original.tools = dev_env_descriptor["tools"]
    else:
        new_dev_env = DevEnvLocal(dev_env_descriptor)
        dev_env_local_setup.dev_envs.append(new_dev_env)
    derserialized_local_dev_nev = dev_env_local_setup.get_deserialized()
    data_management.write_deserialized_dev_env_json(derserialized_local_dev_nev)