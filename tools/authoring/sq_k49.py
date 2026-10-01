#!/usr/bin/env python3
"""K49 – Nebenquests I: SQ_001–SQ_070 (Verdanthain, Kharsgrat, Morvenmoor, Saltrand Teil 1)."""
import sys
from sq_common import Q, QUESTS, validate, write

IDS = [f"SQ_{i:03d}" for i in range(1, 71)]

# ───────────────────────────── R01 Verdanthain ─────────────────────────────
Q("SQ_001", "Messlatten im Farn", "NPC_PELL|Archivarin Pell", "SET_C_EICHENHALL", 2, 25,
  "Die neue Akademie-Außenstelle braucht Messreihen vom Rand der geheilten Lindwald-Zone. Pell gibt dem Wärter drei Resonanzlatten mit – und die Bitte, nicht nur zu messen, sondern aufzuschreiben, wie sich die Echos dort verhalten. Ihre These: Geheilte Zonen klingen eine Weile nach.",
  ["OBJ_TALK NPC_PELL 1 @SET_C_EICHENHALL | Archivarin Pell in der Außenstelle aufsuchen",
   "OBJ_GOTO R01_Z04 1 @R01_Z04 | Drei Messlatten am Rand der geheilten Zone setzen",
   "OBJ_OBSERVE ECHO_014 2 @R01_Z04 | Zwei Verhaltensmerkmale der Mossling-Herde am Zonenrand festhalten",
   "OBJ_DELIVER ITM_MAT_SOUNDRESIN 1 @SET_C_EICHENHALL | Die Klangharz-Probe von der Latte zu Pell bringen"],
  "Kodex-Beobachtung Mossling; ITM_LURE_BELLCHIME", "Pells Messkarte hängt in der Außenstelle; Barks über „nachklingende Zonen“")
Q("SQ_002", "Das Rillo, das rückwärts schwimmt", "NPC_LINA|Lina (Kind, Lindwiesen)", "SET_V_LINDWIESEN", 2, 20,
  "Lina schwört, dass ein Rillo im Mühlbach gegen die Strömung zurück zum Wald schwimmt, jeden Abend. Die Erwachsenen lachen. Der Wärter folgt dem Rillo und findet ein Nest unter einer eingestürzten Brücke, das seit der Stillezone abgeschnitten war.",
  ["OBJ_TALK NPC_LINA 1 @SET_V_LINDWIESEN | Lina zuhören",
   "OBJ_OBSERVE ECHO_021 1 @R01_Z02 | Das Rillo in der Dämmerung beobachten",
   "OBJ_INVESTIGATE - 3 @R01_Z02 | Spuren am Bach bis zur alten Brücke verfolgen",
   "OBJ_CHOICE DLG_SQ_002_01 1 @R01_Z02 | Den Durchgang freiräumen oder Lina zeigen, wie man es selbst tut"],
  "ITM_FOOD_LINDHONEY ×3; Kodex-Beobachtung Rillo", "Rillo-Familie lebt am Mühlbach (sichtbar); Lina grüßt den Wärter mit Namen",
  var="Time=Dusk", solution="Selbst räumen (schnell) oder Lina anleiten (+Bark-Kette, Lina wird später Wildwacht-Helferin im Nachhall).")
Q("SQ_003", "Kaels altes Notizbuch", "NPC_PELL|Archivarin Pell", "SET_C_EICHENHALL", 3, 30,
  "Pell hat in den Kisten der Außenstelle ein Notizbuch von Kael gefunden – aus der Zeit vor seiner Aufnahme. Seine Thesen über „messbares Hören“ sind klug und falsch zugleich. Pell bittet den Wärter, drei Versuche nachzustellen, um zu sehen, wo Kael recht hatte.",
  ["OBJ_TALK NPC_PELL 1 @SET_C_EICHENHALL | Pell zeigt das Notizbuch",
   "OBJ_INVESTIGATE - 3 @R01_Z03 | Drei Versuchsorte im Eichenhall-Forst wiederfinden",
   "OBJ_PHOTO ECHO_011 3 @R01_Z03 | Ein Chimbal beim Antwortgesang fotografieren (≥ 3 Sterne)",
   "OBJ_CHOICE DLG_SQ_003_01 1 @SET_C_EICHENHALL | Pell sagen, was an Kaels Thesen stimmt"],
  "ITM_KS_017; Kodex-Fragment „Messbares Hören“", "Notizbuch wird in K45 (MQ_A2_06) von Kael erwähnt; Dialogvariante je Antwort",
  solution="Einfühlsam (Kael hatte Angst, nicht zu hören), neugierig (die Messungen sind brauchbar), entschlossen (die Methode ist gefährlich) – alle gleich belohnt.")
Q("SQ_004", "Der Schläfer im Uralthain", "NPC_TORBEN|Holzfäller Torben", "SET_O_URALTHAINLAGER", 3, 25,
  "Ein Torgrath liegt seit Tagen quer über dem Holzweg im Uralthain und rührt sich nicht. Torben will ihn nicht wecken – „man weckt keinen Berg“. Der Wärter findet heraus, warum das Echo dort ruht: Unter ihm brütet eine Brokk-Familie in einer Mulde.",
  ["OBJ_TALK NPC_TORBEN 1 @SET_O_URALTHAINLAGER | Torben am Lager",
   "OBJ_OBSERVE ECHO_006 2 @R01_Z06 | Den ruhenden Torgrath beobachten",
   "OBJ_INVESTIGATE - 2 @R01_Z06 | Die Mulde unter dem Torgrath untersuchen",
   "OBJ_CHOICE DLG_SQ_004_01 1 @SET_O_URALTHAINLAGER | Den Holzweg verlegen oder auf das Schlüpfen warten"],
  "ITM_TRAP_REST; Rezept RCP_037", "Neuer Holzweg (Data Layer) oder Brokk-Jungtiere am alten Weg nach 3 Spieltagen",
  solution="Weg verlegen (Torben brummt, hilft aber) · warten (3 Spieltage, kein Echtzeit-Timer) · Torgrath mit Ruhekorb umsiedeln (nur mit ITM_TRAP_REST aus SQ_001-Kette, Kodex-Bonus).")
Q("SQ_005", "Das Echo der Außenstelle", "NPC_PELL|Archivarin Pell", "SET_C_EICHENHALL", 4, 35,
  "In der Außenstelle verschwinden nachts Messinstrumente. Pell verdächtigt die Freien Stimmen. Der Wärter findet stattdessen ein junges Lumow, das die glänzenden Teile sammelt – und eine Frage: Darf die Akademie ein Echo einfangen, das sie stört?",
  ["OBJ_INVESTIGATE - 3 @SET_C_EICHENHALL | Spuren in der Außenstelle bei Nacht",
   "OBJ_OBSERVE ECHO_019 1 @SET_C_EICHENHALL | Das Lumow beim Sammeln beobachten",
   "OBJ_GOTO R01_Z03 1 @R01_Z03 | Dem Lumow zu seinem Hort folgen",
   "OBJ_CHOICE DLG_SQ_005_01 1 @SET_C_EICHENHALL | Pell vorschlagen, was mit dem Lumow geschieht"],
  "ITM_LURE_LANTERN; Kodex-Beobachtung Lumow (Sammler)", "Lumow wohnt im Dachgebälk der Außenstelle oder im Forst; Pell entschuldigt sich bei Tavesh' Leuten (Bark)",
  var="Time=Night", solution="Lumow binden (Wärter) · freilassen im Forst mit Ersatz-Glanzsteinen (Wildwacht-Bark) · Pell richtet ein „Lumow-Fach“ ein (dritte Lösung, Pell-Bark im Nachhall).")
Q("SQ_006", "Das Gewitter der Wisplets", "NPC_R01_ODO|Wirt Odo", "SET_C_EICHENHALL", 4, 25,
  "Seit der Resonanzsturm über Aethris lag, ziehen Wisplets bei jedem Gewitter in Schwärmen über Eichenhall und schlagen Funken an den Dachrinnen. Odo fürchtet um sein Strohdach. Der Wärter findet heraus, dass die Wisplets einem Ton folgen, der vom alten Wetterturm kommt.",
  ["OBJ_CONDITION Weather=Thunderstorm 1 @R01 | Auf ein Gewitter über Eichenhall warten (Zeit vorspulen erlaubt)",
   "OBJ_OBSERVE ECHO_007 2 @SET_C_EICHENHALL | Den Schwarm beobachten",
   "OBJ_INVESTIGATE - 2 @SET_C_EICHENHALL | Den Ton zum Wetterturm zurückverfolgen",
   "OBJ_PUZZLE PZ_SQ006_BELLS 1 @SET_C_EICHENHALL | Die Windglocken des Turms neu stimmen"],
  "ITM_LURE_WINDCHIME; Hain-Dekor ITM_DECO_WEATHERBELL", "Wisplets tanzen bei Gewitter um den Turm statt um die Dächer; Odo stiftet ein Freibier-Bark",
  var="Weather=Thunderstorm", truth=0)
Q("SQ_007", "Honig für Kharsholm", "NPC_OSSIAN|Kontorschreiber Ossian", "SET_C_EICHENHALL", 2, 25,
  "Ossian will einen kleinen Handelsweg eröffnen: Lindenhonig aus Lindwiesen gegen Bergkäse aus Kharsholm. Dafür braucht er einen Wärter, der die Imker überzeugt – die trauen dem Kontor nicht, seit es vor Jahren ihre Preise drückte.",
  ["OBJ_TALK NPC_OSSIAN 1 @SET_C_EICHENHALL | Ossian im Kontor",
   "OBJ_TALK NPC_IMKERIN_HILDE 1 @SET_V_LINDWIESEN | Imkerin Hilde zuhören",
   "OBJ_OBSERVE ECHO_015 1 @R01_Z02 | Die Myrthorn bei der Bestäubung beobachten (Hildes Bedingung)",
   "OBJ_CHOICE DLG_SQ_007_01 1 @SET_V_LINDWIESEN | Einen Preis aushandeln"],
  "ITM_FOOD_LINDHONEY ×5; Rezept RCP_041", "Honigfässer am Kontor; Hilde verkauft ab jetzt an Wendels Wärterbedarf",
  solution="Hoher Preis (Hilde zufrieden, Ossian murrt) · niedriger Preis (Ossian zufrieden) · Gewinnbeteiligung (beide zufrieden, nur mit neugieriger Frage nach den Bienen-Echos freigeschaltet).")
Q("SQ_008", "Die Glyphe unter dem Moos", "NPC_R01_ANSELM|Schnitzer Anselm", "SET_C_EICHENHALL", 3, 30,
  "Anselm hat beim Holzholen im Moosgrund eine Steinplatte mit dorunischen Zeichen gefunden. Er will sie als Tischplatte. Der Wärter erkennt, dass die Glyphen einen Ton beschreiben – und dass drei weitere Platten im Hügel liegen müssen.",
  ["OBJ_TALK NPC_R01_ANSELM 1 @SET_C_EICHENHALL | Anselms Fund ansehen",
   "OBJ_INVESTIGATE - 3 @R01_Z04 | Drei weitere Platten im Moosgrund finden",
   "OBJ_PUZZLE PZ_SQ008_GLYPH 1 @R01_Z04 | Die Platten in Klangreihenfolge legen",
   "OBJ_OBSERVE ECHO_017 1 @R01_Z04 | Das Glyphaune beobachten, das auf den Ton antwortet"],
  "ITM_EVO_GLYPHSHARD; Klangfragment (TruthLevel 0)", "Glyphenkreis im Moosgrund (POI, Rückkehrort); Glyphaune nachts dort häufiger",
  var="Time=Night")
