from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item
import random

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create categories
category1 = Category(name="Books")
category2 = Category(name="Movies, Music & Games")
category3 = Category(name="Electronics, Computers & Office")
category4 = Category(name="Home, Garden & Tools")
category5 = Category(name="Food & Grocery")
category6 = Category(name="Beauty & Health")
category7 = Category(name="Toys, Kids & Baby")
category8 = Category(name="Clothing, Shoes & Jewelry")
category9 = Category(name="Handmade")
category10 = Category(name="Sports & Outdoors")
category11 = Category(name="Automotive & Industrials")

categories = [category1, category2, category3, category4, category5,
              category6, category7, category8, category9, category10,
              category11]

# Add categories to database
for category in categories:
    if session.query(Category).filter_by(
       name=category.name).first() is not None:
        print("Category already existing. Skipping...")
    else:
        session.add(category)
        session.commit()
print "Categories added!"

# Create items
item1 = Item(name="Origin", description="Robert Langdon, Harvard professor\
    of symbology and religious iconology, arrives at the ultramodern \
    Guggenheim Museum Bilbao to attend a major announcement-the unveiling of \
    a discovery that \"will change the face of science forever.\" The \
    evening's host is Edmond Kirsch, a forty-year-old billionaire and \
    futurist whose dazzling high-tech inventions and audacious predictions \
    have made him a renowned global figure. Kirsch, who was one of Langdon's \
    first students at Harvard two decades earlier, is about to reveal an \
    astonishing breakthrough . . . one that will answer two of the \
    fundamental questions of human existence.", category=category1)
item2 = Item(name="It", description="Stephen King's terrifying, classic \
    #1 New York Times bestseller, \"a landmark in American literature\" \
    (Chicago Sun-Times)-about seven adults who return to their hometown to \
    confront a nightmare they had first stumbled on as teenagers...an evil \
    without a name: It.", category=category1)
item3 = Item(name="A Column of Fire", description="As Europe erupts, can \
    one young spy protect his queen? International bestselling author Ken \
    Follett takes us deep into the treacherous world of powerful monarchs, \
    intrigue, murder, and treason with his magnificent new epic, \
    A Column of Fire.", category=category1)
item4 = Item(name="The Rooster Bar", description="Mark, Todd, and Zola came \
    to law school to change the world, to make it a better place. But now, \
    as third-year students, these close friends realize they have been duped. \
    They all borrowed heavily to attend a third-tier, for-profit law school \
    so mediocre that its graduates rarely pass the bar exam, let alone get \
    good jobs. And when they learn that their school is one of a chain owned \
    by a shady New York hedge-fund operator who also happens to own a bank \
    specializing in student loans, the three know they have been caught up \
    in The Great Law School Scam.", category=category1)
item5 = Item(name="Harry Potter and the Sorcerer's Stone", description="\
    Harry Potter has never even heard of Hogwarts when the letters start \
    dropping on the doormat at number four, Privet Drive. Addressed in green \
    ink on yellowish parchment with a purple seal, they are swiftly \
    confiscated by his grisly aunt and uncle. Then, on Harry's eleventh \
    birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts \
    in with some astonishing news: Harry Potter is a wizard, and he has a \
    place at Hogwarts School of Witchcraft and Wizardry. An incredible \
    adventure is about to begin!", category=category1)
item6 = Item(name="Before We Were Yours", description="Memphis, 1939. \
    Twelve-year-old Rill Foss and her four younger siblings live a magical \
    life aboard their family's Mississippi River shantyboat. But when their \
    father must rush their mother to the hospital one stormy night, Rill is \
    left in charge-until strangers arrive in force. Wrenched from all that is \
    familiar and thrown into a Tennessee Children's Home Society orphanage, \
    the Foss children are assured that they will soon be returned to their \
    parents-but they quickly realize the dark truth. At the mercy of the \
    facility's cruel director, Rill fights to keep her sisters and brother \
    together in a world of danger and uncertainty.", category=category1)
item7 = Item(name="The Cuban Affair", description="Daniel Graham \
    MacCormick-Mac for short-seems to have a pretty good life. At age \
    thirty-five he's living in Key West, owner of a forty-two-foot charter \
    fishing boat, The Maine. Mac served five years in the Army as an infantry \
    officer with two tours in Afghanistan. He returned with the Silver Star, \
    two Purple Hearts, scars that don't tan, and a boat with a big bank \
    loan. Truth be told, Mac's finances are more than a little \
    shaky.", category=category1)
item8 = Item(name="Harry Potter and the Order of the Phoenix", description="\
    Dark times have come to Hogwarts. After the Dementors' attack on his \
    cousin Dudley, Harry Potter knows that Voldemort will stop at nothing to \
    find him. There are many who deny the Dark Lord's return, but Harry is \
    not alone: a secret order gathers at Grimmauld Place to fight against the \
    Dark forces. Harry must allow Professor Snape to teach him how to protect \
    himself from Voldemort's savage assaults on his mind. But they are \
    growing stronger by the day and Harry is running out of \
    time ...", category=category1)
item9 = Item(name="Sleeping Beauties", description="In a future so real and \
    near it might be now, something happens when women go to sleep: they \
    become shrouded in a cocoon-like gauze. If they are awakened, if the \
    gauze wrapping their bodies is disturbed or violated, the women become \
    feral and spectacularly violent. And while they sleep they go to another \
    place, a better place, where harmony prevails and conflict is \
    rare.", category=category1)
item10 = Item(name="A Game of Thrones", description="From a master of \
    contemporary fantasy comes the first novel of a landmark series unlike \
    any you've ever read before. With A Game of Thrones, George R. R. Martin \
    has launched a genuine masterpiece, bringing together the best the genre \
    has to offer. Mystery, intrigue, romance, and adventure fill the pages \
    of this magnificent saga, the first volume in an epic series sure to \
    delight fantasy fans everywhere.", category=category1)
item11 = Item(name="Call of Duty: WWII", description="Call of Duty returns \
    to its roots with Call of Duty: WWII-a breathtaking experience that \
    redefines World War II for a new gaming generation. Land in Normandy on \
    D-Day and battle across Europe through iconic locations in history's most \
    monumental war. Experience classic Call of Duty combat, the bonds of \
    camaraderie, and the unforgiving nature of war against a global power \
    throwing the world into tyranny.", category=category2)
item12 = Item(name="Assassin's Creed Origins", description="Ancient Egypt: \
    home of colossal pyramids, gilded tombs, tyrannical god-kings, and the \
    origin story of the Assassins. As Cleopatra empire crumbles, the birth of \
    the Assassin's Brotherhood will lead to an extraordinary shift of the \
    world order. Along your journey, the mysteries of Ancient Egypt will be \
    revealed. Assassin Creed Origins uncovers the beginning of the \
    Brotherhood. Fight in epic battles, master a completely reinvented combat \
    system, and explore the entirety of Egypt. With the all-new quest system, \
    complete missions in any order you choose, and follow your own path to \
    greatness.", category=category2)
item13 = Item(name="Crash Bandicoot N. Sane Trilogy", description="Your \
    favorite marsupial, Crash Bandicoot, is back! He's enhanced, entranced & \
    ready-to-dance with the N. Sane Trilogy game collection. Now you can \
    experience Crash Bandicoot like never before in Fur-K. Spin, jump, wump \
    and repeat as you take on the epic challenges and adventures through the \
    three games that started it all, Crash Bandicoot, Crash Bandicoot 2: \
    Cortex Strikes Back and Crash Bandicoot: Warped. Relive all your favorite \
    Crash moments in their fully-remastered HD graphical glory and get ready \
    to put some UMPH in your WUMP!", category=category2)
