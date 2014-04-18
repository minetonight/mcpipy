import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import server


class PyramideBuilder:
	
	def __init__(self, corner_vec3, sideX, sideZ, slopeXRatio, slopeZRatio, offsetX, offsetZ, material_id):
		
		self.x1 = corner_vec3.x
		self.y1 = corner_vec3.y
		self.z1 = corner_vec3.z
		self.sideX = sideX # base dimentions
		self.sideZ = sideZ
		self.slopeXRatio = slopeXRatio # the vertical size of pyramide steps
		self.slopeZRatio = slopeZRatio
		self.offsetX = offsetX  # the horisontal size of the pyramide steps
		self.offsetZ = offsetZ 
		self.material_id = material_id
	#eof init
	
	
	def createPyramide(self):
		
		# Connect to Minecraft.
		try:
				self.mc = minecraft.Minecraft.create(server.address)
		except:
				print "Cannot connect to Minecraft."
				sys.exit(0)
		
		# creation loop
		dx = 0
		dz = 0
		level = 0
		widthX = self.sideX
		widthZ = self.sideZ
		while (widthX >= self.sideX/2 or self.slopeXRatio < 1) and (widthZ >= self.sideZ/2 or self.slopeZRatio < 1):
			#put layer of the material
			self.mc.setBlocks(self.x1+dx, self.y1+level, self.z1+dz, self.x1+widthX, self.y1+level, self.z1+widthZ, self.material_id)
			print "level %s" % level
			
			level += 1
			
			if self.slopeXRatio > 0 and level % self.slopeXRatio == 0:
				dx += self.offsetX
				widthX -= self.offsetX
			if self.slopeZRatio > 0 and level % self.slopeZRatio == 0:
				dz += self.offsetZ
				widthZ -= self.offsetZ
		#eof while
		
	#eof createPyramide
	
#eof PyramideBuilder


if __name__ == "__main__":
	"""user variables"""
	# base center coordinates
	x0 = 321
	y0 = 119
	z0 = 86

	sideX = 32 # base dimentions
	sideZ = 5
	slopeXRatio = 1 # the vertical size of pyramide steps
	slopeZRatio = 0
	offsetX = 1 # the horisontal size of the pyramide steps
	offsetZ = 1
	#material_id = block.AIR.id 				# to clean what you did :D
	material_id = block.SANDSTONE.id

	# your world spown location
	spawnX = 200
	spawnY = 65
	spawnZ = 200

	"""eof user variables"""

	#calc starting corner point
	x1 = x0 - sideX/2 - spawnX
	y1 = y0 - spawnY
	z1 = z0 - sideZ/2 - spawnZ
	
	builder = PyramideBuilder(Vec3(x1, y1, z1), sideX, sideZ, slopeXRatio, slopeZRatio, offsetX, offsetZ, material_id)
	builder.createPyramide()
#eof main
