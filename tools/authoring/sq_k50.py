#!/usr/bin/env python3
"""K50 – Nebenquests II: SQ_071–SQ_140 (Saltrand II, Sahrun-Weite, Ignareth, Hvitfell I)."""
import sys
from sq_common import Q, QUESTS, validate, write
import sq_common as _c

IDS = [f"SQ_{i:03d}" for i in range(71, 141)]
W6 = "Quest.MQ_A2_07"

# ───────────────────────────── R06 Saltrand (Teil 2) ─────────────────────────────
Q("SQ_071", "Der Leuchtfelsen-Chor", "NPC_LEUCHTWART_FOKKE|Leuchtwart Fokke", "SET_O_LEUCHTFELSENWACHT", 2, 25,
  "Nachts singen Glimkins auf dem Leuchtfelsen – Fokke sagt, sie hätten Schiffe gerettet, lange bevor es den Turm gab. Seit das neue Leuchtfeuer brennt, sind sie verstummt. Der Wärter findet heraus, dass das Licht ihren Gesang überstrahlt.",
  ["OBJ_TALK NPC_LEUCHTWART_FOKKE 1 @SET_O_LEUCHTFELSENWACHT | Fokke am Turm",
   "OBJ_OBSERVE ECHO_102 2 @R06_Z04 | Glimkins nachts beobachten",
   "OBJ_INVESTIGATE - 2 @R06_Z04 | Den Lichtkegel des Feuers vermessen",
   "OBJ_CHOICE DLG_SQ_071_01 1 @SET_O_LEUCHTFELSENWACHT | Fokke eine Blende vorschlagen"],
  "ITM_LURE_LANTERN; Kodex-Beobachtung Glimkin", "Glimkins singen wieder (Ambient nachts); Leuchtfeuer mit Blende",
  var="Time=Night")
Q("SQ_072", "Zahlen, die nicht klingen", "NPC_WIEBKE|Prokuristin Wiebke", "SET_C_SALTRANDHAFEN", 3, 35,
  "Wiebke, Mariekes Prokuristin, findet in den Hafenbüchern Lieferungen, die es nie gab: Fässer, die zweimal verbucht wurden. Marieke will keine Schuldigen, sondern die Wahrheit. Der Wärter zählt im Lagerhaus nach – und ein Brisel zählt mit.",
  ["OBJ_TALK NPC_WIEBKE 1 @SET_C_SALTRANDHAFEN | Wiebke im Goldklang-Haupthaus",
   "OBJ_INVESTIGATE - 3 @SET_C_SALTRANDHAFEN | Im Lagerhaus nachzählen",
   "OBJ_OBSERVE ECHO_092 1 @SET_C_SALTRANDHAFEN | Den Lager-Brisel beim Stapeln beobachten",
   "OBJ_TALK NPC_WIEBKE 1 @SET_C_SALTRANDHAFEN | Wiebke berichten"],
  "ITM_GEAR_BAG_2; Kontor-Lieferscheine (Lore)", "Wiebke führt doppelte Buchprüfung ein (Bark)")
Q("SQ_073", "Sturmflut", "NPC_R06_HAUKE|Taucher Hauke", "SET_C_SALTRANDHAFEN", 5, 35,
  "Bei Gewitter in Akt II drückt eine Sturmflut in die Tangwerft-Bucht. Brisions reiten auf den Wellen und schlagen Boote los. Hauke braucht Hilfe, die Boote zu sichern und ein Tidling-Gelege vor dem Abtreiben zu retten.",
  ["OBJ_CONDITION Weather=Thunderstorm 1 @R06_Z02 | Gewitter über der Bucht",
   "OBJ_OBSERVE ECHO_093 1 @R06_Z02 | Den Brision-Zug beobachten",
   "OBJ_TRAVERSE Mount.Swim 1 @R06_Z02 | Zu den losgerissenen Booten schwimmen",
   "OBJ_ESCORT NPC_R06_HAUKE 1 @R06_Z02 | Mit Hauke das Tidling-Gelege bergen"],
  "ITM_GEAR_MASK_3; ITM_CON_HEAL_ALL", "Sturmflutmauer in Tangwerft (Data Layer); Hauke-Barks",
  var="Weather=Thunderstorm")
Q("SQ_074", "Das zweite Siegel", "NPC_WIEBKE|Prokuristin Wiebke", "SET_C_SALTRANDHAFEN", 4, 35,
  "Die doppelten Fässer tragen zwei Siegel – ein echtes Kontorsiegel und ein gefälschtes. Wiebke vermutet einen Siegelschneider in Möwenhuk. Der Wärter findet ihn: einen alten Mann, der für einen Konsortium-Agenten arbeitet, weil er seine Werkstatt nicht verlieren will.",
  ["OBJ_GOTO SET_V_MOEWENHUK 1 @SET_V_MOEWENHUK | Nach Möwenhuk",
   "OBJ_INVESTIGATE - 3 @SET_V_MOEWENHUK | Siegelspuren in den Werkstätten finden",
   "OBJ_TALK NPC_SIEGELSCHNEIDER_EDO 1 @SET_V_MOEWENHUK | Edo befragen",
   "OBJ_CHOICE DLG_SQ_074_01 1 @SET_V_MOEWENHUK | Was mit Edo geschieht"],
  "ITM_SEAL_TUNED ×2; Rezept RCP_038", "Edo arbeitet für Wiebke oder verlässt die Insel",
  solution="Edo melden · Edo laufen lassen · Edo als Siegelprüfer für das Kontor gewinnen (dritte Lösung, Wiebke-Bark).")
Q("SQ_075", "Die Tangernte", "NPC_TANGSAMMLERIN_GESA|Tangsammlerin Gesa", "SET_V_TANGWERFT", 2, 25,
  "Bei Springflut legt das Meer die äußeren Tangbänke frei – zwei Stunden lang. Gesa sammelt dann für das ganze Jahr. Doch Tangix haben sich in den Bänken eingenistet. Der Wärter sorgt dafür, dass Ernte und Tangix sich vertragen.",
  ["OBJ_CONDITION Moon=Full 1 @R06_Z02 | Springflut bei Vollmond",
   "OBJ_OBSERVE ECHO_107 2 @R06_Z02 | Tangix in den Bänken beobachten",
   "OBJ_COLLECT ITM_MAT_KELP 8 @R06_Z02 | Mit Gesa Tang ernten (nur abseits der Nester)",
   "OBJ_CHOICE DLG_SQ_075_01 1 @SET_V_TANGWERFT | Gesa eine Erntekarte vorschlagen"],
  "ITM_MAT_KELP ×5; ITM_FOOD_KELPSNACK ×3", "Gesas Erntekarte im Dorf; Tangix-Bänke als Schutzgebiet markiert",
  var="Moon=Full")
Q("SQ_076", "Der Agent", "NPC_WIEBKE|Prokuristin Wiebke", "SET_C_SALTRANDHAFEN", 5, 40,
  "Der Konsortium-Agent heißt Bartol und sitzt in der Hafenkneipe. Er will das Kontor nicht betrügen, sondern übernehmen – die doppelten Fässer finanzieren Anteile. Wiebke braucht Beweise, die vor dem Kontorrat halten.",
  ["OBJ_INVESTIGATE - 3 @SET_C_SALTRANDHAFEN | Bartol beobachten",
   "OBJ_ESCORT NPC_BOTENJUNGE_LUTZ 1 @SET_C_SALTRANDHAFEN | Dem Boten zu Bartols Lager folgen",
   "OBJ_INVESTIGATE - 2 @R06_Z03 | Das Lager im Kliffsund durchsuchen",
   "OBJ_TALK NPC_WIEBKE 1 @SET_C_SALTRANDHAFEN | Wiebke die Beweise zeigen"],
  "ITM_CON_SENSE ×2; Anteilsschein (Lore)", "Bartol meidet den Hafen (oder wird später in SQ_078 gestellt)",
  var="Time=Night")
Q("SQ_077", "Das Wrack der Möwe", "NPC_R06_ODALIS|Kuriositätenhändlerin Odalis", "SET_C_SALTRANDHAFEN", 3, 30,
  "Odalis kauft Kurioses aus Wracks. Im Riffgrund liegt die „Möwe“, ein Schiff aus den Siegelkriegen, und darin, sagt sie, eine Kiste mit dorunischen Glasplatten. Die Opalisks im Wrack sehen das anders.",
  ["OBJ_TALK NPC_R06_ODALIS 1 @SET_C_SALTRANDHAFEN | Odalis' Seekarte",
   "OBJ_TRAVERSE Mount.Swim 1 @R06_Z05 | Zum Wrack tauchen",
   "OBJ_OBSERVE ECHO_110 1 @R06_Z05 | Die Opalisks im Wrack beobachten",
   "OBJ_PUZZLE PZ_SQ077_WRECK 1 @R06_Z05 | Die Glasplatten-Kiste aus dem Laderaum befreien"],
  "ITM_EVO_TIDEPEARL; Klangfragment (TruthLevel 0)", "Odalis stellt die Glasplatten aus (Laden-Inventar +1)")
Q("SQ_078", "Vor dem Kontorrat", "NPC_WIEBKE|Prokuristin Wiebke", "SET_C_SALTRANDHAFEN", 6, 55,
  "Der Kontorrat tagt. Bartol hat Freunde im Rat; Wiebke hat Beweise; Marieke hat nur eine Bedingung: „Keine Hexenjagd.“ Der Wärter spricht als Zeuge – in drei Haltungen – und am Ende steht eine Entscheidung über Bartols Anteile.",
  ["OBJ_TALK NPC_MARIEKE 1 @SET_C_SALTRANDHAFEN | Marieke vor der Sitzung",
   "OBJ_CHOICE DLG_SQ_078_01 1 @SET_C_SALTRANDHAFEN | Als Zeuge sprechen",
   "OBJ_CHOICE DLG_SQ_078_02 1 @SET_C_SALTRANDHAFEN | Vorschlag zu Bartols Anteilen",
   "OBJ_OBSERVE ECHO_092 1 @SET_C_SALTRANDHAFEN | Den Lager-Brisel als „Zeugen“ vorführen"],
  "Titel „Kontorzeuge“; ITM_GEAR_TOOL_3", "Neue Satzungsklausel (Vorstufe „Klangtreue“, K47); Bartol verliert Anteile oder wird Teilhaber mit Auflage",
  solution="Ausschluss (Gesetz) · Rückzahlung und Bewährung (Gnade) · Anteile in einen Fonds für Werft-Echos umwandeln (dritte Lösung, Marieke lacht).")
