import bpy


# return selected object materials
def gpmi_return_materials_from_object(object):

    mat = []

    for ms in object.material_slots:
        if ms.material.is_grease_pencil:
            if ms.material not in mat:
                mat.append(ms.material)

    return mat


# return gp materials
def gpmi_return_gp_materials():

    mat = []

    for m in bpy.data.materials:
        if m.is_grease_pencil:
            mat.append(m)

    mat = sorted(mat, key=lambda x: x.name, reverse=False)

    return mat


# draw material
def gpmi_draw_material(mat, container):

    gp = mat.grease_pencil
        
    # header
    row = container.row(align=True)

    if mat.gpmi_show_details:
        icon_details = "DISCLOSURE_TRI_DOWN"
    else:
        icon_details = "DISCLOSURE_TRI_RIGHT"

    row.prop(mat, "gpmi_show_details", text = "", icon=icon_details, emboss=False)

    row.prop(mat, "name", text="")

    row.prop(gp, "hide", text="", emboss=False)
    
    # details
    if not mat.gpmi_show_details:
        row.separator()
        row.prop(gp, "show_stroke", text="", icon="STROKE")
        row.prop(gp, "color", text="")
        row.separator()
        row.prop(gp, "show_fill", text="", icon="GP_SELECT_STROKES")
        row.prop(gp, "fill_color", text="")

    else:
        row = container.row()
        split = row.split(align=True)
        
        subcol1 = split.column(align=True)
        subcol1.prop(gp, "show_stroke", text="", icon="STROKE")
        subcol1.prop(gp, "show_fill", text="", icon="GP_SELECT_STROKES")
        
        subcol2 = split.column(align=True)
        subcol2.prop(gp, "color", text="")
        subcol2.prop(gp, "fill_color", text="")
        
        subcol5 = split.column(align=True)
        subcol5.prop(gp, "mode", text="")
        
        subcol3 = split.column(align=True)
        subcol3.prop(gp, "stroke_style", text="")
        subcol3.prop(gp, "fill_style", text="")
        
        subcol4 = split.column(align=True)
        subcol4.prop(gp, "use_stroke_holdout", text="", icon="HOLDOUT_ON")
        subcol4.prop(gp, "use_fill_holdout", text="", icon="HOLDOUT_ON")
        
        subcol6 = split.column(align=True)
        subcol6.prop(gp, "use_overlap_strokes", text="", icon="MOD_MASK")


# draw function
def gpmi_draw_checker(layout, context):

    scn = context.scene
    layout.prop(scn, "gpmi_selected_only")

    col = layout.column(align=True)

    for ob in bpy.data.objects:
        if ob.type == "GPENCIL":
            
            if scn.gpmi_selected_only and ob.select_get() \
            or not scn.gpmi_selected_only:

                mat = gpmi_return_materials_from_object(ob)
                if mat:
                    if ob.gpmi_show_materials:
                        icon_show = "DISCLOSURE_TRI_DOWN"
                    else:
                        icon_show = "DISCLOSURE_TRI_RIGHT"
                    
                    row = col.row(align=True)
                    row.prop(ob, "gpmi_show_materials", text="", icon=icon_show, emboss=False)
                    row.label(text=ob.name, icon="MESH_CUBE")

                    if ob.gpmi_show_materials:
                        for m in mat:
                            gpmi_draw_material(m, col)


# popup operator
class GP_OT_material_inspector_popup_operator(bpy.types.Operator):
    bl_idname = "gp.material_inspector_popup"
    bl_label = "GP Material Inspector"
    bl_options = {"REGISTER"}
    bl_description = "GP material inspector popup"
 
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)
 
    def draw(self, context):
        gpmi_draw_checker(self.layout, context)

    def execute(self, context):
        return {'FINISHED'}


# panel
class GP_PT_material_inspector(bpy.types.Panel):
    bl_label = "GP Material Inspector"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Grease Pencil"
 
    @classmethod
    def poll(cls, context):
        return True
 
    def draw(self, context):       
        gpmi_draw_checker(self.layout, context)


### REGISTER ---

def register():
    bpy.utils.register_class(GP_OT_material_inspector_popup_operator)
    bpy.utils.register_class(GP_PT_material_inspector)

def unregister():
    bpy.utils.unregister_class(GP_OT_material_inspector_popup_operator)
    bpy.utils.unregister_class(GP_PT_material_inspector)