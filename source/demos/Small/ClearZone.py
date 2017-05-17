#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
 
def clearZone( alocx, alocz, blocx, blocz ):
    mc.setBlocks( alocx, 0, alocz, blocx, 64, blocz, block.AIR )
    mc.setBlocks( alocx, -1, alocz, blocx, -1, blocz, block.STONE )
 
if __name__ == "__main__":
    mc = minecraft.Minecraft.create( server.address )
    clearZone( -20, -20, 20, 20 )