Q("SQ_009", "Leere Fässer", "NPC_OSSIAN|Kontorschreiber Ossian", "SET_C_EICHENHALL", 3, 30,
  "Die erste Honiglieferung kommt in Kharsholm leer an. Ossian vermutet Diebe. Der Wärter verfolgt den Weg zurück und findet bei der Linnfurt einen Riss im Fass – und eine Spur, die nicht von Menschen stammt, sondern von einer Sporix-Kolonie, die süchtig nach Honig geworden ist.",
  ["OBJ_GOTO SET_O_LINNFURTPOSTEN 1 @SET_O_LINNFURTPOSTEN | Zum Linnfurt-Posten",
   "OBJ_INVESTIGATE - 3 @R01_Z05 | Spuren der Fässer in der Farnschlucht",
   "OBJ_OBSERVE ECHO_024 1 @R01_Z05 | Die Sporix-Kolonie nachts beobachten",
   "OBJ_CHOICE DLG_SQ_009_01 1 @R01_Z05 | Lösung für Weg und Kolonie wählen"],
  "ITM_TRAP_SCENT; ITM_MAT_FERNFIBER ×5", "Neue Wegführung mit Duftfallen-Schutz; Sporix-Kolonie bleibt und bestäubt die Farnschlucht",
  var="Time=Night", solution="Kolonie vertreiben (schnell, Wildwacht-Bark tadelt) · Fässer mit Harz versiegeln (Ossian zahlt) · Köderhonig an einem anderen Ort anbieten (dritte Lösung, Kodex-Bonus).")
Q("SQ_010", "Wendelins erste Seite", "NPC_R01_GRETA|Greta (Wildwacht-Kammer)", "SET_C_EICHENHALL", 2, 25,
  "Greta hat beim Ausräumen der Wildwacht-Kammer eine Seite in Wendelins Handschrift gefunden – eine Wegbeschreibung zu einem Ort „wo die erste Arena hätte stehen sollen“. Der Ort ist ein Felsring im Lindwald, in dem Echos still werden, um zu lauschen.",
  ["OBJ_TALK NPC_R01_GRETA 1 @SET_C_EICHENHALL | Greta zeigt die Seite",
   "OBJ_GOTO R01_Z01 1 @R01_Z01 | Der Wegbeschreibung in den Lindwald folgen",
   "OBJ_INVESTIGATE - 3 @R01_Z01 | Den Felsring untersuchen",
   "OBJ_OBSERVE ECHO_012 1 @R01_Z01 | Das Cantaroth beobachten, das im Ring singt"],
  "Wendelin-Tagebuch (Sammelseite); ITM_LURE_TUNINGFORK", "Felsring wird zum Rastplatz (Lager-Moment möglich)",
  var="Time=Dawn")
Q("SQ_011", "Der Mann mit dem Wagen", "NPC_OSSIAN|Kontorschreiber Ossian", "SET_C_EICHENHALL", 4, 35,
  "Ein fremder Händler bietet den Imkern das Doppelte für ihren Honig – unter der Bedingung, nicht mehr an Ossian zu liefern. Der Wärter folgt seinem Wagen und findet heraus, dass er für ein Konsortium arbeitet, das den Weg nach Kharsholm übernehmen will.",
  ["OBJ_TALK NPC_IMKERIN_HILDE 1 @SET_V_LINDWIESEN | Hilde erzählt vom Angebot",
   "OBJ_ESCORT NPC_HAENDLER_BRISK 1 @R01_Z03 | Dem Wagen unauffällig folgen (Abstand halten)",
   "OBJ_INVESTIGATE - 2 @SET_O_FARNWACHT | Die Ladepapiere am Farnwacht-Posten lesen",
   "OBJ_CHOICE DLG_SQ_011_01 1 @SET_C_EICHENHALL | Ossian, Hilde oder den Händler selbst ansprechen"],
  "Kontor-Lieferschein (Lore); ITM_CON_SENSE ×2", "Konsortium-Händler verschwindet oder bleibt als fairer Konkurrent (Preise in Lindwiesen −5 %)",
  solution="Ossian berichten (Kontor setzt sich durch) · Hilde warnen (Imker gründen eine Genossenschaft) · mit dem Händler reden (er gibt zu, unter Druck zu stehen; wird zum fairen Zweitkäufer).")
Q("SQ_012", "Briefe an Ilen", "NPC_MAREN|Maren (Lindwiesen)", "SET_V_LINDWIESEN", 3, 30,
  "Die alte Maren schreibt seit sechzig Jahren Briefe an „Ilen“ und legt sie in den Klangbrunnen von Lindwiesen. Nach Akt III fragt sie den Wärter, ob Ilen sie je gelesen hat. Der Wärter findet die Briefe – und in ihnen Erinnerungen an seine eigene Familie.",
  ["OBJ_TALK NPC_MAREN 1 @SET_V_LINDWIESEN | Maren besuchen",
   "OBJ_INVESTIGATE - 3 @SET_V_LINDWIESEN | Den Klangbrunnen und die alte Kapelle durchsuchen",
   "OBJ_CHOICE DLG_SQ_012_01 1 @SET_V_LINDWIESEN | Maren antworten, was mit Ilen geschah"],
  "Familienchronik (Lore, TruthLevel 5); Hain-Dekor ITM_DECO_LETTERBOX", "Maren legt ihren letzten Brief „für den, der zuhört“ in den Brunnen; Epilog-Bark",
  truth=5, solution="Die Wahrheit (Nachklang) erzählen · schonend erzählen · Maren selbst schließen lassen – alle drei würdevoll, kein Flag.")
Q("SQ_013", "Wo Brannoc saß", "NPC_FENJA|Zeugmeisterin Fenja", "SET_C_EICHENHALL", 2, 25,
  "Die Wildwacht ehrt Brannoc die Lauscherin, die 287 ein Echo durch Geduld statt Gewalt zähmte. Fenja glaubt, der Ort liege im Uralthain, nicht dort, wo das Denkmal steht. Der Wärter soll drei Tage-Nächte-Zeichen deuten, die in Brannocs Lied vorkommen.",
  ["OBJ_TALK NPC_FENJA 1 @SET_C_EICHENHALL | Fenja und Brannocs Lied",
   "OBJ_INVESTIGATE - 3 @R01_Z06 | Die Zeichen aus dem Lied im Uralthain finden",
   "OBJ_OBSERVE ECHO_013 1 @R01_Z06 | Das Lorncant am Fundort beobachten"],
  "ITM_LURE_WHISTLE; Kodex-Fragment „Brannoc I“", "Steinmal „Brannocs Platz“ im Uralthain (Rastort); Denkmal in Eichenhall erhält Tafel",
  var="Time=Night")
Q("SQ_014", "Odos Rezept", "NPC_R01_ODO|Wirt Odo", "SET_C_EICHENHALL", 1, 20,
  "Odo kocht seit dreißig Jahren den gleichen Wurzeleintopf und hat das Rezept vergessen – seine Mutter hatte es nur gesungen. Ein altes Chimkin, das im Hof des Wurzelkrugs lebt, summt die Melodie noch. Der Wärter hört hin.",
  ["OBJ_TALK NPC_R01_ODO 1 @SET_C_EICHENHALL | Odos Kummer",
   "OBJ_OBSERVE ECHO_010 1 @SET_C_EICHENHALL | Dem Chimkin im Hof zuhören",
   "OBJ_COLLECT ITM_MAT_LINDBLOSSOM 3 @R01_Z02 | Die besungenen Zutaten sammeln",
   "OBJ_DELIVER ITM_MAT_LINDBLOSSOM 3 @SET_C_EICHENHALL | Odo beim Kochen helfen"],
  "Rezept RCP_046; ITM_FOODC_STEW ×2", "„Odos Wurzeleintopf“ als Gasthaus-Gericht; Chimkin wird Hausechos-Bark")
Q("SQ_015", "Das alte Echo", "NPC_FENJA|Zeugmeisterin Fenja", "SET_C_EICHENHALL", 3, 30,
  "Ein uralter Myrthorn soll sich an Brannoc erinnern – Myrthorn werden alt, und dieser hat einen Klangmal-Riss, der zu Brannocs Lied passt. Der Wärter muss sein Vertrauen gewinnen, ohne ihn zu binden.",
  ["OBJ_GOTO R01_Z06 1 @R01_Z06 | Den alten Myrthorn im Uralthain finden",
   "OBJ_OBSERVE ECHO_015 3 @R01_Z06 | Drei Verhaltensmerkmale des Alten beobachten",
   "OBJ_CHOICE DLG_SQ_015_01 1 @R01_Z06 | Annäherung wählen (Lockmittel, Lied, Geduld)",
   "OBJ_INVESTIGATE - 1 @R01_Z06 | Dem Myrthorn zu Brannocs zweitem Ort folgen"],
  "Kodex-Fragment „Brannoc II“; ITM_FOOD_MOSSCAKE ×3", "Der alte Myrthorn begleitet den Wärter im Uralthain als Gast (keine Bindung)",
  var="Weather=Rain", solution="Geduld (Zeit vorspulen nicht erlaubt im Kreis; 2 Spielstunden) · Lied (Resonanzsinn-Minispiel) · Lockmittel (schnell, aber Fenja ist enttäuscht – Bark).")
Q("SQ_016", "Farnzählung", "NPC_R01_LORIN|Apotheker Lorin", "SET_C_EICHENHALL", 2, 25,
  "Lorin braucht Fernlit-Sporen für Heilsalben, aber Fernlits sind sehr selten geworden. Bevor jemand sammelt, will er wissen, wie viele es gibt. Der Wärter zählt in der Morgendämmerung im Regen – nur dann zeigen sich Fernlits.",
  ["OBJ_TALK NPC_R01_LORIN 1 @SET_C_EICHENHALL | Lorins Sorge",
   "OBJ_CONDITION Time=Dawn&Weather=Rain 1 @R01_Z06 | Regnerische Morgendämmerung abwarten",
   "OBJ_PHOTO ECHO_001 3 @R01_Z06 | Drei Fernlits fotografieren (Zählung)",
   "OBJ_CHOICE DLG_SQ_016_01 1 @SET_C_EICHENHALL | Lorin eine Sammelmenge empfehlen"],
  "ITM_CON_HEAL_2 ×3; Kodex-Beobachtung Fernlit", "Lorin sammelt nur noch, was der Wärter empfiehlt; Fernlit-Bestand im Nachhall höher oder gleich",
  var="Time=Dawn & Weather=Rain")
Q("SQ_017", "Das Lied im Stein", "NPC_FENJA|Zeugmeisterin Fenja", "SET_C_EICHENHALL", 3, 30,
  "Am dritten Ort Brannocs, in der Farnschlucht, ist ein Lied in den Fels geritzt – aber zerstört, Teile fehlen. Ein Skirrow imitiert Bruchstücke davon. Der Wärter setzt das Lied aus Fels und Vogelruf zusammen.",
  ["OBJ_GOTO R01_Z05 1 @R01_Z05 | Zur Felswand in der Farnschlucht",
   "OBJ_INVESTIGATE - 3 @R01_Z05 | Lesbare Liedteile finden",
   "OBJ_OBSERVE ECHO_026 1 @R01_Z05 | Die Imitationen des Skirrow aufzeichnen",
   "OBJ_PUZZLE PZ_SQ017_SONG 1 @R01_Z05 | Das Lied zusammensetzen"],
  "ITM_KS_009; Kodex-Fragment „Brannoc III“", "Das Lied ist am Lagerfeuer spielbar (Lager-Moment-Option)")
