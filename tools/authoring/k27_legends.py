#!/usr/bin/env python3
"""K27 – Kreaturenkatalog: Ursprungsstimmen (#241–#250) und Mythische (#251–#256).

Namen, Typen, Gestalt und Schlafort sind seit K07 §5–§6 (CANON §34) gesperrt; hier werden
die vollständigen Artdaten ergänzt. Legendäre/Mythische entwickeln sich nicht, wachsen „Late“
und erscheinen nie wild (Spawn.None) – Zugang ausschließlich über Begegnungen (K44–K46, K62).
"""
from catalog_lib import Catalog


def legend(c, genus, region, **e):
    c.region = region
    e.setdefault("zones", [])
    e.setdefault("conds", ["Spawn.None"])
    e.setdefault("growth", "Late")
    e.setdefault("exp", 320)
    c.line_of(e.pop("kind"), genus, [e])


c = Catalog(start_kodex=241, start_line=108, region="R01")
L = dict(kind="Legendary", rarity="Legendary")
M = dict(kind="Mythical", rarity="Mythical")

legend(c, "Archisonus", "R01", **L, name="Sylv'anor", epithet="radix", cat="Blütenstimmen-Echo",
       arch="A03", size="XL", h=4.2, types=("Bloom", "Sound"), habitat="Wurzelhalle unter der Arena von Eichenhall",
       act="Diurnal", traits=["Singer", "Guardian", "Pollinator"], niches=["Combat", "Research"], role="Support",
       polish="HP:3", stats=("Support", 660), bond=3, lure="ITM_LURE_BELLCHIME",
       sig="Wurzellied: Feldklang – jede Runde heilen alle Verbündeten und Blüte-Fähigkeiten kosten weniger",
       mark="Ein Geweih aus singenden Ästen, an denen Glockenblüten im Takt des Weltlieds läuten",
       lore=["Die Grundstimme des Wachstums; aus ihrem ersten Ton entsprangen die Wälder Verdanthains.",
             "Schläft unter Eichenhall; ihre Wurzeln durchziehen den Boden der ganzen Region und tragen ihr Atmen.",
             "Die Druiden des Waldes sagen, jeder Baum singe einen Ton aus Sylv'anors Lied.",
             "Die Wildwacht hütet die Wurzelhalle seit ihrer Gründung, ohne zu wissen, wen sie bewacht.",
             "Erwacht nach dem Akkord von Eichenhall und der Hauptquest Verdanthains. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R02", **L, name="Orh'gruun", epithet="mons", cat="Steinstimmen-Echo",
       arch="A11", size="XXL", h=9.0, types=("Stone", "Gravity"), habitat="Schlund unter Kharsholm",
       act="Diurnal", traits=["Guardian", "Sleepy", "Lithophage"], niches=["Combat", "Research"], role="Tank",
       polish="Defense:3", stats=("Tank", 670), bond=3, lure="ITM_LURE_TUNINGFORK",
       sig="Bergschwere: Feldklang – Gegner können die Reihe nicht wechseln, Verbündete VER +2",
       mark="Ein Panzer wie ein Gebirgsgrat, um den Felsbrocken in eigener Schwerkraft kreisen",
       lore=["Die Grundstimme der Beständigkeit; ihr Ton gab den Bergen ihre Form.",
             "Schläft im Schlund unter Kharsholm; jedes Beben in Kharsgrat ist ein Atemzug Orh'gruuns.",
             "Die Bergvölker glauben, Kharsgrat sei Orh'gruuns Panzer und sie lebten auf seinem Rücken.",
             "Die Ahnenfelsen Kharsholms sind seit Jahrhunderten zu ihm hin ausgerichtet.",
             "Erwacht nach dem Akkord von Kharsholm und der Hauptquest Kharsgrats. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R03", **L, name="Nhael'vesh", epithet="nebularis", cat="Moorstimmen-Echo",
       arch="A05", size="L", h=2.9, types=("Venom", "Spirit"), habitat="Versunkener Turm unter Morvenfurt",
       act="Crepuscular", traits=["Flier", "Solitary", "Camouflaged"], niches=["Combat", "Research"], role="Control",
       polish="SpDefense:3", stats=("Control", 660), bond=3, lure="ITM_LURE_LANTERN",
       sig="Moorgedächtnis: Feldklang – besiegte Echos beider Seiten hinterlassen Nebel, der Gift überträgt und heilt",
       mark="Ein Reiher mit Schlangenhals, dessen Federn sich in Moordunst auflösen",
       lore=["Die Grundstimme des Kreislaufs; in ihr wird Verfall zu Erinnerung und Erinnerung zu neuem Leben.",
             "Schläft im versunkenen Turm unter Morvenfurt; ihr Atem ist der Nebel, der über dem Moor liegt.",
             "Die Moorweisen sagen, Nhael'vesh erinnere sich an jedes Leben, das im Moor endete.",
             "Die Freien Stimmen in der Unterstadt halten Nhael'vesh für die Schutzpatronin der Vergessenen.",
             "Erwacht nach dem Akkord von Morvenfurt und der Hauptquest Morvenmoors. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R06", **L, name="Thal'assyr", epithet="procellaris", cat="Gezeitenstimmen-Echo",
       arch="A06", size="XXL", h=11.0, w=40000, types=("Tide", "Storm"), habitat="Tiefseegrotte vor Saltrand-Hafen",
       act="Diurnal", traits=["Swimmer", "Flier", "Migratory"], niches=["Combat", "Research"], role="Speed",
       polish="Speed:3", stats=("Speed", 670), bond=3, lure="ITM_LURE_WINDCHIME",
       sig="Gezeitenwende: Feldklang – Reihen beider Seiten tauschen jede zweite Runde; eigene Seite handelt zuerst",
       mark="Flügel, deren Schläge Sturmfronten über das Meer treiben",
       lore=["Die Grundstimme der Freiheit und des Wandels; aus ihrem Ton entstanden Gezeiten und Winde.",
             "Schläft in der Tiefseegrotte vor Saltrand-Hafen; die Gezeiten folgen ihrem Atem.",
             "Der Gezeitenkult nennt jeden Rochen ein Kind Thal'assyrs.",
             "Der Felsbogen ‚Thal'assyrs Rippe‘ gilt den Seeleuten als heiligster Ort der Küste.",
             "Erwacht nach dem Akkord von Saltrand-Hafen und der Hauptquest Saltrands. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R04", **L, name="Ash'kareth", epithet="aenigma", cat="Wahrheitsstimmen-Echo",
       arch="A02", size="XL", h=4.0, types=("Light", "Arcane"), habitat="Unter dem Sonnenhof von Qasr Sahrun",
       act="Diurnal", traits=["Guardian", "Sunbather", "Solitary"], niches=["Combat", "Research"], role="Caster",
       polish="SpAttack:3", stats=("Caster", 665), bond=3, lure="ITM_LURE_MIRROR",
       sig="Rätselglanz: Feldklang – alle verborgenen Werte und Fähigkeiten werden enthüllt, Täuschungen enden",
       mark="Eine Mähne aus Lichtglyphen, die Fragen in die Luft schreibt",
       lore=["Die Grundstimme der Wahrheit; in ihrem Licht lässt sich nichts verbergen.",
             "Schläft unter dem Sonnenhof; Trugbilder der Weite sind Träume, die aus ihrem Schlaf aufsteigen.",
             "Die Nomaden sagen, Ash'kareth stelle jedem Wanderer eine Frage – wer lügt, verdurstet.",
             "Qasr Sahruns Herrscher legen ihren Eid auf dem Sonnenhof ab, über Ash'kareths Schlaf.",
             "Erwacht nach dem Akkord von Qasr Sahrun und der Hauptquest der Weite. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R05", **L, name="Pyr'thagon", epithet="faber", cat="Schmiedestimmen-Echo",
       arch="A15", size="XXL", h=8.5, types=("Ember", "Metal"), habitat="Kraterherz unter Schlackenwehr",
       act="Diurnal", traits=["Flier", "Thermal", "Guardian"], niches=["Combat", "Research"], role="Striker",
       polish="Attack:3", stats=("Striker", 675), bond=3, lure="ITM_FOOD_SULFURCANDY",
       sig="Weltenschmiede: Feldklang – jeder Treffer härtet den Anwender (VER +1), Glut-Terrain dauerhaft",
       mark="Schuppen aus gehärtetem Erz, zwischen denen Glut wie geschmolzenes Metall fließt",
       lore=["Die Grundstimme der Schöpfung durch Zerstörung; ihr Ton schmolz die ersten Erze aus dem Fels.",
             "Schläft im Kraterherz; jeder Ausbruch des Ignar ist ein Traum Pyr'thagons.",
             "Die Schmiedezunft sagt, jedes gute Werkstück trage einen Funken Pyr'thagons in sich.",
             "Kaldrex Vorn hat einen Eid geleistet, den Krater zu hüten, ohne zu wissen, was darunter schläft.",
             "Erwacht nach dem Akkord von Schlackenwehr und der Hauptquest Ignareths. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R07", **L, name="Isv'aldr", epithet="memoria", cat="Polarstimmen-Echo",
       arch="A06", size="XXL", h=9.5, w=24000, types=("Frost", "Light"), habitat="Gletscherdom unter Hvitmark",
       act="Nocturnal", traits=["Singer", "Glowing", "Guardian"], niches=["Combat", "Research"], role="Support",
       polish="SpDefense:3", stats=("Support", 665), bond=3, lure="ITM_LURE_AURORAGLASS",
       sig="Aurora der Erhaltung: Feldklang – Werteveränderungen der Verbündeten können nicht entfernt werden",
       mark="Schwingen wie die eines Schwans und ein Leib wie ein Wal, über die Polarlicht fließt",
       lore=["Die Grundstimme des Gedächtnisses; was sie besingt, vergeht nicht.",
             "Schläft im Gletscherdom; das Polarlicht über Hvitfell ist ihr Lied im Schlaf.",
             "Die Hvitfeller glauben, die Toten wanderten im Polarlicht zu Isv'aldr.",
             "Die Archivare Hvitmarks sehen sich als Diener Isv'aldrs: Erinnern ist ihr Gottesdienst.",
             "Erwacht nach dem Akkord von Hvitmark und der Hauptquest Hvitfells. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R08", **L, name="Ka'thurel", epithet="custos", cat="Erinnerungsstimmen-Echo",
       arch="A13", size="XL", h=5.0, types=("Spirit", "Arcane"), habitat="Thronsaal-Gewölbe unter Dorunsruh",
       act="Nocturnal", traits=["Guardian", "Collector", "Solitary"], niches=["Combat", "Research"], role="Control",
       polish="SpDefense:3", stats=("Control", 665), bond=3, lure="ITM_LURE_GLYPHTOKEN",
       sig="Weltgedächtnis: Feldklang – jede eingesetzte Fähigkeit wird gespeichert; Verbündete können sie einmal kopieren",
       mark="Eine gesichtslose Gestalt aus schwebenden Ruinenfragmenten, auf denen Glyphen wandern",
       lore=["Die Grundstimme der Erinnerung der Welt; sie bewahrt, was geschah, ob es jemand wissen will oder nicht.",
             "Schläft im Gewölbe unter dem Thronsaal; ihre Fragmente tragen die Geschichte Ael'Doruns.",
             "Die Dorunsruher sagen, Ka'thurel kenne die Antwort auf jede Frage – und schweige aus Gnade.",
             "Die Akademie hält Ka'thurel für die Quelle aller lesbaren Glyphen in den Säulen.",
             "Erwacht nach dem Akkord von Dorunsruh und der Hauptquest Ael'Doruns. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R09", **L, name="Prism'aion", epithet="amplificans", cat="Kristallstimmen-Echo",
       arch="A15", size="XXL", h=8.0, types=("Crystal", "Sound"), habitat="Resonanzkammer unter Prismara",
       act="Nocturnal", traits=["Flier", "Glowing", "Echolocator"], niches=["Combat", "Research"], role="Caster",
       polish="SpAttack:3", stats=("Caster", 670), bond=3, lure="ITM_FOOD_CRYSTALSALT",
       sig="Brechung: Feldklang – jeder Klang- oder Kristall-Angriff trifft ein zweites Ziel mit halber Kraft",
       mark="Eine kristallene Drachenschlange, deren Körper Licht in Töne bricht",
       lore=["Die Grundstimme der Verstärkung und Speicherung; was durch sie hindurchgeht, wird lauter und bleibt.",
             "Schläft in der Resonanzkammer; die Kristalle der Prismtiefen wachsen im Takt ihres Herzschlags.",
             "Die Bergleute glauben, jeder Kristall sei ein erstarrter Ton Prism'aions.",
             "Prismaras Glasmacher verbieten das Schleifen von Kristallen aus der Resonanzkammer.",
             "Erwacht nach dem Akkord von Prismara und der Hauptquest der Tiefen. Bindung nur mit Stimmsiegel."])

legend(c, "Archisonus", "R10", **L, name="Aeth'rion", epithet="dux", cat="Leitstimmen-Echo",
       arch="A05", size="L", h=2.9, types=("Sound", "Light"), habitat="Sternenarena von Aerion",
       act="Diurnal", traits=["Flier", "Singer", "Glowing"], niches=["Combat", "Research"], role="AllRound",
       polish="SpAttack:3", stats=("AllRound", 680), bond=3, lure="ITM_LURE_STARCHIME",
       sig="Einklang: Feldklang – Eigenklang-Bonus aller Verbündeten wirkt für jeden ihrer Typen",
       mark="Schwingen aus Notenlinien aus Licht, auf denen die Töne aller Stimmen stehen",
       lore=["Die Leitstimme, die alle anderen Stimmen verbindet; ohne sie zerfällt das Lied in einzelne Töne.",
             "Ruht über der Sternenarena; ihre Wärterin im Erstchor war Ilen.",
             "Die Aerioner nennen den Himmel über der Arena ‚Aeth'rions Notenblatt‘.",
             "Oruma Siyel ist die letzte Hüterin der Sternenarena; sie spricht von Aeth'rion nur in Liedern.",
             "Erwacht als letzte Stimme nach dem zehnten Akkord. Bindung nur mit Stimmsiegel."])

# Mythische
legend(c, "Pausa", "R10", **M, name="Velnox", epithet="silentium", cat="Pausen-Echo",
       arch="A12", size="L", h=2.9, w=600, types=("Void", "Gravity"), habitat="Im Riegel unter der Krone von Nimbara",
       act="Nocturnal", traits=["Solitary", "Drifter", "Camouflaged"], niches=["Combat", "Research"], role="Control",
       polish="SpAttack:3", stats=("Control", 650), bond=2, lure="ITM_LURE_BELLCHIME",
       sig="Große Pause: Feldklang – Harmonie beider Seiten wird jede Runde auf null gesetzt; Klang-Fähigkeiten verstummen",
       mark="Ein Körper aus Abwesenheit; Töne in seiner Nähe enden mitten im Klang",
       lore=["Die Pause selbst – kein Ton, sondern der Raum zwischen den Tönen, den das Weltlied braucht und fürchtet.",
             "Seit der Großen Stille in einem Riegel gebunden; es zieht Klang in sich hinein wie ein Abgrund Licht.",
             "Kein Volk von Aethris kennt seinen Namen; nur in einem einzigen Klangfragment wird er geflüstert.",
             "Der Orden der Stille sucht ohne es zu wissen nach Velnox; die Akademie hält ihn für eine Legende.",
             "Begegnung im Finale; bindbar erst im Nachhall. Nicht Ranked-zulässig."])

legend(c, "Metronomus", "R08", **M, name="Chronaire", epithet="tactus", cat="Takthüter-Echo",
       arch="A04", size="M", h=1.5, types=("Sound", "Arcane"), habitat="Zwischen zwei Herzschlägen",
       act="Diurnal", traits=["Dancer", "Solitary", "Glowing"], niches=["Combat", "Research"], role="Speed",
       polish="Speed:3", stats=("Speed", 640), bond=2, lure="ITM_LURE_TUNINGFORK",
       sig="Taktwechsel: Feldklang – die Zeitleiste läuft rückwärts; der langsamste Kämpfer handelt zuerst",
       mark="Eine schmale Gestalt mit Pendel statt Herz, deren Schritte den Takt der Welt angeben",
       lore=["Der Hüter des Takts; Chronaire existiert in dem Augenblick zwischen zwei Herzschlägen.",
             "Erscheint nur dem, der eine Herausforderung schneller als möglich besteht – und wieder verschwindet.",
             "Musiker schwören, bei perfekten Aufführungen eine zusätzliche Gestalt im Takt tanzen zu sehen.",
             "Die Akademie führt Chronaire als ‚unbewiesenes Phänomen T‘ in ihren Akten.",
             "Zugang über die Zeitherausforderungen des Endspiels."])

legend(c, "Speculum", "R09", **M, name="Mirrowisp", epithet="imago", cat="Spiegel-Echo",
       arch="A12", size="S", h=0.7, w=10, types=("Crystal", "Spirit"), habitat="Nur auf Fotografien sichtbar",
       act="Crepuscular", traits=["Mimic", "Shy", "Glowing"], niches=["Combat", "Research"], role="Control",
       polish="SpDefense:3", stats=("Control", 630), bond=2, lure="ITM_LURE_MIRROR",
       sig="Spiegelwelt: Feldklang – jeder Angriff trifft zusätzlich ein Spiegelbild des Angreifers",
       mark="Ein Lichtwesen, das auf Fotos scharf und mit bloßem Auge unsichtbar ist",
       lore=["Ein Spiegelbild, das sich selbstständig gemacht hat und nun ein eigenes Leben führt.",
             "Erscheint nur auf Fotografien – im Hintergrund, im Glas, in einer Pfütze.",
             "Fotografen hängen ihre misslungenen Bilder auf, weil Mirrowisp sich gern darin versteckt.",
             "Die Kodex-Linse wurde angeblich erfunden, um Mirrowisp zu beweisen.",
             "Zugang über die Fotografie-Meisterschaft."])

legend(c, "Ouroboros", "R03", **M, name="Ouroveth", epithet="perpetuus", cat="Kreislaufschlangen-Echo",
       arch="A07", size="XXL", h=8.5, w=30000, types=("Venom", "Bloom"), habitat="Wo Verfall in Wachstum übergeht",
       act="Crepuscular", traits=["Solitary", "Pollinator", "Camouflaged"], niches=["Combat", "Breeding"],
       role="Tank", polish="HP:3", stats=("Tank", 650), bond=2, lure="ITM_FOOD_MOORBERRY",
       sig="Ewiger Kreis: Feldklang – Gift heilt Verbündete und schadet Gegnern; besiegte Verbündete keimen einmal neu",
       mark="Eine Schlange, die blüht, wo sie verwest – vorne Knospen, hinten Moder",
       lore=["Der ewige Kreislauf aus Verfall und Wachstum, verkörpert als Schlange, die sich selbst erneuert.",
             "Zieht durch Orte, an denen etwas stirbt und etwas Neues entsteht; bleibt nie lange.",
             "Die Moorweisen behaupten, jede Blume auf einem Grab sei eine Schuppe Ouroveths.",
             "Züchter verehren Ouroveth als Schutzpatron ihres Handwerks.",
             "Zugang über die Zucht-Meisterschaft."])

legend(c, "Astrometallum", "R05", **M, name="Zenthrax", epithet="caducus", cat="Sternfall-Echo",
       arch="A15", size="XXL", h=10.0, types=("Gravity", "Metal"), habitat="Tiefenresonanz eines Sternenfalls",
       act="Nocturnal", traits=["Flier", "Solitary", "Stargazer"], niches=["Combat", "Research"], role="Striker",
       polish="Attack:3", stats=("Striker", 660), bond=2, lure="ITM_LURE_STARCHIME",
       sig="Sternensturz: Feldklang – jede Runde schlägt ein Meteor auf ein zufälliges Feld; Schwerkraft verdoppelt",
       mark="Ein Drachenleib aus dunklem Sternenmetall mit einem Herzen, das wie ein fallender Stern glüht",
       lore=["Ein gefallener Stern, dessen Herz aus Sternenmetall in der Tiefe weiterschlägt.",
             "Ruht in einer Tiefenresonanz; wenn er erwacht, beginnt die Erde nach oben zu fallen.",
             "Die Bergleute erzählen vom ‚Stern unter dem Berg‘, der in klaren Nächten zurückwill.",
             "Das Goldklang-Kontor hat eine Expedition finanziert, die nie zurückkehrte.",
             "Zugang über Raid RAID_06 oder die Solo-Tiefenresonanz DR_08."])

legend(c, "Eclipsis", "R10", **M, name="Aurelune", epithet="obscurans", cat="Finsternis-Echo",
       arch="A15", size="XL", h=5.5, types=("Light", "Void"), habitat="Nachthimmel während eines Resonanzsturms",
       act="Nocturnal", traits=["Flier", "Glowing", "Solitary"], niches=["Combat", "Research"], role="Caster",
       polish="SpAttack:3", stats=("Caster", 655), bond=2, lure="ITM_LURE_AURORAGLASS",
       sig="Finsternis: Feldklang – Licht- und Leere-Angriffe tauschen ihre Typvorteile",
       mark="Ein Drache mit einem Ring aus Licht um einen schwarzen Kern, wie eine Sonnenfinsternis",
       lore=["Ein Echo der Finsternis, in dem Licht und Leere einander umkreisen, ohne sich zu berühren.",
             "Erscheint nur nachts während eines Resonanzsturms; danach bleibt ein Ring am Himmel zurück.",
             "Die Aerioner nennen den Ring nach dem Sturm ‚Aurelunes Auge‘ und schließen die Fenster.",
             "Die Akademie zeichnet jeden Resonanzsturm auf – in der Hoffnung, Aurelune zu messen.",
             "Zugang über das Resonanzsturm-Ereignis oder den storygebundenen Solo-Sturm im Nachhall."])

c.write()