item14 = Item(name="Grand Theft Auto V", description="Experience Rockstar \
    Games' critically acclaimed open world game, Grand Theft Auto V. When a \
    young street hustler, a retired bank robber and a terrifying psychopath \
    find themselves entangled with some of the most frightening and deranged \
    elements of the criminal underworld, the U.S. government and the \
    entertainment industry, they must pull off a series of dangerous heists \
    to survive in a ruthless city in which they can trust nobody, least of \
    all each other.", category=category2)
item15 = Item(name=".hack//G.U. Last Recode", description="Log back into \
    the .hack//G.U. trilogy and return to \"The World\", as Haseo tracks down \
    Tri-Edge in .hack//G.U. Last Recode, now with enhanced graphics, improved \
    gameplay, and brand new modes! This collection includes all 3 original \
    .hack//G.U. titles, Rebirth, Reminisce, and Redemption, all fully \
    restored and remastered for PS4and PC. Immerse yourself in \"The World\", \
    a MMORPG, and find out what is real and what is reality in .hack//G.U. \
    Set in 2017, years after the events of the first .hack series, \"The \
    World\" has now been rebuilt. Follow Haseo as logs into \"The World\" \
    and hunts PKs (Player Killers), in order to gain strength and track down \
    Tri-Edge, a strong PK who attacked his friend, Shino, in the game and put \
    her into a coma in real life. Relive the drama and epic battles in 1080p \
    and 60fps, and improved battle balance and pacing for the definitive \
    .hack//G.U. experience.", category=category2)
item16 = Item(name="South Park: The Fractured but Whole", description="\
    From the creators of South Park, Trey Parker and Matt Stone, comes an \
    outrageous sequel to 2014's South Park: The Stick of Truth. In the quiet \
    mountain town of South Park, darkness has spread across the land. An \
    entire squad of superheroes will rise to combat this evil, led by a \
    nocturnal scavenger sworn to clean the trash can of South Park society. \
    Create your superhero and use your superpowers to save South Park so \
    Coon and Friends can take their rightful place as the greatest team of \
    superheroes ever assembled, and get the movie deal they so richly \
    deserve.", category=category2)
item17 = Item(name="Destiny 2", description="From the makers of the \
    acclaimed hit game Destiny, comes the much-anticipated sequel. An action \
    shooter that takes you on an epic journey across the solar system. \
    Humanity's last safe city has fallen to an overwhelming invasion force, \
    led by Ghaul, the imposing commander of the brutal Red Legion. He has \
    stripped the city's Guardians of their power, and forced the survivors \
    to flee. You will venture to mysterious, unexplored worlds of our solar \
    system to discover an arsenal of weapons and devastating new combat \
    abilities. To defeat the Red Legion and confront Ghaul, you must reunite \
    humanity's scattered heroes, stand together, and fight back to reclaim \
    our home. ", category=category2)
item18 = Item(name="Minecraft", description="Build! Craft! Explore! The \
    critically acclaimed Minecraft comes to PlayStation 4, offering bigger \
    worlds and greater draw distance than the PS3 and PS Vita editions. \
    Create your own world, then, build, explore and conquer. When night \
    falls the monsters appear, so be sure to build a shelter before they \
    arrive. The world is only limited by your imagination! Bigger worlds and \
    greater draw distance than PS3 and PS Vita Editions Includes all \
    features from the PS3 version Import your PS3 and PS Vita worlds to the \
    PS4 Edition.", category=category2)
item19 = Item(name="Middle-Earth: Shadow Of War", description="The sequel \
    to the critically-acclaimed Middle-Earth: Shadow of Mordor - winner of \
    over 50 industry awards - arrives this August, continuing the original \
    story of Talion and Celebrimbor, who must now go behind enemy lines to \
    forge an army and turn all of Mordor against the dark lord, Sauron. \
    Immerse yourself in the epic war for Middle-earth as you confront the \
    Dark Lord Sauron and his Ringwraith's. Forge a Ring of Power to dominate \
    your enemies and command your followers as you experience a unique, \
    personal story brought to life by the award-winning Nemesis \
    System.", category=category2)
item20 = Item(name="Uncharted: The Lost Legacy ", description="From \
    critically acclaimed developers Naughty Dog comes the first standalone \
    adventure in UNCHARTED franchise history led by fan-favorite character, \
    Chloe Frazer. UNCHARTED: The Lost Legacy will come with access to \
    UNCHARTED 4: A Thief's End Multiplayer and Survival modes. Online \
    multiplayer on PS4 requires a PlayStation Plus membership, sold \
    separately. Owners of UNCHARTED 4: A Thief's End Digital Deluxe Edition, \
    UNCHARTED 4: A Thief's End Triple Pack, and UNCHARTED 4: A Thief's End \
    Explorer's Pack will receive UNCHARTED: The Lost Legacy as a download at \
    launch.", category=category2)
item21 = Item(name="Samsung 850 EVO 500GB 2.5-Inch SATA III Internal \
    SSD", description="Upgrading your PC with a Samsung SSD is the most \
    economical way to breathe new life into an aging PC. The 850 EVO reads, \
    writes and multi-tasks at incredible speeds, enhancing boot-up speed, \
    application loading and multi-tasking performance. It's more than an \
    upgrade, it's a complete transformation of your PC.", category=category3)
item22 = Item(name="Raspberry Pi 3 Model B Motherboard", description="Built on \
    the latest Broadcom 2837 ARMv8 64 bit processor the Raspberry Pi 3 Model \
    B is faster and more powerful than its predecessors. It has improved \
    power management to support more powerful external USB devices and now \
    comes with built-in wireless and Bluetooth connectivity. To take full \
    advantage of the improved power management on the Raspberry Pi 3 and \
    provide support for even more powerful devices on the USB ports, a 2.5A \
    adapter is required", category=category3)
item23 = Item(name="WD Blue 1TB SATA 6 Gb/s 7200 RPM 64MB Cache 3.5 Inch \
    Desktop Hard Drive", description="Boost your PC storage with WD Blue \
    drives, the brand designed just for desktop and all-in-one PCs with a \
    variety of storage capacities.", category=category3)
item24 = Item(name="Cooler Master Hyper 212 EVO CPU Cooler with 120mm PWM \
    Fan", description="Cooler Master, an industry leading chassis, thermal \
    solution, peripheral, and accessory manufacturer, signals the rebirth of \
    a household name in computing, the Hyper 212 EVO CPU Cooler. It comes \
    packed with an improved tower fin design, heat pipe layout, and upgraded \
    fans and fan brackets that provide an even more extreme value for \
    end-users of all types. Dents are created when the heat pipes are sealed. \
    The cut and seal is not a damage, after the heatpipe is full, machine \
    will crimp it.", category=category3)
item25 = Item(name="Samsung 960 EVO Series - 250GB PCIe NVMe - M.2 Internal \
    SSD", description="Give your desktop PC or laptop a performance boost \
    with the Samsung 960 EVO NVMe M.2 SSD. Featuring Samsung V-NAND \
    technology and Dynamic Thermal Guard protection, the 960 EVO ensures the \
    integrity of your data even under heavy workloads. Its NVMe interface and \
    Polaris controller enable exceptionally fast read/write speeds. \
    TurboWrite technology adds a performance boost, making the 960 EVO ideal \
    for high-intensity tasks such as video editing, data analysis, and \
    gaming. And it comes with Samsung's Magician software, which makes it \
    easy to to manage, monitor and optimize drive \
    performance.", category=category3)
item26 = Item(name="Intel 7th Gen Intel Core Desktop Processor \
    i7-7700K", description="Socket LGA 1151 Intel 200/1001 Series Chipset \
    Compatibility (1. Excludes Intel Optane Technology support) Intel HD \
    Graphics 630 Intel Turbo Boost 2.0 Technology Intel Hyper-Threading \
    Technology", category=category3)
