from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("robot.usda")
robot = UsdGeom.Xform.Define(stage, "/Robot")
stage.setDefaultPrim(robot.GetPrim())

def add_component(name, file_path, translate, parent, rotate, scale):
    path = f"{parent}/{name}"
    xform = UsdGeom.Xform.Define(stage, path)
    UsdGeom.XformCommonAPI(xform).SetTranslate(translate)
    UsdGeom.XformCommonAPI(xform).SetRotate(rotate)
    UsdGeom.XformCommonAPI(xform).SetScale(scale)
    xform.GetPrim().GetReferences().AddReference(file_path)
    return path

base_path = add_component("base", "base.usda", (0, 0, 0), "/Robot", (0, 0, 0), (1, 1, 1))
lower_arm_path = add_component("lower_arm", "lower_arm.usda", (0, 0.5, 0), base_path, (0, 0, 0), (1, 1, 1))
upper_arm_path = add_component("upper_arm", "upper_arm.usda", (0, 3.5, 0), lower_arm_path,(0, 45, 0), (1, 1, 1))
gripper_path = add_component("gripper", "gripper.usda", (0, 6.5, 0), upper_arm_path,(0, 0, 0), (1, 1, 1))

stage.GetRootLayer().Save()