Q("SQ_018", "Nachklang im Lindwald", "NPC_PELL|Archivarin Pell", "SET_C_EICHENHALL", 3, 35,
  "Im Nachhall bittet Pell um einen letzten Vergleich: Wie klingt der Lindwald heute, verglichen mit ihrer Messung vom Anfang? Je nach Ende hört der Wärter grünes Wachstum oder silbrige Ruhe – und Pell schreibt ihre Abschlussarbeit darüber.",
  ["OBJ_GOTO R01_Z04 1 @R01_Z04 | Zu den alten Messlatten",
   "OBJ_INVESTIGATE - 3 @R01_Z04 | Die Latten ablesen",
   "OBJ_OBSERVE ECHO_016 1 @R01_Z04 | Das Vernaune am Zonenrand beobachten",
   "OBJ_TALK NPC_PELL 1 @SET_C_EICHENHALL | Pell die Ergebnisse bringen"],
  "Hain-Dekor ITM_DECO_MEASURESTAFF; Kodex-Eintrag „Pells Abschlussarbeit“", "Pells Arbeit liegt in der Akademie-Bibliothek; Text je Ende verschieden",
  truth=9, pre="Ending=NewSong | Ending=SoftSilence")
Q("SQ_019", "Die Lauscherin", "NPC_FENJA|Zeugmeisterin Fenja", "SET_C_EICHENHALL", 5, 45,
  "Mit allen drei Orten und dem Lied hört der Wärter, was Brannoc 287 hörte: Ein Echo kommt, wenn man lange genug still ist. In einer Nacht am Uralthain wird die Probe wiederholt – ohne Siegel, ohne Köder, nur mit Zuhören. Am Ende steht kein gebundenes Echo, sondern ein Gelöbnis der Wildwacht.",
  ["OBJ_TALK NPC_FENJA 1 @SET_C_EICHENHALL | Fenja und Hralda erwarten den Wärter",
   "OBJ_GOTO R01_Z06 1 @R01_Z06 | Zu Brannocs Platz",
   "OBJ_REST R01_Z06 1 @R01_Z06 | Die Nacht in Stille verbringen (kein Kampf, kein Ruf)",
   "OBJ_OBSERVE ECHO_020 1 @R01_Z06 | Das Phantalume, das sich nähert, beobachten",
   "OBJ_CHOICE DLG_SQ_019_01 1 @R01_Z06 | Das Gelöbnis der Lauscher sprechen"],
  "Titel „Lauscher“; Hain-Dekor ITM_DECO_LISTENERSTONE; ITM_LURE_TUNINGFORK", "Wildwacht-Barks nennen den Wärter „Lauscher“; Phantalume erscheint im Uralthain häufiger",
  var="Time=Night & Moon=New")
Q("SQ_020", "Die Probe der Wurzeln", "NPC_MAELIS|Maelis Wendt", "SET_C_EICHENHALL", 5, 30,
  "Maelis lädt zu einer Schauprobe: drei Kämpfe in Folge, jeder mit einer eigenen Regel des Gartens – nur Blüte-Echos, Überwuchs ab Runde 1, und ein Kampf, in dem nur Formation entscheidet. Wer alle drei besteht, darf im Garten der Arena trainieren.",
  ["OBJ_TALK NPC_MAELIS 1 @SET_C_EICHENHALL | Maelis' Einladung",
   "OBJ_BATTLE NPC_GARDENER_1 1 @SET_C_EICHENHALL | Erste Probe: nur Blüte-Echos",
   "OBJ_BATTLE NPC_GARDENER_2 1 @SET_C_EICHENHALL | Zweite Probe: Überwuchs ab Runde 1",
   "OBJ_BATTLE NPC_MAELIS 1 @SET_C_EICHENHALL | Dritte Probe: Formationsduell",
   "OBJ_OBSERVE ECHO_241 1 @SET_C_EICHENHALL | Unter der Arena lauschen (Sylv'anor im Schlaf)"],
  "ITM_HELD_TONE_BLOOM; Trainingsplatz Arena-Garten", "Arena-Garten als Trainingsort; Maelis-Barks",
  pre="Akkorde>=4")
Q("SQ_021", "Die Wanderung beginnt", "NPC_FENJA|Zeugmeisterin Fenja", "SET_C_EICHENHALL", 3, 30,
  "Jedes Jahr ziehen Gratkins aus dem Kharsgrat über die Pässe in die Lindwiesen-Auen. Seit der Stille sind die Wege durcheinander. Fenja bittet den Wärter, die Vorhut der Wanderung zu finden und ihren Weg zu kennzeichnen.",
  ["OBJ_TALK NPC_FENJA 1 @SET_C_EICHENHALL | Fenja und die Wanderkarte",
   "OBJ_OBSERVE ECHO_043 2 @R01_Z02 | Die Vorhut der Gratkins beobachten",
   "OBJ_INVESTIGATE - 3 @R01_Z05 | Alte Wegmarken in der Farnschlucht finden",
   "OBJ_GOTO SET_O_LINNFURTPOSTEN 1 @SET_O_LINNFURTPOSTEN | Den Weg am Linnfurt-Posten melden"],
  "ITM_LURE_WHISTLE; Kodex-Beobachtung Gratkin (Wanderung)", "Wegmarken mit Wildwacht-Bändern; Gratkin-Zug sichtbar in R01_Z02",
  var="Time=Day")
Q("SQ_022", "Eine Kiste Äpfel", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_MOOSGRUND", 3, 25,
  "Ennis Rook bittet den Wärter, eine Kiste Äpfel durch die Kontrolle am Linnfurt-Posten zu bringen. Unter den Äpfeln schläft ein junges Brokkar, freigekauft aus einem Steinbruch. Ennis sagt es dem Wärter erst, nachdem er die Kiste trägt.",
  ["OBJ_TALK NPC_ENNIS 1 @SET_V_MOOSGRUND | Ennis am Rand von Moosgrund",
   "OBJ_CHOICE DLG_SQ_022_01 1 @SET_V_MOOSGRUND | Die Wahrheit über die Kiste aufnehmen",
   "OBJ_ESCORT NPC_ENNIS 1 @SET_O_LINNFURTPOSTEN | Mit Ennis durch die Kontrolle",
   "OBJ_OBSERVE ECHO_005 1 @R01_Z05 | Das Brokkar beim ersten freien Schritt beobachten"],
  "ITM_FOOD_BERRYMIX ×3; Kodex-Beobachtung Brokkar", "Ennis vertraut dem Wärter (Bark), Brokkar lebt in der Farnschlucht",
  solution="Mitspielen · Ennis überreden, die Kiste offen vorzuzeigen (die Wildwacht lässt es durch – Hralda-Bark) · Wildwacht vorab informieren (Ennis enttäuscht, Ruf trotzdem).")
Q("SQ_023", "Der Steinbruch von Moosgrund", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_MOOSGRUND", 4, 35,
  "Woher kam das Brokkar? Ennis führt den Wärter zum Steinbruch hinter Moosgrund, wo Brokks in Schichten arbeiten – gut gefüttert, aber angekettet. Der Besitzer ist kein Unmensch, nur arm. Die Freien Stimmen wollen die Echos befreien; der Wärter sucht einen Weg, der auch den Besitzer Arnulf nicht ruiniert.",
  ["OBJ_GOTO R01_Z04 1 @R01_Z04 | Zum Steinbruch",
   "OBJ_OBSERVE ECHO_004 2 @R01_Z04 | Die Arbeits-Brokks beobachten",
   "OBJ_TALK NPC_STEINBRECHER_ARNULF 1 @R01_Z04 | Steinbrecher Arnulf zuhören",
   "OBJ_CHOICE DLG_SQ_023_01 1 @R01_Z04 | Lösung für Brokks und Arnulf"],
  "ITM_TRAP_HOARD; ITM_MAT_COPPERORE ×5", "Arnulfs Steinbruch arbeitet mit freiwilligen Brokks (Lohn: Erzkrümel) oder steht still",
  solution="Befreien (Freie Stimmen jubeln, Arnulf verarmt – Bark) · Arnulf mit Kontor-Kredit Maschinen ermöglichen (Ossian-Bark) · Brokks frei lassen und Arnulf zeigen, wie man mit Erzkrümeln freiwillige Hilfe gewinnt (dritte Lösung).")
Q("SQ_024", "Die Nachtfähre", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_MOOSGRUND", 4, 30,
  "Ennis muss sieben befreite Echos über den Linnfluss bringen, nachts, ohne Laterne. Ein Rillward-Paar kennt die Furt. Der Wärter muss die Echos ruhig halten – ein einziger Ruf, und die Kontrolle am Posten wird aufmerksam.",
  ["OBJ_CONDITION Time=Night 1 @R01_Z02 | Nacht abwarten",
   "OBJ_OBSERVE ECHO_022 1 @R01_Z02 | Dem Rillward-Paar zur Furt folgen",
   "OBJ_ESCORT NPC_ENNIS 1 @R01_Z02 | Ennis und die Echos über die Furt begleiten",
   "OBJ_CHOICE DLG_SQ_024_01 1 @R01_Z02 | Am anderen Ufer: Ennis' Frage beantworten, wohin die Echos sollen"],
  "ITM_CON_REPEL ×2; Hain-Dekor ITM_DECO_FERRYLANTERN", "Rillwards nisten an der Furt; Ennis' Zelle hat einen sicheren Weg",
  var="Time=Night")

# ───────────────────────────── R02 Kharsgrat ─────────────────────────────
Q("SQ_025", "Basalt, der zurückklingt", "NPC_MESSER_HAKON|Messmeister Hakon (Akademie)", "SET_C_KHARSHOLM", 5, 50,
  "Die Messreihen der Außenstelle enden in Kharsholm: Der Grollbasalt der Kettenbrücken klingt nach, wenn ein Echo darüber geht – stärker, seit Orh'gruun im Schlaf liegt. Hakon will den Basalt anbohren. Die Klans verbieten es. Der Wärter sucht eine Messung, die nichts zerstört.",
  ["OBJ_TALK NPC_MESSER_HAKON 1 @SET_C_KHARSHOLM | Hakon an den Kettenbrücken",
   "OBJ_TALK NPC_R02_GERD 1 @SET_C_KHARSHOLM | Gerd in der Halle der Klans",
   "OBJ_OBSERVE ECHO_035 2 @R02_Z02 | Kraggoths auf den Brücken beobachten",
   "OBJ_PUZZLE PZ_SQ025_RESON 1 @R02_Z02 | Die Brücke mit Resonanzlatten „abhören“",
   "OBJ_CHOICE DLG_SQ_025_01 1 @SET_C_KHARSHOLM | Ergebnis an Hakon und Gerd übergeben"],
  "Resonator-Upgrade-Bauteil ITM_MAT_SOUNDRESIN ×3; Kodex-Fragment „Grollbasalt“", "Akademie und Klans teilen sich die Messung; Brücken-Barks",
  solution="Bohrung (Hakon gewinnt, Klans grollen) · Verbot (Gerd gewinnt) · Abhören ohne Bohrung (dritte Lösung, beide akzeptieren).")
Q("SQ_026", "Das Tetri ohne Gewicht", "NPC_SIGGA|Sigga (Brakkfels)", "SET_V_BRAKKFELS", 3, 25,
  "Siggas junges Tetri schwebt plötzlich und kommt nicht mehr herunter. Die Dörfler sagen, es sei verflucht. Der Wärter erkennt eine Schwerkraft-Anomalie an den Ahnenfelsen, die das Tetri im Schlaf aufgeladen hat.",
  ["OBJ_TALK NPC_SIGGA 1 @SET_V_BRAKKFELS | Sigga und ihr schwebendes Tetri",
   "OBJ_OBSERVE ECHO_037 1 @SET_V_BRAKKFELS | Das Tetri beobachten",
   "OBJ_INVESTIGATE - 3 @R02_Z01 | Die Anomalie an den schwebenden Ahnenfelsen finden",
   "OBJ_ESCORT NPC_SIGGA 1 @R02_Z01 | Sigga und das Tetri zur Gegenanomalie begleiten"],
  "ITM_EVO_GRAVITY; Kodex-Beobachtung Tetri", "Sigga erklärt den Dörflern die Anomalie (Bark); Tetri landet",
  var="Time=Night")
