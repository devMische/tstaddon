import bpy


class TST_PT_main_panel(bpy.types.Panel):

    bl_label = "tst-addon 1.3.0"
    bl_idname = "TST_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TST'

    def draw(self, context):
        layout = self.layout
        layout.label(text="TST ADDON 1.3.0")
