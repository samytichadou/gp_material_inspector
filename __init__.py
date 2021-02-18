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
    "name": "GP Material Checker",
    "description": "Handy reload for Image Textures and Linked Libraries",
    "author": "Samy TIchadou (tonton), RenFinkle",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "Properties > Scene",
    "wiki_url": "https://github.com/samytichadou/Auto_Reload_Images-Blender_addon",
    "tracker_url": "https://github.com/samytichadou/Auto_Reload_Images-Blender_addon/issues/new",
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

    ## update tab name with update in pref file (passing addon_prefs)
    addon_prefs.update_panel(addon_prefs.get_addon_preferences(), bpy.context)


def unregister():

    addon_prefs.unregister()
    gui.unregister()