# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle ():
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        
#вычисляем стороны
        self.AB = round(math.sqrt(((By - Ay)**2) + ((Bx - Ax)**2)),2)
        self.BC = round(math.sqrt(((Cy - By)**2) + ((Cx - Bx)**2)),2)
        self.CA = round(math.sqrt(((Ay - Cy)**2) + ((Ax - Cx)**2)),2)

    def perimetr(self):
        self.perimetr = round((self.AB + self.BC + self.CA), 2)
        return (self.perimetr)

    def square(self):
        self.perimetr = self.perimetr*0.5
        self.square =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.square)

    def height_a(self):
        self.height = round((2*self.square/self.AB),2)
        return (self.height)
        
    def height_b(self):
        self.height = round((2*self.square/self.BC),2)
        return (self.height)
        
    def height_c(self):
        self.height = round((2*self.square/self.CA),2)
        return (self.height)        

calc = Triangle(int(input("Ax= ")), int(input("Ay= ")), int(input("Bx= ")), int(input("By= ")), int(input("Cx= ")), int(input("Cy= ")))     

print('Длина строн: АВ = {}, ВС = {}, СА = {}'.format(calc.AB, calc.BC,calc.CA))
print('Периметр: {}'.format(calc.perimetr()))
print('Площадь: {}'.format(calc.square()))
print('Высота A: {}'.format(calc.height_a()))     
print('Высота B: {}'.format(calc.height_b()))  
print('Высота C: {}'.format(calc.height_c())) 

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
# м б равнобедренная??
import math
class Trapeze ():
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.Cx = Cx
        self.Cy = Cy
        self.Cx = Dx
        self.Cy = Dy        
        
#вычисляем стороны
        self.AB = round(math.sqrt(((By - Ay)**2) + ((Bx - Ax)**2)),2)
        self.BC = round(math.sqrt(((Cy - By)**2) + ((Cx - Bx)**2)),2)
        self.CD = round(math.sqrt(((Dy - Cy)**2) + ((Dx - Cx)**2)),2)
        self.DA = round(math.sqrt(((Ay - Dy)**2) + ((Ax - Dx)**2)),2)
        
#вычисляем диагонали    
        self.AC = round(math.sqrt(((Cy - Ay)**2) + ((Cx - Ax)**2)),2)
        self.BD = round(math.sqrt(((Dy - By)**2) + ((Dx - Bx)**2)),2)
        
#проверяем, является ли трапеция равнобедренной(длина диагоналей должна совпадать)
    def check(self):
        if self.AC == self.BD:
           self.check = 'Да'
        else: 
           self.check = 'Нет'
        return (self.check)

    def perimetr(self):
        self.perimetr = round((self.AB + self.BC + self.CD + self.DA), 2)
        return (self.perimetr)
        
    def square(self):
        self.square =  ((self.BC + self.DA)/2)* math.sqrt(self.AB**2 - (((self.DA - self.BC)**2)/4)) 
        return (self.square)        
  
calc = Trapeze(2, 2, 3, 5, 8, 5, 9, 2)

print('Длина строн: АВ = {}, ВС = {}, СD = {}, DА = {}'.format(calc.AB, calc.BC,calc.CD,calc.DA))
print('Длина диагоналей: АС = {}, BD = {} '.format(calc.AC, calc.BD))
print('Является ли трапеция равнобедренной? {} '.format(calc.check()))
print('Периметр: {}'.format(calc.perimetr()))
print('Площадь: {}'.format(calc.square()))


