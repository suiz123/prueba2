from django.shortcuts import render

from django.shortcuts import render
 
class CalculadoraBasica:
    def __init__(self, num1, num2, operacion):
        self.num1 = num1
        self.num2 = num2
        self.operacion = operacion
 
    def calcular(self):
        if self.operacion == 'suma':
            return self.num1 + self.num2
        elif self.operacion == 'resta':
            return self.num1 - self.num2
        elif self.operacion == 'multiplicacion':
            return self.num1 * self.num2
        elif self.operacion == 'division':
            return self.num1 / self.num2 
        else:
            return "Operación no válida"
 
def calculadora_view(request):
    resultado = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operacion = request.POST.get('operacion')
 
        calculadora = CalculadoraBasica(num1, num2, operacion)
        resultado = calculadora.calcular()
 
    return render(request, 'calculadora.html', {'resultado': resultado})
