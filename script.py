import sys
import os
sys.path.append(os.path.dirname(__file__))  # nopep8
from Sollumz import register
import bpy


def main():
    register()
    args = sys.argv

    try:
        args = args[args.index("--") + 1:]
    except ValueError:
        args = []

    if len(args) < 2:
        print("Usage: blender -b -P script.py -- [yddpath] [objpath]")
        exit(1)

    [yddpath, objpath] = args

    for obj in bpy.context.scene.objects:
        obj.select_set(True)

    bpy.ops.object.delete()
    bpy.ops.importxml.ydd(filepath=yddpath)
    bpy.ops.export_scene.obj(filepath=objpath)


if __name__ == '__main__':
    main()
