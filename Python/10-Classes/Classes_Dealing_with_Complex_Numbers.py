import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.imag = imaginary
        self.real = real
        
    def __add__(self, no):
        real = str(round(float(self.real + no.real), 2))
        if len(real[real.index('.'):]) == 2:
            real = real + '0'
        imag = str(round(float(self.imag + no.imag), 2))
        if len(imag[imag.index('.'):]) == 2:
            imag = imag + '0'
        if float(imag) >= 0:
            return real + '+' + imag + 'i'
        else:
            return real + imag + 'i'
        
    def __sub__(self, no):
        real = str(round(float(self.real - no.real), 2))
        if len(real[real.index('.'):]) == 2:
            real = real + '0'
        imag = str(round(float(self.imag - no.imag), 2))
        if len(imag[imag.index('.'):]) == 2:
            imag = imag + '0'

        if float(imag) >= 0:
            return real + '+' + imag + 'i'
        else:
            return real + imag + 'i'    

    def __mul__(self, no):
        real = str(round(float(self.real * no.real) - (self.imag * no.imag), 2))
        if len(real[real.index('.'):]) == 2:
            real = real + '0'
        imag = str(round(float(self.real * no.imag) + (self.imag * no.real), 2))
        if len(imag[imag.index('.'):]) == 2:
            imag = imag + '0'
        
        if float(imag) >= 0:
            return real + '+' + imag + 'i'
        else:
            return real + imag + 'i'  

    def __truediv__(self, no):
        real = (self.real * no.real) + (self.imag * no.imag)
        imag = (self.imag * no.real) - (self.real * no.imag)
        denominator = no.real ** 2 + no.imag ** 2
        real = str(round(float(real / denominator), 2))
        if len(real[real.index('.'):]) == 2:
            real = real + '0'
        imag = str(round(float(imag / denominator), 2))
        if len(imag[imag.index('.'):]) == 2:
            imag = imag + '0'
        if float(imag) >= 0:
            return real + '+' + imag + 'i'
        else:
            return real + imag + 'i'

    def mod(self):
        Mod = str(round((self.real ** 2 + self.imag ** 2) ** 0.5, 2))
        if len(Mod[Mod.index('.'):]) == 2:
            Mod = Mod + '0'
        return Mod + '+0.00i'

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
