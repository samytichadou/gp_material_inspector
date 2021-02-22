import bpy


# return selected object materials
def gpmc_return_materials_from_objects(scene):

    mat = []

    for ob in scene.objects:
        if ob.type == "GPENCIL" and ob.select_get():
            for ms in ob.material_slots:
                if ms.material.is_grease_pencil:
                    if ms.material not in mat:
                        mat.append(ms.material)

    return mat


# return gp materials
def gpmc_return_gp_materials():

    mat = []

    for m in bpy.data.materials:
        if m.is_grease_pencil:
            mat.append(m)

    mat = sorted(mat, key=lambda x: x.name, reverse=False)

    return mat


# draw function
def gpmc_draw_checker(layout, context):

    scn = context.scene
    layout.prop(scn, "gpmc_selected_only")

    col = layout.column(align=True)

    if scn.gpmc_selected_only:
        mat = gpmc_return_materials_from_objects(scn)
    else:
        mat = gpmc_return_gp_materials()
        
    for m in mat:
        if m.is_grease_pencil:
            gp = m.grease_pencil
            
            box = col.box()
            
            row = box.row(align=True)
            row.label(text="", icon="MATERIAL")
            row.prop(m, "name", text="")
            
            row = box.row()
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


# popup operator
class GP_OT_materialchecker_popup_operator(bpy.types.Operator):
    bl_idname = "gp.popup_operator"
    bl_label = "GP Material Checker"
    bl_options = {"REGISTER"}
 
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)
 
    def draw(self, context):
        gpmc_draw_checker(self.layout, context)

    def execute(self, context):
        return {'FINISHED'}


# panel
class GP_PT_material_checker(bpy.types.Panel):
    bl_label = "GP Material Checker "
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Grease Pencil"
 
    @classmethod
    def poll(cls, context):
        return True
 
    def draw(self, context):
        layout = self.layout
        
        #layout.operator("gp.popup_operator", text="Popup")
        gpmc_draw_checker(self.layout, context)


### REGISTER ---

def register():
    bpy.utils.register_class(GP_OT_materialchecker_popup_operator)
    bpy.utils.register_class(GP_PT_material_checker)

def unregister():
    bpy.utils.unregister_class(GP_OT_materialchecker_popup_operator)
    bpy.utils.unregister_class(GP_PT_material_checker)