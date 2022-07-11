import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList


class Goal(Choice):
    """
    Determines the goal of the seed
    Knautilus: Reach the Knautilus and defeat Baron K. Roolenstein
    Banana Bird Hunt: Find a certain number of Banana Birds and rescue their mother
    """
    display_name = "Goal"
    option_knautilus = 0
    option_banana_bird_hunt = 1
    default = 0


class IncludeTradeSequence(Toggle):
    """
    Allows logic to place items at the various steps of the trade sequence
    """
    display_name = "Include Trade Sequence"


class DKCoinsForGyrocopter(Range):
    """
    How many DK Coins are needed to unlock the Gyrocopter
    """
    display_name = "DK Coins for Gyrocopter"
    range_start = 0
    range_end = 41
    default = 30


class KrematoaBonusCoinCost(Range):
    """
    How many Bonus Coins are needed to unlock each level in Krematoa
    """
    display_name = "Krematoa Bonus Coins Cost"
    range_start = 1
    range_end = 17
    default = 15


class NumberOfBananaBirds(Range):
    """
    How many Banana Birds are put into the item pool
    """
    display_name = "Number of Banana Birds"
    range_start = 5
    range_end = 15
    default = 15


class PercentageOfBananaBirds(Range):
    """
    What Percentage of Banana Birds in the item pool are required for Banana Bird Hunt
    """
    display_name = "Percentage of Banana Birds"
    range_start = 20
    range_end = 100
    default = 100


class LevelShuffle(Toggle):
    """
    Whether levels are shuffled
    """
    display_name = "Level Shuffle"


class MusicShuffle(Toggle):
    """
    Whether music is shuffled
    """
    display_name = "Music Shuffle"


class KongPaletteSwap(Choice):
    """
    Which Palette to use for the Kongs
    """
    display_name = "Kong Palette Swap"
    option_default = 0
    option_purple = 1
    option_spooky = 2
    option_dark = 3
    option_chocolate = 4
    option_shadow = 5
    option_red_gold = 6
    option_gbc = 7
    option_halloween = 8
    default = 0


class StartingLifeCount(Range):
    """
    How many extra lives to start the game with
    """
    display_name = "Starting Life Count"
    range_start = 1
    range_end = 99
    default = 5


dkc3_options: typing.Dict[str, type(Option)] = {
    #"death_link": DeathLink,                                 # Disabled
    "goal": Goal,
    #"include_trade_sequence": IncludeTradeSequence,          # Disabled
    "dk_coins_for_gyrocopter": DKCoinsForGyrocopter,
    "krematoa_bonus_coin_cost": KrematoaBonusCoinCost,
    "number_of_banana_birds": NumberOfBananaBirds,
    "percentage_of_banana_birds": PercentageOfBananaBirds,
    "level_shuffle": LevelShuffle,
    #"music_shuffle": MusicShuffle,                           # Disabled
    "kong_palette_swap": KongPaletteSwap,
    "starting_life_count": StartingLifeCount,
}