Q("SQ_027", "Kharsk-Formen", "NPC_MESSER_HAKON|Messmeister Hakon (Akademie)", "SET_C_KHARSHOLM", 3, 35,
  "Vael beschrieb 812 die Lithi als reine Steinart. Hakon hat Lithshells mit Wasserklang gefunden – eine Regionalform, die Vael übersah. Der Wärter soll drei Belege fotografieren und eine Herde in der Dämmerung beobachten.",
  ["OBJ_TALK NPC_MESSER_HAKON 1 @SET_C_KHARSHOLM | Hakons Zweifel an Vael",
   "OBJ_PHOTO ECHO_049 3 @R02_Z03 | Drei Lithshells im Grollschlund fotografieren",
   "OBJ_OBSERVE ECHO_048 2 @R02_Z03 | Eine Lithi-Herde in der Dämmerung beobachten",
   "OBJ_DELIVER ITM_MAT_QUARTZSHARD 1 @SET_C_KHARSHOLM | Eine Schalenprobe abliefern (Fundstück, kein Verletzen)"],
  "ITM_KS_022; Kodex-Fragment „Vaels Lücken I“", "Kodex-Eintrag Lithshell erhält „Regionalform (Kharsgrat)“",
  var="Time=Dusk")
Q("SQ_028", "Schneenacht am Grollhorn", "NPC_BRANDA|Bergführerin Branda", "SET_O_GROLLHORNBIWAK", 4, 30,
  "Bei Schneefall ziehen Rimpaws auf das Grollhorn, um auf dem Gipfel im Schnee zu singen – eine Wanderung, die kein Mensch je ganz gesehen hat. Branda will sie sehen, bevor ihre Knie nicht mehr mitmachen.",
  ["OBJ_CONDITION Weather=Snow 1 @R02_Z05 | Schneefall am Grollhorn abwarten",
   "OBJ_ESCORT NPC_BRANDA 1 @R02_Z05 | Branda zum Gipfel begleiten",
   "OBJ_OBSERVE ECHO_051 2 @R02_Z05 | Den Rimpaw-Gesang beobachten",
   "OBJ_PHOTO ECHO_051 1 @R02_Z05 | Ein Foto für Branda (≥ 4 Sterne)"],
  "ITM_CON_WARM ×3; Hain-Dekor ITM_DECO_SUMMITFLAG", "Brandas Foto hängt im Biwak; Rimpaw-Gesang als Wetterzeichen in Barks",
  var="Weather=Snow")
Q("SQ_029", "Käse und Klanschwur", "NPC_R02_TOVA|Tova (Erzkontor)", "SET_C_KHARSHOLM", 5, 50,
  "Das Ende des Honigwegs: Tova soll den Bergkäse liefern, aber der Klan der Hralls verweigert das Geschäft mit dem Kontor – ein alter Klanschwur. Der Wärter findet heraus, dass der Schwur nicht gegen das Kontor gerichtet ist, sondern gegen einen Mann, der vor Jahren Hralls betrogen hat: den Konsortiums-Händler aus SQ_011.",
  ["OBJ_TALK NPC_R02_TOVA 1 @SET_C_KHARSHOLM | Tova erklärt das Problem",
   "OBJ_GOTO SET_V_HRALLSTED 1 @SET_V_HRALLSTED | Nach Hrallsted",
   "OBJ_INVESTIGATE - 3 @SET_V_HRALLSTED | Die Klanchronik am Ahnenfelsen lesen",
   "OBJ_CHOICE DLG_SQ_029_01 1 @SET_V_HRALLSTED | Den Klan um ein neues Wort bitten",
   "OBJ_DELIVER ITM_FOOD_ALPINECHEESE 3 @SET_C_EICHENHALL | Den ersten Käse nach Eichenhall bringen"],
  "ITM_FOOD_ALPINECHEESE ×5; Rezept RCP_043", "Handelsweg Eichenhall–Kharsholm offen (Händler-Sortimente +2 Waren)",
  solution="Ossians Vertrag vorlegen (Kontor-Weg) · den betrügerischen Händler zum Klan bringen (nur wenn in SQ_011 mit ihm gesprochen) · dem Klan einen eigenen Schwur anbieten (dritte Lösung, Klan-Bark).")
Q("SQ_030", "Die Tür ohne Griff", "NPC_R02_YRSA|Ahnenstein-Tutorin Yrsa", "SET_C_KHARSHOLM", 4, 35,
  "Nach W4 kennt der Wärter Wendelins Wort von den „Türen, die nur von außen aufgehen“. Yrsa zeigt ihm eine Tür im Erzgrat, die die Klans seit Jahrhunderten bewachen. Mit dem Akkord von Kharsholm öffnet sie sich – dahinter liegt kein Schatz, sondern ein Raum zum Zuhören.",
  ["OBJ_TALK NPC_R02_YRSA 1 @SET_C_KHARSHOLM | Yrsa am Ahnenstein",
   "OBJ_GOTO R02_Z04 1 @R02_Z04 | Zur Tür im Erzgrat",
   "OBJ_PUZZLE PZ_SQ030_DOOR 1 @R02_Z04 | Den Akkord an der Tür anschlagen",
   "OBJ_INVESTIGATE - 3 @R02_Z04 | Den Raum dahinter untersuchen"],
  "Wendelin-Tagebuch (Sammelseite); ITM_LURE_TUNINGFORK", "Hörraum im Erzgrat (Rückkehrort, Resonanzsinn +10 m dort)",
  truth=4)
Q("SQ_031", "Das Gewicht der Bücher", "NPC_R02_TOVA|Tova (Erzkontor)", "SET_C_KHARSHOLM", 3, 30,
  "Im Erzkontor stimmen die Erzmengen nicht. Tova fürchtet, ein Vorarbeiter zweige ab. Der Wärter findet heraus, dass die Waage falsch wiegt – ein Ponderath hat sich darunter eingenistet und macht alles schwerer.",
  ["OBJ_TALK NPC_R02_TOVA 1 @SET_C_KHARSHOLM | Tova und die Bücher",
   "OBJ_INVESTIGATE - 3 @SET_C_KHARSHOLM | Waage, Lager und Bücher prüfen",
   "OBJ_OBSERVE ECHO_039 1 @SET_C_KHARSHOLM | Das Ponderath unter der Waage beobachten",
   "OBJ_CHOICE DLG_SQ_031_01 1 @SET_C_KHARSHOLM | Was wird aus dem Ponderath?"],
  "ITM_HELD_ROOTCHARM; Kodex-Beobachtung Ponderath", "Vorarbeiter entlastet (Bark); Ponderath als „Kontorgewicht“ oder im Grollschlund",
  var="Time=Night", solution="Umsiedeln · binden · die Waage verlegen und das Ponderath als Kontor-Maskottchen behalten (Tova lacht).")
Q("SQ_032", "Die Linn-Quelle", "NPC_BRANDA|Bergführerin Branda", "SET_O_GROLLHORNBIWAK", 3, 30,
  "Die Linn entspringt im Kharsgrat und fließt bis Lindwiesen. Seit Wochen ist ihr Wasser trüb. Branda vermutet einen Erdrutsch. Der Wärter findet eine Höhle, in der Rivetkins Metall aus dem Fels lösen – und eine alte Glyphe, die vor genau diesem Ort warnt.",
  ["OBJ_GOTO R02_Z04 1 @R02_Z04 | Zur Linn-Quelle",
   "OBJ_INVESTIGATE - 3 @R02_Z04 | Den Ursprung der Trübung finden",
   "OBJ_OBSERVE ECHO_031 1 @R02_Z04 | Die Rivetkins in der Höhle beobachten",
   "OBJ_PUZZLE PZ_SQ032_GLYPH 1 @R02_Z04 | Die Warnglyphe deuten"],
  "ITM_MAT_KHARSIRON ×3; Klangfragment (TruthLevel 0)", "Linn klärt sich nach 2 Spieltagen; Mühlbach in Lindwiesen sichtbar klarer",
  var="Weather=Rain")
Q("SQ_033", "Verschüttet", "NPC_R02_TOVA|Tova (Erzkontor)", "SET_C_KHARSHOLM", 4, 40,
  "Ein Stollen der Erzgrat-Minen ist eingestürzt; drei Bergleute und ihre Ferrows sitzen fest. Der Klan will graben, das Kontor will die Kosten nicht tragen. Der Wärter rettet zuerst – und verhandelt danach.",
  ["OBJ_GOTO SET_O_ERZGRATHUETTE 1 @SET_O_ERZGRATHUETTE | Zur Erzgrat-Hütte",
   "OBJ_INVESTIGATE - 3 @R02_Z04 | Den Stollen mit Resonanzsinn abhören",
   "OBJ_TRAVERSE Mount.Climb 1 @R02_Z04 | Über den Lüftungsschacht hinab",
   "OBJ_ESCORT NPC_ULF_BRAKK 1 @R02_Z04 | Ulf Brakk und die Eingeschlossenen hinausführen",
   "OBJ_CHOICE DLG_SQ_033_01 1 @SET_C_KHARSHOLM | Wer zahlt die Stützbalken?"],
  "ITM_GEAR_TOOL_2; ITM_CON_STAMINA ×3", "Stollen mit neuen Balken (Data Layer); Bergleute-Barks",
  solution="Kontor zahlt (Tova setzt es durch) · Klan zahlt (Ehre) · beide teilen und die Ferrows erhalten Ruhetage (dritte Lösung).")
Q("SQ_034", "Ein Hammer für Hralda", "NPC_R02_HRALDA_SMITH|Grollschmied Hraldur", "SET_C_KHARSHOLM", 2, 25,
  "Der Grollschmied hat für Hralda Brakk – seine Cousine – einen Hammer geschmiedet, den sie nie abgeholt hat. „Sie trägt keine Waffen mehr, seit Eichenhall.“ Er bittet den Wärter, ihr den Hammer zu bringen und zu fragen, warum.",
  ["OBJ_TALK NPC_R02_HRALDA_SMITH 1 @SET_C_KHARSHOLM | Der Grollschmied",
   "OBJ_DELIVER ITM_KEY_HRALDAHAMMER 1 @SET_C_EICHENHALL | Den Hammer zu Hralda bringen",
   "OBJ_CHOICE DLG_SQ_034_01 1 @SET_C_EICHENHALL | Hralda fragen – oder nicht"],
  "Kodex-Fragment „Hraldas Hammer“; Hain-Dekor ITM_DECO_ANVIL", "Hralda hängt den Hammer in die Wildwacht-Kammer; Gespräch im Lager von K45 MQ_A2_08 erhält eine Zeile")
