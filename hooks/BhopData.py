__all__ = ["Tiers", "Meme", "Tedious", "MapToTier", "ParseTier"]

Tier1 = ["I Don't Know", '^w^', 'de_dust2', 'Strafe FiBzY', 'Ambience', 'Dom', 'Fatberg', 'Persp', 'Reddish', 'Glacial', 'Sonoran', '1n5an3 hard', 'Epic Minigames', 'Eco', 'I Forgot', 'Tangent', 'Diorama', 'Alt Terassi', 'Yuki', 'Snow', 'Synergy', 'Marble', 'TaiShi', 'Stonework', 'The 24th', 'FabricColorz', 'Ruins', 'Springland', 'Floating Sakura', 'Pandemic', 'Orange V2', 'Easyhop', 'Passionlessly', 'Sunday', 'Sea Flow', 'Rainbow', 'Quickly, Quickly', 'Sandy', 'Ploitan', 'Namaste', 'Dumb Blocks', 'Mirage', 'Dice', 'Marble Fanta', 'Dust', 'DownDownDown', 'Autumnland', 'Zoom', 'Lava Escape', 'Lavender', 'Kiwi Cwfx', 'Castaway', 'Stref Amazon', 'Candy Land', 'SDC01', 'Spookstrafe', 'Bless', 'Linen', 'Tide', 'Salmon On Mars', 'Doms', 'Ravine', 'Aztec', 'Drain 2', 'Colorz', 'NeonWood', 'Space Core', 'Spearmint', 'Aziz v2', 'Tri', 'Vertigo', 'Turf', 'Horsepoop 1', 'Dumb Blocks 4', 'Swamp', 'Boppy Bricks', 'Way Too Easy', 'Bobop', 'I DROPPED MY HECKIN POP-TARTS!!', 'Dumb Blocks 3', 'Tropica', 'Obs', 'Concrete', 'Beach Run', 'Barn', 'Grotto', 'Anyyy', 'AcidicHopping', 'Clarity', 'Gotta Go Fast', 'Alone', 'Autumn', 'IceHoppers', 'Go', 'Ice Cave', 'Alley', 'Around The Round', 'Ares', 'Slab', 'Surfhop', 'Lapis', 'Back To Earth', 'Animal', 'Deluxe', 'LM', 'Dawn', 'SimpleHop', 'Saimaa', 'Dumb Blocks 2', 'Down hill', 'Overline', 'Lab', 'Lemon', 'Brick', 'Grass', 'Ascendant', 'Caved in', 'Short N Easy', 'Dream', 'Pro bhopper', 'Strayff', 'Quarry', 'Tutorial', 'Atom', 'Water', 'Tractus', 'City Run V2', 'Patio', 'Slope', 'The Darkness', 'Proving a Point', 'Above and Below', 'Forest River', 'Strafing in Siberia', 'Brick 2', 'Cks Stref', 'Cuboidal', 'Neon Vibes V2', 'Referral', 'The Depraved Expanse', 'OGBLOX', 'Current', 'Dumb Blocks 6', 'Dumb Blocks Mashup', 'O_o', 'Contrast', 'Helios', 'Clarify', 'Splash', 'Read', 'Obby', 'Sard', 'Mediocre', '0000', 'Sidus v2', 'Nandayo', 'Nature', 'Neon Colors', 'Lonely Road', 'Guffaw', 'Wooden', 'Derelict', 'Failure', 'City Fun', 'Waterblocks']
Tier2 = ['Alt Vaahtera', '0 Sanity', '0zirk', 'Frenzy', 'Dipl', 'Royalty', 'Bright', 'Spike Valley', 'Hidden Place', 'RnF', 'Valley of the Kings', 'Nihility', 'Quaint', 'No Lost', 'Qwplint', 'Pasture', 'The Cookhouse', 'Swampy', 'Salmon', 'Rezar', 'A Deep Chicago Night', 'Persepillu', 'Switch', 'Tide2', 'Shade', 'Ocean', 'BaQee', 'Pyte', 'Awake', 'Siberia', 'July', 'Colossus', 'Blue', 'Meadows', 'Nebula', 'Bumblebee', 'Gram of Haze', 'Warzone', 'Magma', 'Waryhm', 'Virus', 'Xaxa', 'Juma', 'Faith', 'FrozenRuins', 'Kotodama', 'Cpm', 'Dusty Run', 'Eazy v2', 'Danger Noodle', 'Cubelights', 'Venerial', 'Crypt', 'Wild', 'Hue', 'Nandayo 2', 'Not Flat', 'Futurebound', 'Cobblestone', 'AutoBadges', 'Heights', 'Horrible V2', 'Coloration', 'Namaste 2', 'Construction', 'Dawn3', 'Blue Shade', 'Rising', 'Manpoo', 'Arc Simtre', 'Splash 2', 'Abbez1337', 'Pumpkins', 'Stone', 'Serenity', 'Adventure v2', 'Reach', 'Fizzle', 'Azure', 'Cotton Candy', 'Colorize', 'Macaroni and Cheese', 'Moderated', 'The Darkness 2', 'FL Eli', 'Brick Worship', 'Cyber', 'Fortnite', 'Mauve', 'Planets', 'Pohb not idiot', 'Reborn', 'Ruined (New)', 'ShadowKeep', 'The Gift of Giving', 'Default', 'Snowy Heights', 'Epiphany (Short)', 'Vastum Desertum', 'Itaek', 'Lost in Forest', 'Synced V2', 'Weld', 'Outback Shore', 'Harmony', 'Reflexes', 'Tropics', 'The Darkness3', 'Office Run', 'Helios II', 'Nedone', 'Freedom Puppies XXX', 'Studs', 'Ravashing Ravine', 'Memento Vivere', 'Soaatana', '[]', 'Lego', 'Who needs checkpoints', 'Sidle', 'Emily', 'Reversal', '3d', 'Calm Down', 'Maze', 'Senpai', 'Dreamwave', 'Leaf Beach', 'Indigo', 'Candy', 'Bounce Pad', 'Green', 'Eskay', 'Island Adventure', 'Triumphant Light', 'FrankerZ', 'Bellow', 'Trials Of The Endless Beige Bricks And Sands Below', 'Difficulties', 'Touch']
Tier3 = ['Hello', 'Technicolor', 'Landshaft', 'Bubblegum', 'Aura', 'Backrooms', 'Symphony', 'Geometrical', 'Living Like a Ghost', 'Dev V1', 'Translucidity v2', 'Materials 2', 'Ruined (Old)', 'Patent', 'Chrysanthemum Throne', 'Impulse', 'Rexlum', 'FrostBite', 'Kynto', 'JakeThe_God', 'ThirdTime', 'Elysian', 'Larena', 'Flux', 'Levels', 'Cave', 'Ultimate', 'Minimalism', 'Cast', 'Happy Gummy Bear', 'Cartoons', 'Tech', 'Jolt', 'Rin', 'Yunch', 'Bunte Kuh', 'Paradise 2', 'Paradigm', 'Hefty Trashbags', 'Minecraft', 'Woods', 'Radiant', 'Tyle', 'One Vector', 'Pastel', 'Green Shade', 'X', 'Bhop World', 'Z', 'Deletive', 'Rise', 'Reverse', 'Vice Spice', 'Bloc', 'Wasteland', 'Aloof', 'Azulis', 'The Crusher', 'Way Back When', 'Y', 'Horizon', 'Fus', 'Accuracy2', 'Sam9268', 'Emevaelx3', 'Pruxish', 'Tomb', 'Bad map', 'Dust town', 'Acid', 'Mush2room', 'Bruh', 'Abstract', 'Lucid', 'Dawn2', 'Kitsune', 'Monotonous', 'Cobalt', 'Compact', 'Emblem Easy', 'Dumb Studs 3', 'Halycon', 'Vibrant', 'Avery', 'Materials', 'Mushrooms v1', 'Spectrum', 'Jon', 'Stages', 'Spongebob', 'Alpine', 'Bibbas', 'Screech', 'Attack of the Big Fat Meanies', 'Zyper', 'Danmark', 'Legoflix remade', 'Navigator', 'Overgrown', 'Terral', 'Vacation', 'Snowstorm', 'Little Scavenger Hunt', 'Chrome', 'The Map', 'Hex', 'Quarry (CS:S)', 'Questionable Trials', 'Soulscape', 'IdiotHop', 'Purple Flow', 'Dumb Studs', 'Green Yellow Red Rtv', 'Rise To', 'Solitude', 'Ascend', 'Phobic', 'Omgdogs', 'The Fool', 'Automatic', 'Lazy Larry', 'Golf Yourself', 'Haarukka', 'Melancholy']
Tier4 = ['Fur', 'Emblem 6', 'Grasspain', 'Potato3', 'Dumb Studs Mashup', 'Trials', 'Moonlight', 'Ice', 'Clarion', 'Phunedmonium', 'Downfall', 'BloodBath', 'Emblem 2', 'Lenchuonium', 'Calibrate', 'Xerox', 'Super Easy Tutorial', 'Arcane V2', 'Legowo', 'Im Eating a Bagel', 'Totem', 'Emblem 5', 'Iso', 'Dumb Studs 2', 'Emblem 4', 'Paradise', 'Numismatic', 'Sad Gummy Worm', "The Dragon's Lair", 'Hibiscus', 'Toc', 'Concord', 'Sincerely, Tokyo', 'Septic', 'MadeinTYO', 'Emblem', 'Aeiou', 'Quaternium', 'Dumb Studs 6', 'Stone Tower', 'Dumb Studs 4', 'FPS Max SR', 'RPG', 'Monster Jam', 'Accuracy', 'Emblem 3', 'Sandstorm', 'Finding 400bc', 'Just One Stage']
Tier5 = ['Wannabe', 'Dumb Cave', 'Kulla', 'Bleak, Bland, and Boring', 'Badges(Full) recreated', 'Badges2', 'Accuracy3', 'Three Mountains', 'Ka-Chow!', 'Koi', 'Norwegian Wood', 'Sqee', 'Canary', 'Yonkoma', 'Alvo 2', 'Blocky Compacts (無駄のない立方体)', 'Drewfc was being uncool', 'Very Long Map', 'Bluebeat v2', "Dracula's Revenge", 'Tension', 'Grozy', 'Plink', 'Plink 2', 'Hiraeth']
Tier6 = ['In Progress', ':3', 'BrickColors', 'Hm3']

