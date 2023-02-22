class Calculator:

    @staticmethod
    def bmi(kg: float, meter: float) -> float:
        return round(kg/meter**2, 2)