Q("SQ_035", "Die zweite Waage", "NPC_R02_TOVA|Tova (Erzkontor)", "SET_C_KHARSHOLM", 4, 35,
  "Tova hat einen Vertrag mit Saltrand in Aussicht: Kharsk-Eisen für Schiffsbeschläge. Doch der Klanrat verlangt, dass das Eisen gesungen, nicht nur gewogen wird – ein altes Ritual, bei dem ein Echo das Metall prüft. Ein Forgoth soll singen, aber er singt nicht für Fremde.",
  ["OBJ_TALK NPC_R02_GERD 1 @SET_C_KHARSHOLM | Der Klanrat stellt die Bedingung",
   "OBJ_OBSERVE ECHO_042 2 @R02_Z04 | Den Forgoth bei der Arbeit beobachten",
   "OBJ_CHOICE DLG_SQ_035_01 1 @R02_Z04 | Den Forgoth um den Gesang bitten",
   "OBJ_BATTLE NPC_KLANPRUEFER_ASKE 1 @SET_C_KHARSHOLM | Probe gegen den Klanprüfer (Metall-Regel)"],
  "ITM_HELD_TONE_METAL; Rezept RCP_051", "Vertrag geschlossen; Kharsk-Eisen in Saltrand-Händlern (K50)",
  var="Time=Night")
Q("SQ_036", "Die Schuld der Lastzüge", "NPC_R02_GERD|Gerd (Halle der Klans)", "SET_C_KHARSHOLM", 3, 30,
  "Nach Akt III will Gerd die Klanchronik um die Wahrheit über die Siegelkriege ergänzen – auch um die Rolle der Kharsk-Klans, die Echos als Lastträger in den Krieg schickten. Der Wärter sammelt Erinnerungen der Ältesten und eines alten Cragar, der dabei war.",
  ["OBJ_TALK NPC_R02_GERD 1 @SET_C_KHARSHOLM | Gerds Vorhaben",
   "OBJ_TALK NPC_AELTESTE_INGRID 1 @SET_V_BRAKKFELS | Die Älteste Ingrid",
   "OBJ_OBSERVE ECHO_034 1 @R02_Z01 | Den alten Cragar mit den Kriegsnarben beobachten",
   "OBJ_CHOICE DLG_SQ_036_01 1 @SET_C_KHARSHOLM | Was in die Chronik kommt"],
  "Lore „Klanchronik, Siegelkriege“; ITM_LURE_BELLCHIME", "Neue Tafel in der Halle der Klans; Barks über „die schweren Jahre“",
  truth=0)
Q("SQ_037", "Pass der Gratkins", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_PASSWACHTNORD", 3, 30,
  "Die Gratkin-Wanderung erreicht den Nordpass – und stockt. Ein Kraggoth hat sich auf die enge Stelle gelegt und lässt niemanden vorbei. Jorn will den Pass sprengen. Der Wärter findet heraus, was der Kraggoth bewacht.",
  ["OBJ_TALK NPC_PASSWART_JORN 1 @SET_O_PASSWACHTNORD | Jorn und der blockierte Pass",
   "OBJ_OBSERVE ECHO_035 2 @R02_Z01 | Den Kraggoth beobachten",
   "OBJ_INVESTIGATE - 2 @R02_Z01 | Die Felsspalte hinter ihm untersuchen",
   "OBJ_CHOICE DLG_SQ_037_01 1 @R02_Z01 | Einen Weg für Gratkins und Kraggoth finden"],
  "ITM_TRAP_NET; Kodex-Beobachtung Kraggoth (Wächter)", "Gratkins passieren; Kraggoth bleibt als Passwächter (Bark)",
  var="Time=Day", solution="Kampf (Kraggoth erschöpft, weicht) · Sprengung verhindern und Ausweichpfad bauen · Kraggoth' Gelege mit Brokkar-Hilfe umbetten (dritte Lösung).")
Q("SQ_038", "Kristalle, die nachts wachsen", "NPC_LEHRLING_MIKKEL|Akademie-Lehrling Mikkel", "SET_O_ERZGRATHUETTE", 3, 30,
  "Mikkel behauptet, dass Quarlings nachts Kristalle wachsen lassen, indem sie singen. Niemand glaubt einem Lehrling. Der Wärter beobachtet drei Nächte lang – und findet etwas Seltsameres: Die Kristalle wachsen nur, wenn ein Resonix in der Nähe antwortet.",
  ["OBJ_TALK NPC_LEHRLING_MIKKEL 1 @SET_O_ERZGRATHUETTE | Mikkels Theorie",
   "OBJ_OBSERVE ECHO_052 2 @R02_Z04 | Quarlings nachts beobachten",
   "OBJ_OBSERVE ECHO_057 1 @R02_Z04 | Das antwortende Resonix finden",
   "OBJ_PHOTO ECHO_053 1 @R02_Z04 | Einen Quarcoil im Kristallgesang fotografieren"],
  "ITM_KS_028; ITM_MAT_QUARTZSHARD ×5", "Mikkels Aufsatz in der Akademie (Bark „der Lehrling hatte recht“)",
  var="Time=Night")
Q("SQ_039", "Lawinenhunde", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_PASSWACHTNORD", 4, 35,
  "Die Wildwacht will Rimlets zu Lawinensuchern ausbilden – sie spüren Wärme unter Schnee. Jorn bittet den Wärter, drei Rimlets zu gewinnen, die das freiwillig tun. Am Ende steht eine echte Suche.",
  ["OBJ_OBSERVE ECHO_050 2 @R02_Z05 | Rimlets beim Spiel im Schnee beobachten",
   "OBJ_BOND ECHO_050 1 @R02_Z05 | Ein Rimlet binden (oder einen Rimlet-Begleiter aus dem Chor einsetzen)",
   "OBJ_CONDITION Weather=Snow 1 @R02_Z05 | Auf Schnee warten",
   "OBJ_INVESTIGATE - 3 @R02_Z05 | Mit den Rimlets drei Verschüttete (Übungspuppen) finden"],
  "ITM_SEAL_TUNED ×2; Wildwacht-Abzeichen (Kosmetik)", "Rimlet-Staffel an der Passwacht (sichtbar); Bark „unsere Schneenasen“",
  var="Weather=Snow")
Q("SQ_040", "Die Stimme unter Kharsholm", "NPC_R02_YRSA|Ahnenstein-Tutorin Yrsa", "SET_C_KHARSHOLM", 3, 30,
  "Yrsa hört seit dem Akkord ein Brummen unter der Stadt. Sie fragt, ob Orh'gruun träumt. Der Wärter lauscht an drei Ahnenfelsen und zeichnet den Rhythmus auf – er stimmt mit den Gezeiten der schwebenden Felsen überein.",
  ["OBJ_TALK NPC_R02_YRSA 1 @SET_C_KHARSHOLM | Yrsas Frage",
   "OBJ_INVESTIGATE - 3 @R02_Z02 | An drei Ahnenfelsen lauschen",
   "OBJ_OBSERVE ECHO_036 1 @R02_Z01 | Ein Anchrex bei den schwebenden Felsen beobachten",
   "OBJ_TALK NPC_R02_YRSA 1 @SET_C_KHARSHOLM | Yrsa vom Rhythmus erzählen"],
  "Kodex-Eintrag Orh'gruun (Seite 1); ITM_LURE_BELLCHIME", "Yrsa singt den Rhythmus in der Halle (Bark, Musik-Variante)",
  pre="Quest.MQ_A1_03")
Q("SQ_041", "Die Grenze hält", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_PASSWACHTNORD", 6, 50,
  "Die Wanderung ist fast am Ziel, als ein Unwetter die Gratkins am Grollhorn überrascht. Gleichzeitig wartet am Pass ein Händler mit Netzen, der weiß, dass verängstigte Gratkins leicht zu fangen sind. Der Wärter muss die Herde durch den Sturm führen und den Fänger aufhalten – ohne Gewalt gegen Menschen.",
  ["OBJ_CONDITION Weather=Thunderstorm 1 @R02_Z05 | Das Unwetter bricht los",
   "OBJ_ESCORT NPC_PASSWART_JORN 1 @R02_Z05 | Mit Jorn die Herde zum Pass treiben",
   "OBJ_BATTLE NPC_FAENGER_RASK 1 @R02_Z01 | Die Echos des Fängers erschöpfen",
   "OBJ_CHOICE DLG_SQ_041_01 1 @SET_O_PASSWACHTNORD | Was mit Rask geschieht",
   "OBJ_OBSERVE ECHO_045 1 @R01_Z02 | Die Gratrex-Leitkuh in den Auen beobachten"],
  "ITM_GEAR_CLOAK_2; Hain-Dekor ITM_DECO_GRATKINBANNER", "Gratkin-Wanderung jährlich (Weltereignis WE_GRATKIN_MIGRATION); Rask arbeitet für die Wildwacht oder ist verbannt",
  var="Weather=Thunderstorm", solution="Rask übergeben (Gesetz) · laufen lassen (Gnade) · Rask als Netzflicker für die Wildwacht anwerben (dritte Lösung).")
Q("SQ_042", "Die Probe der Ahnen", "NPC_TORVIK|Torvik Hrall", "SET_C_KHARSHOLM", 5, 40,
  "Im Nachhall lädt Torvik zur Ahnenprobe: drei Kämpfe auf den Kettenbrücken bei Wind, jede Brücke mit verschobenen Plattformen. Nur wer seinen Chor kennt, besteht – Torvik will sehen, ob der Wärter ohne seine alte Gabe (oder mit ihr) noch zuhört.",
  ["OBJ_TALK NPC_TORVIK 1 @SET_C_KHARSHOLM | Torviks Einladung",
   "OBJ_BATTLE NPC_KLANKRIEGER_1 1 @R02_Z02 | Erste Brücke",
   "OBJ_BATTLE NPC_KLANKRIEGER_2 1 @R02_Z02 | Zweite Brücke",
   "OBJ_BATTLE NPC_TORVIK 1 @R02_Z02 | Dritte Brücke gegen Torvik",
   "OBJ_CHOICE DLG_SQ_042_01 1 @SET_C_KHARSHOLM | Torvik antworten, was sich verändert hat"],
  "ITM_HELD_TONE_GRAVITY; Titel „Brückengänger“", "Torvik-Barks im Nachhall je Ende",
  truth=9)
Q("SQ_043", "Das Horn im Nebel", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_PASSWACHTNORD", 4, 35,
  "Ein Wanderer ist im Nebel am Grollschlund verschwunden. Die Wildwacht hat ein altes Rettungshorn, aber niemand weiß mehr, wie man es bläst – es muss auf einen Ton gestimmt sein, den Gratwyns hören. Der Wärter stimmt das Horn und sucht.",
  ["OBJ_CONDITION Weather=Fog 1 @R02_Z03 | Nebel am Grollschlund",
   "OBJ_PUZZLE PZ_SQ043_HORN 1 @SET_O_PASSWACHTNORD | Das Horn auf den Gratwyn-Ton stimmen",
   "OBJ_OBSERVE ECHO_044 1 @R02_Z03 | Den Gratwyns zum Verirrten folgen",
   "OBJ_ESCORT NPC_WANDERER_PIET 1 @SET_O_PASSWACHTNORD | Den Wanderer zurückbringen"],
  "ITM_LURE_WHISTLE; ITM_CON_HEAL_ALL", "Rettungshorn hängt wieder an der Passwacht (spielbar bei Nebel)",
  var="Weather=Fog")
Q("SQ_044", "Die Lawine von Brakkfels", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_PASSWACHTNORD", 5, 40,
  "In Akt II fällt eine Lawine auf die Straße nach Brakkfels; ein Fuhrwerk und zwei Cragars liegen darunter. Die Rimlet-Staffel aus SQ_039 kommt zum ersten echten Einsatz – oder der Wärter sucht mit dem Resonanzsinn allein.",
  ["OBJ_GOTO R02_Z01 1 @R02_Z01 | Zur Lawine",
   "OBJ_INVESTIGATE - 4 @R02_Z01 | Verschüttete mit Rimlets oder Resonanzsinn finden",
   "OBJ_TRAVERSE Mount.Dig 1 @R02_Z01 | Einen Gang zum Fuhrwerk graben (Grabreiten, falls vorhanden; sonst Werkzeug)",
   "OBJ_ESCORT NPC_KUTSCHERIN_ALMA 1 @SET_V_BRAKKFELS | Die Kutscherin nach Brakkfels bringen"],
  "ITM_GEAR_BOOTS_2; ITM_CON_WARM ×3", "Neue Lawinengalerie an der Straße (Data Layer)",
  var="Weather=Snow", pre="Act>=Akt II")
