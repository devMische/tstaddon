import bpy


class TST_PT_main_panel(bpy.types.Panel):

    bl_label = "tst-addon"
    bl_idname = "TST_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TST'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="TST ADDON 2.1.0")
        col.label(text="Thanks for testing!", icon="FUND")
