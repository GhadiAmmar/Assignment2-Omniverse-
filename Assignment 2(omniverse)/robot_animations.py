from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("animated_robot.usda")
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)
robot_prim = UsdGeom.Xform.Define(stage, "/Robot")
robot_prim.GetPrim().GetReferences().AddReference("robot.usda")
#base rotation
base_xform = UsdGeom.Xformable(stage.GetPrimAtPath("/Robot/base/lower_arm"))
base_rotate_op = base_xform.AddRotateYOp(opSuffix="BaseRotation")
for frame in [1, 192]:
    angle = 360.0 * (frame - 1) / (192 - 1)
    base_rotate_op.Set(angle, time=frame)

#upper arm twisting rotation
upper_arm_xform = UsdGeom.Xformable(stage.GetPrimAtPath("/Robot/base/lower_arm/upper_arm"))
upper_arm_twist_op = upper_arm_xform.AddRotateYOp(opSuffix="UpperArmTwist")
for frame in [1, 96]:
    angle = 30.0 * (frame - 1)/(96 - 1)
    upper_arm_twist_op.SetAngle(angle, time=frame)

#Gripper Scaling
gripper_xform = UsdGeom.Xformable(stage.GetPrimAtPath("/Robot/base/lower_arm/upper_arm/gripper"))
gripper_scale_op = gripper_xform.AddScaleOp(opSuffix="GripperScaler")
gripper_scale_op.Set((1.0, 1.0, 1.0), time=1)
gripper_scale_op.Set((2.0, 2.0, 2.0), time=96)
gripper_scale_op.Set((1.0, 1.0, 1.0), time=192)

stage.GetRootLayer().Save()