Q("SQ_045", "Nacht der Ahnenfeuer", "NPC_R02_GERD|Gerd (Halle der Klans)", "SET_C_KHARSHOLM", 4, 35,
  "Einmal im Jahr entzünden die Klans Feuer auf allen Ahnenfelsen. Dieses Jahr fehlt der Klan von Hrallsted, weil sein Feuerträger krank ist. Gerd bittet den Wärter, das Feuer mit einem Emblit über den Erzgrat zu tragen – Emblits tragen Glut nur bei Mittagssonne.",
  ["OBJ_TALK NPC_R02_GERD 1 @SET_C_KHARSHOLM | Gerd bittet um Hilfe",
   "OBJ_OBSERVE ECHO_054 1 @R02_Z04 | Ein Emblit zur Mittagszeit finden",
   "OBJ_ESCORT NPC_FEUERTRAEGER_KNUT 1 @SET_V_HRALLSTED | Mit dem Emblit das Feuer nach Hrallsted tragen",
   "OBJ_CHOICE DLG_SQ_045_01 1 @SET_V_HRALLSTED | Das Feuer mit dem Klanspruch entzünden"],
  "ITM_EVO_EMBER; Hain-Dekor ITM_DECO_ANCESTORFIRE", "Ahnenfeuer-Nacht als jährliches Weltereignis; Hrallsted-Klan dankt (Bark)",
  var="Time=Day")
Q("SQ_046", "Über die Kettenbrücken", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_C_KHARSHOLM", 6, 50,
  "Ennis' letzte Fahrt in dieser Kette: zwölf befreite Echos, darunter das Brokkar aus Moosgrund, sollen über die Kettenbrücken in ein verborgenes Tal. Die Kontor-Wache am Erzkontor zählt jeden Wagen. Der Wärter muss wählen, wem er vertraut: Tova, den Klans oder der Nacht.",
  ["OBJ_TALK NPC_ENNIS 1 @SET_C_KHARSHOLM | Ennis' Plan",
   "OBJ_CHOICE DLG_SQ_046_01 1 @SET_C_KHARSHOLM | Weg wählen: Kontor, Klan oder Nacht",
   "OBJ_ESCORT NPC_ENNIS 1 @R02_Z02 | Über die Kettenbrücken",
   "OBJ_FLEE ROUTE_SQ046 1 @R02_Z03 | Angekündigter Hinterhalt eines Fängers – durch den Grollschlund ausweichen",
   "OBJ_OBSERVE ECHO_005 1 @R02_Z03 | Das Brokkar im neuen Tal beobachten"],
  "ITM_HELD_SWIFTFEATHER; Zellen-Schnellreisepunkt Grollschlund (K47 F04 Rang 3)", "Verborgenes Tal der Freien Stimmen (Rückkehrort mit freien Echos)",
  var="Time=Night", solution="Tova bitten (sie schaut weg – Kontor-Bark) · Klanrat bitten (Gerd gewährt Durchgang) · nachts ohne Hilfe (Hinterhalt schwerer).")

# ───────────────────────────── R03 Morvenmoor ─────────────────────────────
Q("SQ_047", "Moorformen", "NPC_GELEHRTE_OONA|Gelehrte Oona (Akademie)", "SET_C_MORVENFURT", 3, 35,
  "Oona setzt Vaels Lücken im Moor fort: Mirels in Duvreth tragen ein Klangmal, das Vael nur aus Saltrand kannte. Sie braucht Fotos bei Nebel – nur dann leuchten die Male – und Beobachtungen, ob sich die Mirels mit Brinlets paaren.",
  ["OBJ_TALK NPC_GELEHRTE_OONA 1 @SET_C_MORVENFURT | Oona in der Laternengasse",
   "OBJ_CONDITION Weather=Fog 1 @R03_Z03 | Nebel in Duvreth",
   "OBJ_PHOTO ECHO_060 2 @R03_Z03 | Zwei Mirels mit leuchtendem Klangmal fotografieren",
   "OBJ_OBSERVE ECHO_076 1 @R03_Z01 | Brinlets im Ried beobachten (Paarungsverhalten)"],
  "ITM_KS_031; Kodex-Fragment „Vaels Lücken II“", "Kodex Mirel: „Regionalform Morvenmoor“",
  var="Weather=Fog")
Q("SQ_048", "Der Humbog-Chor", "NPC_R03_NIALLA|Nialla (Laternensteg)", "SET_C_MORVENFURT", 2, 25,
  "Der Nachtmarkt von Morvenfurt beginnt traditionell mit dem ersten Humbog-Ruf. Seit Wochen ruft keiner. Die Händler warten, die Laternen bleiben dunkel. Nialla bittet den Wärter, die Humbogs zu finden – sie sind in eine neue Senke gezogen, weil der alte Teich verlandet.",
  ["OBJ_TALK NPC_R03_NIALLA 1 @SET_C_MORVENFURT | Nialla am dunklen Laternensteg",
   "OBJ_INVESTIGATE - 3 @R03_Z02 | Den alten Teich untersuchen",
   "OBJ_OBSERVE ECHO_083 1 @R03_Z05 | Die Humbogs in der Senke beobachten",
   "OBJ_CHOICE DLG_SQ_048_01 1 @SET_C_MORVENFURT | Markt verlegen oder Teich ausbaggern?"],
  "ITM_LURE_LANTERN; Hain-Dekor ITM_DECO_MARKETLANTERN", "Nachtmarkt öffnet wieder; Händlerangebot nachts +2 Waren",
  var="Time=Night", solution="Teich ausbaggern (Kontor zahlt) · Markt an die Senke verlegen (neuer Markt-Ort) · Humbog-Rufe mit einem Ruf-Horn ersetzen (Nialla lehnt traurig ab – dritte Lösung nur als Gesprächsoption).")
Q("SQ_049", "Irrlichtjagd", "NPC_GELEHRTE_OONA|Gelehrte Oona (Akademie)", "SET_C_MORVENFURT", 4, 35,
  "Seit Generationen jagen Moorleute bei Nacht dem „Irrel-Weißling“ hinterher – einer Form, die Vael nie bestätigte. Oona will die Jagd beenden, mit einer Antwort. Der Wärter findet heraus, dass das „Weißling“ ein Irrel ist, das sich in einem Kalkbecken weiß gefärbt hat – oder doch nicht?",
  ["OBJ_GOTO R03_Z04 1 @R03_Z04 | In den Nebelwald Corrach",
   "OBJ_OBSERVE ECHO_066 2 @R03_Z04 | Irrels bei Nacht beobachten",
   "OBJ_INVESTIGATE - 3 @R03_Z04 | Das Kalkbecken untersuchen",
   "OBJ_CHOICE DLG_SQ_049_01 1 @SET_C_MORVENFURT | Oona das Ergebnis vortragen"],
  "ITM_EVO_MISTVEIL; Kodex-Fragment „Vaels Lücken III“", "Kodex-Anmerkung „Weißling = Kalkfärbung“ (oder offene Frage, je Antwort)",
  var="Time=Night")
Q("SQ_050", "Wenn das Moor steigt", "NPC_R03_FINN|Bootsbauer Finn", "SET_C_MORVENFURT", 4, 30,
  "Bei Regen steigt das Morvenmoor um fast einen halben Meter. Dann treiben Undlinge aus ihren Senken in die Kanäle der Stadt und verirren sich. Finn baut Boote; er braucht jemanden, der die Undlinge zurückführt, bevor die Fischer sie für Schädlinge halten.",
  ["OBJ_CONDITION Weather=Rain 1 @R03_Z02 | Regen über Morvenfurt",
   "OBJ_OBSERVE ECHO_062 2 @R03_Z02 | Verirrte Undlinge in den Kanälen finden",
   "OBJ_TRAVERSE Mount.Swim 1 @R03_Z02 | Mit einem Schwimm-Echo durch die Kanäle",
   "OBJ_ESCORT NPC_R03_FINN 1 @R03_Z03 | Die Undlinge mit Finns Boot zur Senke leiten"],
  "ITM_GEAR_MASK_2; ITM_FOOD_SMOKEDFISH ×3", "Kanal-Sperrgitter mit Durchlass (Data Layer); Fischer-Barks über „Finns Undlinge“",
  var="Weather=Rain")
Q("SQ_051", "Eine Nacht im Moor", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_RIEDWACHT", 6, 55,
  "Jorn hat einen Auftrag angenommen, den er bereut: Ein Kind aus Fennhaven ist ins Moor gelaufen, einem Irraune nach. Die Bergretter sind fremd im Moor. Der Wärter führt die Suche durch eine Nebelnacht – und findet das Kind bei einem Echo, das es beschützt hat.",
  ["OBJ_TALK NPC_PASSWART_JORN 1 @SET_O_RIEDWACHT | Jorn an der Riedwacht",
   "OBJ_CONDITION Time=Night 1 @R03_Z01 | Nacht über dem Ried",
   "OBJ_INVESTIGATE - 4 @R03_Z01 | Spuren im Nebel verfolgen",
   "OBJ_OBSERVE ECHO_067 1 @R03_Z04 | Das Irraune beobachten, das das Kind wärmt",
   "OBJ_ESCORT NPC_KIND_TAMSIN 1 @SET_V_FENNHAVEN | Tamsin nach Fennhaven bringen"],
  "ITM_GEAR_LANTERN_2; Titel „Moorläufer“", "Tamsin und das Irraune besuchen sich (Bark); Riedwacht erhält Nebelglocken",
  var="Time=Night & Weather=Fog")
Q("SQ_052", "Der Stein mit zwei Seiten", "NPC_R03_CORRACH|Moorweise Corrach", "SET_C_MORVENFURT", 4, 35,
  "Nach W6 bringt Corrach dem Wärter einen Stillstein, den ihr Sohn im Moor gefunden hat. Auf der Rückseite: eine Akademie-Prägung. Corrach will wissen, wie lange das schon so geht. Die Spur führt zu einer verlassenen Ordenskapelle bei Duvreth.",
  ["OBJ_TALK NPC_R03_CORRACH 1 @SET_C_MORVENFURT | Corrach zeigt den Stein",
   "OBJ_GOTO R03_Z03 1 @R03_Z03 | Zur Kapelle bei Duvreth",
   "OBJ_INVESTIGATE - 3 @R03_Z03 | Lieferlisten in der Kapelle finden",
   "OBJ_CHOICE DLG_SQ_052_01 1 @SET_C_MORVENFURT | Corrach die Wahrheit erzählen"],
  "Lore „Lieferlisten 991–1003“ (TruthLevel 6); ITM_EMAT_STILLSHARD", "Corrach warnt die Moorleute vor Ordenssteinen (Barks)",
  truth=6, pre="Quest.MQ_A2_07")
