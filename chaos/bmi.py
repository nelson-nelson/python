from collections import OrderedDict


class HealthData:
    def __init__(self, weight: float, height: float):
        self.weight = weight
        self.height = height
        self.bmi = weight / height ** 2

    def obesity_status(self) -> str:
        obesity_dict = OrderedDict({
            18.5: 'underweight',
            25: 'normal',
            30: 'overweight',
            100: 'obesity'
        })
        for bmi, obesity in obesity_dict.items():
            if self.bmi < bmi:
                return obesity
        return 'invalid bmi'


if __name__ == '__main__':
    nelson = HealthData(79.38, 1.70)
    print(f"Nelson is {nelson.weight} Kg, {nelson.height} M")
    print(f"His BMI number is {nelson.bmi} and he is {nelson.obesity_status()}")


