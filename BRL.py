# Apache License 2.0
import bpy


bl_info = {
    "name": "BlenderAI",
    "author": "Fredrick K",
    "version": (0, 0, 0),
    "blender": (3, 8, 0),
    "location": "Anywhere",
    "description": "AI Assistant for Blender can generates assets(model, materials)",
    "doc_url": "https://github.com/BlenderAI/BlenderRL",
    "tracker_url": "https://github.com/BlenderAI/BlenderRL/issues",
    "category": "AI",
}


class BRL:
    def __init__(self, name, age):
        self.model = ""
        self.age = age
    """Button/Operators"""
    class RequestModelOperator(bpy.types.Operator):
        """Add a Cube to the Scene"""
        bl_idname = "object.request_model_operator"
        bl_label = "Add Cube"
        def execute(self, context):
            bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
            prompt = bpy.context.scene.request_model_prompt
            model = request_model_from_api(self.prompt)

            return {'FINISHED'}
        '''def execute(self, context):
            # request the reinforcement learning model from API
            model = request_model_from_api(self.prompt)
            
            if model:
                # perform tasks based on the model
                if model['task'] == 'create_sphere':
                    bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0))
                elif model['task'] == 'create_cube':
                    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
                # add more tasks based on the model
            
            return {'FINISHED'}
        
        def invoke(self, context, event):
            # prompt user to enter the prompt for the model
            return context.window_manager.invoke_props_dialog(self)'''
    class UseMicrophoneOperator(bpy.types.Operator):
        """Add a Cube to the Scene"""
        bl_idname = "object.use_microphone"
        bl_label = "Add Cube"
        def execute(self, context):
            bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
            prompt = bpy.context.scene.request_model_prompt
            model = request_model_from_api(self.prompt)
            return {'FINISHED'}
        
    """UI""" 
    class RequestModelPanel(bpy.types.Panel):
        """Panel for Requesting Reinforcement Learning Model"""
        bl_label = "Request Reinforcement Learning Model"
        bl_idname = "OBJECT_PT_request_model"
        bl_space_type = 'VIEW_3D'
        bl_region_type = 'UI'
        bl_category = "BRL"

        def draw(self, context):
            layout = self.layout
            row = layout.row()
            row.prop(context.scene, "request_model_prompt", text="Prompt")
            row = layout.row()
            #row.operator("object.add_cube_operator", text="Submit")
            row.operator("object.request_model_operator", text="Submit")
            row.operator("object.use_microphone", text="Speak", icon='OUTLINER_DATA_SPEAKER')
    """Function"""
    def request_model_from_api(prompt):
        # API endpoint for requesting the model
        API_ENDPOINT = "http://your-api.com/getmodel"
        
        # header for API request
        header = {'Content-Type': 'application/json'}
        
        # data to be sent to API
        data = {'prompt': prompt}
        
        # sending post request to API endpoint
        response = requests.post(API_ENDPOINT, headers=header, json=data)
        
        # check if API request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to request model from API")
            return None



def register():
    bpy.utils.register_class(BRL.RequestModelPanel)
    """Button/Operators"""
    bpy.utils.register_class(BRL.RequestModelOperator)
    bpy.utils.register_class(BRL.UseMicrophoneOperator)
    bpy.types.Scene.request_model_prompt = bpy.props.StringProperty(name="Prompt", default="")

    
def unregister():
    bpy.utils.unregister_class(BRL.RequestModelPanel)
    
if __name__ == "__main__":
    register()
