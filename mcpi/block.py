class Block:
    """Minecraft PI block description. Can be sent to Minecraft.setBlock/s"""
    def __init__(self, id, data=0):
        self.id = id
        self.data = data

    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    def __hash__(self):
        return (self.id << 8) + self.data

    def withData(self, data):
        return Block(self.id, data)

    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))
        
    def __repr__(self):
        return "%d, %d"%(self.id, self.data)

AIR                 = Block(0)
STONE               = Block(1)
GRASS               = Block(2)
DIRT                = Block(3)
COBBLESTONE         = Block(4)
WOOD_PLANKS         = Block(5)
SAPLING             = Block(6)
BEDROCK             = Block(7)
WATER_FLOWING       = Block(8)
WATER               = WATER_FLOWING
WATER_STATIONARY    = Block(9)
LAVA_FLOWING        = Block(10)
LAVA                = LAVA_FLOWING
LAVA_STATIONARY     = Block(11)
SAND                = Block(12)
GRAVEL              = Block(13)
GOLD_ORE            = Block(14)
IRON_ORE            = Block(15)
COAL_ORE            = Block(16)
WOOD                = Block(17)
LEAVES              = Block(18)
GLASS               = Block(20)
LAPIS_ORE           = Block(21)
LAPIS_BLOCK         = Block(22)
SANDSTONE           = Block(24)
SANDSTONE_CHISELED  = Block(24, 1)
SANDSTONE_SMOOTH    = Block(24, 2)
BED                 = Block(26)
COBWEB              = Block(30)
GRASS_TALL          = Block(31)
WOOL                = Block(35)
FLOWER_YELLOW       = Block(37)
FLOWER_CYAN         = Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
GOLD_BLOCK          = Block(41)
IRON_BLOCK          = Block(42)
STONE_SLAB_DOUBLE   = Block(43)
STONE_SLAB          = Block(44)
COBBLESTONE_SLAB    = Block(44, 3)
BRICK_BLOCK         = Block(45)
TNT                 = Block(46)
BOOKSHELF           = Block(47)
MOSS_STONE          = Block(48)
OBSIDIAN            = Block(49)
TORCH               = Block(50)
FIRE                = Block(51)
STAIRS_WOOD         = Block(53)
CHEST               = Block(54)
CHEST_TRAPPED       = Block(146)
DIAMOND_ORE         = Block(56)
DIAMOND_BLOCK       = Block(57)
CRAFTING_TABLE      = Block(58)
FARMLAND            = Block(60)
FURNACE_INACTIVE    = Block(61)
FURNACE_ACTIVE      = Block(62)
DOOR_WOOD           = Block(64)
LADDER              = Block(65)
STAIRS_COBBLESTONE  = Block(67)
DOOR_IRON           = Block(71)
REDSTONE_ORE        = Block(73)
REDSTONE_ORE_GLOWING= Block(74)
REDSTONE_TORCH_OFF 	= Block(75)
REDSTONE_TORCH_ON 	= Block(76)
SNOW                = Block(78)
ICE                 = Block(79)
SNOW_BLOCK          = Block(80)
CACTUS              = Block(81)
CLAY                = Block(82)
SUGAR_CANE          = Block(83)
FENCE               = Block(85)
NETHER_BRICK        = Block(112)
NETHER_BRICK_FENCE  = Block(113)
COBBLESTONE_WALL    = Block(139)
MOSSY_COBBLESTONE_WALL = Block(139, 1)
NETHER_RACK 				= Block(87)
GLOWSTONE_BLOCK     = Block(89)
BEDROCK_INVISIBLE   = Block(95)
STONE_BRICK         = Block(98)
GLASS_PANE          = Block(102)
MELON               = Block(103)
FENCE_GATE          = Block(107)
EMERALD_BLOCK       = Block(133)
ANVIL               = Block(145)
REDSTONE_BLOCK      = Block(152)
GLOWING_OBSIDIAN    = Block(246)
NETHER_REACTOR_CORE = Block(247)