Q("SQ_053", "Graue Ränder", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_RIEDWACHT", 4, 40,
  "Rang 4 der Wildwacht: Jorn wird an die Riedwacht versetzt, um die Nachwirkungen der geheilten Zone zu beobachten. Am Rand wachsen Pflanzen grau nach, und Blossis meiden die Stelle. Der Wärter findet einen vergessenen Stillstein-Splitter im Schlamm.",
  ["OBJ_GOTO R03_Z05 1 @R03_Z05 | Zur Versunkenen Senke",
   "OBJ_OBSERVE ECHO_069 2 @R03_Z05 | Das Ausweichverhalten der Blossis beobachten",
   "OBJ_HEALZONE ZONE_SQ053 2 @R03_Z05 | Zwei graue Nachwirkungs-Kreise heilen",
   "OBJ_INVESTIGATE - 1 @R03_Z05 | Den Splitter im Schlamm finden"],
  "ITM_EMAT_STILLSHARD; ITM_GEAR_RESONATOR_2", "Graue Ränder verschwinden; Blossis kehren zurück",
  var="Weather=Rain")
Q("SQ_054", "Das Turmgeheimnis der Fährmeisterin", "NPC_AILSA|Fährmeisterin Ailsa Duvreth", "SET_C_MORVENFURT", 3, 30,
  "Bei Ebbe im Morve-Delta hört man eine Glocke unter Wasser – Ailsas Großvater, auch er Fährmeister, nannte sie „die Glocke des versunkenen Turms“. Seit MQ_A1_08 läutet sie öfter. Der Wärter taucht und findet eine Glocke mit dorunischen Zeichen, aber nicht vom Turm.",
  ["OBJ_TALK NPC_AILSA 1 @SET_C_MORVENFURT | Ailsa an der Fähre",
   "OBJ_TRAVERSE Mount.Swim 1 @R03_Z05 | Zum Delta schwimmen",
   "OBJ_INVESTIGATE - 3 @R03_Z05 | Die Glocke und ihre Inschrift untersuchen",
   "OBJ_PUZZLE PZ_SQ054_BELL 1 @R03_Z05 | Den Glockenton mit dem Resonator spiegeln"],
  "ITM_LURE_BELLCHIME; Klangfragment (TruthLevel 3)", "Die Glocke läutet bei Ebbe hörbar über die Stadt (Ambient)",
  truth=3, pre="Quest.MQ_A1_08")
Q("SQ_055", "Schulden in der Unterstadt", "NPC_R03_SHADE|Der Schatten", "SET_C_MORVENFURT", 3, 30,
  "Der Schatten – Rüstmeister der Freien Stimmen – hat ein Problem: Ein Mitglied schuldet einem Hehler Geld und hat dafür sein Echo verpfändet. Die Freien Stimmen kaufen keine Echos frei, aus Prinzip. Der Wärter soll eine andere Lösung finden.",
  ["OBJ_TALK NPC_R03_SHADE 1 @SET_C_MORVENFURT | Der Schatten im Hinterzimmer",
   "OBJ_TALK NPC_SCHULDNER_ROAN 1 @SET_C_MORVENFURT | Roan erzählen lassen",
   "OBJ_INVESTIGATE - 2 @SET_C_MORVENFURT | Den Hehler und sein Lager finden",
   "OBJ_CHOICE DLG_SQ_055_01 1 @SET_C_MORVENFURT | Lösung wählen"],
  "ITM_CON_SENSE ×2; Zugang Schwarzmarkt (Vorbereitung)", "Roan hat sein Echo zurück; Hehler-Barks",
  var="Time=Night", solution="Schuld bezahlen (Prinzip gebrochen, Schatten seufzt) · Hehler beim Stadtrat melden (Echo kommt frei, Roan verliert Ansehen) · Roans Schuld durch Arbeit für Finn tilgen (dritte Lösung).")
Q("SQ_056", "Fennhavens Brücke", "NPC_BRUECKENWART_ELWYN|Brückenwart Elwyn", "SET_V_FENNHAVEN", 2, 25,
  "Die Stelzenbrücke von Fennhaven fault. Neue Pfähle aus Moorweide würden halten, aber Weiduna wohnen in den Weiden und verlassen sie nicht, solange dort gesungen wird – und die Dorfkinder singen immer dort.",
  ["OBJ_TALK NPC_BRUECKENWART_ELWYN 1 @SET_V_FENNHAVEN | Elwyns Brücke",
   "OBJ_OBSERVE ECHO_081 1 @R03_Z01 | Die Weiduna in den Weiden beobachten",
   "OBJ_COLLECT ITM_MAT_MOORWILLOW 6 @R03_Z01 | Weidenholz aus verlassenen Weiden sammeln",
   "OBJ_CHOICE DLG_SQ_056_01 1 @SET_V_FENNHAVEN | Die Kinder an einen neuen Singplatz führen"],
  "Rezept RCP_052; ITM_MAT_MOORWILLOW ×4", "Neue Brücke (Data Layer); Kinderchor an neuem Ort (Ambient)")
Q("SQ_057", "Die Liederschuld", "NPC_R03_SHADE|Der Schatten", "SET_C_MORVENFURT", 4, 35,
  "In der Unterstadt bezahlt man mit Liedern: Wer einen Gefallen erhält, singt dafür. Ein Lied wurde gestohlen – ein Händler aus der Oberstadt verkauft es als eigenes. Die Unterstadt will es zurück, ohne aufzufallen.",
  ["OBJ_TALK NPC_R03_SHADE 1 @SET_C_MORVENFURT | Das gestohlene Lied",
   "OBJ_INVESTIGATE - 3 @SET_C_MORVENFURT | Den Händler in der Oberstadt beobachten",
   "OBJ_OBSERVE ECHO_083 1 @SET_C_MORVENFURT | Den Humbog hören, der das Lied „bezeugt“",
   "OBJ_CHOICE DLG_SQ_057_01 1 @SET_C_MORVENFURT | Das Lied zurückholen"],
  "ITM_KS_035; Hain-Dekor ITM_DECO_SONGSHEET", "Lied wird in der Unterstadt gesungen (Musik-Variante)",
  var="Time=Night", solution="Beweis öffentlich machen · Händler unter vier Augen stellen · dem Händler anbieten, das Lied gemeinsam zu singen (dritte Lösung, er wird Gast der Unterstadt).")
Q("SQ_058", "Die Ouroveth-Legende", "NPC_R03_CORRACH|Moorweise Corrach", "SET_C_MORVENFURT", 3, 30,
  "In Akt III erzählt Corrach von Ouroveth, dem Mythischen, das „im Kreis der Generationen“ lebt. Wer züchtet, sagt sie, hört es irgendwann. Der Wärter sammelt drei Moorlieder über Ouroveth – der erste Schritt zu einer Spur, die erst die Zucht-Meisterschaft vollendet (K62).",
  ["OBJ_TALK NPC_R03_CORRACH 1 @SET_C_MORVENFURT | Corrachs Erzählung",
   "OBJ_INVESTIGATE - 3 @R03_Z03 | Drei Moorlieder bei Ältesten in Duvreth hören",
   "OBJ_OBSERVE ECHO_071 1 @R03_Z03 | Ein Blossmire beim Laichen beobachten"],
  "Kodex-Eintrag Ouroveth (Gerücht); ITM_BREED_KEIMWAERME", "Spur „Ouroveth“ im Kodex aktiv (K62)",
  truth=0)
Q("SQ_059", "Ein Verrat, der keiner war", "NPC_R03_SHADE|Der Schatten", "SET_C_MORVENFURT", 5, 45,
  "Eine Razzia der Stadtwache trifft ein Versteck der Unterstadt. Alle glauben, Roan habe sie verraten. Der Wärter findet heraus, dass ein Irrlit die Wachen zum Versteck geführt hat – angelockt von den Laternen, die die Freien Stimmen selbst aufgehängt hatten.",
  ["OBJ_TALK NPC_R03_SHADE 1 @SET_C_MORVENFURT | Die Unterstadt ist in Aufruhr",
   "OBJ_INVESTIGATE - 4 @SET_C_MORVENFURT | Das geräumte Versteck untersuchen",
   "OBJ_OBSERVE ECHO_065 1 @R03_Z02 | Irrlits und Laternen beobachten",
   "OBJ_CHOICE DLG_SQ_059_01 1 @SET_C_MORVENFURT | Vor der Versammlung sprechen"],
  "ITM_GEAR_LANTERN_2; ITM_TRAP_SHADE", "Roan bleibt in der Unterstadt; Laternen werden abgedunkelt (Ambient)",
  var="Time=Night")
Q("SQ_060", "Torf und Glut", "NPC_TORFSTECHER_BRAN|Torfstecher Bran", "SET_V_DUVRETH", 3, 30,
  "Bran sticht Torf in Duvreth. Ein Torfgor hat sich dort eingegraben, und wo es schläft, glüht der Torf – Cindrel-Eier, eingeschleppt von Händlern aus Verdanthain. Ein Moorbrand droht.",
  ["OBJ_TALK NPC_TORFSTECHER_BRAN 1 @SET_V_DUVRETH | Bran und der glühende Torf",
   "OBJ_OBSERVE ECHO_084 1 @R03_Z03 | Das Torfgor beobachten",
   "OBJ_INVESTIGATE - 3 @R03_Z03 | Glutnester finden",
   "OBJ_CHOICE DLG_SQ_060_01 1 @R03_Z03 | Eier umsiedeln oder Feld fluten?"],
  "ITM_MAT_PEATCOAL ×5; ITM_EVO_EMBER", "Kein Moorbrand; Cindrels leben im Uralthain (R01) oder im Moor",
  solution="Eier nach Verdanthain zurückbringen (Wildwacht-Bark) · Feld fluten (Torfgor zieht um) · Torfgor als Glutwächter belassen und Gräben ziehen (dritte Lösung).")
Q("SQ_061", "Lieder für Tavesh", "NPC_TAVESH|Tavesh Amaru", "SET_C_MORVENFURT", 6, 50,
  "Tavesh will die Unterstadt aus dem Verborgenen holen – ein Fest am Laternensteg, offen für alle, mit Liedern, die die Unterstadt sonst nur unter sich singt. Die Stadtwache ist nervös, der Rat skeptisch. Der Wärter organisiert, vermittelt und hält am Ende eine Rede (drei Haltungen).",
  ["OBJ_TALK NPC_TAVESH 1 @SET_C_MORVENFURT | Tavesh' Idee",
   "OBJ_TALK NPC_STADTRAETIN_MAIRE 1 @SET_C_MORVENFURT | Ratsherrin Maire überzeugen",
   "OBJ_DELIVER ITM_LURE_LANTERN 3 @SET_C_MORVENFURT | Laternen für den Steg bringen",
   "OBJ_CHOICE DLG_SQ_061_01 1 @SET_C_MORVENFURT | Die Rede am Laternensteg",
   "OBJ_REST SET_C_MORVENFURT 1 @SET_C_MORVENFURT | Das Fest feiern"],
  "Titel „Chorfreund“; Hain-Dekor ITM_DECO_UNDERSTREETFLAG", "Unterstadt-Fest als Weltereignis im Nachhall (jeden 20. Spieltag)",
  var="Time=Night")
Q("SQ_062", "Die Probe im Nebel", "NPC_EVHE|Evhe Corrach", "SET_C_MORVENFURT", 5, 30,
  "Evhe, Corrachs Tochter und Arenameisterin, bietet eine Nebelprobe an: Zwei Kämpfe bei so dichtem Nebel, dass die Zeitleiste nur drei Züge zeigt – eine Lektion darin, Gegner zu hören statt zu sehen.",
  ["OBJ_TALK NPC_EVHE 1 @SET_C_MORVENFURT | Evhes Angebot",
   "OBJ_CONDITION Weather=Fog 1 @SET_C_MORVENFURT | Dichter Nebel",
   "OBJ_BATTLE NPC_NEBELPRUEFER_1 1 @SET_C_MORVENFURT | Erster Kampf im Nebel",
   "OBJ_BATTLE NPC_EVHE 1 @SET_C_MORVENFURT | Zweiter Kampf gegen Evhe",
   "OBJ_OBSERVE ECHO_243 1 @SET_C_MORVENFURT | Unter der Arena lauschen (Nhael'vesh)"],
  "ITM_HELD_FOGSCARF; ITM_KS_041", "Evhe-Barks; Nebeltraining in der Arena verfügbar",
  var="Weather=Fog", pre="Akkorde>=4")
