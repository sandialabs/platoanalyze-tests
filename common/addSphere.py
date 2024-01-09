import exodus
import math

mesh = exodus.ExodusDB()
mesh.read("cylinder.exo")

Zbasis = [0.0, 0.0, 1.0]

elementBlock = mesh.elementBlocks[0]
for elemIndex in range(elementBlock.numElements):
  elemNodes = elementBlock.getElement(elemIndex)
  X = 0.0
  Y = 0.0
  Z = 0.0
  for nodeCoord in elemNodes:
    X += nodeCoord[0]/len(nodeCoord)
    Y += nodeCoord[1]/len(nodeCoord)
    Z += nodeCoord[2]/len(nodeCoord)

  tMag = math.sqrt(X*X+Y*Y)
  X /= tMag
  Y /= tMag
  Xbasis = [X, Y, 0.0]
  Ybasis = [-Y, X, 0.0]
  print(elemIndex, ",", Xbasis[0], ",", Xbasis[1], ",", Xbasis[2], ",", Ybasis[0], ",", Ybasis[1], ",", Ybasis[2], ",", Zbasis[0], ",", Zbasis[1], ",", Zbasis[2])