item27 = Item(name="EVGA GeForce GTX 1050 Ti SC GAMING, 4GB GDDR5, DX12 OSD \
    Support (PXOC) Graphics Card", description="The EVGA GeForce GTX 1050 Ti \
    hits the perfect spot for that upgrade you know you need, but at the \
    price you want! With the latest NVIDIA Pascal architecture, the 4GB GTX \
    1050 Ti displays stunning visuals and great performance at 1080p HD+. \
    Installing a EVGA GeForce GTX 1050 Ti gives you the power to take on \
    today's next-gen titles in full 1080p HD - with room to spare. These \
    cards give you a choice of memory sizes, cooling options, factory \
    overclocks, and power options to fit every need and every system. Of \
    course, no GTX card would be complete without essential gaming \
    technologies, such as NVIDIA GameStream, G-Sync, and GeForce Experience. \
    If you've been waiting for that card that gives you the performance to \
    take back the competitive edge, but without taking out your wallet, then \
    the GTX 1050 Ti is the card for you!", category=category3)
item28 = Item(name="EVGA 500 W1, 80+ WHITE 500W Power Supply", description="\
    When building on a budget, the EVGA 500W 80 PLUS is a great choice at a \
    low cost. Supporting 40A on a single +12V rail provides more options \
    without having to reduce your component requirements. Save space with the \
    500W's compact design, well-placed power switch and fully sleeved cables. \
    The 500W offers the connections and protections needed for basic system \
    builds. With a standard 3 year warranty and ultra quiet fan design the \
    500W will be a great asset for your next build on a \
    budget.", category=category3)
item29 = Item(name="AMD Ryzen 5 1600 Processor with Wraith Spire \
    Cooler", description="Frequency: 3.6 ghz precision boost 6 cores/12 \
    threads unlocked Cache: 3 mb/16 mb (l2/l3) Socket type: Am4 Thermal \
    solution: Wraith spire cooler", category=category3)
item30 = Item(name="ASUS ROG STRIX Z270E GAMING LGA1151 DDR4 DP HDMI DVI M.2 \
    ATX Motherboard with onboard AC Wifi and USB 3.1", description="\
    Experience next-level performance and personalization options with the \
    ROG STRIX Z270E GAMING, supporting 7th generation Intel Core processors. \
    Unlock full calibration and customization with 5-Way Optimization, AURA \
    Sync RGB lighting and 3D printing mounts. Dual M.2, onboard AC Wi-Fi and \
    front panel USB 3.1 deliver maximum connectivity \
    speeds.", category=category3)
item31 = Item(name="Instant Pot DUO60 6 Qt 7-in-1 Multi-Use Programmable \
    Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Saute, Yogurt Maker \
    and Warmer", description="Instant Pot is a smart Electric Pressure Cooker \
    designed by Canadians aiming to be Safe, Convenient and Dependable. It \
    speeds up cooking by 2~6 times using up to 70% less energy and, above \
    all, produces nutritious healthy food in a convenient and consistent \
    fashion. Instant Pot Duo is a 7-in-1 programmable cooker, it replaces 7 \
    kitchen appliances as it has the functions of a pressure cooker, slow \
    cooker, rice cooker, steamer, saute, yogurt maker and warmer. 14 built-in \
    smart programs (Soup, Meat/Stew, Bean/Chili, Poultry, Saute, Steam, Rice, \
    Porridge, Multigrain, Slow Cook, Keep-Warm, Yogurt, Pasteurize & Jiu \
    Niang) cook your favorite dishes with the press of a \
    button. ", category=category4)
item32 = Item(name="URPOWER 2nd Version Essential Oil Diffuser, 100ml Aroma \
    Essential Oil Cool Mist Humidifier with Adjustable Mist Mode,Waterless \
    Auto Shut-off and 7 Color LED Lights Changing for Home Office \
    Baby", description="Looking for a simple way to smell better in your \
    room? The URPOWER Ultrasonic Aroma Essential Oil Diffuser is elegant and \
    easy to use. just add 100ML of water and a few drops of your favorite \
    essential oil. Advanced ultrasonic vaporizing diffusion technology \
    quietly releases a soothing fragrant mist up to 6 hours. Automatic shut \
    off safety system when waterless protects the product from being burned \
    out. Keep essential oil 100% natural without burning or heating and \
    automatic shut off safely. The URPOWER ultrasonic aroma humidifier does \
    double duty to make your home smell better for up to 6 hours. First, the \
    humidifier function adds moisture to the air to help you sleep better, \
    cough less and alleviate dry sinuses. This handy unit also diffuses your \
    favorite scented oils without heat, so their holistic properties stay \
    intact. The result will be moist air.", category=category4)
item33 = Item(name="ThermoPro TP03A Digital Food Cooking Thermometer Instant \
    Read Meat Thermometer for Kitchen BBQ Grill Smoker", description="The \
    ThermoPro TP-03A is an effective solution to achieve the most accurate \
    temperature in a matter of seconds. The digital kitchen thermometer with \
    a simplistic yet practical design, and a push of the button, the foldaway \
    probe will pop open for quick an easy temperature reading, and when \
    you're done taking the temperature measurement you can fold the probe \
    back in to ensure the probe is kept safe and clean. Don't sweat powering \
    the food thermometer off as it's designed to conserve battery power \
    after 10 minutes of no use. Stop overcooking or under-cooking your meat \
    and perfect meat temperatures like a professional, ensuring the perfect \
    temp every time you're grilling or cooking. The meat thermometer with a \
    LCD display, reading temperatures in your preferred unit of measurement \
    between Celsius or Fahrenheit is a breeze.", category=category4)
item34 = Item(name="Brita Standard Replacement Filters for Pitchers and \
    Dispensers - BPA Free - 3 Count", description="Keep tap water healthier \
    and tasting better when you regularly change your Brita replacement \
    filter. Made to fit all Brita pitchers and dispensers, this replacement \
    filter reduces copper, mercury and cadmium impurities that can adversely \
    affect your health over time, while cutting chlorine taste and odor to \
    deliver great tasting water. Designed to leave no black flecks in your \
    water and with no pre-soak required, the Brita filters are quick and easy \
    to use. Change your Brita filters every 40 gallons or approximately 2 \
    months for best performance. Start drinking healthier, great tasting \
    water with Brita today.", category=category4)
item35 = Item(name="Royal Classic White Kitchen Towels, 15-Pack 100% Natural \
    Cotton Dish Towels, 14 x 25 inches Flour Sack Towels - Make Great Bar \
    Towels", description="Royal Classic Kitchen Towels are the same towels \
    used by the pro's in restaurants, bars, and hotels all over the world. \
    These tough little towels deliver time after time and you will have them \
    for years to come. We made our kitchen towels with the features that make \
    them an indispensable kitchen tool:", category=category4)
item36 = Item(name="LiBa Mildew Resistant Anti-Bacterial PEVA 8G Shower \
    Curtain Liner, 72x72 Clear - Non Toxic, Eco-Friendly, No Chemical Odor, \
    Rust Proof Grommets", description="The greatest danger in your bathroom \
    could be your new vinyl shower curtain. The EPA found poly vinyl chloride \
    (PVC) products are laden with 108 volatile organic compounds and \
    poisonous chemicals that emit toxic gas into the air which can persist \
    for the first 28 days. PVC plastic is softened with hormone-disrupting \
    phthalates and includes chlorine which creates dioxin, a carcinogenic \
    chemical formed during its creation and destruction. Dioxin is dangerous \
    since it easily penetrates the food chain of the planet as it can travel \
    widely without breaking down. A recent study found that in just six hours \
    after opening a PVC shower curtain, your bathroom would be exposed to \
    volatile organic compounds over 16 times the allowable levels for indoor \
    air quality established by the US Green Building Council and the \
    Washington State Indoor Air Quality Program. Bottom Line: Be wise and \
    don't put your family at risk with poly vinyl chloride (PVC) shower \
    curtains.", category=category4)
