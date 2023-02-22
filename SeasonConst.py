from enum import Enum

# 全穀雜糧類料理添加
class GrainSeasonNutrientsBase(Enum): 
    # 水煮   
    BOILING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 蒸
    STEAMING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }

    # 烤
    ROASTING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 煎,炒
    PANFRYING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 2
        }
    }
    # 乾炸
    DRYFRIED = {
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
    # 濕炸, 酥炸
    DEEPFRIED = {
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
    # 勾芡
    THICKENING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 5,
            "protein": 0,
            "fat": 0
        }
    }

# 豆魚蛋豆類料理添加
class MeatSeasonNutrientsBase(Enum): 
    # 水煮   
    BOILING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 蒸
    STEAMING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }

    # 烤
    ROASTING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 煎,炒
    PANFRYING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 3
        }
    }
    # 乾炸
    DRYFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 5
        }
    }
    # 濕炸, 酥炸
    DEEPFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 10
        }
    }
    # 勾芡
    THICKENING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 5,
            "protein": 0,
            "fat": 0
        }
    }

# 乳品類料理添加
class MilkSeasonNutrientsBase(Enum): 
    # 水煮   
    BOILING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 蒸
    STEAMING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 烤
    ROASTING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 煎,炒
    PANFRYING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 3
        }
    }
    # 乾炸
    DRYFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 5
        }
    }
    # 濕炸, 酥炸
    DEEPFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 10
        }
    }
    # 勾芡
    THICKENING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 5,
            "protein": 0,
            "fat": 0
        }
    }
# 蔬菜類料理添加
class VegSeasonNutrientsBase(Enum): 
    # 水煮   
    BOILING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 蒸
    STEAMING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 烤
    ROASTING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 煎,炒
    PANFRYING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 6
        }
    }
    # 乾炸
    DRYFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 12
        }
    }
    # 濕炸, 酥炸
    DEEPFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 18
        }
    }
    # 勾芡
    THICKENING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 5,
            "protein": 0,
            "fat": 0
        }
    }
# 水果類料理添加
class FruitSeasonNutrientsBase(Enum): 
    # 水煮   
    BOILING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 蒸
    STEAMING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 烤
    ROASTING= {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 0
        }
    }
    # 煎,炒
    PANFRYING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 6
        }
    }
    # 乾炸
    DRYFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 12
        }
    }
    # 濕炸, 酥炸
    DEEPFRIED = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 0,
            "protein": 0,
            "fat": 18
        }
    }
    # 勾芡
    THICKENING = {
        "food_nutrients": {
            "carbon": 15,
            "protein": 2,
            "fat": 0
        },
        "season_nutrients":{
            "carbon": 5,
            "protein": 0,
            "fat": 0
        }
    }