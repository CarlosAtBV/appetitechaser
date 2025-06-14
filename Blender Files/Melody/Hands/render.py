import bpy, bgl, blf, sys
import subprocess, math

scene = bpy.context.scene
actions = [
    [ "test", 1, 1 ],
    [ "testpoke", 1, 1 ],
    [ "melee_idle", 1, 3 ],
    [ "punch_1", 1, 3 ],
    [ "nikki", 1, 5 ],
    [ "nikki_clip", 1, 1 ],
]

actions = [
    [ "nikki_clip", 1, 5 ],
]

for action in actions:
    bpy.data.objects["Armature"].animation_data.action = bpy.data.actions.get(action[0])
    for frame in range(action[1], action[2]+1):
        scene.frame_set(frame)
        scene.render.filepath = "//render/"+action[0]+"-"+str(frame)
        bpy.ops.render.render(write_still=True)