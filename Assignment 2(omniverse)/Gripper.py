from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("gripper.usda")
xform = UsdGeom.Xform.Define(stage, "/Gripper")
sphere = UsdGeom.Sphere.Define(stage, "/Gripper/Sphere")
sphere.CreateRadiusAttr(0.5)
UsdGeom.XformCommonAPI(sphere).setTranslate((0, 0, 0))
stage.GetRootLayer().Save()