item37 = Item(name="Keurig K55 Single Serve Programmable K-Cup Pod Coffee \
    Maker, Black", description="The Classic Keurig K-Cup Single Serve Coffee \
    Maker, and a perennial best-seller, the Keurig K55 brews a rich, smooth, \
    and delicious cup every time with the quality you expect from Keurig. \
    Simple touch buttons make your brewing experience stress free, and \
    multiple K-Cup pod brew sizes help to ensure you get your perfect cup. \
    Whether you like your coffee strong, mild, decaf, or flavored, you can \
    brew all of your favorites with the Keurig K55 - and with large 48oz \
    water reservoir, you can brew 6+ cups before having to \
    refill.", category=category4)
item38 = Item(name="Dirt Devil Vacuum Cleaner Simpli-Stik Lightweight Bagless \
    Corded Stick and Handheld Vacuum ", description="The Dirt Devil Versa \
    Power is a one step solution for quick and convenient cleanups. This \
    versatile unit functions as a stick vac, hand vac, and a utility vac all \
    in one. The vacuum cleaner's lightweight design makes it simple to \
    transport from room to room, while its easy-empty dirt cup means no more \
    bags to buy. An onboard crevice tool comes included, which allows for \
    cleaning hard to reach areas like between couch cushions, along \
    baseboards, or under furniture and appliances. Great for multi-purpose \
    cleaning.", category=category4)
item39 = Item(name="Honeywell HT-900 TurboForce Air Circulator Fan, \
    Black", description="Aerodynamic TurboForce design for maximum air \
    movement. Use for intense personal cooling or energy-saving air \
    circulation. 25% quieter than similar models. Can be used on table or \
    mounted to wall for convenience. Head pivots 90 degrees with 3 speeds and \
    7 inch blade. Dimensions - Length:11.02 in, Width: 6.46 in, Height: 11.22 \
    in", category=category4)
item40 = Item(name="ECOVACS DEEBOT N79 Robotic Vacuum Cleaner with Strong \
    Suction, for Low-pile Carpet, Hard floor, Wi-Fi Connected", description="\
    With the Smart MOTION system and multiple cleaning modes, DN79 covers \
    more floor area with the right cleaning mode for the job. You can also \
    control every aspect of the clean from the palm of your hand, using the \
    ECOVACS App. With a Brushless Motor for exceptional suction power, and \
    the V-shaped main brush which ensures more lifting, DEEBOT can have a \
    thorough and deep clean on carpets.", category=category4)
item41 = Item(name="Nespresso Variety Pack for OriginalLine, 50 \
    Capsules", description="Our Nespresso Coffee Variety Pack ensures \
    everyone their ultimate coffee experience by providing delicious fine and \
    balanced coffees in an assortment of flavors. Let your senses be guided \
    by flavors like Roma (light roast South and Central America Arabicas with \
    sweet woody notes), Arpeggio (dark roast of South and Central America \
    Arabicas with cocoa notes), Capriccio (South American Arabicas for an \
    espresso with a rich aroma and strong note), Livanto (pure Arabica for a \
    well-balanced espresso with a roasted caramelized note), and Ristretto \
    (a blend of South American and East African Arabicas for a full-bodied \
    intense espresso).", category=category5)
item42 = Item(name="Quest Nutrition Chocolate Chip Cookie \
    Dough ", description="A taste so unbelievable, you'll think you're eating \
    the real thing! America's Favorite Protein Bar", category=category5)
item43 = Item(name="Viva Naturals Organic Extra Virgin Coconut \
    Oil", description="Viva Naturals Organic Coconut Oil gives you an easy, \
    wonderful way to add flavor to your diet, and boost your skin and hair \
    regime with the power of MCTs, immune boosters, and compounds found in \
    coconuts.", category=category5)
item44 = Item(name="Rice Krispies Treats Bars", description="Rice Krispies \
    Treats, The Original are crisp rice cereal and marshmallow \
    square.", category=category5)
item45 = Item(name="Essentia 9.5pH Water", description="Essentia Water\
    provides unmatched hydration, health benefits and smooth taste. Its \
    superior hydrating qualities come from a special electrolyte formula and \
    optimal pH level of 9.5, which gives your body more of what it needs to \
    thrive. Drinking Essentia Water boosts the antioxidant properties of \
    your immune system and helps bring your body back into balance. It also \
    helps maintain normal blood pressure, restful sleep, heart health, \
    muscle strength and more.", category=category5)
item46 = Item(name="Sunshine Cheez It Baked Snack Crackers", description="\
    Sunshine cheez-it baked cheese crackers. Delicious baked bite size \
    cheese crackers.", category=category5)
item47 = Item(name="Ritz Cracker Sandwiches, Peanut Butter", description="\
    Delicious Ritz Sandwich Crackers are the classic go-anywhere snack that \
    kids and adults have loved for years. Each sandwiches real, creamy \
    peanut butter between two buttery Ritz crackers. Ritz Sandwich Crackers \
    are the perfect compliment for lunchboxes or quick meals. Each \
    individually wrapped pack is sealed for freshness and includes six Ritz \
    Sandwich Crackers.", category=category5)
item48 = Item(name="Soylent Meal Replacement Drink, Cacao", description="We \
    fuel our bodies every day, but often it feels like hard work. That \
    seemed wrong, so we made a meal that takes no work at all. Soylent \
    Drink eliminates the stress and effort of finding a quick, complete, \
    and low-cost meal. Let Soylent Drink take care of your hunger, so you \
    can worry about the important stuff.", category=category5)
item49 = Item(name="Cheerios Gluten Free Breakfast Cereal", description="First \
    Ingredient Whole Grain A whole grain food is made by using all three \
    parts of the grain. All General Mills Big G Cereals contain more whole \
    grain than any other single ingredient. 23g whole grain per serving. At \
    least 48g recommended daily.", category=category5)
item50 = Item(name="Nutella Hazelnut Spread", description="The original \
    creamy chocolaty hazelnut spread. Made with over 50 hazelnuts per jar. \
    Contains no artificial colors. Contains no artificial preservatives. \
    Spreadably delicious on whole wheat, multigrain and bakery breads, \
    bagels, English muffins, waffles.", category=category5)
item51 = Item(name="Aztec Secret Indian Healing Clay Deep Pore \
    Cleansing", description="How Aztec secret works Indian healing clay clays \
    have been used for centuries to beautify and refresh when used as a \
    facial mask. Cleopatra used clay from the Nile River and the Arabian \
    Desert over 1800 years ago, as part of her beauty ritual. German and \
    roman spas have been using clay packs and treatments in the spas they \
    built 4,000 years ago.", category=category6)
item52 = Item(name="Philips Norelco Multigroom All-In-One Series 3000, 13 \
    attachment trimmer", description="The Philips Norelco Multigroom 3000 is \
    a all-in-one trimmer with everything you need, and nothing you don't. \
    Our toughest multipurpose trimmer boasts tempered steel cutting blades \
    that self-sharpen and won't rust. The trimmer includes 13 pieces to trim \
    your face and head, including a full-size steel trimmer, steel detailer, \
    nose and ear trimmer, 3 hair cutting guards, 3 beard trimming guards, 1 \
    stubble trimming guard, and a storage bag. The durable trimmer includes \
    impact-resistant cutting guards, a steel reinforced motor, and a \
    powerful lithium battery delivering 60 minutes of run time. The blades \
    and guards can be rinsed clean, and the device comes with a 45 day \
    risk-free trial and a full 2-year warranty. ", category=category6)
item53 = Item(name="Active Wow Teeth Whitening Charcoal Powder \
    Natural", description="Active wow - activated coconut charcoal powder - \
    natural teeth whitening is the best way to whiten your teeth naturally. \
    Derived from the highest-quality coconut sources, our activated charcoal \
    is safe to use on your teeth and easy on your gums. Naturally whiten \
    your teeth - if you're not a fan of dental-grade whitening peroxides, \
    active wow charcoal teeth whitening is a great alternative. This formula \
    whitens your teeth over time, and helps remove stains from a number of \
    causes: coffee-stains, wine, cigarettes, and more - all without \
    bleach.", category=category6)
