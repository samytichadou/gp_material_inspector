import bpy
import os

from .gui import GP_PT_material_checker


addon_name = os.path.basename(os.path.dirname(__file__))

def update_panel(self, context):
    try:
        bpy.utils.unregister_class(GP_PT_material_checker)
    except:
        pass
    GP_PT_material_checker.bl_category = get_addon_preferences().category
    bpy.utils.register_class(GP_PT_material_checker)


class GPMI_PF_Addon_Prefs(bpy.types.AddonPreferences):
    bl_idname = addon_name
    
    icon_toggle: bpy.props.BoolProperty(
        name = "Icon Display",
        description = "Display indicator icon for timer mode",
        default = True,
        )

    category : bpy.props.StringProperty(
            name="Category",
            description="Choose a name for the category of the panel",
            default="Grease Pencil",
            update=update_panel)


    def draw(self, context):
        layout = self.layout

        layout.prop(self, "category")
        

# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(addon_name)
    return getattr(addon, "preferences", None)


### REGISTER ---

def register():
    bpy.utils.register_class(GPMI_PF_Addon_Prefs)

def unregister():
    bpy.utils.unregister_class(GPMI_PF_Addon_Prefs)