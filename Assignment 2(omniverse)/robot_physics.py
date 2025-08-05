from pxr import Usd, UsdGeom, UsdPhysics, PhysxSchema, Gf

stage = Usd.Stage.CreateNew("physics_robot.usda")
UsdGeom.XformCommonAPI(robot_xform).SetTranslate((0, 5, 0))
robot_xform.GetPrim().GetReferences().AddReference("animated_robot.usda")
#rigid body and collision
UsdPhysics.RigidBodyAPI.Apply(robot_xform.GetPrim())
UsdPhysics.CollisionAPI.Apply(robot_xform.GetPrim())
# physics material 
material= UsdPhysics.Material.Define(stage, "/PhysicsMaterial")
material.CreateStaicFrictionAttr().Set(1.0)
material.CreateDynamicFrictionAttr().Set(0.7)
material.CreateRestitutionAttr().Set(0.9)

bindingAPI = UsdPhysics.MaterialBindingAPI.Apply(robot_xformGetPrim())
bindingAPI.Bind(material)

ground = UsdGeom.Cube.Define(stage, "/GroundPlane")
UsdGeom.XformCommonAPI(ground).SetScale((50, 1, 50))
UsdGeom.XformCommonAPI(ground).SetTranslate((0, -0.5, 0))
UsdPhysics.CollisionAPI.Apply(ground.GetPrim())
UsdPhysics.RigidBodyAPI.Apply(ground.GetPrim()).CreateRigidBodyEnabledAttr(False)

stage.GetRootLayer().Save()