item54 = Item(name="Gillette Fusion Manual Men's Razor Blade \
    Refills", description=" Designed to bring you optimal performance from \
    either side of its unique cartridge, the Gillette Fusion redefines your \
    expectations of what a shave can be. On the front of this razor blade, \
    Gillette Fusion features five blades spaced closer together to achieve \
    its advanced 5-Blade Shaving Technology surface. This design distributes \
    the shaving force across the blades to help reduce pressure, with more \
    comfort and less irritation than MACH3.", category=category6)
item55 = Item(name="Cosrx Acne Pimple Master Patch", description="Acne Pimple \
    Master Patch heals acne, blemishes and prevents future breakouts \
    quickly. Hydrocolloid patch prevent secondary infections and absorbs \
    exudate to encourage wound repair process more faster. Hypo allergenic \
    dressing that sensitive skin type also can use Various Sizes included. \
    (7mm x 10EA, 10mm x 5EA, 12mm x 9EA)", category=category6)
item56 = Item(name="Baebody Eye Gel for Dark Circles, Puffiness, Wrinkles and \
    Bags. - The Most Effective Anti-Aging Eye Gel for Under and Around \
    Eyes", description="Everyone wants to look their best. You want to turn \
    back time and achieve the youthful skin you see in old photos. Luckily \
    for you, we have a solution. Baebody is a beauty and lifestyle brand \
    with a desire to promote a natural, healthy and beautiful lifestyle. We \
    want you to look and feel fabulous!", category=category6)
item57 = Item(name="Thayers Alcohol-Free Rose Petal Witch Hazel with Aloe \
    Vera", description="Thayers Rose Petal Alcohol-Free Witch Hazel with \
    Aloe Vera Formula Toner will make your skin bloom. Rose Thayer's \
    remarkably soothing Toner is made with rose-petal water, Vitamin E and \
    our proprietary Witch Hazel extract. Ingredients: Purified Water, Aloe \
    Barbadensis Leaf Juice (Certified Organic Filet Of Aloe Vera), Glycerin \
    (Vegetable), Fragrance (Natural Rose), Hamamelis Virginiana Extract \
    (made from Certified Organic Witch Hazel), Rosa Centifolia (Rose) Flower \
    Water, Citric Acid, Citrus Grandis (Grapefruit) Seed Extract. Bullets \
    change to: Alcohol free, paraben-free, naturally preserved, \
    hypoallergenic. Made with organic witch hazel and aloe vera. Natural rose \
    fragrance. Cleanses, soothes and tones skin.", category=category6)
item58 = Item(name="Men's Rogaine Hair Loss & Hair Thinning Treatment \
    Minoxidil Foam", description="For men suffering from hereditary hair \
    loss, Men's Rogaine Foam can help regrow hair. With 5% minoxidil, this \
    is the first FDA-approved hair-regrowth treatment foam. It has been \
    clinically proven to help hair regrowth in men who used it every day for \
    four months*. Easy to use and unscented, Men's Rogaine foam absorbs \
    quickly into the scalp, dries quickly, and has a texture that lets you \
    feel exactly where you are applying it.", category=category6)
item59 = Item(name="CeraVe Moisturizing Cream 16 oz Daily Face and Body \
    Moisturizer for Dry Skin", description="CeraVe Moisturizing Cream \
    increases the skin's ability to attract, hold and distribute moisture. \
    It penetrates deeply into the layers of the stratum corneum (the skin \
    barrier) to restore the balance of lipids that are essential for an \
    effective skin barrier. CeraVe Moisturizing Cream also forms a protective \
    layer over the skin's surface to help prevent moisture \
    loss.", category=category6)
item60 = Item(name="Neutrogena Makeup Remover Cleansing Towelettes & Wipes, \
    Refill Pack", description="#1 choice of make-up artists. Remove makeup in \
    one easy step with Neutrogena Makeup Remover Cleansing Towelettes \
    Refill Pack. Formulated to be gentle and safe around the sensitive eye \
    area and for contact lens wearers, these soft and gentle pre-moistened \
    towelettes effectively dissolve all traces of dirt, oil and makeup--even \
    waterproof mascara--for clean, fresh skin every day. The towelettes help \
    leave skin thoroughly clean and without heavy residue, so there's no need \
    to rinse. This travel pack comes with a total of 25 cleansing \
    sheets.", category=category6)
item61 = Item(name="VTech Sit-to-Stand Learning Walker", description="From \
    baby steps to big steps the Sit-to-Stand Learning Walker by VTech helps \
    your child develop from a crawler to a walker through adaptive \
    technology.", category=category7)
item62 = Item(name="Nuby Octopus Hoopla Bathtime Fun Toys, \
    Purple", description="Nuby's BPA Free Octopus Floating Bath Toy is a fun \
    and interactive toy to make bath time more enjoyable. The cute and \
    engaging toy comes with one floating octopus and three rings to toss on \
    the octopus' tentacles. It helps to develop hand-eye coordination and \
    stimulate your baby's senses. This toy provides endless fun in the bath \
    or pool!", category=category7)
item63 = Item(name="Nuby IcyBite Keys Teether", description="The IcyBite Keys \
    by Nuby is another innovation in the natural teething process as well as \
    a toy which combines exercise for young hands, gums and teeth. This Nuby \
    teether also features areas filled with purICE. The cool resilient \
    surface soothes and stimulates sore gums safely and stays colder, longer \
    than water filled teethers! The colorful key shapes with raised, offset \
    surfaces assist in the eruption of teeth by gently massaging infant's \
    gums. The colorful shapes are also easy for baby to hold and sized for \
    maximum effectiveness as a teether and soother.", category=category7)
item64 = Item(name="Baby Einstein Take Along Tunes Musical Toy", description="\
    Baby Einstein Take Along Tunes", category=category7)
item65 = Item(name="VTech Drop and Go Dump Truck", description="Learning is \
    tons of fun with the Drop and Go Dump Truck by VTech. Drop a colorful \
    rock into the top of this cute toy dump truck, and watch it tumble into \
    the bucket. Your little one will learn numbers as the interactive truck \
    counts each rock. Once the rocks are in the bucket, push or pull the \
    truck along to see the rocks rumble inside. Then, lift the hinged bucket \
    to unload the rocks and start again while developing motor skills. \
    The dump truck also includes 3 colorful buttons that play melodies, \
    phrases and teach tools and colors. Requires 2 AAA batteries (batteries \
    included for demo purposes only; new batteries recommended for regular \
    use). Intended for ages 6 months to 3 years.", category=category7)
item66 = Item(name="Baby Banana Infant Training Toothbrush and Teether, \
    Yellow", description="100% Food Grade silicone teething toothbrush for \
    kids 3-12 months of age. Specifically designed with \"a-peel-ing\" \
    handles that are easy for baby to hold, while preventing choking. \
    Bendable soft silicone reduces risk of injury, providing the safest \
    learning experience possible. Dishwasher and Freezer \
    Friendly.", category=category7)
item67 = Item(name="Playskool Friends Sesame Street Tickle Me \
    Elmo", description="HA! HA! Hee! Hee! Elmo's hysterical laugh is back! \
    The magic of Tickle Me Elmo returns--redesigned for a whole new \
    generation of fans! Little ones can start the hilarious fun when they \
    press his tummy or squeeze his feet. First they'll hear Elmo's contagious \
    giggle. When they continue to squeeze and \"tickle\" Elmo, he laughs \
    harder and harder until he starts to move and shake! Children can't help \
    but giggle along when they hear his funny sayings and hysterical laughing \
    sounds. Tickle Me Elmo is as silly, cuddly, and lovable as ever! He's \
    funny! He's furry! You can't put this giggle monster down! 2 AA demo \
    batteries included. Sesame Street and associated characters, trademarks \
    and design elements are owned and licensed by Sesame Workshop. Hasbro and \
    all related terms are trademarks of Hasbro.", category=category7)