Ignored = ['Nexus', 'Icy Wasteland', 'Pink Lemonade', 'Chromatic Challenges', 'Desperation', 'Referral II', 'Colorful Loop', 'Facility', 'White And Black', 'Poly', 'Burrow', 'Keep It Simple', 'Triple Color', 'Asteria', 'Memento Mori', 'Perspective', 'Tropical', 'Blue Abstract', 'Decorum', 'I Crashed My 2003 Honda Accord Into The Smokeshop', 'Verdant Void', 'Red Shade']
Meme = ['Ka-Chow!', 'Lonely Road', 'Lazy Larry', 'Go', 'Calm Down', 'Maze', 'FrankerZ']
Tedious = ['Plink', 'Plink 2', 'Trials', 'In Progress', ':3', 'Hm3', 'Hiraeth', 'Dumb Cave']
Unreleased = ['Office Run'] # So we can tier maps early but not have them in the pool early

Tiers = [
	Tier1,
	Tier2,
	Tier3,
	Tier4,
	Tier5,
	Tier6,
]

MapToTier = {}

def ParseTier(text):
	if len(text) == 2:
		Low = int(text[1])
		return (Low, Low)
	elif len(text) == 5:
		Low = int(text[1])
		High = int(text[4])
		return (Low, High)
	else:
		error(f"Invalid tier text: '{text}'")

for t in range(len(Tiers)):
	Tier = Tiers[t]
	for i in range(len(Tier)):
		Tier[i] = Tier[i].replace(":", ";") # I hate Quarry (CS:S)
		MapToTier[Tier[i]] = t+1
	for Map in Unreleased:
		if Map in Tier:
			Tier.remove(Map)
for i in range(len(Meme)):
	Meme[i] = Meme[i].replace(":", ";") # I hate :3 too
for i in range(len(Tedious)):
	Tedious[i] = Tedious[i].replace(":", ";")