Q("SQ_063", "Das erste Netz", "NPC_R03_SHADE|Der Schatten", "SET_C_MORVENFURT", 4, 35,
  "Fischer finden in ihren Reusen immer öfter fremde Netze – feinmaschig, mit Klangperlen beschwert, gemacht für Echos, nicht für Fische. Die Freien Stimmen wollen wissen, wer sie knüpft. Der Wärter folgt den Perlen.",
  ["OBJ_INVESTIGATE - 3 @R03_Z02 | Netze in den Kanälen finden",
   "OBJ_OBSERVE ECHO_063 1 @R03_Z02 | Ein gefangenes Undfin beobachten und befreien",
   "OBJ_INVESTIGATE - 2 @SET_C_MORVENFURT | Den Perlenhändler aufspüren",
   "OBJ_TALK NPC_R03_SHADE 1 @SET_C_MORVENFURT | Dem Schatten berichten"],
  "ITM_MAT_FOGPEARL ×3; ITM_TRAP_POOL", "Netzfunde werden seltener; Spur führt nach Saltrand (SQ_065, K50)")
Q("SQ_064", "Der Moorkönig", "NPC_EVHE|Evhe Corrach", "SET_C_MORVENFURT", 6, 40,
  "Im Nachhall fordert ein alter Moorkönig – Evhes Lehrer, der sich zurückgezogen hatte – jeden heraus, der Nhael'vesh geweckt hat oder schlafen ließ. Sein Kampf läuft bei Nacht in der Versunkenen Senke; Gift und Geist, Nebel und Wasser.",
  ["OBJ_TALK NPC_EVHE 1 @SET_C_MORVENFURT | Evhe kündigt ihren Lehrer an",
   "OBJ_CONDITION Time=Night 1 @R03_Z05 | Nacht in der Senke",
   "OBJ_BATTLE NPC_MOORKOENIG_ORRIN 1 @R03_Z05 | Kampf gegen Orrin",
   "OBJ_CHOICE DLG_SQ_064_01 1 @R03_Z05 | Orrins Frage beantworten"],
  "ITM_HELD_TONE_VENOM; Titel „Moorkönigs Gast“", "Orrin bleibt als Trainer in der Senke (wöchentlicher Rückkampf)",
  var="Time=Night", truth=9)
Q("SQ_065", "Perlen aus Saltrand", "NPC_R03_SHADE|Der Schatten", "SET_C_MORVENFURT", 4, 40,
  "Die Klangperlen der Netze stammen aus Saltrand – aus einer Werkstatt, die auch für das Kontor arbeitet. Bevor der Wärter nach Saltrand reist, sucht er in Morvenfurt den Mittelsmann und findet eine Liste mit Abnehmern.",
  ["OBJ_INVESTIGATE - 3 @SET_C_MORVENFURT | Den Mittelsmann beim Perlenkauf beobachten",
   "OBJ_CHOICE DLG_SQ_065_01 1 @SET_C_MORVENFURT | Den Mittelsmann zur Rede stellen oder beschatten",
   "OBJ_GOTO SET_C_SALTRANDHAFEN 1 @SET_C_SALTRANDHAFEN | Nach Saltrand-Hafen reisen"],
  "Abnehmerliste (Lore); ITM_CON_REPEL ×2", "Kette setzt sich in Saltrand fort (SQ_088, K50)")
Q("SQ_066", "Die Kapelle öffnet sich", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_C_MORVENFURT", 3, 30,
  "In Akt III öffnen die Sereth-treuen Ordensleute ihre Kapelle in Morvenfurt. Schwester Ivra, mit Schiefertafel, lädt den Wärter ein, eine Stunde mit ihnen zu schweigen. Danach schreibt sie: „Wir wussten nicht, wem wir dienten. Hilf uns, es wiedergutzumachen.“",
  ["OBJ_TALK NPC_SCHWESTER_IVRA 1 @SET_C_MORVENFURT | Ivras Tafel",
   "OBJ_REST SET_C_MORVENFURT 1 @SET_C_MORVENFURT | Eine Stunde Stille in der Kapelle",
   "OBJ_INVESTIGATE - 3 @R03_Z03 | Drei alte Stillsteine im Moor finden, die der Orden gesetzt hat",
   "OBJ_CHOICE DLG_SQ_066_01 1 @SET_C_MORVENFURT | Ivra sagen, was mit den Steinen geschehen soll"],
  "ITM_EMAT_STILLSHARD ×2; Kodex-Fragment „Ordensgelübde“", "Kapelle bleibt offen; Ordensleute grüßen schweigend (Gesten-Barks)",
  truth=7, solution="Steine zerstören (Ivra nickt) · der Akademie zur Untersuchung geben · im Moor versenken, wo sie niemandem schaden (Ivra schreibt: „Stille, die niemanden zwingt.“).")
Q("SQ_067", "Was Stille heilt", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_C_MORVENFURT", 4, 40,
  "Ivra bringt den Wärter zu einem Undrath, das seit der Klangpest-ähnlichen Raserei eines Sturms nicht mehr schläft. Der Orden glaubt, nur Stille kann es heilen. Der Wärter versucht beides: ein Lied und eine Stille – und beobachtet, was hilft.",
  ["OBJ_GOTO R03_Z05 1 @R03_Z05 | Zum ruhelosen Undrath",
   "OBJ_OBSERVE ECHO_064 3 @R03_Z05 | Drei Verhaltensmerkmale des Undrath beobachten",
   "OBJ_CHOICE DLG_SQ_067_01 1 @R03_Z05 | Lied oder Stille anbieten",
   "OBJ_OBSERVE ECHO_064 1 @R03_Z05 | Die Wirkung beobachten"],
  "ITM_CON_CLEANSE ×3; Rezept RCP_058", "Das Undrath schläft; Ivras Notiz „Beides heilt – aber nicht dasselbe.“ im Kodex",
  var="Time=Dusk", truth=7)

# ───────────────────────────── R06 Saltrand (Teil 1) ─────────────────────────────
Q("SQ_068", "Die Küste hat eigene Regeln", "NPC_GELEHRTE_OONA|Gelehrte Oona (Akademie)", "SET_C_SALTRANDHAFEN", 5, 50,
  "Oonas Arbeit über Vaels Lücken endet in Saltrand: Marwyns an der Dünenküste haben zwei Klangmal-Muster, je nach Gezeit. Vael hielt sie für zwei Arten. Der Wärter beweist, dass es eine ist – oder dass Vael doch recht hatte. Oona will die Wahrheit, keine Bestätigung.",
  ["OBJ_TALK NPC_GELEHRTE_OONA 1 @SET_C_SALTRANDHAFEN | Oona an der Kaimauer",
   "OBJ_OBSERVE ECHO_086 2 @R06_Z01 | Marwyns bei Flut beobachten",
   "OBJ_OBSERVE ECHO_086 2 @R06_Z01 | Marwyns bei Ebbe beobachten",
   "OBJ_PHOTO ECHO_087 1 @R06_Z03 | Ein Maraune beim Musterwechsel fotografieren",
   "OBJ_CHOICE DLG_SQ_068_01 1 @SET_C_SALTRANDHAFEN | Ergebnis vortragen"],
  "ITM_KS_029; Kodex-Fragment „Vaels Lücken IV“; Akademie-Abzeichen (Kosmetik)", "Oonas Arbeit „Vaels Lücken“ in der Akademie-Bibliothek; Kodex-Korrekturen in drei Arten",
  var="Time=Day")
Q("SQ_069", "Die Möwe von Möwenhuk", "NPC_FISCHERIN_TJARKE|Fischerin Tjarke", "SET_V_MOEWENHUK", 2, 20,
  "Ein Aerlet folgt Tjarkes Boot jeden Morgen und stiehlt einen Fisch. Tjarke ist das recht – bis das Aerlet ausbleibt. Sie bittet den Wärter, nachzusehen. Das Aerlet hat sich im Kliffsund in einem alten Netz verfangen.",
  ["OBJ_TALK NPC_FISCHERIN_TJARKE 1 @SET_V_MOEWENHUK | Tjarke am Hafen",
   "OBJ_INVESTIGATE - 2 @R06_Z03 | Im Kliffsund nach dem Aerlet suchen",
   "OBJ_OBSERVE ECHO_098 1 @R06_Z03 | Das verfangene Aerlet beruhigen und beobachten",
   "OBJ_DELIVER ITM_FOOD_SMOKEDFISH 1 @SET_V_MOEWENHUK | Mit dem Aerlet einen Fisch zu Tjarke bringen"],
  "ITM_FOOD_KELPSNACK ×3; Kodex-Beobachtung Aerlet", "Aerlet begleitet Tjarkes Boot wieder (morgens sichtbar)",
  var="Time=Dawn")
Q("SQ_070", "Eisen für die Werft", "NPC_R06_KLAAS|Werftmeister Klaas", "SET_C_SALTRANDHAFEN", 5, 50,
  "Das Kharsk-Eisen aus SQ_035 kommt in Saltrand an – und Werftmeister Klaas weigert sich, es zu verbauen: Es „singt“ unter dem Hammer. Tova und Klaas streiten per Klangbrief. Der Wärter muss zeigen, dass singendes Eisen kein Mangel ist, sondern ein Qualitätsmerkmal.",
  ["OBJ_TALK NPC_R06_KLAAS 1 @SET_C_SALTRANDHAFEN | Klaas und das singende Eisen",
   "OBJ_OBSERVE ECHO_108 1 @R06_Z02 | Ein Brassel in der Werft beim Nieten beobachten",
   "OBJ_PUZZLE PZ_SQ070_FORGE 1 @SET_C_SALTRANDHAFEN | Mit dem Resonator den Klang des Eisens vergleichen",
   "OBJ_CHOICE DLG_SQ_070_01 1 @SET_C_SALTRANDHAFEN | Klaas und Tova (per Klangbrief) zusammenbringen",
   "OBJ_TALK NPC_MARIEKE 1 @SET_C_SALTRANDHAFEN | Marieke den Abschluss melden"],
  "ITM_GEAR_BAG_2; Rezept RCP_060", "Werft verbaut Kharsk-Eisen; neue Schiffe im Hafen (Data Layer, Akt II)",
  solution="Klaas überzeugen (Messung) · Tova anweisen, „stilles“ Eisen zu liefern (teurer) · Brassel als Prüfer in die Werft holen (dritte Lösung, Werftmeister-Bark).")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    err = validate(IDS)
    print("\n".join(err) if err else "", end="")
    print(f"K49: {len(IDS)} Nebenquests, {len(err)} Fehler.")
    if cmd == "write" and not err:
        print("geschrieben:", write(IDS))


# ── Platzhalter-Funktionen für build_doc ({{py sq_k49 …}}) ──
import sq_common as _c


def _ids(region=None):
    return [i for i in IDS if region is None or _c.SKEL[i]["RegionId"] == region]


def overview_region(region):
    return _c.overview(_ids(region))


def cards_region(region):
    return _c.region_cards(_ids(region), region)


def stats_all():
    return _c.stats(IDS)


def stats_region(region):
    return _c.stats(_ids(region))


def chains():
    return _c.chain_table(IDS)


def givers():
    return _c.giver_table(IDS)
