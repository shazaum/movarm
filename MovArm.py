import RPi.GPIO as GPIO
import time

class MovArm():

    def __init__(self, moveUp, moveDown, moveRight, moveLeft):
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.moveRight = moveRight
        self.moveLeft = moveLeft
  
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([moveUp, moveDown, moveRight, moveLeft], GPIO.OUT)  # Inicia o movimento
        GPIO.output([moveUp, moveDown, moveRight, moveLeft], GPIO.LOW) # Para o movimento
    
    def moving(self, move, isMoving):
        try:
            if move == "up":
                if isMoving:
                    GPIO.output(self.moveUp, 1)
                else:
                    GPIO.output(self.moveUp, 0)
            if move == "down":
                if isMoving:
                    GPIO.output(self.moveDown, 1)
                else:
                    GPIO.output(self.moveDown, 0)
            if move == "right":
                if isMoving:
                    GPIO.output(self.moveRight, 1)
                else:
                    GPIO.output(self.moveRight, 0)
            if move == "left":
                if isMoving:
                    GPIO.output(self.moveLeft, 1)
                else:
                    GPIO.output(self.moveLeft, 0)

            time.sleep(1)
        
        except KeyboardInterrupt:
            # Ctrl+C foi pressionado
            GPIO.cleanup()  # Limpa configuração
            pass