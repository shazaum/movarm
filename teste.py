import MovArm

moveUp = 10
moveDown = 11
moveRight = 12
moveLeft = 13

movimento = MovArm(moveUp, moveDown, moveRight, moveLeft)

#Mover para cima
movimento.moving("up", True)
movimento.moving("up", False)

#Mover para baixo
movimento.moving("down", True)
movimento.moving("down", False)

#Mover para direita
movimento.moving("right", True)
movimento.moving("right", False)

#Mover para esquerda
movimento.moving("left", True)
movimento.moving("left", False)
