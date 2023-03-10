[![Netlify Status](https://api.netlify.com/api/v1/badges/7c999fe1-0ef0-4794-8099-0aea6a9ed1c2/deploy-status)](https://app.netlify.com/sites/blenderai/deploys)
https://blenderai.netlify.app/ 
# BlenderRL (BRL)
Blender Reinforcement Learning requires defining several key components such as the reward function, agent, environment, rewards, state, and interpreter. The purpose of the RL model is to create specific 3D models as prompted by the user, animate existing 3D models, or perform some other general task. The RL agent in Blender 3D is trained on all the controls of the software, mapping them to actions it can take to maximize the reward.


# Blender Plugin for Reinforcement Learning
Introduction
This Blender plugin allows users to perform tasks in Blender using a reinforcement learning model. The plugin provides a UI in the 3D viewport for users to input commands, either by typing or using their microphone. The commands are then sent to the reinforcement learning model, which performs the task automatically.

# Installation
To install the plugin, follow these steps:

Download the plugin file `BRL.py` and save it to your Blender addons folder.
Start Blender and go to the preferences.
In the Add-ons tab, search for "Reinforcement Learning" and enable the plugin.
Save your preferences to make the plugin available every time you start Blender.
Usage
The plugin adds a panel to the 3D viewport, which allows you to input commands either by typing or using your microphone. The commands are then sent to the reinforcement learning model for execution.

# Typing Commands
To input commands by typing, simply enter your command in the text field and press the "Submit" button. The plugin will send your command to the reinforcement learning model for execution.

# Using Microphone
To input commands using your microphone, press the microphone icon. The plugin will record your voice for 5 seconds and send the audio to the reinforcement learning model for execution. Note that you will need to have the `sounddevice` module installed to use this feature.

# Code Overview
The plugin is implemented in a single file, `BRL.py`, which contains the following parts:

1. Import statements
2. Custom operator classes for sending commands to the reinforcement learning model
3. UI panel for the 3D viewport
4. `register` and un`register` functions

# Custom Operator Classes
The plugin defines two custom operator classes: `RequestModelOperator` and `UseMicrophoneOperator`. The `RequestModelOperator` class sends the text entered by the user to the reinforcement learning model for execution. The `UseMicrophoneOperator` class records audio using the `sounddevice` module and sends the audio to the reinforcement learning model for execution.

# UI Panel
The plugin adds a UI panel to the 3D viewport, which contains a text field and buttons for entering commands. The panel is defined in the `draw` method of the ``ReinforcementLearningPanel`` class, which inherits from `bpy.types.Panel`. The panel contains two buttons, one for submitting text commands and one for recording audio commands.

# Register and Unregister Functions
The plugin provides `register` and `unregister` functions to enable and disable the plugin, respectively. The functions `register` and `unregister` the custom operator classes and the UI panel.

# Conclusion
This Blender plugin provides a convenient way for users to interact with a reinforcement learning model and perform tasks in Blender. The plugin is easy to install and use, and provides a user-friendly interface for inputting commands. With the ability to record audio, the plugin opens up new possibilities for hands-free interaction with Blender.
