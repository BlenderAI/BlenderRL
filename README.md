# BlenderRL (BRL)
[![Netlify Status](https://api.netlify.com/api/v1/badges/7c999fe1-0ef0-4794-8099-0aea6a9ed1c2/deploy-status)](https://app.netlify.com/sites/blenderai/deploys)

Blender Reinforcement Learning (BlenderAI) is an innovative AI-powered solution designed to automate 3D modeling, animation, and various Blender tasks using reinforcement learning (RL). By integrating Python Blender scripts and OpenUSD (Universal Scene Description), BlenderAI delivers a robust platform for creating, sharing, and managing 3D assets with ease.

---

## **Key Features**
1. **Reinforcement Learning in Blender**:
   - RL agents trained to perform complex Blender tasks by mapping software controls to optimal actions for specific goals.
   - Applications include creating 3D models, animating existing models, and executing user-defined tasks.

2. **OpenUSD Integration**:
   - **Interoperability**: Enables seamless data exchange across various 3D tools (e.g., Blender, Maya, Houdini).
   - **Scalability**: Handles large, complex scenes efficiently using OpenUSD's hierarchical structure.
   - **Collaboration**: Facilitates consistent asset sharing and collaborative workflows.

3. **Plugin for Blender**:
   - **User-Friendly Interface**: Input commands via text or voice in Blender's 3D viewport.
   - **Task Automation**: Commands are executed by the RL model, streamlining 3D creation.
     
---

## **Installation**
1. Download the plugin file `BRL.py` and save it to your Blender addons folder.
2. Open Blender and navigate to **Edit > Preferences > Add-ons**.
3. Search for "Reinforcement Learning" and enable the plugin.
4. Save preferences to make the plugin available every time Blender starts.

---

## **Usage**
### **Typing Commands**
- Enter commands in the provided text field and click "Submit" to execute tasks via the RL model.

### **Using Microphone**
- Click the microphone icon to record voice commands (5 seconds) and send them to the RL model.
- Note: Install the `sounddevice` module for this feature.

---

## **OpenUSD Workflow**
1. **Exporting Assets**:
   - Use OpenUSD to save generated 3D models, animations, and scenes for reuse in other software or workflows.
2. **Data Interoperability**:
   - Easily integrate BlenderAI assets with tools like Maya, Houdini, or Unreal Engine for a seamless pipeline.
3. **Collaborative Training**:
   - Store and share RL training data, such as scene configurations and control actions, using OpenUSD for reproducibility.

---

## **Code Overview**
The plugin is implemented in a single file, `BRL.py`, which contains:
1. **Import Statements**: Required modules for Blender and RL integration.
2. **Custom Operator Classes**:
   - `RequestModelOperator`: Sends user commands to the RL model.
   - `UseMicrophoneOperator`: Records and processes audio commands.
3. **UI Panel**:
   - Adds a panel to Blender’s 3D viewport for text and voice input.
4. **Register and Unregister Functions**:
   - Manage plugin activation and deactivation.

---

## **Future Plans**
- Extend RL agent capabilities to support more advanced modeling and animation tasks.
- Leverage OpenUSD for RL model output, enabling faster workflows and multi-tool compatibility.
- Introduce a feedback loop for user ratings to refine RL agent performance.

---


## **Conclusion**
BlenderAI combines the power of Python Blender scripting and OpenUSD to redefine 3D content creation. With reinforcement learning at its core, this project bridges the gap between creativity and automation, making Blender tasks more efficient and accessible.
