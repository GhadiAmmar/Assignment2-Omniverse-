from pxr import Usd,UsdGeom

stage = Usd.Stage.CreateNew("base.usda")
xform = UsdGeom.Xform.Define(Stage, "/Base")
cylinder = UsdGeom.Cylinder.Define(Stage, "/Base/Cylinder")
cylinder.CreateRadiusAttr(1.0)
cylinder.CreateHeightAttr(0.5)
UsdGeom.XformCommonAPI(cylinder).setTranslate((0, 0.25, 0))
stage.GetRootLayer().Save()
