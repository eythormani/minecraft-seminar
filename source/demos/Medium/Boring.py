from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    
    startx = pos.x + 3
    starty = pos.y + 3
    startz = pos.z + 3

    endx = pos.x - 3
    endy = pos.y - 3
    endz = pos.z - 3
    mc.setBlocks(startx, starty, startz, endx, endy, endz, 0)
    
    