item68 = Item(name="Mega Bloks 80-Piece Big Building Bag, \
    Classic", description="Build and stack for limitless fun with the \
    award-winning Big Building Bag by Mega Bloks. These bright \
    primary-colored blocks encourage hands-on exploration as children imagine \
    and create. Building blocks are big and easy for little fingers to \
    assemble. When playtime is over, zip the blocks up in an \
    environmental-friendly bag and stash them in the toy box until the next \
    adventure. Ideal for ages one and up!", category=category7)
item69 = Item(name="VTech Musical Rhymes Book", description="Explore classic \
    nursery rhymes with the musical rhymes book by VTech. Your little one \
    will build motor skills by sliding and twisting the fun play pieces while \
    exploring each easy-to-turn page. Then they'll play piano sounds with the \
    five colorful piano keys that introduce colors and instruments. Two fun \
    modes include learning mode that introduces age-appropriate vocabulary \
    and music mode that plays music and instrument sounds. The interactive \
    storybook provides visual stimulation with brightly colored pages and a \
    light-up Star that flashes along with the sounds.", category=category7)
item70 = Item(name="Sassy Developmental Bumpy Ball", description="The bright \
    colors, bold patterns and easy-to-grasp bumps make the Sassy Bumpy Ball a \
    must-have. The high contrast colors of the ball allow baby to focus, \
    strengthening vision. The gentle rattle sounds from the trapped beads \
    create neural connections in baby's brains from birth through 3 years of \
    age. Chunky sized bumps on the ball encourage reaching, grasping, and \
    transferring from one hand to another, developing baby's motor skill. \
    The differing materials engage baby's developing tactile sensitivity and \
    teach baby about variety.", category=category7)
item71 = Item(name="DEARCASE Women's Long Sleeve Casual Loose T-Shirt \
    Dress", description="Fabric:Rayon,some review says size run bigger, \
    suggest choose 1 size down if you do not wish loose fit. Features: casual \
    style,asymmetrical hem lines,short length,V-Neck,Not lined Color: Army \
    Green,Wine red,Coffee,Light Blue,Blue,Beige,Black,Purple,Navy Blue,Grey,\
    Dark Green,Brown,Red;US Standard Size S/M/L/XL Stretch,fitted,\
    Irregular Dress,Occasion:Casual/Beach/Party Super soft, stretchy and \
    lightweight,Can be easily dress up or dress down", category=category8)
item72 = Item(name="LILBETTER Women's Casual Plain Simple T-shirt Loose \
    Dress", description="Lightweight, soft and stretchy ,Can be easily dress \
    up or dress down Main material:cotton Unique style,make you beautiful,\
    fashionable,sexy and elegant. ", category=category8)
item73 = Item(name="Levi's Men's 505 Regular Fit Jean", description="100% \
    Cotton Imported Zipper closure Machine Wash Regular-fit jean featuring \
    five-pocket styling and signature logo label at back \
    waist", category=category8)
item74 = Item(name="Leggings Depot Ultra Soft Basic Solid REGULAR and PLUS 42 \
    COLORS", description="Stretch Fabric + Full Length Leggings: A figure \
    flattering & ultra comfortable fit!! Solid Color Design: Will match with \
    nearly anything! Great for layering under dresses and tops! Wear casually \
    or as yoga pants! Comfort and movability!", category=category8)
item75 = Item(name="Levaca Womens Long Sleeve Button Cowl Neck Casual Slim \
    Tunic Tops With Pockets", description="Levaca's clothes are fresh, please \
    give yourself a chance to be a topic woman. Levaca Womens Long Sleeve \
    Button Cowl Neck Casual Slim Tunic Tops With Pockets, in any single wear, \
    or as a basic shirts,Have a good show in all seasons. Levaca thinks, \
    choosing the right size of clothes, you put on will be more \
    beautiful.", category=category8)
item76 = Item(name="Champion Men's Closed Bottom Light Weight Jersey \
    Sweatpant", description="The Champion Closed Bottom Jersey Pant is Jersey \
    at its best - the ultimate in comfort and durability", category=category8)
item77 = Item(name="Carhartt Men's Acrylic Watch Hat A18", description="A \
    classic. You'll reach for it every time the wind gets blustery and the \
    temperatures drop. Not only warm, but comfortable, too. Our acrylic watch \
    hat is made of stretchable, 100% acrylic rib-knit fabric for warmth and \
    comfort. The Carhartt logo is sewn on the front of this classic, \
    one-size-fits-all hat.", category=category8)
item78 = Item(name="Trendy Warm Chunky Soft Stretch Cable Knit Beanie \
    Skully", description="Head measurement: 57 cm, 22-3/8\", Size 7-1/8 100% \
    soft acrylic One size fits most Great for any outdoor activities,skiing, \
    snowboarding, camping Imported", category=category8)
item79 = Item(name="Levi's Men's 501 Original-Fit Jean", description="Since \
    we invented it in 1873, the 501 Jean has been a blank canvas for \
    self-expression. The iconic straight fit with signature button fly, the \
    501 Jean sits at the waist and is regular through the thigh with a \
    straight leg. Message from the Manufacturer: You asked. We listened. \
    Based on customer feedback, we've remastered our 501 Jean. The \
    construction of the front fly was modified in 2013 to help prevent \
    tearing in this area.", category=category8)
item80 = Item(name="90 Degree by Reflex Womens Power Flex Yoga \
    Pants", description="The Power Flex yoga pant from 90 Degree by Reflex is \
    the ideal combination of fashion, function, and performance. Our fabric \
    is designed to contour perfectly to your body, giving you a streamlined \
    look. We've created the perfect fabric at the perfect price. The Power \
    Flex pant is created from a blend of Nylon and Spandex and is designed \
    to remove moisture from your body, providing maximum comfort. A wide \
    waistband contours your curves and streamlines your natural \
    shape.", category=category8)
item81 = Item(name="Lineon 100 Pack Gel Pens Set, 50 Colors Gel Pens with 50 \
    Refills Gel Pen Set for Adult Coloring Books Drawing Doodling Art \
    Markers", description="Lineon's gel pen team members are coloring fans \
    too. So we know the key points for coloring: ink and tip. We select top \
    quality ink, long lasting and super smooth tip as well as the most \
    suitable tip size for customers.  ", category=category9)
item82 = Item(name="The Candlemaker's Store Natural Soy Wax", description="\
    Natural Soy 444 Wax: 10 pound bag - Flakes, priced per bag. This is a \
    good container blend with a 121-125 melt point that is blended with 2% of \
    our Universal Soy Wax Additive. This wax can hold up to 15% Fragrance and \
    has an incredible hot throw. You can also blend this with the 416 Soy wax \
    to create beautiful tarts.", category=category9)
item83 = Item(name="Tombow Fudenosuke Brush Pen 2 Pens Set", description="\
    Contains both the soft and hard tip Fudenosuke Brush Pens. Features a \
    flexible brush tip for different lettering and drawing techniques. Create \
    extra-fine, fine or medium strokes by a change in brush pressure. Great \
    for calligraphy and art drawings. Barrels are made of recycled \
    polypropylene plastic.  Soft tip and hard tip- water-based, pigmented \
    black ink. Odorless. Non-refillable.", category=category9)
item84 = Item(name="Cricut 2001974 Adhesive Cutting Mat, Standard Grip, 12 x \
    12-Inch", description="Cricut cutting mats have been customized to match \
    commonly used crafting materials. Each has just the right level of grip \
    to not only hold your material firmly in place during cutting, but to \
    also allow you to easily remove the material from the adhesive surface. \
    The StandardGrip mat is a multi-purpose mat that is perfect for a wide \
    range of medium-weight materials, including patterned paper, vinyl, \
    iron-on and cardstock. Two mats are included in each package. Using both \
    mats allows you to cut one image while working on \
    another.", category=category9)