Q("SQ_079", "Thal'assyrs Grotte", "NPC_R06_BEKE_FISH|Fischhändlerin Beke", "SET_C_SALTRANDHAFEN", 4, 40,
  "In Akt III erzählt Beke – nicht die Arenameisterin, sondern ihre Tante am Fischmarkt – dass die Tiefseegrotte vor dem Hafen „atmet“, seit alle Stimmen erwacht sind (oder schlafen). Sie bittet den Wärter, nachzusehen, ob Thal'assyr Hilfe braucht.",
  ["OBJ_TALK NPC_R06_BEKE_FISH 1 @SET_C_SALTRANDHAFEN | Beke am Fischmarkt",
   "OBJ_TRAVERSE Mount.Swim 1 @R06_Z05 | In die Tiefseegrotte tauchen",
   "OBJ_INVESTIGATE - 3 @R06_Z05 | Die Strömungen der Grotte untersuchen",
   "OBJ_OBSERVE ECHO_244 1 @R06_Z05 | Thal'assyr beobachten"],
  "Kodex-Eintrag Thal'assyr (Seite 3); ITM_LURE_TUNINGFORK", "Grotte als Pilgerort der Fischer; Tidal-Barks",
  truth=7)
Q("SQ_080", "Glas für das Feuer", "NPC_RAGNA|Kapitänin Ragna", "SET_C_SALTRANDHAFEN", 4, 40,
  "Saltrands Leuchtfeuer brauchen Linsen aus Sahrun-Glas. Die alte Route über Land ist zu langsam. Kapitänin Ragna will eine Seeroute um die Küste wagen – wenn ein Wärter die Riffe kennt und ein Brisel-Schwarm das Schiff lotst.",
  ["OBJ_TALK NPC_RAGNA 1 @SET_C_SALTRANDHAFEN | Ragna an Bord der „Salzbraut“",
   "OBJ_OBSERVE ECHO_092 2 @R06_Z05 | Brisel-Schwärme über dem Riff beobachten",
   "OBJ_INVESTIGATE - 3 @R06_Z05 | Die gefährlichen Riffpassagen kartieren",
   "OBJ_CHOICE DLG_SQ_080_01 1 @SET_C_SALTRANDHAFEN | Route festlegen"],
  "Seekarte (Lore); ITM_LURE_WINDCHIME", "Die „Salzbraut“ läuft aus (Hafen-Data-Layer)")
Q("SQ_081", "Die Witwe vom Kliff", "NPC_WITWE_ALKE|Alke (Kliffsund)", "SET_V_MOEWENHUK", 3, 30,
  "Alkes Mann fuhr vor zwölf Jahren hinaus und kam nicht wieder. Seitdem sitzt ein Ariette auf ihrem Dach und singt jeden Abend. Alke will wissen, ob es sein Echo ist. Der Wärter vergleicht den Gesang mit einem Klangbrief, den ihr Mann hinterließ.",
  ["OBJ_TALK NPC_WITWE_ALKE 1 @SET_V_MOEWENHUK | Alke zuhören",
   "OBJ_OBSERVE ECHO_104 1 @SET_V_MOEWENHUK | Das Ariette in der Dämmerung beobachten",
   "OBJ_INVESTIGATE - 1 @SET_V_MOEWENHUK | Den alten Klangbrief abspielen",
   "OBJ_CHOICE DLG_SQ_081_01 1 @SET_V_MOEWENHUK | Alke antworten"],
  "Hain-Dekor ITM_DECO_CLIFFBELL; Kodex-Beobachtung Ariette (Bindungsgedächtnis)", "Alke spricht mit dem Ariette (Bark); im Epilog-Nachhall singt es mit anderen",
  var="Time=Dusk")
Q("SQ_082", "Sturm vor Sahrun", "NPC_RAGNA|Kapitänin Ragna", "SET_C_SALTRANDHAFEN", 5, 50,
  "Die erste Fahrt der Salzbraut gerät in einen Sturm vor der Südküste. Ragna will umkehren, die Mannschaft weiter. Der Wärter hält das Schiff mit seinen Echos auf Kurs und findet in der Bucht von Sahrun einen sicheren Hafen – und einen Händler, der schon auf sie wartet.",
  ["OBJ_CONDITION Weather=Thunderstorm 1 @R06_Z05 | Sturm auf See",
   "OBJ_CHOICE DLG_SQ_082_01 1 @R06_Z05 | Umkehren oder weiter",
   "OBJ_BATTLE NPC_STURMECHO_BRISION 1 @R06_Z05 | Einen aufgebrachten Brision-Leitbullen erschöpfen",
   "OBJ_GOTO R04_Z01 1 @R04_Z01 | Die Bucht vor der Harrâd-Oase erreichen"],
  "ITM_GEAR_GLIDER_3; Seefahrer-Abzeichen (Kosmetik)", "Seeroute Saltrand–Sahrun (Schnellreise per Schiff zwischen Häfen)",
  var="Weather=Thunderstorm")
Q("SQ_083", "Die Perlen der Aquadrals", "NPC_FORSCHERIN_LIV|Meeresforscherin Liv", "SET_O_RIFFPOSTEN", 3, 30,
  "Aquadrals leuchten nachts in Mustern, die sich alle drei Nächte wiederholen. Liv glaubt, sie zählen etwas. Der Wärter dokumentiert drei Nächte und findet heraus: Sie zählen Mondphasen – und warnen so vor Springfluten.",
  ["OBJ_TALK NPC_FORSCHERIN_LIV 1 @SET_O_RIFFPOSTEN | Liv am Riffposten",
   "OBJ_PHOTO ECHO_096 3 @R06_Z05 | Drei Leuchtmuster fotografieren (drei Nächte)",
   "OBJ_OBSERVE ECHO_095 1 @R06_Z05 | Aquafins beim Nachahmen beobachten",
   "OBJ_TALK NPC_FORSCHERIN_LIV 1 @SET_O_RIFFPOSTEN | Liv die Deutung vortragen"],
  "ITM_KS_030; Kodex-Fragment „Mondzähler“", "Fischer lesen die Aquadral-Muster als Flutwarnung (Bark)",
  var="Time=Night")
Q("SQ_084", "Salz auf grauem Sand", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_DUENENKATE", 4, 40,
  "Die stillen Ränder in Saltrand: An der Dünenküste bleiben nach der Heilung graue Flecken, auf denen kein Tangi wächst. Jorn vermutet Salz. Der Wärter findet Stillstein-Staub, den die Flut verteilt hat.",
  ["OBJ_GOTO R06_Z01 1 @R06_Z01 | Zur Dünenküste",
   "OBJ_OBSERVE ECHO_106 2 @R06_Z01 | Tangis meiden die Flecken – beobachten",
   "OBJ_HEALZONE ZONE_SQ084 3 @R06_Z01 | Drei graue Flecken heilen",
   "OBJ_INVESTIGATE - 2 @R06_Z01 | Den Ursprung des Staubs finden"],
  "ITM_EMAT_STILLSHARD; ITM_CON_CLEANSE ×2", "Flecken verschwinden; Tangis wachsen nach")
Q("SQ_085", "Die Probe der Gezeiten", "NPC_BEKE|Beke Tamsen", "SET_C_SALTRANDHAFEN", 6, 40,
  "Im Nachhall bietet Beke Tamsen eine Gezeitenprobe: drei Kämpfe, deren Arena sich mit jeder Runde hebt und senkt. Die Probe findet nur bei Vollmond statt, wenn die Flut am höchsten steht.",
  ["OBJ_CONDITION Moon=Full 1 @SET_C_SALTRANDHAFEN | Vollmond",
   "OBJ_BATTLE NPC_GEZEITENPRUEFER_1 1 @SET_C_SALTRANDHAFEN | Erste Flut",
   "OBJ_BATTLE NPC_GEZEITENPRUEFER_2 1 @SET_C_SALTRANDHAFEN | Zweite Flut",
   "OBJ_BATTLE NPC_BEKE 1 @SET_C_SALTRANDHAFEN | Höchste Flut gegen Beke",
   "OBJ_OBSERVE ECHO_244 1 @SET_C_SALTRANDHAFEN | Der Grotte lauschen"],
  "ITM_HELD_TONE_TIDE; Titel „Gezeitenreiter“", "Beke-Barks im Nachhall", var="Moon=Full", truth=9)
Q("SQ_086", "Der Leuchtturm schweigt", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_LEUCHTFELSENWACHT", 5, 45,
  "Der Staub kam vom Leuchtfelsen: Ordensleute hatten dort vor Jahren einen Stillstein vergraben, „damit die Glimkins nicht so laut singen“. Der Stein ist zerbrochen, die Splitter wandern mit der Flut. Jorn und der Wärter bergen sie – vor der nächsten Flut.",
  ["OBJ_INVESTIGATE - 3 @R06_Z04 | Die Splitter am Leuchtfelsen finden",
   "OBJ_CONDITION Time=Day 1 @R06_Z04 | Bei Ebbe am Tag arbeiten",
   "OBJ_HEALZONE ZONE_SQ086 2 @R06_Z04 | Den Fundort heilen",
   "OBJ_OBSERVE ECHO_103 1 @R06_Z04 | Glimars am geheilten Felsen beobachten"],
  "ITM_EMAT_STILLSHARD ×2; ITM_GEAR_RESONATOR_3", "Leuchtfelsen klar; Glimar-Chor stärker (mit SQ_071)",
  var="Time=Day")
Q("SQ_087", "Die Regatta", "NPC_R06_KLAAS|Werftmeister Klaas", "SET_C_SALTRANDHAFEN", 4, 30,
  "Einmal im Jahr segeln die Werften gegeneinander – mit Echos als Zugkraft. Klaas fehlt ein Steuermann. Der Wärter tritt an: drei Wettkämpfe gegen die Konkurrenzwerften, in denen Sturm- und Flut-Echos den Ausschlag geben.",
  ["OBJ_TALK NPC_R06_KLAAS 1 @SET_C_SALTRANDHAFEN | Klaas sucht einen Steuermann",
   "OBJ_BATTLE NPC_WERFT_NORD 1 @R06_Z02 | Gegen die Nordwerft",
   "OBJ_BATTLE NPC_WERFT_SUED 1 @R06_Z02 | Gegen die Südwerft",
   "OBJ_OBSERVE ECHO_099 1 @R06_Z02 | Das Aerluna der Siegercrew beobachten"],
  "ITM_HELD_SWIFTFEATHER; Hain-Dekor ITM_DECO_REGATTAFLAG", "Regatta als jährliches Weltereignis (WE_REGATTA)",
  var="Time=Day")
