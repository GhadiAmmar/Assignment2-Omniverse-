from pxr import Usd, UsdGeom, Sdf

stage = Usd.Stage.CreateNew("multiple_animations.usda")
stage.setStartTimeCode(1)
stage.setEndTimeCode(192)
#add robot function
def add_robot(name, reference_path, x_offset, layer_offset=None):
    xform = UsdGeom.Xform.Define(stage, f"/{name}")
    UsdGeom.XformCommonAPI(xform).SetTranslate((x_offset,0, 0))
    ref = xform.GetPrim().GetReferences()
    if layer_offset:
        ref.AddReference(reference_path, layerOffset=layer_offset)
    else:
        ref.AddReference(reference_path)

add_robot("Original", "animated_robot.usda", 0)
add_robot("Shifted", "animated_robot.usda", 5, Sdf.LayeOffset(offset=48))
add_robot("HalfSpeed", "animated_robot.usda", 10, Sdf.LayeOffset(scale=0.5))
      
stage.GetRootLayer().Save()