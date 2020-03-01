1. Bug grows every step. Grow can be positive or negative.
2. Bug grows life long.
3. Bug needs food for maintanence, which is proportional to size.
4. Food supply less than maintanance, bug size reduces, otherwise increases.
5. Bug dies if too thin. e.g. 50% of expected size which is proportional to age.
6. Bug has a food limit, which is proportional to maintanence amount.

ExpectedSize = Age * ExpectedSizeAgeRatio
FoodLimit = Maintanence * FoodLimitRatio + Age * FoodAgeRatio
Growth = f(FoodSupply, Maintanence) = (min(FoodSupply, FoodLimit) / Maintanence - 1) * FoodGrowthRatio
Maintanence = MaintanenceSizeRatio
Size(n+1) = size(n) + Growth * SizeGrowthRatio