item85 = Item(name="Huhuhero Fineliner Color Pen Set, 0.38 mm Fine Line \
    Drawing Pen, Porous Fine Point Markers Perfect for Coloring Book and \
    Bullet Journal Art Projects", description="The Huhuhero 0.38mm fineliner \
    markers are specially designed for artists, designers, students.. and \
    even for kids! They have a confortable shape to prevent hand pain. The \
    fine tip let you draw precise, detailed lines and outline bullet \
    journal... and if you're coloring it will let you reach small and \
    difficult areas.", category=category9)
item86 = Item(name="Heartybay 10Pieces Round Pointed Tip Nylon Hair Brush \
    Set, Blue", description="Seamless nickel ferrules won't rust or split. \
    They are double-crimped to last longer and won't come loose after a few \
    uses. Brushes don't shed hairs. No more frustration trying to get brush \
    hairs off your artwork. Easier to clean and won't deteriorate as quickly. \
    Short wooden handles with a smooth finish, perfect for greater control \
    over small details.", category=category9)
item87 = Item(name="Strathmore Series 400 Sketch Pads 9 in. x 12 in.\
    ", description="A general purpose, medium weight sketch paper intended \
    for technique practices or quick studies with any dry media. This package \
    contains one 12 by 9-inch side spiral-bound sketch book with 100 sheets \
    of 60-pound acid free, lightly textured paper. Made in \
    usa.", category=category9)
item88 = Item(name="Foam Balls for Slime - Colorful Styrofoam Balls Beads \
    Mini 0.1-0.18 inch ", description="More foam beads for slime = more \
    crunchy slime blobs = more fun! A colorful slime gets poked, prodded, \
    maybe even cut, and then reformed and squashed back together \
    again.", category=category9)
item89 = Item(name="Apple Barrel Acrylic Paint Set, 18 Piece", description="\
    Quality selection and value. Formulated for use on all surfaces \
    including wood, styrofoam, plaster, terra cotta and tin. These matte \
    colors glide on smoothly, dry quickly and stay beautiful as the day they \
    were painted. Can be brushed, stamped, stenciled or sponged on. Easy \
    cleanup with soap and water.", category=category9)
item90 = Item(name="EricX Light 100 Piece Natural Candle Wick, Low Smoke 6\" \
    Pre-Waxed & 100% Natural Cotton Core,For Candle Making", description="\
    Pre-waxed and Tabbed Wick Lenght:6 inch.Base Dia:12.5mm 100% natural \
    cotton, contains no lead, zinc or other metals Low Smoke,perfect for \
    candle making NOTICE:Please be cautious with dosage of dye and scent \
    whilst making candles,excessive dosage might influence burning \
    effectiveness and reduce the candles ability to stay \
    lit.", category=category9)
item91 = Item(name="Arctix Infant/Toddler Chest High Insulated Snow Bib \
    Overalls", description="ThermaLock 100% nylon shell fabric provides \
    water and wind resistance while maintaining breathability. ThermaTech \
    insulation provides advanced lightweight warmth while allowing maximum \
    comfort and mobility. Adjustable comfort suspenders. Elasticized side \
    gussets for maximum motion and comfortable fit. Reinforced Cordura 3/4 \
    inch hem and scuff guard for durable wear.", category=category10)
item92 = Item(name="Etekcity 2 Pack Portable LED Camping Lantern Flashlights \
    with 6 AA Batteries - Survival Kit for Emergency, Hurricane, \
    Outage", description="No matter where you may be, the Etekcity \
    collapsible lantern was created with the means for safer visibility and \
    easier operation. Easy to change its batteries, the lantern needs no \
    setup or prepping with fires or oils.", category=category10)
item93 = Item(name="Arctix Youth Snow Pants with Reinforced Knees and \
    Seat", description="The reinforced version of our classic pant is \
    designed for the kid who punishes their gear. Whether on the slopes of \
    in the backyard, the reinforced knees and seat are ready to withstand \
    high demand. The water and wind resistant product will keep the kids \
    warm and dry, DWR finish (Durable Water Repellent) helps repel water \
    from fabric surface. The Arctix youth reinforced snow pants are made \
    with dobby w/R + w/P 3000mm with coating which offers a maximum degree \
    of durability.", category=category10)
item94 = Item(name="Fit Simplify Resistance Loop Exercise Bands with \
    Instruction Guide", description="High end exercise bands. Our 12in by 2in \
    heavy duty resistance loop bands are made of 100% natural latex - free \
    of non-natural Thermoplastic Elastomer (TPE) - and come in 5 varying \
    resistance levels. This makes them perfect whether you are just \
    starting to workout or a seasoned workout warrior. Our extra light and \
    light bands are great for beginners, while our medium, heavy and extra \
    heavy exercise bands are targeted for more intermediate and advanced \
    strength training.", category=category10)
item95 = Item(name="Legendary Whitetails Men's Buck Camp Flannel \
    Shirt", description="A hunter's wardrobe is not complete without a \
    great flannel. Our exclusive plaids are made from heavyweight 100% \
    cotton soft brushed flannel. Featuring double pleat back for ease of \
    movement and contrasting corduroy lined collar and cuffs for a great \
    look and lasting durability. Left chest pocket with pencil slot and \
    button closure, and adjustable cuffs.", category=category10)
item96 = Item(name="Coleman White Water Sleeping Bag, 6-Feet \
    4-inches", description="Sleep comfortably, even when it's 30 F outside \
    in the Coleman White Water Sleeping Bag with a brushed polyester cover \
    and cozy cotton flannel liner. It fits heights up to 6 ft. 4 in. and is \
    designed to keep you cozy. The contoured head with Comfort Cuff \
    stitching surrounds your head in softness. The specially-designed, \
    patented zipper system plows the fabric away from the zipper to avoid \
    snags and zips up all the way every time. The Thermolock System reduces \
    heat loss through the zipper. When you're ready to pack up, the Roll \
    Control loop fasteners help you perfectly fold the sleeping bag and \
    the Quick Cord System makes rolling it up and fastening it a cinch \
    without tying. The sleeping bag is machine washable for easy cleaning \
    at home.", category=category10)
item97 = Item(name="Compression Socks for Men and Women Graduated Athletic \
    Sport Socks for Running, Biking, Hockey, Baseball, Flight Travel, Nurse, \
    Maternity Pregnancy- (S-XL)", description="HOFAM Compression Socks \
    maximize muscle oxygenation and boost energy with unparalleled, \
    scientifically optimized, compression technology for all-day benefits.\
    Better Circulation, Strong Muscles, Healthy Joints.", category=category10)
item98 = Item(name="Compression Socks for Men & Women, BEST Graduated \
    Athletic Fit for Running, Nurses, Shin Splints, Flight Travel, & \
    Maternity Pregnancy. Boost Stamina, Circulation, & \
    Recovery", description="Unlike normal athletic socks, Physix Gear \
    Stamina Socks are designed with gradient compression, The perfect \
    performance gear designed for any activity where your legs are pushed \
    to the limit. Physix Gear Stamina Socks are engineered with the latest \
    arch to calf compression technology, offering a targeted foot to calf \
    muscle support unseen on lesser quality socks.The results are a boost \
    in circulation, delivering an enhanced oxygen blood flow keeping you \
    going harder, for longer, and recovering faster.", category=category10)
item99 = Item(name="LifeStraw Personal Water Filter for Hiking, Camping, \
    Travel, and Emergency Preparedness", description="A Time Magazine \
    Invention of the Year winner, the LifeStraw Personal Water Filter \
    contains no chemicals, no batteries and no moving parts to wear out. \
    It features a high flow rate and weighs only 2oz. The ultimate survival \
    tool for hiking, camping, ultralight backpacking, hunting, travel, \
    scouting, and emergency preparedness, its straw design is ideal for \
    purifying water from streams, lakes, ponds and other contaminated \
    sources. No disaster kit or bugout bag is complete without a LifeStraw, \
    an essential component of any prepper gear lineup.", category=category10)