Q("SQ_088", "Die Perlenwerkstatt", "NPC_R03_SHADE|Der Schatten", "SET_C_SALTRANDHAFEN", 5, 45,
  "Die Klangperlen der Fangnetze stammen aus einer Werkstatt in Saltrand, die auch für das Kontor Perlen schleift. Die Besitzerin weiß nicht, wofür ihre Perlen verwendet werden – oder will es nicht wissen. Der Wärter muss sie zum Hinsehen bringen.",
  ["OBJ_TALK NPC_FS_ZELLE_SALTRAND 1 @SET_C_SALTRANDHAFEN | Die Zelle der Freien Stimmen am Hafen",
   "OBJ_INVESTIGATE - 3 @SET_C_SALTRANDHAFEN | Die Werkstatt beobachten",
   "OBJ_TALK NPC_PERLENSCHLEIFERIN_ANKE 1 @SET_C_SALTRANDHAFEN | Anke zur Rede stellen",
   "OBJ_CHOICE DLG_SQ_088_01 1 @SET_C_SALTRANDHAFEN | Anke eine Wahl lassen"],
  "ITM_MAT_NACRE ×3; ITM_TRAP_POOL", "Anke liefert keine Netzperlen mehr (oder heimlich weiter – Bark)",
  var="Time=Night", solution="Anke an Wiebke melden (Kontor) · Anke öffentlich bloßstellen · Anke zeigen, was ein Netz anrichtet – Undfin in SQ_063 (dritte Lösung).")
Q("SQ_089", "Netze verbrennen", "NPC_R03_SHADE|Der Schatten", "SET_C_SALTRANDHAFEN", 6, 55,
  "Die Netzknüpfer lagern ihre Ware in einem Kliffversteck. Die Freien Stimmen wollen es anzünden. Der Wärter weiß: Im Versteck sind auch gefangene Echos. Bei Nacht und Nebel führt er den Einsatz – ohne Feuer, mit Befreiung.",
  ["OBJ_CONDITION Weather=Fog 1 @R06_Z03 | Nebel im Kliffsund",
   "OBJ_GOTO R06_Z03 1 @R06_Z03 | Zum Versteck",
   "OBJ_HEALZONE ZONE_SQ089 3 @R06_Z03 | Drei verstummte Gefangene befreien und heilen",
   "OBJ_BATTLE NPC_NETZKNUEPFER_HARM 1 @R06_Z03 | Die Echos des Netzknüpfers erschöpfen",
   "OBJ_CHOICE DLG_SQ_089_01 1 @R06_Z03 | Die Netze: verbrennen, versenken, umknüpfen"],
  "Titel „Netzlöser“; ITM_GEAR_LANTERN_3", "Keine Fangnetze mehr in R03/R06 (Population erholt sich); Netzknüpfer Harm flieht oder wird Fischer",
  var="Weather=Fog", solution="Verbrennen (Tavesh-Bark) · versenken · zu Fischernetzen umknüpfen (dritte Lösung, Harm hilft).")
Q("SQ_090", "Weißes Gold", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_TANGWERFT", 4, 40,
  "Ennis ist zurück, diesmal mit einer Spur: In den Salzgärten hinter Tangwerft arbeiten Stonshells unter Vertrag – einem Vertrag, den sie nie unterschreiben konnten. Die Salzsieder sagen, es sei „Tradition“. Ennis nennt es Schuldknechtschaft. Der Wärter sieht sich beides an.",
  ["OBJ_TALK NPC_ENNIS 1 @SET_V_TANGWERFT | Ennis in Tangwerft",
   "OBJ_OBSERVE ECHO_101 2 @R06_Z02 | Stonshells in den Salzgärten beobachten",
   "OBJ_TALK NPC_SALZSIEDER_OLE 1 @SET_V_TANGWERFT | Salzsieder Ole zuhören",
   "OBJ_INVESTIGATE - 2 @SET_V_TANGWERFT | Die Verträge im Siedehaus lesen"],
  "ITM_MAT_SALTWORT ×5; Vertragsabschrift (Lore)", "Kette führt nach Sahrun (SQ_109)")

# ───────────────────────────── R04 Sahrun-Weite ─────────────────────────────
Q("SQ_091", "Scherben im Sand", "NPC_LUND|Grabungsleiterin Saphira Lund", "SET_O_GLASEBENETURM", 3, 35,
  "Die Akademie gräbt auf der Glasebene. Saphira Lund leitet die Grabung, freundlich und gründlich. Sie braucht jemanden, der Glasscherben nach Klang sortiert – die Hochkultur schrieb in Tönen, nicht in Zeichen. Vor W6 arbeitet Venns Team mit; danach Shirahs Leute.",
  ["OBJ_TALK NPC_LUND 1 @SET_O_GLASEBENETURM | Lund am Grabungszelt",
   "OBJ_INVESTIGATE - 3 @R04_Z03 | Drei Scherbenfelder abhören",
   "OBJ_PUZZLE PZ_SQ091_SHARDS 1 @SET_O_GLASEBENETURM | Scherben nach Tonhöhe ordnen",
   "OBJ_OBSERVE ECHO_129 1 @R04_Z03 | Vitrels, die nachts auf den Scherben leuchten"],
  "ITM_MAT_SUNGLASS ×3; Kodex-Fragment „Glaslied I“", "Grabungsfeld erweitert (Data Layer)", var="Time=Night")
Q("SQ_092", "Die Dunhorn-Mutter", "NPC_HIRTIN_NAJLA|Hirtin Najla (Ashurim)", "SET_V_ASHURIM", 3, 30,
  "Eine Dunhorn-Mutter hat ihr Kalb in der Tiefen Weite verloren. Sie weigert sich, mit der Herde weiterzuziehen, und das Wanderdorf kann nicht ohne sie aufbrechen. Najla bittet den Wärter, das Kalb zu finden, bevor der Sandsturm kommt.",
  ["OBJ_TALK NPC_HIRTIN_NAJLA 1 @SET_V_ASHURIM | Najla bei der Herde",
   "OBJ_OBSERVE ECHO_115 1 @SET_V_ASHURIM | Die Dunhorn-Mutter beobachten (Rufmuster)",
   "OBJ_INVESTIGATE - 3 @R04_Z05 | Spuren des Kalbs in der Tiefen Weite",
   "OBJ_ESCORT NPC_HIRTIN_NAJLA 1 @SET_V_ASHURIM | Mit dem Kalb zur Herde"],
  "ITM_FOOD_DATES ×5; Kodex-Beobachtung Dunkalb", "Das Wanderdorf zieht weiter (neuer Lagerplatz); Najla-Barks",
  var="Weather=Sandstorm")
Q("SQ_093", "Das Lied der Glasstadt", "NPC_LUND|Grabungsleiterin Saphira Lund", "SET_O_GLASEBENETURM", 4, 40,
  "Die sortierten Scherben ergeben ein Lied – die Hymne einer Stadt, die „die Sonne zu laut besang“. Lund will es aufführen. Der Wärter sammelt in Mirsaan und Harrâd Liedreste, die als Kinderreime überlebt haben.",
  ["OBJ_GOTO SET_V_MIRSAAN 1 @SET_V_MIRSAAN | Nach Mirsaan",
   "OBJ_TALK NPC_LEHRERIN_DALIA 1 @SET_V_MIRSAAN | Kinderreime bei Lehrerin Dalia",
   "OBJ_INVESTIGATE - 2 @SET_V_HARRAD | Reimreste in der Oase",
   "OBJ_PUZZLE PZ_SQ093_HYMN 1 @SET_O_GLASEBENETURM | Hymne aus Scherben und Reimen setzen"],
  "ITM_KS_043; Kodex-Fragment „Glaslied II“", "Die Kinder von Mirsaan singen die Hymne (Ambient)")
Q("SQ_094", "Skarits im Wind", "NPC_STERNDEUTER_HARUN|Sterndeuter Harun", "SET_C_QASRSAHRUN", 2, 25,
  "Harun beobachtet Skarits, die bei Wind seltsame Kreise ziehen. Er glaubt, sie lesen die Schwerkraft der Dünen. Der Wärter vermisst die Kreise und findet einen hohlen Dünenkern, in dem Skarabons nisten.",
  ["OBJ_TALK NPC_STERNDEUTER_HARUN 1 @SET_C_QASRSAHRUN | Harun im Sternturm",
   "OBJ_OBSERVE ECHO_117 2 @R04_Z02 | Skarit-Kreise beobachten",
   "OBJ_TRAVERSE Mount.Dig 1 @R04_Z02 | In den Dünenkern graben",
   "OBJ_PHOTO ECHO_119 1 @R04_Z02 | Ein Skarabon im Nest fotografieren"],
  "ITM_EVO_GRAVITY; Kodex-Beobachtung Skarabon", "Harun veröffentlicht „Dünenkerne“ (Bark)")
Q("SQ_095", "Wer die Sonne zu laut sang", "NPC_LUND|Grabungsleiterin Saphira Lund", "SET_O_GLASEBENETURM", 5, 45,
  "Das Lied der Glasstadt erzählt von einem Herrscher, der die Sonne zwang, länger zu scheinen – mit einem Kronenreif aus Glas. Lund erkennt Parallelen zu den Kronensplitter-Gerüchten. Nach W6 versteht der Wärter, was sie gefunden hat: ein Vorbild Maedryns.",
  ["OBJ_INVESTIGATE - 3 @R04_Z03 | Den Herrschersaal unter der Glasebene freilegen",
   "OBJ_TRAVERSE Mount.Dig 1 @R04_Z03 | Durch den Sand in den Saal",
   "OBJ_OBSERVE ECHO_128 1 @R04_Z03 | Das Mirazhar im Saal beobachten",
   "OBJ_CHOICE DLG_SQ_095_01 1 @SET_O_GLASEBENETURM | Lund sagen, was der Saal bedeutet"],
  "Lore „Der Glasreif“ (TruthLevel 6); ITM_LURE_MIRROR", "Der Saal wird zum Rückkehrort; Lunds Bericht in K50/K51-Akten",
  truth=6, pre=W6)
Q("SQ_096", "Die Nacht der Spiegel", "NPC_SHIRAH|Shirah Harrad", "SET_C_QASRSAHRUN", 4, 35,
  "In Akt III, wenn Ash'kareth wach ist (oder schläft), richtet Qasr Sahrun die Nacht der Spiegel aus: Alle Spiegel der Stadt werden auf den Mond gerichtet. Wer hineinsieht, sieht eine Wahrheit über sich. Shirah bittet den Wärter, die Spiegel zu stellen – und selbst hineinzusehen.",
  ["OBJ_CONDITION Moon=Full 1 @SET_C_QASRSAHRUN | Vollmond",
   "OBJ_PUZZLE PZ_SQ096_MIRRORS 1 @SET_C_QASRSAHRUN | Die Spiegel der Stadt ausrichten",
   "OBJ_OBSERVE ECHO_245 1 @SET_C_QASRSAHRUN | Ash'kareths Licht im Hauptspiegel beobachten",
   "OBJ_CHOICE DLG_SQ_096_01 1 @SET_C_QASRSAHRUN | In den Spiegel sehen"],
  "ITM_LURE_MIRROR; Hain-Dekor ITM_DECO_SUNMIRROR", "Nacht der Spiegel als Weltereignis (Vollmond, R04)",
  var="Moon=Full", truth=7)
