from SeasonConst import *

def test_grain_type():
    grainDeepFriedBase = GrainSeasonNutrientsBase.DEEPFRIED.value
    assert grainDeepFriedBase == {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 4
        }
    }