item100 = Item(name="Lirisy Inside The Waistband Holster | Gun Concealed \
    Carry IWB Holster | Fits S&W M&P Shield / GLOCK 26 27 29 30 33 42 43 / \
    Springfield XD XDS / Ruger LC9 & All Similar Handguns", description="The \
    Lirisy IWB Holster is comfortable enough for every day carry of your \
    weapon. It is designed to be worn inside the waistband for concealed \
    carry. We make our holsters with the end user in mind. We have put much \
    attention to our materials, design and process to bring you a top of the \
    line holster at a better price. ", category=category10)
item101 = Item(name="Royal Reusable Microfiber Cleaning Cloth Set - 12 x 16 \
    Inch Microfiber Cloth", description="Royal Microfiber Cleaning Cloths are \
    a highly effective tool for all your cleaning tasks. From your garage or \
    shop to your home, these tough, durable cleaning cloths will not \
    disappoint. At 12 x 16 they are perfectly sized for a wide range of \
    cleaning jobs such as cleaning cars, trucks, boats, and RV's as well as \
    TV's, counter tops, bathroom floors, and more. The soft material is super \
    absorbent and grabs dirt and grime without streaking or leaving lint \
    behind. The non-abrasive material won't scratch your cars, paint jobs, \
    or other surfaces and it doesn't even need cleaning products to \
    clean.", category=category11)
item102 = Item(name="Car Vacuum Cleaner High Power 12V 120W Strong Suction Dust \
    Buster Handheld Vac", description="With this vacuum cleaner, you can \
    thoroughly clean any places in your car with the 14.6ft super long power \
    cord and 4 different specific attachments. It can get rid of all annoying \
    rubbish in your car including liquid, debris, pet hair even they fall \
    into hard-to-reach area", category=category11)
item103 = Item(name="Hopkins 532 Mallory 26\" Snow Brush with Foam \
    Grip ", description="Mallory USA, by Hopkins Manufacturing, is the \
    leading brand of snow and ice tools in Canada and North America. \
    Mallory is recognized for quality, durability and lightweight solutions. \
    Mallory's 26\" Snow Tool Brush is comfortable and easy to use with its \
    curved handle, comfort foam grip, and unbreakable scraper blade. Thick \
    bristles make brushing snow and ice quick and painless. A must have for \
    any vehicle.", category=category11)
item104 = Item(name="Ergodyne N-Ferno 6823 Wind-Resistant Hinged Balaclava, \
    Black", description="High quality thermal outdoor sports mask to provide \
    the best protection and warmth in cold winter climates. Perfect addition \
    to any winter gear kit for skiing, snowmobiling, hunting, motorcycling, \
    snowboarding, hiking, cross country skiing, or just shoveling the \
    driveway!", category=category11)
item105 = Item(name="Bosch ICON 22A Wiper Blade", description="The \
    award-winning design of Bosch ICON distributes more uniform pressure \
    along the entire length of the blade for ultimate all-season performance \
    that lasts up to 40% longer than other premium wiper blades. Bosch ICON \
    is the perfect choice for your wiper blade replacement \
    needs.", category=category11)
item106 = Item(name="Battery Tender 021-0123 Battery Tender Junior 12V, 0.75A \
    Battery Charger", description="Battery Tender Junior 12V Battery Charger \
    is much more than a trickle charger. It has a brain, is lightweight, \
    compact, fully automatic and very easy to use especially in small spaces. \
    This battery charger will keep the battery fully charged so that it is \
    ready to go always. It has a microprocessor controlled fully automatic \
    charger and maintainer and is designed to extend the life of any lead \
    acid battery commonly used in automobiles, motorcycles, ATVs, personal \
    watercraft, RVs, boats, airplanes, golf carts, back-up generator \
    systems, etc.", category=category11)
item107 = Item(name="Moso Natural Air Purifying Bag. Odor Eliminator for Cars, \
    Closets, Bathrooms and Pet Areas. Captures and Eliminates Odors. Charcoal \
    Color", description="The 200 gram Moso Bag is an easy and convenient way \
    to maintain a fresh, dry and odorless environment. Made of just one \
    incredibly powerful natural ingredient, moso bamboo charcoal, the Moso \
    Bag is continuously working to effectively absorb and remove odors, \
    allergens and harmful pollutants and to clean and freshen the air. The \
    bamboo charcoal neutralizes even stubborn smells, such as those caused \
    by smoke, pet urine, cat litterboxes, wet dogs, gym shoes and more. The \
    Moso Bag is also excellent for use in  damp, musty environments, where it \
    will absorb excess moisture to prevent mold, mildew and bacteria from \
    forming. ", category=category11)
item108 = Item(name="Car Trunk Storage Organizer with Straps and Cargo Net \
    Cover, Original Gray", description="The Beloved Car Trunk Organizer is \
    now available complete with industry exclusive fitted cargo net, lock \
    down harnesses, large pockets, and sturdy frame inserts all from the \
    trusted name - DRIVE Auto Products. (New great Cargo Net Cover option is \
    great for the ATV market)", category=category11)
item109 = Item(name="Leather Honey Leather Conditioner, Best Leather \
    Conditioner Since 1968. For Use on Leather Apparel, Furniture, Auto \
    Interiors, Shoes, Bags and Accessories.", description="HISTORY Leather \
    Honey is the best leather conditioner, made in the USA and hand-bottled \
    by the same family for nearly 50 years. The original leather conditioner \
    formula, developed in 1968, is still used today. Our time-tested brand \
    has millions of satisfied customers. BETTER THAN THE REST Leather Honey \
    rejuvenates and conditions old leather, protects and softens new leather. \
    Our leather conditioner formula is non-toxic and water, snow and rain \
    repellent. Leather Honey is proven to penetrate deep into the leather's \
    pores, increasing flexibility and durability. PRODUCT USES Leather Honey \
    prolongs the life of boots, leather furniture, saddles and tack, gloves, \
    baseball mitts, apparel, upholstery and automobile and motorcycle seats \
    and accessories.", category=category11)
item110 = Item(name="Mobil 1 120764 Synthetic Motor Oil 5W-30", description="\
    Mobil 1 5W-30 is an advanced full synthetic motor oil designed to keep \
    your engine running like new by providing exceptional wear protection, \
    cleaning power and overall performance. It meets the demanding ILSAC GF-5 \
    performance standards, and is dexos1 approved by General Motors. Mobil 1 \
    5W-30 meets or exceeds the requirements of the industry's toughest \
    standards and outperforms our conventional motor oils. Mobil 1 technology \
    comes as standard equipment in many different vehicles, including select \
    high-performance vehicles.", category=category11)

items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,
         item11, item12, item13, item14, item15, item16, item17, item18,
         item19, item20, item21, item22, item23, item24, item25, item26,
         item27, item28, item29, item30, item31, item32, item33, item34,
         item35, item36, item37, item38, item39, item40, item41, item42,
         item43, item44, item45, item46, item47, item48, item49, item50,
         item51, item52, item53, item54, item55, item56, item57, item58,
         item59, item60, item61, item62, item63, item64, item65, item66,
         item67, item68, item69, item70, item71, item72, item73, item74,
         item75, item76, item77, item78, item79, item80, item81, item82,
         item83, item84, item85, item86, item87, item88, item89, item90,
         item91, item92, item93, item94, item95, item96, item97, item98,
         item99, item100, item101, item102, item103, item104, item105, item106,
         item107, item108, item109, item110]

# Randomize items order and add them to database
randomized_items_order = random.shuffle(items)

for item in items:
    if session.query(Item).filter_by(name=item.name).first() is not None:
        print("Item already existing. Skipping...")
    else:
        session.add(item)
        session.commit()

print "Catalog items added!"