Q("SQ_097", "Der Reif bleibt im Sand", "NPC_LUND|Grabungsleiterin Saphira Lund", "SET_O_GLASEBENETURM", 6, 55,
  "Im Saal liegt ein Reif aus Glas – kein Kronensplitter, aber nach demselben Prinzip gebaut. Venn-treue Grabungswachen halten den Saal noch besetzt und wollen den Reif nach Nimbara schaffen; Aevrins Akademie will ihn studieren, Shirah ihn zerstören. Lund überlässt die Entscheidung dem Wärter.",
  ["OBJ_GOTO R04_Z03 1 @R04_Z03 | Zurück in den Herrschersaal",
   "OBJ_BATTLE NPC_GRABUNGSWACHE_ODO 1 @R04_Z03 | Die Echos der Venn-treuen Grabungswache erschöpfen",
   "OBJ_INVESTIGATE - 2 @R04_Z03 | Den Reif mit dem Resonator abhören",
   "OBJ_CHOICE DLG_SQ_097_01 1 @R04_Z03 | Reif zerstören, studieren oder begraben"],
  "Titel „Glaslauscher“; ITM_HELD_MIRRORSCALE", "Reif in der Akademie (Ausstellung, Nachhall) · zerstört · wieder versiegelt (dritte Lösung)",
  truth=6, pre=W6, solution="Zerstören (Shirah) · der Akademie unter Aevrin geben · im Saal versiegeln und den Ort schützen (dritte Lösung).")
Q("SQ_098", "Sandsturm-Lotsen", "NPC_KARAWANENFUEHRERIN_AMARA|Amara (Karawanserei)", "SET_C_QASRSAHRUN", 4, 35,
  "Bei Sandsturm stehen die Karawanen still – außer man folgt den Sirrkorns, die im Sturm Bahnen fliegen. Amara will eine Karawane mit Arzneien nach Harrâd bringen, die nicht warten kann. Der Wärter navigiert per Resonanzsinn.",
  ["OBJ_CONDITION Weather=Sandstorm 1 @R04_Z02 | Sandsturm",
   "OBJ_OBSERVE ECHO_125 2 @R04_Z02 | Sirrkorn-Bahnen im Sturm beobachten",
   "OBJ_ESCORT NPC_KARAWANENFUEHRERIN_AMARA 1 @SET_V_HARRAD | Die Karawane nach Harrâd führen",
   "OBJ_DELIVER ITM_CON_HEAL_2 3 @SET_V_HARRAD | Arzneien übergeben"],
  "ITM_GEAR_CLOAK_3; ITM_FOOD_DATES ×3", "Amaras Karawanen nutzen die Sirrkorn-Bahnen (Bark)",
  var="Weather=Sandstorm")
Q("SQ_099", "Geschwärzte Zeilen", "NPC_AEVRIN|Aevrin Thal", "SET_C_QASRSAHRUN", 5, 45,
  "Nach dem Verrat öffnet Aevrin Venns Akten. Eine Spur führt zur Grabung am Sonnenhof: geschwärzte Zeilen über „Fundstücke für das Rektorat“. Aevrin schickt den Wärter, die Originalnotizen der Grabungshelfer zu finden, bevor sie verbrannt werden.",
  ["OBJ_TALK NPC_AEVRIN 1 @SET_C_QASRSAHRUN | Aevrins Klangbrief",
   "OBJ_GOTO R04_Z04 1 @R04_Z04 | Zur verlassenen Grabung am Sonnenhof",
   "OBJ_INVESTIGATE - 3 @R04_Z04 | Notizen der Grabungshelfer finden",
   "OBJ_TALK NPC_GRABUNGSHELFER_TAMIR 1 @SET_V_ASHURIM | Den Helfer Tamir befragen"],
  "Lore „Fundliste Sonnenhof“ (TruthLevel 6); ITM_CON_SENSE ×2", "Aevrins Akte wächst (K51: SQ_132, SQ_152)",
  truth=6, pre=W6)
Q("SQ_100", "Das vergrabene Observatorium", "NPC_STERNDEUTER_HARUN|Sterndeuter Harun", "SET_C_QASRSAHRUN", 4, 40,
  "Harun hat eine Sternkarte der Hochkultur gefunden. Sie zeigt ein Observatorium unter dem Sonnenhof-Plateau, dessen Linsen „die Sonne stimmten“. Der Wärter gräbt sich hinein und richtet die Linsen neu aus – auf die Sterne statt auf die Sonne.",
  ["OBJ_TALK NPC_STERNDEUTER_HARUN 1 @SET_C_QASRSAHRUN | Haruns Sternkarte",
   "OBJ_TRAVERSE Mount.Dig 1 @R04_Z04 | Zum vergrabenen Observatorium",
   "OBJ_PUZZLE PZ_SQ100_LENSES 1 @R04_Z04 | Die Linsen ausrichten",
   "OBJ_OBSERVE ECHO_130 1 @R04_Z04 | Vitraphas im Sternenlicht beobachten"],
  "ITM_LURE_STARCHIME; Klangfragment (TruthLevel 4)", "Observatorium als Aussichtspunkt (Wärter-EP Entdeckung)",
  var="Time=Night", truth=4)
Q("SQ_101", "Glas ab Harrâd", "NPC_RAGNA|Kapitänin Ragna", "SET_V_HARRAD", 4, 40,
  "Die Salzbraut liegt in der Bucht vor Harrâd. Ragna verhandelt mit der Glasbläserei Tavi um Linsenglas, doch Tavi liefert nur, wenn Saltrand im Gegenzug Salz für die Oase schickt – Salz, das die Oase gegen Hitze braucht.",
  ["OBJ_TALK NPC_RAGNA 1 @SET_V_HARRAD | Ragna in der Bucht",
   "OBJ_TALK NPC_R04_TAVI 1 @SET_C_QASRSAHRUN | Tavi in der Glasbläserei",
   "OBJ_OBSERVE ECHO_120 1 @R04_Z01 | Sengels beim Glasschmelzen helfen sehen",
   "OBJ_CHOICE DLG_SQ_101_01 1 @SET_C_QASRSAHRUN | Tauschverhältnis Glas gegen Salz"],
  "ITM_MAT_SUNGLASS ×3; Rezept RCP_062", "Glas-Salz-Handel (Händler-Sortimente in R04/R06 +2)")
Q("SQ_102", "Die alte Brunnenköchin", "NPC_R04_SAYA|Brunnenköchin Saya", "SET_C_QASRSAHRUN", 2, 25,
  "Saya kocht seit fünfzig Jahren an der Brunnenküche. Im Nachhall will sie ihr Rezeptbuch an jemanden weitergeben, der „zuhört, wenn das Wasser kocht“. Der Wärter kocht mit ihr drei Gerichte – jedes mit einem Echo als Küchenhilfe.",
  ["OBJ_TALK NPC_R04_SAYA 1 @SET_C_QASRSAHRUN | Saya an der Brunnenküche",
   "OBJ_COLLECT ITM_MAT_OASISMINT 3 @R04_Z01 | Oasenminze sammeln",
   "OBJ_OBSERVE ECHO_111 1 @SET_C_QASRSAHRUN | Ein Solkit beim Feuermachen beobachten",
   "OBJ_CHOICE DLG_SQ_102_01 1 @SET_C_QASRSAHRUN | Das Rezeptbuch annehmen"],
  "Rezept RCP_064; ITM_FOODC_STEW ×3", "Sayas Gerichte im Gasthaus; Bark über „den Wärter, der kochen kann“",
  truth=9)
Q("SQ_103", "Die gläserne Route", "NPC_RAGNA|Kapitänin Ragna", "SET_V_HARRAD", 5, 55,
  "Die erste volle Ladung Linsenglas soll über Land nach Saltrand – auf einer neuen Route durch die Weite, die Sengrath-Herden als Wegweiser nutzt. Die Reise dauert drei Spieltage; unterwegs: Hitzewellen, eine Furt, ein Händlerzug, der die Route für sich will.",
  ["OBJ_CONDITION Weather=Heatwave 1 @R04_Z05 | Aufbruch in der Hitze",
   "OBJ_OBSERVE ECHO_122 1 @R04_Z05 | Einer Sengrath-Herde folgen",
   "OBJ_ESCORT NPC_RAGNA 1 @R04_Z02 | Den Glaszug durch die Mirsaan-Dünen führen",
   "OBJ_CHOICE DLG_SQ_103_01 1 @SET_O_DUENENWACHT | Mit dem konkurrierenden Händlerzug verhandeln",
   "OBJ_DELIVER ITM_MAT_SUNGLASS 3 @SET_C_SALTRANDHAFEN | Linsenglas in Saltrand abliefern"],
  "Titel „Routenfinder“; ITM_GEAR_BAG_4", "Gläserne Route als Handelsweg; Leuchtfeuer Saltrand mit Sahrun-Linsen",
  var="Weather=Heatwave", solution="Route teilen · Zoll erheben · gemeinsamen Karawanenverband gründen (dritte Lösung).")
Q("SQ_104", "Die Uhr der Stachiks", "NPC_FORSCHER_IDRIS|Forscher Idris", "SET_O_PLATEAULAGER", 3, 30,
  "Stachiks kommen nachts aus dem Sand – aber nicht zu jeder Nacht. Idris vermutet einen Takt. Der Wärter beobachtet sie über drei Nächte und findet: Sie folgen nicht dem Mond, sondern der Temperatur des Sandes um Mitternacht.",
  ["OBJ_TALK NPC_FORSCHER_IDRIS 1 @SET_O_PLATEAULAGER | Idris' Hypothese",
   "OBJ_OBSERVE ECHO_123 3 @R04_Z04 | Stachiks drei Nächte beobachten",
   "OBJ_INVESTIGATE - 3 @R04_Z04 | Sandtemperaturen messen",
   "OBJ_TALK NPC_FORSCHER_IDRIS 1 @SET_O_PLATEAULAGER | Ergebnis vortragen"],
  "ITM_KS_046; Kodex-Fragment „Sanduhr“", "Kodex Stachik: Aktivität mit Temperaturregel",
  var="Time=Night")
Q("SQ_105", "Die Karawanserei-Wette", "NPC_KARAWANENFUEHRERIN_AMARA|Amara (Karawanserei)", "SET_C_QASRSAHRUN", 3, 30,
  "Amara hat mit einem Kontor-Händler gewettet, dass ein Solvar schneller durch die Weite läuft als jedes Lastechos des Kontors. Der Einsatz: freie Lagerplätze für ein Jahr. Der Wärter soll das Solvar vorbereiten – und auf faires Spiel achten.",
  ["OBJ_TALK NPC_KARAWANENFUEHRERIN_AMARA 1 @SET_C_QASRSAHRUN | Die Wette",
   "OBJ_OBSERVE ECHO_112 2 @R04_Z01 | Das Solvar im Training beobachten",
   "OBJ_INVESTIGATE - 2 @SET_C_QASRSAHRUN | Herausfinden, ob der Kontor-Händler betrügt",
   "OBJ_CHOICE DLG_SQ_105_01 1 @SET_C_QASRSAHRUN | Das Rennen eröffnen"],
  "ITM_HELD_SWIFTFEATHER; ITM_FOOD_DATES ×3", "Rennen als monatliches Ereignis; Kontor- und Karawanserei-Barks",
  var="Time=Day")
