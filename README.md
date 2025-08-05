# Assignment2-Omniverse-
Animations of robotic arm using usdview
The aim of this assignment is to create an animation for the robotic arm 
The hierarchy is structured in the following way: robot -> base -> lower arm -> upper arm -> gripper (parent to child) so that any animation on a componenet, leads to the same animation on its child components

The animations include : 
Base rotation which rotates the lower arm  around the base for 360 degrees over 192 frames
upper arm twist which rotates the the upper arm for 30 degrees along 96 frames
gripper scaler which increases the scale of the gripper to 2 and back to its original size in 192 frames

multiple animations: this file has 3 versions of the robotic arm, one is original with normal attributes, one is shifted by 48 frames, and one is animated at halfspeed

physics: this file introduces a rigidbody and collider to the robtic arm
A material is defined and binded to the robotic arm and initiated 5 meters on the y-axis, and this material has the attributes of static friction, dynamic friction, and restitution.

a ground plane is defined with collider and rigid body.
