
from SeasonConst import GrainSeasonNutrientsBase
from util.calculate import Calculator

if __name__ == "__main__":
    abcBase = GrainSeasonNutrientsBase
    print(format(abcBase.THICKENING.value))
    mybmi = Calculator.bmi(62, 1.63)
    print(mybmi)