Q("SQ_106", "Die Probe des Mittags", "NPC_SHIRAH|Shirah Harrad", "SET_C_QASRSAHRUN", 5, 35,
  "In Akt III fordert Shirah den Wärter zur Mittagsprobe: drei Kämpfe bei Hitzewelle, bei denen Sonnenspiegel jede zweite Runde blenden. Wer bestehen will, muss Licht lesen – oder sich davor schützen.",
  ["OBJ_CONDITION Weather=Heatwave 1 @SET_C_QASRSAHRUN | Hitzewelle",
   "OBJ_BATTLE NPC_SPIEGELTRAEGER_1 1 @SET_C_QASRSAHRUN | Erste Mittagsprobe",
   "OBJ_BATTLE NPC_SPIEGELTRAEGER_2 1 @SET_C_QASRSAHRUN | Zweite Mittagsprobe",
   "OBJ_BATTLE NPC_SHIRAH 1 @SET_C_QASRSAHRUN | Shirah selbst",
   "OBJ_OBSERVE ECHO_245 1 @SET_C_QASRSAHRUN | Unter der Arena lauschen (Ash'kareth)"],
  "ITM_HELD_TONE_LIGHT; ITM_KS_047", "Shirah-Barks; Mittagstraining", var="Weather=Heatwave")
Q("SQ_107", "Die stillen Ränder der Weite", "NPC_PASSWART_JORN|Passwart Jorn (Wildwacht)", "SET_O_DUENENWACHT", 6, 55,
  "Die letzte Station der stillen Ränder: In der Tiefen Weite ist eine alte Stillezone geheilt, aber ein Ring aus grauem Glas bleibt. Darin leben Mahrsils, die nur dort sicher sind, weil kein anderes Echo hineingeht. Heilen heißt: ihr Refugium zerstören.",
  ["OBJ_GOTO R04_Z05 1 @R04_Z05 | Zum Glasring in der Tiefen Weite",
   "OBJ_OBSERVE ECHO_134 2 @R04_Z05 | Mahrsils im Ring beobachten",
   "OBJ_INVESTIGATE - 3 @R04_Z05 | Den Ring vermessen",
   "OBJ_CHOICE DLG_SQ_107_01 1 @R04_Z05 | Heilen, lassen oder umsiedeln",
   "OBJ_HEALZONE ZONE_SQ107 1 @R04_Z05 | (je nach Wahl) den Rand oder den ganzen Ring heilen"],
  "Titel „Randgänger“; Hain-Dekor ITM_DECO_GLASSRING", "Mahrsil-Refugium bleibt (Teilheilung) oder Ring verschwindet; Jorns Abschiedsbrief",
  var="Time=Night", solution="Ganz heilen (Mahrsils ziehen weg) · lassen (Ring bleibt grau) · nur den Rand heilen und einen Schutzring markieren (dritte Lösung).")
Q("SQ_108", "Das Duell der Karawanen", "NPC_KARAWANENFUEHRERIN_AMARA|Amara (Karawanserei)", "SET_C_QASRSAHRUN", 4, 30,
  "Zwei Karawanen streiten um denselben Rastplatz an der Harrâd-Oase. Die Tradition der Weite: ein Wärterkampf, ausgetragen von einem Unbeteiligten für jede Seite. Der Wärter kämpft – für wen, entscheidet er selbst.",
  ["OBJ_TALK NPC_KARAWANENFUEHRERIN_AMARA 1 @SET_V_HARRAD | Amara erklärt den Brauch",
   "OBJ_CHOICE DLG_SQ_108_01 1 @SET_V_HARRAD | Eine Seite wählen",
   "OBJ_BATTLE NPC_KARAWANENKAEMPFER_ZAHIR 1 @SET_V_HARRAD | Kampf gegen den Vertreter der anderen Seite",
   "OBJ_OBSERVE ECHO_113 1 @R04_Z01 | Das Solaryx des Siegers beobachten"],
  "ITM_HELD_TONE_EMBER; ITM_FOOD_DATES ×3", "Rastplatz-Ordnung an der Oase (Ambient)")
Q("SQ_109", "Salz in der Oase", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_HARRAD", 4, 40,
  "Die Salzsieder aus Tangwerft haben Verwandte in Harrâd – und auch hier arbeiten Stonshell-Verwandte, Mesakils, in den Salzpfannen, unter denselben Verträgen. Ennis will beide Seiten gleichzeitig angehen.",
  ["OBJ_TALK NPC_ENNIS 1 @SET_V_HARRAD | Ennis in Harrâd",
   "OBJ_OBSERVE ECHO_131 2 @R04_Z01 | Mesakils in den Salzpfannen beobachten",
   "OBJ_INVESTIGATE - 2 @SET_V_HARRAD | Die Verträge der Oase vergleichen",
   "OBJ_TALK NPC_SALZMEISTERIN_FARAH 1 @SET_V_HARRAD | Salzmeisterin Farah zuhören"],
  "ITM_MAT_SALTCOPPER ×3; Vertragsabschrift II (Lore)", "Kette geht weiter (SQ_110)", var="Weather=Heatwave")
Q("SQ_110", "Der Vertrag, den niemand unterschrieb", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_HARRAD", 5, 45,
  "Beide Verträge gehen auf einen Mustervertrag zurück, den ein Kontor-Notar vor vierzig Jahren aufsetzte – mit einer Klausel, die Echos „als Inventar des Salzgartens“ führt. Der Notar lebt noch, in Mirsaan. Ennis will ihn bloßstellen; der Wärter will ihn verstehen.",
  ["OBJ_GOTO SET_V_MIRSAAN 1 @SET_V_MIRSAAN | Nach Mirsaan",
   "OBJ_TALK NPC_NOTAR_BASIM 1 @SET_V_MIRSAAN | Den alten Notar Basim befragen",
   "OBJ_INVESTIGATE - 2 @SET_V_MIRSAAN | Basims Archiv durchsehen",
   "OBJ_CHOICE DLG_SQ_110_01 1 @SET_V_MIRSAAN | Basim um einen Widerruf bitten"],
  "ITM_CON_SENSE; Widerrufsurkunde (Lore)", "Basim widerruft öffentlich oder schweigt (beeinflusst SQ_111)")
Q("SQ_111", "Salz und Freiheit", "NPC_ENNIS|Ennis Rook (Kurierin)", "SET_V_HARRAD", 6, 60,
  "Mit oder ohne Widerruf: Die Salzgärten in Harrâd und Tangwerft sollen an einem Tag die Echos freigeben. Ennis organisiert, Wiebke (Kontor) prüft die Verträge, die Salzsieder fürchten den Ruin. Der Wärter steht dazwischen und hält am Ende eine Rede in der Oase.",
  ["OBJ_TALK NPC_SALZMEISTERIN_FARAH 1 @SET_V_HARRAD | Farah zögert",
   "OBJ_CHOICE DLG_SQ_111_01 1 @SET_V_HARRAD | Rede in der Oase",
   "OBJ_HEALZONE ZONE_SQ111 2 @R04_Z01 | Zwei verstummte Mesakils in den Pfannen heilen",
   "OBJ_OBSERVE ECHO_132 1 @R04_Z01 | Den ersten freien Mesakor beobachten",
   "OBJ_REST SET_V_HARRAD 1 @SET_V_HARRAD | Das Salzfest feiern"],
  "Titel „Salzbrecher“; Hain-Dekor ITM_DECO_SALTCRYSTAL", "Salzgärten arbeiten mit freiwilligen Echos gegen Lohn; Salzfest als Weltereignis (R04/R06)",
  solution="Sofortige Freigabe (Freie Stimmen) · stufenweise mit Kontor-Krediten · Genossenschaft aus Siedern und Echos mit Rückkehrrecht (dritte Lösung).")
Q("SQ_112", "Die Zelle in Mirsaan", "NPC_FS_ZELLE_MIRSAAN|Zelle Mirsaan (Freie Stimmen)", "SET_V_MIRSAAN", 4, 35,
  "Die Freie-Stimmen-Zelle in Mirsaan versteckt ein Dutzend Echos, die aus Arbeitslagern geflohen sind. Ein Sandsturm hat ihr Versteck freigelegt. Der Wärter hilft, ein neues zu finden – mit Grabreiten unter die Dünen.",
  ["OBJ_TALK NPC_FS_ZELLE_MIRSAAN 1 @SET_V_MIRSAAN | Die Zelle in Not",
   "OBJ_TRAVERSE Mount.Dig 1 @R04_Z02 | Einen Gang unter die Dünen graben",
   "OBJ_INVESTIGATE - 2 @R04_Z02 | Eine tragfähige Höhle finden",
   "OBJ_ESCORT NPC_FS_ZELLE_MIRSAAN 1 @R04_Z02 | Die Echos ins neue Versteck führen"],
  "ITM_CON_REPEL ×3; Zellen-Schnellreisepunkt Mirsaan", "Neues Versteck (verborgener Ort, Rückkehr)",
  var="Weather=Sandstorm")

# ───────────────────────────── R05 Ignareth ─────────────────────────────
Q("SQ_113", "Die Erzwaage", "NPC_R05_VOLK|Erzwaage Volk", "SET_C_SCHLACKENWEHR", 3, 30,
  "Volk betreibt die Erzwaage des Kontors in Schlackenwehr. Seit Wochen fehlen kleine Mengen Slagsteel. Er verdächtigt die Arbeiter. Der Wärter findet Amboltspuren – die jungen Ambolts fressen Metallspäne und wachsen daran.",
  ["OBJ_TALK NPC_R05_VOLK 1 @SET_C_SCHLACKENWEHR | Volk an der Waage",
   "OBJ_INVESTIGATE - 3 @SET_C_SCHLACKENWEHR | Spuren im Lager",
   "OBJ_OBSERVE ECHO_138 1 @SET_C_SCHLACKENWEHR | Ambolts beim Fressen beobachten",
   "OBJ_CHOICE DLG_SQ_113_01 1 @SET_C_SCHLACKENWEHR | Volk einen Futterplatz vorschlagen"],
  "ITM_MAT_SLAGSTEEL ×2; Kodex-Beobachtung Ambolt", "Futterplatz für Ambolts; Arbeiter entlastet (Bark)")
