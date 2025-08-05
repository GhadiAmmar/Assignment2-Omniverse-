from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("upper_arm.usda")
xform = UsdGeom.Xform.Define(stage, "/UpperArm")
cube = UsdGeom.Cube.Define(stage, "/UpperArm/Cube") 
cube.CreateSizeAttr(1.0)
UsdGeom.XformCommonAPI(cube).setScale((1, 3, 1))
UsdGeom.XformCommonAPI(cube).setTranslate((0, 1.5, 0))
stage.GetRootLayer().Save()