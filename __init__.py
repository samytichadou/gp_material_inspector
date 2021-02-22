'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "GP Material Inspector",
    "description": "Blender addon to inspect all available GP materials in a glimpse",
    "author": "Samy Tichadou (tonton)",
    "version": (1, 0, 0),
    "blender": (2, 91, 2),
    "location": "Sidebar > Grease Pencil > Grease Pencil Tools",
    "warning": "",
    "doc_url": "https://github.com/samytichadou/gp_material_inspector",
    "tracker_url": "https://github.com/samytichadou/gp_material_inspector/issues/new",
    "category": "Object" }

import bpy


# IMPORT SPECIFICS
##################################

from . import   (addon_prefs,
                gui,
                )


# register
##################################


def register():

    addon_prefs.register()
    gui.register()

    bpy.types.Scene.gpmi_selected_only = \
        bpy.props.BoolProperty(name = "Selected Only", default = True)

    bpy.types.Material.gpmi_show_details = \
        bpy.props.BoolProperty(name = "Show Details", default = False)

    bpy.types.Object.gpmi_show_materials = \
        bpy.props.BoolProperty(name = "Show Materials", default = False)

    ## update tab name with update in pref file (passing addon_prefs)
    addon_prefs.update_panel(addon_prefs.get_addon_preferences(), bpy.context)


def unregister():

    addon_prefs.unregister()
    gui.unregister()

    del bpy.types.Scene.gpmi_selected_only
    del bpy.types.Material.gpmi_show_details
    del bpy.types.Object.gpmi_show_materials