Q("SQ_114", "Das Pyrolm-Nest", "NPC_SCHMIEDIN_ISOLDE|Schmiedin Isolde", "SET_V_VORTHAX", 2, 25,
  "Isolde findet jeden Morgen ein Pyrolm in ihrer Esse. Sie mag es, aber es frisst ihre Kohle. Der Wärter findet heraus, dass das Pyrolm sein Nest im Schlackenstrom verloren hat.",
  ["OBJ_TALK NPC_SCHMIEDIN_ISOLDE 1 @SET_V_VORTHAX | Isolde und der Gast",
   "OBJ_OBSERVE ECHO_135 1 @SET_V_VORTHAX | Das Pyrolm beobachten",
   "OBJ_INVESTIGATE - 2 @R05_Z03 | Das alte Nest im Schlackenstrom suchen",
   "OBJ_CHOICE DLG_SQ_114_01 1 @SET_V_VORTHAX | Neues Nest bauen oder Pyrolm behalten"],
  "ITM_FOOD_CHARCOAL ×5; ITM_EVO_EMBER", "Pyrolm-Nest in Isoldes Hof oder am Strom")
Q("SQ_115", "Nach dem Lager", "NPC_R05_ITHREN|Wehrmarkt-Händler Ithren", "SET_C_SCHLACKENWEHR", 4, 35,
  "In Akt III, nach der Lagerbefreiung, stehen die Kontor-Hallen am Kraterrand leer. Ithren will sie als Markt nutzen; die Zunft will sie abreißen; die befreiten Echos kehren nachts zurück, weil sie dort Wärme finden.",
  ["OBJ_GOTO POI_R05_9001 1 @R05_Z05 | Zum ehemaligen Lager",
   "OBJ_OBSERVE ECHO_142 2 @R05_Z05 | Aschunds in den Hallen nachts beobachten",
   "OBJ_TALK NPC_R05_ITHREN 1 @SET_C_SCHLACKENWEHR | Ithrens Plan",
   "OBJ_CHOICE DLG_SQ_115_01 1 @SET_C_SCHLACKENWEHR | Was aus den Hallen wird"],
  "ITM_GEAR_TOOL_3; Lore „Lagerakte“", "Hallen werden Markt, Wärmehaus für Echos oder abgerissen",
  var="Time=Night", truth=0, pre="Quest.MQ_A2_03",
  solution="Markt (Kontor) · Abriss (Zunft) · Wärmehaus für Echos mit Markt am Tag (dritte Lösung).")
Q("SQ_116", "Glockenguss", "NPC_GIESSER_BRAM|Glockengießer Bram", "SET_C_SCHLACKENWEHR", 3, 30,
  "Jeder 12. Spieltag ist Glockenguss in Schlackenwehr. Diesmal springt die Form. Bram braucht ein Bassalt, das den Ton der neuen Glocke „vorsingt“, damit die Form im Klang gegossen werden kann.",
  ["OBJ_TALK NPC_GIESSER_BRAM 1 @SET_C_SCHLACKENWEHR | Bram und die gesprungene Form",
   "OBJ_OBSERVE ECHO_155 1 @R05_Z04 | Ein Bassalt in der Obsidianklamm beobachten",
   "OBJ_PUZZLE PZ_SQ116_BELL 1 @SET_C_SCHLACKENWEHR | Form und Ton abstimmen",
   "OBJ_CINEMATIC SEQ_SQ116_POUR 1 @SET_C_SCHLACKENWEHR | Der Guss"],
  "ITM_LURE_BELLCHIME; Hain-Dekor ITM_DECO_FORGEBELL", "Neue Glocke läutet (eine der sechs Schmiedeglocken)")
Q("SQ_117", "Das Konsortium", "NPC_MARIEKE|Marieke Holm", "SET_C_SCHLACKENWEHR", 5, 45,
  "Marieke will wissen, wer hinter dem Lager-Konsortium steckt. Die Spur führt zu drei Kontor-Teilhabern – einer davon ist Bartol aus Saltrand. Der Wärter sammelt Beweise in Vorthax, Kaldra und an der Obsidianwacht.",
  ["OBJ_TALK NPC_MARIEKE 1 @SET_C_SCHLACKENWEHR | Marieke im Kontor",
   "OBJ_INVESTIGATE - 2 @SET_V_VORTHAX | Lieferbücher in Vorthax",
   "OBJ_INVESTIGATE - 2 @SET_V_KALDRA | Lagerlisten in Kaldra",
   "OBJ_INVESTIGATE - 2 @SET_O_OBSIDIANWACHT | Frachtbriefe an der Obsidianwacht",
   "OBJ_CHOICE DLG_SQ_117_01 1 @SET_C_SCHLACKENWEHR | Marieke die Namen nennen"],
  "ITM_GEAR_BAG_3; Konsortiumsakte (Lore)", "Konsortium verliert Kontorrechte (Kontor-Barks)", pre="Quest.MQ_A2_03")
Q("SQ_118", "Die Aschenacht", "NPC_R05_SERAPHE|Thermenwirtin Seraphe", "SET_C_SCHLACKENWEHR", 4, 35,
  "Im Nachhall fällt bei Ascheregen ein feines Leuchten über Ignareth: Aschgrims tanzen in den Flocken. Seraphe will das Schauspiel ihren Gästen zeigen, aber die Aschgrims verschwinden, sobald jemand näherkommt. Der Wärter findet einen Weg, zuzusehen, ohne zu stören.",
  ["OBJ_CONDITION Weather=Ashfall 1 @R05_Z01 | Ascheregen",
   "OBJ_OBSERVE ECHO_143 2 @R05_Z01 | Aschgrims beim Tanz beobachten",
   "OBJ_INVESTIGATE - 2 @R05_Z01 | Einen verdeckten Aussichtsplatz finden",
   "OBJ_ESCORT NPC_R05_SERAPHE 1 @R05_Z01 | Seraphes Gäste leise hinführen"],
  "Hain-Dekor ITM_DECO_ASHLANTERN; ITM_CON_WARM ×3", "Aschenacht-Führungen (Weltereignis bei Ascheregen)",
  var="Weather=Ashfall", truth=9)
Q("SQ_119", "Die Zunft und das Kontor", "NPC_R05_KALDREX_GUILD|Zunftsprecherin Helka", "SET_C_SCHLACKENWEHR", 4, 35,
  "Die Schmiedezunft hat ein Gelübde gegen Waffen (seit den Siegelkriegen). Ein Kontor-Auftrag verlangt „Werkzeuge“, die verdächtig nach Stillstein-Fassungen aussehen. Helka bittet den Wärter, die Pläne zu prüfen.",
  ["OBJ_TALK NPC_R05_KALDREX_GUILD 1 @SET_C_SCHLACKENWEHR | Helka in der Zunfthalle",
   "OBJ_INVESTIGATE - 2 @SET_C_SCHLACKENWEHR | Die Auftragspläne prüfen",
   "OBJ_OBSERVE ECHO_140 1 @R05_Z02 | Ein Ambross beim Schmieden der Probe beobachten",
   "OBJ_CHOICE DLG_SQ_119_01 1 @SET_C_SCHLACKENWEHR | Helka raten"],
  "ITM_HELD_TONE_METAL; Rezept RCP_066", "Zunft lehnt ab oder liefert harmlose Werkzeuge (Bark)")
Q("SQ_120", "Ausbruch", "NPC_KRATERWART_OSK|Kraterwart Osk", "SET_O_KRATERRANDPOSTEN", 5, 35,
  "Alle drei Spieltage bricht der Ignar aus. Der Kraterrand-Posten kündigt es einen Tag vorher an. Diesmal ist ein Pyroluth-Gelege genau im Weg der Lava. Osk und der Wärter haben bis zum Ausbruch Zeit – Spielzeit, keine Echtzeit.",
  ["OBJ_TALK NPC_KRATERWART_OSK 1 @SET_O_KRATERRANDPOSTEN | Osks Warnung",
   "OBJ_OBSERVE ECHO_137 1 @R05_Z05 | Das Pyroluth-Elternpaar beobachten",
   "OBJ_INVESTIGATE - 2 @R05_Z05 | Einen sicheren Nistplatz finden",
   "OBJ_ESCORT NPC_KRATERWART_OSK 1 @R05_Z05 | Das Gelege mit Osk umbetten"],
  "ITM_GEAR_BOOTS_3; ITM_EVO_EMBERCORE", "Pyroluths nisten auf dem neuen Platz (sichtbar nach Ausbruch)",
  var="Weather=Heatwave")
Q("SQ_121", "Die Kisten von gestern", "NPC_MARIEKE|Marieke Holm", "SET_C_SCHLACKENWEHR", 4, 40,
  "In Akt III bittet Marieke den Wärter um einen Gefallen, der keiner ist: Sie will die Kisten aus MQ_A2_03 zurückverfolgen und wissen, wo sie gelandet sind. Je nachdem, was der Wärter damals tat, ist das ein Geständnis – oder eine Abrechnung.",
  ["OBJ_TALK NPC_MARIEKE 1 @SET_C_SCHLACKENWEHR | Marieke ohne Lächeln",
   "OBJ_INVESTIGATE - 3 @SET_O_OBSIDIANWACHT | Frachtspuren an der Obsidianwacht",
   "OBJ_CHOICE DLG_SQ_121_01 1 @SET_C_SCHLACKENWEHR | Marieke antworten (Ton nach FLAG_KONTOR_CRATES)"],
  "Lore „Frachtweg nach Dorunsruh“; ITM_GEAR_TOOL_4", "Marieke-Vignette im Epilog erhält eine Zeile",
  truth=7, pre="Quest.MQ_A2_07")
Q("SQ_122", "Das Kraterherz träumt", "NPC_R05_ASHA|Glutnarben-Tutorin Asha", "SET_C_SCHLACKENWEHR", 4, 40,
  "Asha hat Glutnarben – Zeichen, dass sie als Kind in einen Ausbruch geriet und ein Ignavyr sie trug. Sie glaubt, Pyr'thagon träumt in Bildern, die man im Obsidian sehen kann. Der Wärter sucht drei Obsidianflächen, in denen sich „Träume“ spiegeln.",
  ["OBJ_TALK NPC_R05_ASHA 1 @SET_C_SCHLACKENWEHR | Ashas Geschichte",
   "OBJ_INVESTIGATE - 3 @R05_Z04 | Drei Obsidianspiegel in der Klamm",
   "OBJ_PUZZLE PZ_SQ122_OBSIDIAN 1 @R05_Z04 | Die Bilder in Reihenfolge bringen",
   "OBJ_OBSERVE ECHO_147 1 @R05_Z05 | Ein Ignavyr am Kraterrand beobachten"],
  "Kodex-Eintrag Pyr'thagon (Seite 2); ITM_MAT_OBSIDIAN ×3", "Ashas Traumtafeln in der Zunfthalle",
  truth=4)
