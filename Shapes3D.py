import Shapes

class Cylinder:
	def __init__(self, radius, height):
		self._height = height
		self._base = Shapes.Circle(radius)

		self._surfaceArea = self._GetSurfaceArea()
		self._volume = self._GetVolume()

	def _GetSurfaceArea(self):
		baseArea = self._base.GetArea()
		faceArea = self._base.GetPerimeter() * self._height

		# base area * 2 + faceArea
		return (baseArea * 2) + faceArea

	def _GetVolume(self):
		return self._base.GetArea() * self._height

	def GetSurfaceArea(self):
		return self._surfaceArea

	def GetVolume(self):
		return self._volume