Q("SQ_123", "Rauchzeichen", "NPC_WILDWAECHTERIN_EILA|Wildwächterin Eila", "SET_O_ASCHEHUETTE", 3, 30,
  "Eila leitet die Aschehütte. Seit dem letzten Ausbruch kommen Fumels aus dem Krater ins Tal und lassen Vieh verstummen. Die Bauern wollen sie vertreiben. Eila glaubt, die Fumels fliehen vor etwas.",
  ["OBJ_TALK NPC_WILDWAECHTERIN_EILA 1 @SET_O_ASCHEHUETTE | Eila an der Aschehütte",
   "OBJ_OBSERVE ECHO_149 2 @R05_Z01 | Fumels im Tal beobachten",
   "OBJ_INVESTIGATE - 3 @R05_Z05 | Im Krater den Grund der Flucht finden",
   "OBJ_CHOICE DLG_SQ_123_01 1 @SET_O_ASCHEHUETTE | Bauern und Fumels"],
  "ITM_CON_CLEANSE ×2; ITM_TRAP_SHADE", "Fumels kehren zurück, Vieh erholt sich (Bark)", var="Weather=Ashfall")
Q("SQ_124", "Thermen für alle", "NPC_R05_SERAPHE|Thermenwirtin Seraphe", "SET_C_SCHLACKENWEHR", 2, 25,
  "Im Nachhall will Seraphe die Thermen für Echos öffnen – ein Becken nur für sie. Die Stammgäste murren. Der Wärter überzeugt die Gäste mit einem Nachmittag, an dem Echos und Menschen nebeneinander baden.",
  ["OBJ_TALK NPC_R05_SERAPHE 1 @SET_C_SCHLACKENWEHR | Seraphes Plan",
   "OBJ_TALK NPC_STAMMGAST_ALDO 1 @SET_C_SCHLACKENWEHR | Stammgast Aldo murrt",
   "OBJ_OBSERVE ECHO_141 1 @SET_C_SCHLACKENWEHR | Aschwels im warmen Becken beobachten",
   "OBJ_REST SET_C_SCHLACKENWEHR 1 @SET_C_SCHLACKENWEHR | Einen Nachmittag in den Thermen"],
  "ITM_FOODC_STEW ×2; Hain-Dekor ITM_DECO_HOTSPRING", "Echo-Becken in den Thermen (Ambient)", truth=9)
Q("SQ_125", "Die Obsidianklamm-Brücke", "NPC_WILDWAECHTERIN_EILA|Wildwächterin Eila", "SET_O_ASCHEHUETTE", 4, 35,
  "Die Hängebrücke über die Obsidianklamm ist gerissen; Obsidrax nisten auf beiden Seiten und lassen niemanden die Ankerpunkte erreichen. Eila braucht die Brücke für Rettungseinsätze.",
  ["OBJ_GOTO R05_Z04 1 @R05_Z04 | Zur gerissenen Brücke",
   "OBJ_OBSERVE ECHO_146 2 @R05_Z04 | Obsidrax-Nester beobachten",
   "OBJ_TRAVERSE Mount.Climb 1 @R05_Z04 | Zu den Ankerpunkten klettern",
   "OBJ_CHOICE DLG_SQ_125_01 1 @R05_Z04 | Brücke versetzen oder Nester umgehen"],
  "ITM_GEAR_BOOTS_3; ITM_MAT_OBSIDIAN ×2", "Neue Brücke (Data Layer)", var="Time=Day")
Q("SQ_126", "Drusen, die summen", "NPC_KRISTALLKUNDLERIN_MAJA|Kristallkundlerin Maja", "SET_V_KALDRA", 3, 30,
  "Drusils lassen Kristalldrusen in Gesteinsblasen wachsen. Maja hat herausgefunden, dass die Drusen summen, wenn ein Gewitter naht. Sie will ein Frühwarnnetz bauen – mit Drusen, nicht mit gefangenen Echos.",
  ["OBJ_TALK NPC_KRISTALLKUNDLERIN_MAJA 1 @SET_V_KALDRA | Majas Werkstatt",
   "OBJ_OBSERVE ECHO_151 2 @R05_Z04 | Drusils beim Wachsenlassen beobachten",
   "OBJ_CONDITION Weather=Thunderstorm 1 @R05_Z04 | Ein Gewitter abwarten",
   "OBJ_INVESTIGATE - 3 @R05_Z04 | Summende Drusen für das Netz finden"],
  "ITM_KS_052; ITM_MAT_SULFURCRYSTAL ×3", "Gewitter-Warnnetz in Kaldra (Glocken vor Gewitter)",
  var="Weather=Thunderstorm")
Q("SQ_127", "Was die Freien bauen", "NPC_TAVESH|Tavesh Amaru", "SET_C_SCHLACKENWEHR", 4, 40,
  "In Akt III bitten die Freien Stimmen den Wärter, ihnen beim Bau eines Hauses für befreite Echos in Kaldra zu helfen – ihr erstes offenes Haus. Die Zunft liefert Metall, wenn der Wärter für die Freien bürgt.",
  ["OBJ_TALK NPC_TAVESH 1 @SET_V_KALDRA | Tavesh in Kaldra",
   "OBJ_TALK NPC_R05_KALDREX_GUILD 1 @SET_C_SCHLACKENWEHR | Helka um Metall bitten",
   "OBJ_DELIVER ITM_MAT_SLAGSTEEL 3 @SET_V_KALDRA | Metall liefern",
   "OBJ_OBSERVE ECHO_139 1 @SET_V_KALDRA | Ambraks beim Bau beobachten"],
  "Hain-Dekor ITM_DECO_FREEHOUSE; ITM_CON_STAMINA ×3", "Haus der Freien Stimmen in Kaldra (offen, sichtbar)", pre="Quest.MQ_A2_03")
Q("SQ_128", "Die Esse-Probe", "NPC_KALDREX|Kaldrex Vorn", "SET_C_SCHLACKENWEHR", 5, 35,
  "Kaldrex' Schmiedeprobe (CANON §54): drei Kämpfe an der Großen Esse, in denen jede dritte Runde Glutboden entsteht. Danach erzählt Kaldrex, warum er das Lager-Tor nie schloss.",
  ["OBJ_TALK NPC_KALDREX 1 @SET_C_SCHLACKENWEHR | Kaldrex' Herausforderung",
   "OBJ_BATTLE NPC_SCHMIEDEGESELLE_1 1 @SET_C_SCHLACKENWEHR | Erste Esse",
   "OBJ_BATTLE NPC_SCHMIEDEGESELLE_2 1 @SET_C_SCHLACKENWEHR | Zweite Esse",
   "OBJ_BATTLE NPC_KALDREX 1 @SET_C_SCHLACKENWEHR | Kaldrex an der Großen Esse",
   "OBJ_CHOICE DLG_SQ_128_01 1 @SET_C_SCHLACKENWEHR | Kaldrex zuhören"],
  "ITM_HELD_TONE_EMBER; ITM_HELD_EMBERCORE", "Kaldrex-Barks; Essentraining", pre="Akkorde>=6")
Q("SQ_129", "Die Glut im Keller", "NPC_FS_ZELLE_SCHLACKENWEHR|Zelle Schlackenwehr", "SET_C_SCHLACKENWEHR", 4, 35,
  "Die Zelle der Freien Stimmen in Schlackenwehr versteckt in einem Keller ein Nucleox – ein sehr seltenes Echo, das jemand als Energiequelle für eine illegale Schmiede missbrauchte. Es glüht zu stark; der Keller wird zur Falle.",
  ["OBJ_TALK NPC_FS_ZELLE_SCHLACKENWEHR 1 @SET_C_SCHLACKENWEHR | Hilferuf der Zelle",
   "OBJ_OBSERVE ECHO_156 1 @SET_C_SCHLACKENWEHR | Das überhitzte Nucleox beobachten",
   "OBJ_HEALZONE ZONE_SQ129 2 @SET_C_SCHLACKENWEHR | Seine Glut mit zwei Kühlkreisen beruhigen",
   "OBJ_ESCORT NPC_FS_ZELLE_SCHLACKENWEHR 1 @R05_Z05 | Das Nucleox in den Krater zurückbringen"],
  "ITM_CON_WARM ×3; Kodex-Beobachtung Nucleox", "Nucleox im Krater sichtbar (nachts)", var="Time=Night")
Q("SQ_130", "Ein Lied für Kaldra", "NPC_TAVESH|Tavesh Amaru", "SET_V_KALDRA", 3, 30,
  "Im Nachhall feiert das Haus in Kaldra seinen ersten Jahrestag. Tavesh will ein Lied, das Echos und Menschen gemeinsam singen. Der Wärter sammelt Rufe von fünf befreiten Echos und setzt sie zusammen.",
  ["OBJ_TALK NPC_TAVESH 1 @SET_V_KALDRA | Tavesh' Wunsch",
   "OBJ_OBSERVE ECHO_136 1 @SET_V_KALDRA | Rufe der befreiten Echos aufzeichnen",
   "OBJ_PUZZLE PZ_SQ130_SONG 1 @SET_V_KALDRA | Das Lied setzen",
   "OBJ_REST SET_V_KALDRA 1 @SET_V_KALDRA | Jahrestag feiern"],
  "Hain-Dekor ITM_DECO_KALDRASONG; ITM_LURE_WHISTLE", "Lied als Musikvariante in Kaldra", truth=9)
Q("SQ_131", "Der Volket-Zaun", "NPC_FS_ZELLE_SCHLACKENWEHR|Zelle Schlackenwehr", "SET_C_SCHLACKENWEHR", 4, 35,
  "Ein Landbesitzer hat Volkets an einen Metallzaun gekettet, um ihn mit Blitz aufzuladen. Die Zelle will die Volkets befreien, ohne dass der Besitzer sie erneut fängt. Der Wärter sucht einen Weg, den Besitzer zu überzeugen – oder zu überlisten.",
  ["OBJ_GOTO R05_Z02 1 @R05_Z02 | Zum Zaun",
   "OBJ_OBSERVE ECHO_153 2 @R05_Z02 | Die angeketteten Volkets beobachten",
   "OBJ_TALK NPC_LANDBESITZER_GRIM 1 @R05_Z02 | Grim zur Rede stellen",
   "OBJ_CHOICE DLG_SQ_131_01 1 @R05_Z02 | Lösung wählen"],
  "ITM_TRAP_CHIME; ITM_HELD_TAKTRING", "Volkets frei; Zaun bleibt mit Blitzableiter statt Ketten",
  var="Weather=Thunderstorm", solution="Befreien und gehen · Grim bei der Wildwacht melden · Grim einen Blitzableiter bauen helfen, der die Volkets überflüssig macht (dritte Lösung).")

# ───────────────────────────── R07 Hvitfell (Teil 1) ─────────────────────────────
Q("SQ_132", "Die Briefe aus Hvitmark", "NPC_AEVRIN|Aevrin Thal", "SET_C_HVITMARK", 5, 45,
  "Aevrins Akten führen nach Hvitmark: Venn schrieb über Jahre Briefe an „eine Überlebende der Klangpest“ – an Sereth. Runa die Erinnernde bewahrt Abschriften, weil sie alle Briefe der Stadt aufbewahrt. Der Wärter liest, was Venn Sereth versprach.",
  ["OBJ_TALK NPC_R07_RUNA 1 @SET_C_HVITMARK | Runa die Erinnernde",
   "OBJ_INVESTIGATE - 3 @SET_C_HVITMARK | Venns Briefe im Archiv finden",
   "OBJ_CHOICE DLG_SQ_132_01 1 @SET_C_HVITMARK | Die Briefe an Aevrin senden – oder Sereth zuerst zeigen",
   "OBJ_TALK NPC_AEVRIN 1 @SET_C_HVITMARK | Aevrins Antwort per Klangbrief"],
  "Lore „Venns Briefe“ (TruthLevel 6); ITM_CON_SENSE ×2", "Sereth-Szene in MQ_A2_08 erhält eine Zeile, falls der Wärter ihr die Briefe zeigt",
  truth=6, pre=W6)
Q("SQ_133", "Snevel im Spiegelsee", "NPC_R07_ASKEL|Eisfischer Askel", "SET_C_HVITMARK", 2, 25,
  "Askel fischt im Spiegelsee durch Eislöcher. Snevels klauen seine Köder – und lassen ihm dafür kleine Eisfiguren da. Askel will wissen, ob das ein Tausch ist. Der Wärter beobachtet und findet: Ja, und die Figuren sind Fische.",
  ["OBJ_TALK NPC_R07_ASKEL 1 @SET_C_HVITMARK | Askel am Eisloch",
   "OBJ_OBSERVE ECHO_157 2 @R07_Z01 | Snevels in der Dämmerung beobachten",
   "OBJ_INVESTIGATE - 2 @R07_Z01 | Die Eisfiguren untersuchen",
   "OBJ_CHOICE DLG_SQ_133_01 1 @SET_C_HVITMARK | Askel den Tausch erklären"],
  "ITM_FOOD_ICEFISH ×5; Kodex-Beobachtung Snevel (Tausch)", "Askel tauscht weiter (Bark); Eisfiguren als Hain-Dekor kaufbar",
  var="Time=Dusk")
Q("SQ_134", "Lawinenwinter", "NPC_GLETSCHERWART_TORA|Gletscherwartin Tora", "SET_O_GLETSCHERWACHT", 4, 40,
  "Ein schwerer Schneefall droht die Gletscherzunge abbrechen zu lassen. Darunter liegt Eiðvik-Neu. Tora braucht Messungen am Gletscher und eine Warnkette mit Hallkids, deren Rufe weit tragen.",
  ["OBJ_CONDITION Weather=Snow 1 @R07_Z04 | Schneefall",
   "OBJ_INVESTIGATE - 3 @R07_Z04 | Risse in der Gletscherzunge messen",
   "OBJ_OBSERVE ECHO_174 2 @R07_Z01 | Hallkids für die Warnkette finden",
   "OBJ_TALK NPC_R07_ASTRID 1 @SET_V_EIDVIKNEU | Sprecherin Astrid warnen"],
  "ITM_GEAR_CLOAK_3; ITM_CON_WARM ×3", "Hallkid-Warnkette (Ruf bei Gefahr, Ambient)", var="Weather=Snow")
Q("SQ_135", "Der Name im Eis", "NPC_R07_RUNA|Runa die Erinnernde", "SET_C_HVITMARK", 3, 30,
  "In Akt III bittet Runa den Wärter, einen Namen zu finden, der im Polarlicht von MQ_A2_04 fehlte. Ein Uvarn soll ihn kennen – wer seinen Ruf hört, erinnert sich an einen vergessenen Namen.",
  ["OBJ_TALK NPC_R07_RUNA 1 @SET_C_HVITMARK | Runa und die Namensliste",
   "OBJ_CONDITION Weather=Aurora 1 @R07_Z02 | Polarlicht",
   "OBJ_OBSERVE ECHO_164 1 @R07_Z02 | Den Ruf eines Uvarn hören",
   "OBJ_CHOICE DLG_SQ_135_01 1 @SET_C_HVITMARK | Runa den Namen bringen"],
  "Hain-Dekor ITM_DECO_NAMESTONE; Kodex-Beobachtung Uvarn", "Name auf dem Klangpest-Mahnmal ergänzt",
  var="Weather=Aurora", truth=7)
Q("SQ_136", "Spuren am Pass", "NPC_GLETSCHERWART_TORA|Gletscherwartin Tora", "SET_O_PASSHUETTE", 3, 30,
  "An der Passhütte kommen Kjalmurs aus dem Hochland ins Tal, viel zu früh. Tora vermutet, dass etwas sie vertreibt. Der Wärter folgt den Spuren zurück und findet einen Ordensposten, der Stillsteine im Schnee lagert.",
  ["OBJ_OBSERVE ECHO_161 2 @R07_Z03 | Kjalmurs an der Passhütte beobachten",
   "OBJ_INVESTIGATE - 3 @R07_Z03 | Spuren zum Hochland verfolgen",
   "OBJ_TALK NPC_ORDENSPOSTEN_BRUDER_EIK 1 @R07_Z03 | Bruder Eik (Schiefertafel)",
   "OBJ_CHOICE DLG_SQ_136_01 1 @R07_Z03 | Den Posten auflösen oder verhandeln"],
  "ITM_EMAT_STILLSHARD; ITM_GEAR_BOOTS_3", "Ordensposten geräumt; Kjalmurs ziehen zurück", var="Weather=Snow",
  solution="Mit Gewalt räumen ist nicht vorgesehen – stattdessen: Eik überzeugen · Sigrun Fjall holen · Eik zeigen, was die Kjalmurs tun (dritte Lösung).")
Q("SQ_137", "Die Polarlichtnacht", "NPC_R07_YLVA|Ylva (Wollstube)", "SET_C_HVITMARK", 3, 30,
  "Wenn das Polarlicht über Hvitmark steht, ziehen die Familien auf den Spiegelsee und singen für die Toten von Eiðvik. Ylva fehlen Laternen aus Lysmara-Licht. Der Wärter bittet die Lysmaras, ihr Licht zu teilen.",
  ["OBJ_CONDITION Weather=Aurora 1 @R07_Z01 | Polarlicht",
   "OBJ_OBSERVE ECHO_168 2 @R07_Z04 | Lysmaras im Polarlicht beobachten",
   "OBJ_CHOICE DLG_SQ_137_01 1 @R07_Z04 | Die Lysmaras um Licht bitten (Lied, Köder oder Geduld)",
   "OBJ_REST SET_C_HVITMARK 1 @SET_C_HVITMARK | Mit der Stadt auf dem See singen"],
  "ITM_LURE_AURORAGLASS; Hain-Dekor ITM_DECO_AURORALANTERN", "Polarlichtnacht als Weltereignis", var="Weather=Aurora")
Q("SQ_138", "Die Wacht am Isvaldtind", "NPC_GLETSCHERWART_TORA|Gletscherwartin Tora", "SET_O_ISVALDTINDBIWAK", 5, 45,
  "Im Nachhall richtet die Wildwacht am Isvaldtind ein Biwak ein, um den Gletscherdom zu bewachen, unter dem Isv'aldr wacht oder schläft. Tora will den Weg sicher machen – mit Seilen, Kjalgrund-Spuren und einer Nacht auf dem Gipfel.",
  ["OBJ_TRAVERSE Mount.Climb 1 @R07_Z05 | Den Aufstieg sichern",
   "OBJ_OBSERVE ECHO_162 1 @R07_Z05 | Kjalgrunds auf dem Grat beobachten",
   "OBJ_REST SET_O_ISVALDTINDBIWAK 1 @R07_Z05 | Eine Nacht am Gipfel",
   "OBJ_OBSERVE ECHO_247 1 @R07_Z05 | Isv'aldr im Dom lauschen"],
  "Titel „Gipfelwacht“; ITM_GEAR_CLOAK_4", "Biwak als Schnellreisepunkt", var="Time=Night", truth=9)
Q("SQ_139", "Der Spiegel unter dem See", "NPC_R07_EIRIK|Silberschmied Eirik", "SET_C_HVITMARK", 4, 35,
  "Eirik behauptet, unter dem Spiegelsee liege ein zweiter See – ein Spiegel aus Eis, der zeigt, was vor der Klangpest war. Bei Nebel ist er durch die Eislöcher zu sehen. Der Wärter taucht mit Atemmaske unter das Eis.",
  ["OBJ_TALK NPC_R07_EIRIK 1 @SET_C_HVITMARK | Eiriks Legende",
   "OBJ_CONDITION Weather=Fog 1 @R07_Z01 | Nebel über dem See",
   "OBJ_TRAVERSE Mount.Swim 1 @R07_Z01 | Unter das Eis tauchen",
   "OBJ_INVESTIGATE - 3 @R07_Z01 | Bilder im Eisspiegel deuten"],
  "ITM_EVO_AURORATHREAD; Klangfragment (TruthLevel 0)", "Eiriks Silberarbeiten zeigen das alte Eiðvik (Laden)", var="Weather=Fog")
Q("SQ_140", "Rentiere aus Klang", "NPC_HIRTE_HALVAR|Hirte Halvar (Wildwacht-Helfer)", "SET_V_FJALLSTAD", 3, 30,
  "Vardholms ziehen jedes Jahr über das Fjallstad-Tal. Dieses Jahr fehlt der Leitbulle, und die Herde irrt. Halvar, der für die Wildwacht die Herden zählt, vermutet Wilderer. Der Wärter findet den Bullen in einer Gletscherspalte – lebendig, aber eingeklemmt.",
  ["OBJ_OBSERVE ECHO_171 2 @R07_Z01 | Die irrende Herde beobachten",
   "OBJ_INVESTIGATE - 3 @R07_Z04 | Spuren an der Gletscherzunge",
   "OBJ_TRAVERSE Mount.Climb 1 @R07_Z04 | In die Spalte steigen",
   "OBJ_ESCORT NPC_HIRTE_HALVAR 1 @R07_Z01 | Mit Halvar den Bullen zur Herde führen"],
  "ITM_FOOD_ALPINECHEESE ×3; Kodex-Beobachtung Vardholm (Leittier)", "Herde zieht geordnet (Ambient)", var="Time=Day")


# ── Platzhalter-Funktionen für build_doc ──
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


if __name__ == "__main__":
    import sq_k49  # noqa: F401 – Region R06 vollständig prüfen (SQ_068–070 aus K49)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    err = validate(IDS)
    r06 = [i for i in list(sq_k49.IDS) + IDS if _c.SKEL[i]["RegionId"] == "R06"]
    err += [e for e in validate(r06) if e.startswith("QS-15")]
    print("\n".join(err) if err else "", end="")
    print(f"K50: {len(IDS)} Nebenquests, {len(err)} Fehler.")
    if cmd == "write" and not err:
        print("geschrieben:", write(IDS))
