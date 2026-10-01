#!/usr/bin/env python3
"""K51 – Nebenquests III: SQ_141–SQ_210 (Hvitfell II, Ael'Dorun, Prismtiefen, Nimbara) + Haken-Abgleich K11–K13."""
import sys
from sq_common import Q, QUESTS, validate, write
import sq_common as _c

IDS = [f"SQ_{i:03d}" for i in range(141, 211)]
W6 = "Quest.MQ_A2_07"

# ───────────────────────────── R07 Hvitfell (Teil 2) ─────────────────────────────
Q("SQ_141", "Thing-Streit", "NPC_R07_ASTRID|Sprecherin Astrid Eiðsen", "SET_C_HVITMARK", 4, 40,
  "Alle zehn Spieltage tagt das Thing von Hvitmark. Nach dem Verrat fordern Ordensanhänger, dass die Stadt die Stillsteine weiter duldet – „nur noch freiwillig“. Wärter und Wildwacht wollen ein Verbot. Astrid bittet den Wärter, vor dem Thing zu sprechen, nachdem er beide Seiten gehört hat.",
  ["OBJ_TALK NPC_R07_ASTRID 1 @SET_C_HVITMARK | Astrid lädt zum Thing",
   "OBJ_TALK NPC_ORDENSANHAENGERIN_SOLVEIG 1 @SET_C_HVITMARK | Solveig für die Ordensanhänger",
   "OBJ_TALK NPC_WAERTERIN_GRETE 1 @SET_C_HVITMARK | Grete für die Wärter",
   "OBJ_OBSERVE ECHO_172 1 @R07_Z02 | Ein Eidrun an einem freiwilligen Stillstein beobachten",
   "OBJ_CHOICE DLG_SQ_141_01 1 @SET_C_HVITMARK | Rede vor dem Thing"],
  "Titel „Thingredner“; ITM_LURE_BELLCHIME", "Thing-Beschluss: Verbot, Duldung mit Auflagen oder „Stille Häuser“ (dritte Lösung); Barks in Hvitmark",
  truth=7, solution="Verbot (Wärter) · Duldung (Orden) · freiwillige „Stille Häuser“ für Echos, die Ruhe suchen, ohne Steine in der Wildnis (dritte Lösung).")
Q("SQ_142", "Schlitten ohne Rast", "NPC_FS_ZELLE_HVITMARK|Zelle Hvitmark (Freie Stimmen)", "SET_C_HVITMARK", 4, 35,
  "Ein Eisfisch-Händler lässt Kjalfs Tag und Nacht Schlitten über den Spiegelsee ziehen. Die Zelle der Freien Stimmen will die Kjalfs nachts losschneiden. Der Wärter beobachtet erst – und findet heraus, dass der Händler selbst kurz vor dem Ruin steht.",
  ["OBJ_TALK NPC_FS_ZELLE_HVITMARK 1 @SET_C_HVITMARK | Die Zelle im Wollkeller",
   "OBJ_OBSERVE ECHO_160 2 @R07_Z01 | Die erschöpften Kjalfs beobachten",
   "OBJ_TALK NPC_EISHAENDLER_BJARNE 1 @SET_C_HVITMARK | Bjarne zuhören",
   "OBJ_CHOICE DLG_SQ_142_01 1 @SET_C_HVITMARK | Lösung für Kjalfs und Bjarne"],
  "ITM_FOOD_ICEFISH ×3; ITM_CON_STAMINA ×2", "Kjalfs ziehen nur noch tagsüber mit Ruhezeiten (oder sind frei)", var="Weather=Snow",
  solution="Nachts befreien (Bjarne ruiniert) · Wildwacht melden · Askels Snevel-Tausch (SQ_133) für Bjarnes Fang nutzen, damit er weniger fahren muss (dritte Lösung).")
Q("SQ_143", "Eiðvik-Neu baut auf", "NPC_HALLA|Halla (Eiðvik-Neu)", "SET_V_EIDVIKNEU", 3, 35,
  "Halla hat die Klangpest als Kind überlebt und lebt seitdem in Eiðvik-Neu. Das Dorf will ein Gemeinschaftshaus bauen, aber niemand traut sich, Holz aus dem alten Eiðvik zu holen. Der Wärter begleitet Halla in die Ruinen – sie will selbst gehen.",
  ["OBJ_TALK NPC_HALLA 1 @SET_V_EIDVIKNEU | Halla und der Plan",
   "OBJ_ESCORT NPC_HALLA 1 @R07_Z02 | Halla in die Ruinen begleiten",
   "OBJ_INVESTIGATE - 2 @R07_Z02 | Tragfähige Balken finden",
   "OBJ_OBSERVE ECHO_173 1 @R07_Z02 | Das Eidwacht, das über den Ruinen wacht, beobachten",
   "OBJ_REST SET_V_EIDVIKNEU 1 @SET_V_EIDVIKNEU | Richtfest"],
  "Hain-Dekor ITM_DECO_EIDVIKBEAM; ITM_MAT_FROSTPINE ×4", "Gemeinschaftshaus in Eiðvik-Neu (Data Layer); Halla erzählt Besuchern von früher")
Q("SQ_144", "Die Schwester im Kloster", "NPC_SCHWESTER_IVRA|Schwester Ivra", "LOC_KLOSTER_SCHWEIGFELS", 3, 40,
  "Leif aus Fjallstad hat seine Schwester Gunnhild seit Jahren nicht gesprochen – sie trat dem Orden bei und legte das Schweigegelübde ab. Nach dem Verrat fragt Ivra, ob der Wärter Leifs Brief überbringen will. Gunnhild antwortet auf ihrer Schiefertafel.",
  ["OBJ_TALK NPC_LEIF 1 @SET_V_FJALLSTAD | Leifs Brief",
   "OBJ_GOTO LOC_KLOSTER_SCHWEIGFELS 1 @R07_Z03 | Über den Pass nach Schweigfels",
   "OBJ_DELIVER ITM_KEY_LEIFLETTER 1 @LOC_KLOSTER_SCHWEIGFELS | Gunnhild den Brief geben",
   "OBJ_CHOICE DLG_SQ_144_01 1 @LOC_KLOSTER_SCHWEIGFELS | Gunnhilds Tafel nach Fjallstad tragen – oder sie überreden, selbst zu gehen"],
  "ITM_CON_WARM ×2; Kodex-Fragment „Gelübde und Familie“", "Gunnhild besucht Fjallstad (Nachhall) oder schreibt Briefe (Bark)", truth=7)
Q("SQ_145", "Was das Eis behält", "NPC_R07_RUNA|Runa die Erinnernde", "SET_C_HVITMARK", 3, 35,
  "Im Nachhall bemerkt Runa, dass Uvasils – Leere-Frost-Echos – sich an den Stellen sammeln, wo früher Stillsteine lagen. Sie fragt sich, ob das Eis die Stille „behält“. Der Wärter beobachtet drei Plätze und vergleicht sie mit Ordensakten.",
  ["OBJ_OBSERVE ECHO_166 3 @R07_Z04 | Uvasils an drei ehemaligen Steinplätzen beobachten",
   "OBJ_INVESTIGATE - 2 @LOC_KLOSTER_SCHWEIGFELS | Ordensakten zu den Steinplätzen lesen",
   "OBJ_TALK NPC_R07_RUNA 1 @SET_C_HVITMARK | Runa die Deutung bringen"],
  "Kodex-Fragment „Eisgedächtnis“; ITM_EVO_AURORATHREAD", "Uvasil-Plätze als Beobachtungspunkte (Kodex)", var="Time=Night", truth=9)
Q("SQ_146", "Der Pass der Schweigenden", "NPC_SCHWESTER_IVRA|Schwester Ivra", "LOC_KLOSTER_SCHWEIGFELS", 4, 40,
  "Venn-treue Ordensleute halten den oberen Pass. Sechs Novizen wollen nach Schweigfels zu Sereth, ohne Kampf. Ivra führt sie, der Wärter sichert den Weg – im Schneesturm, mit Hallkids als Rufkette.",
  ["OBJ_CONDITION Weather=Snow 1 @R07_Z03 | Schneesturm am Pass",
   "OBJ_ESCORT NPC_SCHWESTER_IVRA 1 @R07_Z03 | Die Novizen über den Pass führen",
   "OBJ_OBSERVE ECHO_175 1 @R07_Z03 | Ein Hallbrand als Rufkette nutzen",
   "OBJ_FLEE ROUTE_SQ146 1 @R07_Z03 | Angekündigter Posten der Venn-Treuen – im Sturm umgehen"],
  "ITM_GEAR_CLOAK_4; Kodex-Fragment „Novizen“", "Sechs Novizen in Schweigfels (Gesten-Barks)", var="Weather=Snow", truth=7)
Q("SQ_147", "Aurora-Fotografie", "NPC_FOTOGRAFIN_SIGNE|Fotografin Signe (Akademie)", "SET_C_HVITMARK", 3, 30,
  "Signe will das erste Foto eines Lysthane im Polarlicht für die Akademie-Ausstellung. Lysthanes erscheinen nur, wenn die Aurora singt – und fliehen vor Kameras, die klicken. Der Wärter lernt, mit der Kodex-Linse lautlos zu arbeiten.",
  ["OBJ_TALK NPC_FOTOGRAFIN_SIGNE 1 @SET_C_HVITMARK | Signes Ausrüstung",
   "OBJ_CONDITION Weather=Aurora 1 @R07_Z04 | Polarlicht",
   "OBJ_OBSERVE ECHO_169 1 @R07_Z04 | Das Verhalten der Lysthanes vor dem Foto beobachten",
   "OBJ_PHOTO ECHO_169 1 @R07_Z04 | Ein Lysthane im Polarlicht (≥ 4 Sterne)"],
  "ITM_GEAR_LENS_3; Hain-Dekor ITM_DECO_AURORAPRINT", "Foto in der Akademie-Ausstellung (Dorunsruh, Nachhall)", var="Weather=Aurora")
Q("SQ_148", "Ulreks Buße", "NPC_SCHWESTER_IVRA|Schwester Ivra", "LOC_KLOSTER_SCHWEIGFELS", 5, 45,
  "Ulrek, einst Gegner des Wärters, will die Stillsteine bergen, die er selbst gesetzt hat. Er kennt jeden Ort. Er bittet nicht um Vergebung, nur um Begleitung – „damit jemand sieht, dass es getan wird“.",
  ["OBJ_TALK NPC_ULREK 1 @LOC_KLOSTER_SCHWEIGFELS | Ulrek im Hof des Klosters",
   "OBJ_ESCORT NPC_ULREK 1 @R07_Z04 | Mit Ulrek zu seinen Steinen",
   "OBJ_HEALZONE ZONE_SQ148 3 @R07_Z04 | Drei Steinplätze heilen",
   "OBJ_CHOICE DLG_SQ_148_01 1 @R07_Z04 | Ulrek antworten, als er fragt, ob es genug ist"],
  "ITM_EMAT_STILLSHARD ×2; Kodex-Fragment „Ulrek“", "Ulrek arbeitet für die Wildwacht (Nachhall-Bark) oder bleibt im Kloster", truth=7)
Q("SQ_149", "Sigruns Eisprobe", "NPC_SIGRUN|Sigrun Fjall", "SET_C_HVITMARK", 5, 35,
  "Sigrun lädt zur Eisprobe auf dem Spiegelsee: zwei Kämpfe, bei denen jeder dritte Zug auf dem Eis rutscht und die Formation durcheinanderwirft. Danach erzählt sie von ihrer Großmutter, die die Klangpest überlebte.",
  ["OBJ_TALK NPC_SIGRUN 1 @SET_C_HVITMARK | Sigruns Einladung",
   "OBJ_BATTLE NPC_EISPRUEFER_1 1 @SET_C_HVITMARK | Erste Probe auf dem Eis",
   "OBJ_BATTLE NPC_SIGRUN 1 @SET_C_HVITMARK | Sigrun selbst",
   "OBJ_OBSERVE ECHO_247 1 @SET_C_HVITMARK | Unter dem Spiegelsee lauschen (Isv'aldr)"],
  "ITM_HELD_TONE_FROST; ITM_KS_062", "Sigrun-Barks; Eistraining", pre="Akkorde>=6")
Q("SQ_150", "Gast der Stille", "NPC_SCHWESTER_IVRA|Schwester Ivra", "LOC_KLOSTER_SCHWEIGFELS", 5, 55,
  "Am Ende der Kette lädt Sereth den Wärter ein, eine Stille Stunde mit dem ganzen Kloster zu verbringen – nicht als Bekehrung, sondern als Dank. Danach spricht Sereth zum ersten Mal vor allen Ordensleuten laut: über Venn, über Schuld, über eine Stille, die niemanden zwingt.",
  ["OBJ_TALK NPC_SERETH 1 @LOC_KLOSTER_SCHWEIGFELS | Sereths Einladung",
   "OBJ_REST LOC_KLOSTER_SCHWEIGFELS 1 @LOC_KLOSTER_SCHWEIGFELS | Die Stille Stunde",
   "OBJ_OBSERVE ECHO_163 1 @R07_Z03 | Uvlets, die sich zum Kloster setzen, beobachten",
   "OBJ_CHOICE DLG_SQ_150_01 1 @LOC_KLOSTER_SCHWEIGFELS | Sereth nach ihrer Rede antworten"],
  "Titel „Gast der Stille“; Hain-Dekor ITM_DECO_VEILEDWELL", "Kloster öffnet den Hof für Besucher; Stille Stunde täglich (K47 REP_STILLHOUR)", truth=7)
Q("SQ_151", "Die Pause im Gletscher", "NPC_SCHWESTER_IVRA|Schwester Ivra", "LOC_KLOSTER_SCHWEIGFELS", 4, 45,
  "Nach dem Finale sagt Ivra, dass man die Pause an manchen Orten hören kann – dort, wo Velnox den Riegel berührte. Der erste ist eine Spalte im Gletscher. Wer dort still ist, hört zwischen zwei Tönen etwas, das kein Ton ist.",
  ["OBJ_GOTO R07_Z04 1 @R07_Z04 | Zur Gletscherspalte",
   "OBJ_REST R07_Z04 1 @R07_Z04 | Eine Stunde Stille in der Spalte",
   "OBJ_OBSERVE ECHO_178 1 @R07_Z04 | Ein Tysvorn, das ruhig neben dem Wärter liegt, beobachten",
   "OBJ_TALK NPC_SCHWESTER_IVRA 1 @LOC_KLOSTER_SCHWEIGFELS | Ivra berichten"],
  "Kodex-Fragment „Orte der Pause I“; ITM_LURE_TUNINGFORK", "Gletscherspalte als Ort der Pause (Rückkehr)", truth=9)

# ───────────────────────────── R08 Ael'Dorun ─────────────────────────────
Q("SQ_152", "Das Rektorat", "NPC_AEVRIN|Aevrin Thal", "SET_C_DORUNSRUH", 5, 45,
  "Aevrin öffnet Venns Rektorat. Zwischen Messprotokollen liegen Kinderzeichnungen – ein Keller, Echos über einer brennenden Stadt. Aevrin will Fakten für den Bundesrat; der Wärter findet auch den Menschen hinter den Fakten.",
  ["OBJ_TALK NPC_AEVRIN 1 @SET_C_DORUNSRUH | Aevrin am versiegelten Rektorat",
   "OBJ_INVESTIGATE - 4 @SET_C_DORUNSRUH | Das Rektorat durchsuchen",
   "OBJ_PUZZLE PZ_SQ152_SAFE 1 @SET_C_DORUNSRUH | Venns Glyphenschrank öffnen",
   "OBJ_CHOICE DLG_SQ_152_01 1 @SET_C_DORUNSRUH | Was in die Akte kommt"],
  "Lore „Venns Kindheit“ (TruthLevel 6); ITM_CON_SENSE ×2", "Akte für den Bundesrat; Venn-Barks in Dorunsruh werden nachdenklicher", truth=6, pre=W6)
Q("SQ_153", "Der Tikkel im Uhrwerk", "NPC_UHRMACHER_ODIL|Uhrmacher Odil", "SET_V_SAEULENRAST", 2, 25,
  "Die alte dorunische Säulenuhr von Säulenrast tickt wieder – zum ersten Mal seit Jahrhunderten. Odil findet darin eine Tikkel-Familie, die die Zahnräder als Nest nutzt und bewegt. Er will die Uhr reparieren, ohne die Tikkels zu vertreiben.",
  ["OBJ_TALK NPC_UHRMACHER_ODIL 1 @SET_V_SAEULENRAST | Odil an der Säulenuhr",
   "OBJ_OBSERVE ECHO_185 2 @SET_V_SAEULENRAST | Tikkels im Uhrwerk beobachten",
   "OBJ_PUZZLE PZ_SQ153_GEARS 1 @SET_V_SAEULENRAST | Zahnräder so setzen, dass Nest und Uhr laufen"],
  "ITM_HELD_TAKTRING; Kodex-Beobachtung Tikkel", "Die Säulenuhr schlägt die Stunden (Ambient, Säulenrast)")
Q("SQ_154", "Akten für den Bundesrat", "NPC_AEVRIN|Aevrin Thal", "SET_C_DORUNSRUH", 6, 60,
  "Aevrin legt die Akte über Venn dem Bundesrat vor – per Klangbrief aus Dorunsruh, mit dem Wärter als Zeugen. Die Räte streiten, ob die Akademie aufgelöst werden soll. Aevrin will nicht Venn retten, sondern die Akademie.",
  ["OBJ_TALK NPC_AEVRIN 1 @SET_C_DORUNSRUH | Aevrin vor der Sitzung",
   "OBJ_CHOICE DLG_SQ_154_01 1 @SET_C_DORUNSRUH | Als Zeuge sprechen",
   "OBJ_OBSERVE ECHO_183 1 @SET_C_DORUNSRUH | Ein Thaelon im Sitzungssaal beobachten (Zeugenritual der Dorunier)",
   "OBJ_CHOICE DLG_SQ_154_02 1 @SET_C_DORUNSRUH | Empfehlung an den Bundesrat"],
  "Titel „Zeuge des Bundes“; ITM_GEAR_RESONATOR_4", "Bundesrat stellt die Akademie unter Aufsicht (Nachhall: kommissarisch Aevrin, K47)", truth=6, pre=W6,
  solution="Auflösung empfehlen · Aufsicht durch den Bund · Akademie unter Aevrin mit offenen Archiven (dritte Lösung).")
Q("SQ_155", "Neumond der Skrivs", "NPC_GLYPHENSTUDENTIN_MAREK|Glyphenstudent Marek", "SET_V_THAELUUN", 3, 30,
  "Bei Neumond schreiben Skrivs leuchtende Glyphen in die Luft über Thae'Luun. Marek glaubt, sie schreiben ab – Glyphen von den Säulen. Der Wärter vergleicht und findet einen Fehler, den die Skrivs korrigieren.",
  ["OBJ_CONDITION Moon=New 1 @R08_Z02 | Neumond",
   "OBJ_OBSERVE ECHO_179 2 @R08_Z02 | Skrivs beim Schreiben beobachten",
   "OBJ_PHOTO ECHO_181 1 @R08_Z02 | Ein Skriveth-Zeichen fotografieren",
   "OBJ_INVESTIGATE - 2 @R08_Z02 | Die Glyphe mit der Säule vergleichen"],
  "ITM_EVO_GLYPHSHARD; Kodex-Fragment „Skriv-Korrektur“", "Neumond der Skrivs als Weltereignis (WE_SKRIV_NEWMOON)", var="Moon=New")
Q("SQ_156", "Studentenstreik", "NPC_STUDENTIN_HELKE|Studentin Helke", "SET_C_DORUNSRUH", 4, 40,
  "In Akt III streiken die Studierenden der Akademie: Sie wollen offene Archive, ein Ethikgremium für Echo-Forschung und kein Wort mehr von „Ordnung“. Die Professorenschaft ist gespalten. Helke bittet den Wärter, mit beiden Seiten zu reden.",
  ["OBJ_TALK NPC_STUDENTIN_HELKE 1 @SET_C_DORUNSRUH | Helke auf der Mensatreppe",
   "OBJ_TALK NPC_PROFESSOR_ALBRECHT 1 @SET_C_DORUNSRUH | Professor Albrecht zuhören",
   "OBJ_OBSERVE ECHO_193 1 @SET_C_DORUNSRUH | Hymlits, die mit den Streikenden singen, beobachten",
   "OBJ_CHOICE DLG_SQ_156_01 1 @SET_C_DORUNSRUH | Einen Kompromiss vorschlagen"],
  "ITM_KS_064; Hain-Dekor ITM_DECO_STRIKEBANNER", "Ethikgremium der Akademie (K47 Nachhall-Zustand)", truth=7)
Q("SQ_157", "Glyphen-Übersetzung", "NPC_R08_AEVRIN_TUTOR|Professor Thal (Sprechstunde)", "SET_C_DORUNSRUH", 4, 45,
  "Zehn Glyphentafeln, verteilt über Dorunsruh, Thae'Luun und das Archontenviertel, ergeben zusammen einen Text – die letzte Ansprache des Erstchors vor der Großen Stille. Aevrin übersetzt seit Jahren. Der Wärter findet die Tafeln; das Lesen gelingt erst mit dem Akkord von Dorunsruh.",
  ["OBJ_TALK NPC_R08_AEVRIN_TUTOR 1 @SET_C_DORUNSRUH | Aevrins Sprechstunde",
   "OBJ_PUZZLE PZ_SQ157_TABLET 10 @R08 | Zehn Glyphentafeln finden und abhören",
   "OBJ_CONDITION Quest.MQ_A2_09 1 @SET_C_DORUNSRUH | Mit dem Akkord von Dorunsruh lesen",
   "OBJ_INVESTIGATE - 1 @SET_C_DORUNSRUH | Den Text zusammensetzen"],
  "Lore „Ansprache des Erstchors“ (TruthLevel 7); ITM_LURE_GLYPHTOKEN", "Text in der Akademie-Bibliothek; Klangfragment wird entzerrt",
  truth=7, pre="Quest.MQ_A2_10")
Q("SQ_158", "Kaels Forschungsarbeit", "NPC_PELL|Archivarin Pell", "SET_C_DORUNSRUH", 4, 40,
  "Kael hat in Dorunsruh an einer Arbeit geschrieben: „Hören ohne Gabe“. Vor dem Verrat bittet er den Wärter, Versuche zu bezeugen; danach findet Pell die halbfertige Arbeit in seinem verlassenen Labor und bittet den Wärter, sie zu lesen, bevor sie archiviert wird. Beide Fassungen enden mit derselben Frage.",
  ["OBJ_TALK NPC_PELL 1 @SET_C_DORUNSRUH | Pell (vor W6: Kael selbst) im Labor",
   "OBJ_OBSERVE ECHO_194 2 @SET_C_DORUNSRUH | Kaels Hymnora-Versuche beobachten oder nachstellen",
   "OBJ_INVESTIGATE - 2 @SET_C_DORUNSRUH | Kaels Notizen lesen",
   "OBJ_CHOICE DLG_SQ_158_01 1 @SET_C_DORUNSRUH | Kaels Frage beantworten: „Kann man lernen zu hören?“"],
  "ITM_KS_066; Kodex-Fragment „Hören ohne Gabe“", "Kaels Arbeit in der Bibliothek; KAEL_TRUST-Dialoge in Akt III erhalten einen Rückbezug")
Q("SQ_159", "Chronaires Uhr", "NPC_UHRMACHER_ODIL|Uhrmacher Odil", "SET_V_SAEULENRAST", 4, 40,
  "Im Nachhall läuft die Säulenuhr manchmal rückwärts – genau eine Minute, jeden Mittag. Odil hält es für einen Defekt. Der Wärter erkennt eine Spur: Chronaire, das Mythische der Zeit, prüft die, die es suchen, mit Zeitherausforderungen (K62).",
  ["OBJ_CONDITION Time=Day 1 @SET_V_SAEULENRAST | Mittag an der Säulenuhr",
   "OBJ_INVESTIGATE - 3 @SET_V_SAEULENRAST | Die rückwärts laufende Minute untersuchen",
   "OBJ_PUZZLE PZ_SQ159_MINUTE 1 @SET_V_SAEULENRAST | In der rückwärts laufenden Minute die Glyphe setzen",
   "OBJ_OBSERVE ECHO_252 1 @R08 | Ein Flackern von Chronaire bemerken"],
  "Kodex-Eintrag Chronaire (Gerücht); ITM_LURE_TUNINGFORK", "Spur „Chronaire“ im Kodex aktiv (K62)", var="Time=Day", truth=9)
Q("SQ_160", "Die Prüfung der Hörerin", "NPC_KIND_TAMSIN|Tamsin (Hörerin)", "SET_C_DORUNSRUH", 3, 30,
  "Eine junge Hörerin, Tamsin aus Fennhaven (SQ_051), studiert jetzt in Dorunsruh – mit Stipendium der Wildwacht. Sie fürchtet ihre Kodex-Prüfung und bittet den Wärter, mit ihr zu üben: draußen, nicht im Hörsaal.",
  ["OBJ_TALK NPC_KIND_TAMSIN 1 @SET_C_DORUNSRUH | Tamsin vor der Prüfung",
   "OBJ_OBSERVE ECHO_182 2 @R08_Z02 | Mit Tamsin Thaelits beobachten",
   "OBJ_PHOTO ECHO_195 1 @R08_Z01 | Ein Optil für Tamsins Arbeit fotografieren",
   "OBJ_TALK NPC_KIND_TAMSIN 1 @SET_C_DORUNSRUH | Tamsin zur Prüfung bringen"],
  "ITM_GEAR_LENS_3; Kodex-Beobachtung Thaelit", "Tamsin besteht; Bark-Kette über „die Hörerin aus dem Moor“", pre="Quest.SQ_051")
Q("SQ_161", "Der Hehler", "NPC_R08_GRAVE|Hehler Grave", "SET_C_DORUNSRUH", 4, 40,
  "Grave handelt mit Fundstücken aus den Ruinen – meist harmlos, manchmal nicht. Er bietet dem Wärter einen Klangsplitter-Ring an, der einem Sarkon gestohlen wurde, dessen Nest nun leer klingt. Grave sagt, er habe es ehrlich gekauft. Er lügt nicht ganz.",
  ["OBJ_TALK NPC_R08_GRAVE 1 @SET_C_DORUNSRUH | Graves Angebot",
   "OBJ_OBSERVE ECHO_189 1 @R08_Z03 | Das Sarkon am leeren Nest beobachten",
   "OBJ_INVESTIGATE - 2 @SET_C_DORUNSRUH | Den Weg des Rings zurückverfolgen",
   "OBJ_CHOICE DLG_SQ_161_01 1 @SET_C_DORUNSRUH | Was mit Grave und dem Ring geschieht"],
  "ITM_HELD_LASTBREATH; Kodex-Beobachtung Sarkon", "Ring zurück im Nest; Grave handelt vorsichtiger (oder schließt)", var="Time=Night",
  solution="Ring kaufen und zurückbringen · Grave melden · Grave den Weg zeigen, den der Ring genommen hat, und ihn zum Rückgabeweg bewegen (dritte Lösung).")
Q("SQ_162", "Venns leeres Zimmer", "NPC_AEVRIN|Aevrin Thal", "SET_C_DORUNSRUH", 3, 30,
  "In Akt III bittet Aevrin den Wärter um etwas Seltsames: Venns privates Zimmer aufzuräumen, bevor die Studierenden es zum Gedenkraum für die Opfer der Siegelkriege machen. Es ist ein einfaches Zimmer. An der Wand: ein Brief an seine Eltern, nie abgeschickt.",
  ["OBJ_GOTO SET_C_DORUNSRUH 1 @SET_C_DORUNSRUH | Zu Venns Zimmer",
   "OBJ_INVESTIGATE - 3 @SET_C_DORUNSRUH | Das Zimmer ordnen",
   "OBJ_CHOICE DLG_SQ_162_01 1 @SET_C_DORUNSRUH | Was mit dem Brief geschieht"],
  "Kodex-Fragment „Ein Brief an die Eltern“", "Gedenkraum der Siegelkriege in Dorunsruh; Venns Brief liegt aus, verbrannt oder ist im Epilog bei ihm", truth=7)
Q("SQ_163", "Der Bruder, der spricht", "NPC_BRUDER_ODVAR|Bruder Odvar", "SET_V_SAEULENRAST", 2, 25,
  "Bruder Odvar spricht außerhalb des Klosters, weil sein Gelübde nur innerhalb der Mauern gilt. Er sammelt Wörter, die Menschen nie mehr sagen – „weil man sie aufbewahren muss, wenn man schweigt“. Der Wärter hilft, drei solche Wörter zu finden.",
  ["OBJ_TALK NPC_BRUDER_ODVAR 1 @SET_V_SAEULENRAST | Odvars Wortsammlung",
   "OBJ_INVESTIGATE - 3 @R08 | Drei vergessene Wörter in Inschriften und Gesprächen finden",
   "OBJ_CHOICE DLG_SQ_163_01 1 @SET_V_SAEULENRAST | Ein eigenes Wort für Odvars Sammlung"],
  "Hain-Dekor ITM_DECO_WORDBOX; Kodex-Fragment „Odvars Wörter“", "Odvar liest Besuchern die Wörter vor (Bark)", var="Time=Dusk")
Q("SQ_164", "Die große Stille am Archontenviertel", "NPC_WILDWAECHTER_BOAZ|Wildwächter Boaz", "SET_O_ARCHONTENWACHT", 5, 45,
  "Die Archontenwacht bewacht die größte Stillezone des Kontinents. Nach der Heilung durch den Akkord bleibt ein Kern, den kein Wärter allein schließen kann. Boaz organisiert einen Heilkreis aus Wildwacht, Akademie und – auf Wunsch des Wärters – Ordensleuten.",
  ["OBJ_TALK NPC_WILDWAECHTER_BOAZ 1 @SET_O_ARCHONTENWACHT | Boaz an der Wacht",
   "OBJ_CHOICE DLG_SQ_164_01 1 @SET_O_ARCHONTENWACHT | Wer in den Heilkreis kommt",
   "OBJ_HEALZONE ZONE_SQ164 4 @R08_Z03 | Vier Heilkreise im Archontenviertel schließen",
   "OBJ_OBSERVE ECHO_190 1 @R08_Z03 | Ein Sarkothar, das aus der Zone erwacht, beobachten"],
  "ITM_GEAR_RESONATOR_4; Titel „Kernheiler“", "Archontenviertel als begehbare Ruine (Data Layer)", pre="Quest.MQ_A2_09")
Q("SQ_165", "Der Wächter ohne Splitter", "NPC_DR_IMKE_VAEL|Dr. Imke Vael", "SET_V_THAELUUN", 3, 35,
  "Im Nachhall steht Thaelarch noch immer vor dem leeren Thron. Imke Vael fragt, was ein Wächter tut, wenn es nichts mehr zu bewachen gibt. Der Wärter beobachtet ihn über drei Tage.",
  ["OBJ_OBSERVE ECHO_184 3 @R08_Z04 | Thaelarch an drei Tagen beobachten",
   "OBJ_INVESTIGATE - 2 @R08_Z04 | Spuren seiner neuen Wege finden",
   "OBJ_TALK NPC_DR_IMKE_VAEL 1 @SET_V_THAELUUN | Imke berichten"],
  "Kodex-Fragment „Der Wächter ohne Splitter“; ITM_HELD_SHIELDBROOCH", "Thaelarch bewacht nun den Gedenkraum oder die Kinder von Thae'Luun (Ambient)", truth=9)
Q("SQ_166", "Gefangene Gelehrsamkeit", "NPC_FS_ZELLE_DORUNSRUH|Zelle Dorunsruh (Freie Stimmen)", "SET_C_DORUNSRUH", 5, 45,
  "Unter Venn liefen in einem Nebenlabor Versuche mit verstummten Echos. Nach dem Verrat ist das Labor versiegelt – mit den Echos darin. Die Freien Stimmen wollen einbrechen; Aevrin würde öffnen, braucht aber Tage für die Genehmigung.",
  ["OBJ_TALK NPC_FS_ZELLE_DORUNSRUH 1 @SET_C_DORUNSRUH | Die Zelle in der Unterstadt von Dorunsruh",
   "OBJ_CHOICE DLG_SQ_166_01 1 @SET_C_DORUNSRUH | Einbruch oder Genehmigung",
   "OBJ_HEALZONE ZONE_SQ166 3 @SET_C_DORUNSRUH | Drei verstummte Echos im Labor heilen",
   "OBJ_OBSERVE ECHO_191 1 @SET_C_DORUNSRUH | Ein Tilgel nach der Heilung beobachten"],
  "ITM_CON_CLEANSE ×3; Laborakte (Lore)", "Labor wird Ruheort für Echos (Akademie, Nachhall)", truth=6, pre=W6)
Q("SQ_167", "Die Bibliothek der Resonanz", "NPC_DR_IMKE_VAEL|Dr. Imke Vael", "SET_V_THAELUUN", 3, 35,
  "Dr. Imke Vael, Nachfahrin des Taxonomen, baut in Thae'Luun eine „Bibliothek der Resonanz“: Klangproben aller Arten. Sie bittet um Proben aus drei Regionen und um Hilfe beim Katalog. Wer ihr hilft, erhält eine Kopie für den eigenen Kodex.",
  ["OBJ_TALK NPC_DR_IMKE_VAEL 1 @SET_V_THAELUUN | Imke in der Bibliothek",
   "OBJ_OBSERVE ECHO_180 1 @R08_Z02 | Klangprobe Skrivar",
   "OBJ_OBSERVE ECHO_197 1 @R08_Z03 | Klangprobe Menhirok",
   "OBJ_PUZZLE PZ_SQ167_CATALOG 1 @SET_V_THAELUUN | Proben katalogisieren"],
  "Kodex-Funktion „Klangarchiv“ (Rufe aller registrierten Arten abspielbar); ITM_KS_067", "Bibliothek der Resonanz in Thae'Luun (Lore-Sammelort)", var="Time=Night")
Q("SQ_168", "Hymnoras Chor", "NPC_FS_ZELLE_DORUNSRUH|Zelle Dorunsruh (Freie Stimmen)", "SET_C_DORUNSRUH", 4, 40,
  "In Akt III wollen die Freien Stimmen und die Studierenden einen Chor aus Hymnoras gründen, die freiwillig singen – als Gegenbild zum Krone-Motiv. Hymnoras singen aber nur zusammen, wenn sie einander kennen. Der Wärter bringt drei Gruppen zusammen.",
  ["OBJ_OBSERVE ECHO_194 3 @R08_Z02 | Drei Hymnora-Gruppen beobachten",
   "OBJ_ESCORT NPC_STUDENTIN_HELKE 1 @SET_C_DORUNSRUH | Mit Helke die Gruppen zum Säulenfeld führen",
   "OBJ_CHOICE DLG_SQ_168_01 1 @R08_Z02 | Das erste Lied wählen",
   "OBJ_REST R08_Z02 1 @R08_Z02 | Dem Chor zuhören"],
  "Hain-Dekor ITM_DECO_CHOIRSTONE; ITM_LURE_WINDCHIME", "Freier Chor auf dem Säulenfeld (Ambient, Dämmerung)", var="Time=Dusk", truth=7)
Q("SQ_169", "Glyphenduell", "NPC_GLYPHENFECHTER_IVO|Glyphenfechter Ivo", "SET_C_DORUNSRUH", 5, 35,
  "Im Glyphenhof fordert Ivo, Aevrins Assistent, zum Duell nach alter Regel: Jede Fähigkeit hinterlässt eine Glyphe, die in der nächsten Runde wirkt. Zwei Kämpfe; wer Glyphen liest, gewinnt.",
  ["OBJ_TALK NPC_GLYPHENFECHTER_IVO 1 @SET_C_DORUNSRUH | Ivos Herausforderung",
   "OBJ_BATTLE NPC_GLYPHENFECHTER_IVO 1 @SET_C_DORUNSRUH | Erstes Duell",
   "OBJ_BATTLE NPC_AEVRIN 1 @SET_C_DORUNSRUH | Aevrin selbst",
   "OBJ_OBSERVE ECHO_248 1 @SET_C_DORUNSRUH | Unter dem Glyphenhof lauschen (Ka'thurel)"],
  "ITM_HELD_TONE_ARCANE; ITM_KS_068", "Glyphentraining im Hof", pre="Akkorde>=7")
Q("SQ_170", "Die Kapelle im Archontenviertel", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_O_ARCHONTENWACHT", 3, 35,
  "Die zweite Station der Pause: Eine Ordenskapelle im Archontenviertel, in der die Stille seit dem Finale anders klingt. Ivra und Bruder Odvar warten dort mit einer Frage, die sie nicht aufschreiben wollen.",
  ["OBJ_GOTO R08_Z03 1 @R08_Z03 | Zur Kapelle",
   "OBJ_REST R08_Z03 1 @R08_Z03 | Eine Stunde in der Kapelle",
   "OBJ_OBSERVE ECHO_192 1 @R08_Z03 | Ein Tilgrath, das in der Kapelle schläft, beobachten",
   "OBJ_CHOICE DLG_SQ_170_01 1 @R08_Z03 | Ivras Frage beantworten"],
  "Kodex-Fragment „Orte der Pause II“", "Kapelle als Ort der Pause", truth=9)
Q("SQ_171", "Schatten zwischen den Säulen", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_V_THAELUUN", 4, 40,
  "Tilgels verschwinden im Nachhall zwischen den Säulen von Thae'Luun – nicht weg, sondern in die Pause zwischen zwei Säulen. Ivra glaubt, sie zeigen, wo man hören kann. Der Wärter folgt ihnen bei Nebel.",
  ["OBJ_CONDITION Weather=Fog 1 @R08_Z02 | Nebel auf dem Säulenfeld",
   "OBJ_OBSERVE ECHO_191 2 @R08_Z02 | Tilgels zwischen den Säulen beobachten",
   "OBJ_INVESTIGATE - 3 @R08_Z02 | Die drei „stillen Lücken“ finden"],
  "Kodex-Fragment „Orte der Pause III“; ITM_TRAP_SHADE", "Säulenfeld-Lücken als Ort der Pause", var="Weather=Fog", truth=9)
Q("SQ_172", "Der Thron ohne Krone", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_C_DORUNSRUH", 4, 45,
  "Die vierte Station: der Thronsaal. Wo Maedryn die Krone aufsetzte und Ilen die Pause öffnete, ist es jetzt einfach still. Ka'thurel erinnert sich – und zeigt dem Wärter eine Erinnerung, die nicht Maedryn gehört, sondern einem einfachen Echo im Saal.",
  ["OBJ_GOTO POI_R08_9001 1 @R08_Z04 | In den Thronsaal",
   "OBJ_REST POI_R08_9001 1 @R08_Z04 | Stille am leeren Thron",
   "OBJ_OBSERVE ECHO_248 1 @R08_Z04 | Ka'thurels Erinnerung empfangen",
   "OBJ_TALK NPC_SCHWESTER_IVRA 1 @SET_C_DORUNSRUH | Ivra davon erzählen"],
  "Kodex-Fragment „Orte der Pause IV“; Klangfragment „Das Echo im Saal“", "Thronsaal als Ort der Pause", truth=9)

# ───────────────────────────── R09 Prismtiefen ─────────────────────────────
Q("SQ_173", "Labore im Krater", "NPC_LABORLEITERIN_SANNE|Laborleiterin Sanne (Akademie)", "SET_C_PRISMARA", 4, 40,
  "Die Akademie-Labore in Prismara messen die Energiekrise. Sanne braucht Werte aus drei Tiefen, um zu zeigen, dass der Puls von den Missklang-Adern ausgeht – nicht, wie der Rat glaubt, von den Kristallmärkten.",
  ["OBJ_TALK NPC_LABORLEITERIN_SANNE 1 @SET_C_PRISMARA | Sanne im Labor",
   "OBJ_INVESTIGATE - 3 @R09 | Messwerte in Glanzschacht, Quarzgrund und Kaverne nehmen",
   "OBJ_OBSERVE ECHO_213 1 @R09_Z04 | Misslits am Rand der Adern beobachten",
   "OBJ_TALK NPC_R09_SEREN 1 @SET_C_PRISMARA | Seren Quarz (Stimmergilde) die Werte zeigen"],
  "ITM_GEAR_LENS_4; Kodex-Fragment „Puls“", "Rat von Prismara verlagert Energie auf alte Lichtschächte", truth=7)
Q("SQ_174", "Spatlings im Dunkeln", "NPC_SCHLEIFERIN_NYX|Schleiferin Nyx", "SET_V_QUARZGRUND", 2, 25,
  "In Quarzgrund, 310 Meter unter dem Kraterrand, ist es dunkel – Nyx schleift bei Spatling-Licht. Seit der Energiekrise leuchten die Spatlings schwächer. Nyx glaubt, sie hungern; der Wärter findet heraus, dass sie sich vor dem Puls verstecken.",
  ["OBJ_TALK NPC_SCHLEIFERIN_NYX 1 @SET_V_QUARZGRUND | Nyx in der Schleiferei",
   "OBJ_OBSERVE ECHO_203 2 @R09_Z02 | Spatlings im Dunkeln beobachten",
   "OBJ_INVESTIGATE - 2 @R09_Z02 | Ihre Verstecke finden",
   "OBJ_CHOICE DLG_SQ_174_01 1 @SET_V_QUARZGRUND | Nyx einen Schutzraum vorschlagen"],
  "ITM_GEAR_LANTERN_4; Kodex-Beobachtung Spatling", "Spatling-Schutzraum in Quarzgrund; Licht kehrt zurück", var="Time=Night")
Q("SQ_175", "Der Kristall, der zählt", "NPC_LABORLEITERIN_SANNE|Laborleiterin Sanne (Akademie)", "SET_C_PRISMARA", 3, 35,
  "Im Nachhall misst Sanne, wie schnell die Missklang-Adern verheilen (Neues Lied) oder erstarren (Sanfte Stille). Sie hat einen Kristall gezüchtet, der zählt – jede Stunde ein Ton weniger Missklang.",
  ["OBJ_TALK NPC_LABORLEITERIN_SANNE 1 @SET_C_PRISMARA | Sannes Zählkristall",
   "OBJ_INVESTIGATE - 3 @R09_Z04 | Den Kristall an drei Adern ablesen",
   "OBJ_OBSERVE ECHO_214 1 @R09_Z04 | Einen ruhigen Missgrath beobachten"],
  "Kodex-Fragment „Zählkristall“; ITM_MAT_GLYPHCRYSTAL ×2", "Sannes Messreihe je Ende verschieden (Kodex)", truth=9)
Q("SQ_176", "Kristallpuls-Nacht", "NPC_R09_SEREN|Seren Quarz (Stimmergilde)", "SET_C_PRISMARA", 3, 30,
  "Prismaras Fest: In einer Nacht pro Monat lässt die Stimmergilde alle Kristalle der Stadt im selben Takt pulsieren. Wegen der Energiekrise wollen sie es absagen. Seren bittet den Wärter, einen Takt zu finden, der den Puls der Adern ausgleicht statt verstärkt.",
  ["OBJ_CONDITION Time=Night 1 @SET_C_PRISMARA | Nacht in Prismara",
   "OBJ_OBSERVE ECHO_218 1 @R09_Z03 | Den Stalakkord-Takt hören",
   "OBJ_PUZZLE PZ_SQ176_PULSE 1 @SET_C_PRISMARA | Den Gegentakt setzen",
   "OBJ_REST SET_C_PRISMARA 1 @SET_C_PRISMARA | Das Fest erleben"],
  "Hain-Dekor ITM_DECO_PULSECRYSTAL; ITM_LURE_STARCHIME", "Kristallpuls-Nacht findet statt (Weltereignis WE_PULSE_NIGHT)", var="Time=Night", truth=7)
Q("SQ_177", "Psionits Traum", "NPC_R09_SEREN|Seren Quarz (Stimmergilde)", "SET_C_PRISMARA", 4, 35,
  "Psionits träumen laut: In ihrer Nähe sehen Menschen Bilder. Seren will der Akademie erlauben, die Bilder aufzuzeichnen; der Wärter fragt erst, ob die Psionits das wollen. Eine Beobachtung entscheidet, ob die Studie stattfindet.",
  ["OBJ_OBSERVE ECHO_215 2 @R09_Z05 | Psionits beim Träumen beobachten",
   "OBJ_INVESTIGATE - 2 @R09_Z05 | Die Bilder deuten",
   "OBJ_CHOICE DLG_SQ_177_01 1 @SET_C_PRISMARA | Seren raten"],
  "ITM_KS_071; Kodex-Beobachtung Psionit", "Studie mit Einwilligungsregel (Ethikgremium SQ_156) oder abgebrochen", var="Time=Night", truth=7)
Q("SQ_178", "Spiegel ohne Bild", "NPC_R09_QUILL|Glasbläserin Quill", "SET_C_PRISMARA", 3, 35,
  "Quills Spiegel zeigen manchmal einen Schemen, der nicht im Raum ist. Im Nachhall häufen sich die Berichte. Der Wärter dokumentiert die Schemen – die ersten Spuren von Mirrowisp, die erst mit der Fotografie-Meisterschaft greifbar werden (K39 §6).",
  ["OBJ_TALK NPC_R09_QUILL 1 @SET_C_PRISMARA | Quill und die Spiegel",
   "OBJ_PHOTO ECHO_253 1 @SET_C_PRISMARA | Den Schemen in einem Spiegel fotografieren (nur im Album sichtbar)",
   "OBJ_INVESTIGATE - 3 @R09 | Drei weitere Spiegelorte prüfen"],
  "Kodex-Eintrag Mirrowisp (Spur); ITM_LURE_MIRROR", "Spur „Mirrowisp“ im Kodex (K39, K62)", var="Time=Dusk", truth=9)
Q("SQ_179", "Das Stimmer-Archiv", "NPC_R09_BRANNOC_SR|Stimmwerkstatt Brannoc", "SET_C_PRISMARA", 3, 30,
  "Die Stimmwerkstatt hütet ein Archiv aller Stimmgabeln, die je in Prismara gefertigt wurden. Die Akademie will es digital – in Kristallabschriften – sichern. Der Werkstattmeister misstraut der Akademie. Der Wärter vermittelt.",
  ["OBJ_TALK NPC_R09_BRANNOC_SR 1 @SET_C_PRISMARA | Der Werkstattmeister",
   "OBJ_INVESTIGATE - 2 @SET_C_PRISMARA | Das Archiv sichten",
   "OBJ_OBSERVE ECHO_200 1 @R09_Z03 | Ein Klirrflug beim Nachsingen der Gabeln beobachten",
   "OBJ_CHOICE DLG_SQ_179_01 1 @SET_C_PRISMARA | Bedingungen für die Abschrift"],
  "ITM_LURE_TUNINGFORK; Rezept RCP_072", "Archiv-Abschrift in der Akademie (oder nur in Prismara)", truth=7)
Q("SQ_180", "Die Stalakkord-Orgel", "NPC_STEIGER_BRANNOC|Steiger Brannoc d. Ä.", "SET_V_GLANZSCHACHT", 4, 40,
  "Unter Glanzschacht liegt eine Höhle, deren Tropfsteine Stalakkords tragen. Der alte Steiger erzählt, dass man auf ihnen spielen kann – eine Orgel aus Echos. Wer das richtige Lied spielt, öffnet einen Gang zur Tiefen Resonanz.",
  ["OBJ_TALK NPC_STEIGER_BRANNOC 1 @SET_V_GLANZSCHACHT | Brannoc d. Ä. erzählt",
   "OBJ_OBSERVE ECHO_218 2 @R09_Z01 | Stalakkords bei der Antwort beobachten",
   "OBJ_PUZZLE PZ_SQ180_ORGAN 1 @R09_Z01 | Das Lied der Orgel spielen",
   "OBJ_GOTO R09_Z05 1 @R09_Z05 | Den neuen Gang betreten"],
  "ITM_KS_073; Abkürzung Glanzschacht–Tiefe Resonanz", "Neuer Gang (Data Layer); Orgel spielbar")
Q("SQ_181", "Kristallmarkt nach der Krise", "NPC_R09_SEREN|Kristallmarkt Seren", "SET_C_PRISMARA", 3, 30,
  "Im Nachhall ist die Energiekrise vorbei, aber der Kristallmarkt erholt sich nicht: Händler aus Saltrand kaufen billig, weil Prismara Geld braucht. Seren will einen fairen Preis – mit Hilfe des Kontors, ausgerechnet.",
  ["OBJ_TALK NPC_R09_SEREN 1 @SET_C_PRISMARA | Seren am Markt",
   "OBJ_INVESTIGATE - 2 @SET_C_PRISMARA | Die Preise vergleichen",
   "OBJ_TALK NPC_WIEBKE 1 @SET_C_PRISMARA | Wiebke per Klangbrief einbeziehen",
   "OBJ_CHOICE DLG_SQ_181_01 1 @SET_C_PRISMARA | Einen Preisrahmen vorschlagen"],
  "ITM_MAT_GLYPHCRYSTAL ×3; ITM_GEAR_BAG_4", "Fairer Kristallpreis (Händlerpreise R09 stabil)", truth=9)
Q("SQ_182", "Brannocs Erbe", "NPC_ILYX|Ilyx Brannoc", "SET_C_PRISMARA", 4, 45,
  "Ilyx ist ein Nachfahre der Lauscherin. Wer die Kette „Die Spur der Lauscherin“ abgeschlossen hat, bringt ihm deren Lied – das Ilyx nie ganz kannte. Ilyx und der Wärter sitzen eine Nacht neben einem Klirrathan, wie Brannoc 287 neben ihrem Echo saß.",
  ["OBJ_TALK NPC_ILYX 1 @SET_C_PRISMARA | Ilyx in der Prismenhalle",
   "OBJ_CHOICE DLG_SQ_182_01 1 @SET_C_PRISMARA | Brannocs Lied vorspielen (oder erzählen)",
   "OBJ_GOTO R09_Z03 1 @R09_Z03 | In die Kaverne",
   "OBJ_REST R09_Z03 1 @R09_Z03 | Eine Nacht in Stille",
   "OBJ_OBSERVE ECHO_201 1 @R09_Z03 | Das Klirrathan, das sich nähert, beobachten"],
  "Titel „Erbe der Lauscherin“; ITM_LURE_TUNINGFORK", "Ilyx-Dialoge im Nachhall; Klirrathan erscheint häufiger in der Kaverne", var="Time=Night")
Q("SQ_183", "Licht für die Oberwelt", "NPC_KONTORAGENTIN_RIEKE|Kontoragentin Rieke", "SET_C_PRISMARA", 4, 40,
  "Die Energiekrise lässt nicht nur Prismara flackern – auch die Lichter in Städten an der Oberwelt, die Prismara-Kristalle nutzen. Das Kontor will Ersatzkristalle aus Ignareth bringen. Der Wärter organisiert Lieferung und Einbau.",
  ["OBJ_TALK NPC_KONTORAGENTIN_RIEKE 1 @SET_C_PRISMARA | Rieke im Kontor",
   "OBJ_DELIVER ITM_MAT_SULFURCRYSTAL 4 @SET_C_PRISMARA | Ersatzkristalle aus Ignareth bringen",
   "OBJ_OBSERVE ECHO_210 1 @R09_Z03 | Facettors beim Ausrichten der Lichtschächte beobachten",
   "OBJ_PUZZLE PZ_SQ183_SHAFT 1 @R09_Z03 | Die Lichtschächte neu ausrichten"],
  "ITM_GEAR_LANTERN_4; ITM_CON_SENSE ×2", "Lichter in Prismara und an der Oberwelt stabil (globales Flackern endet, Data Layer)", truth=7)
Q("SQ_184", "Missklang verheilt", "NPC_LABORLEITERIN_SANNE|Laborleiterin Sanne (Akademie)", "SET_C_PRISMARA", 3, 30,
  "Misslits waren Missklang-Kinder. Im Nachhall verändern sie sich: Im Neuen Lied werden sie heller, in der Sanften Stille stiller. Sanne bittet um eine letzte Beobachtungsreihe, bevor sie Prismara verlässt.",
  ["OBJ_OBSERVE ECHO_213 3 @R09_Z04 | Misslits an drei Tagen beobachten",
   "OBJ_PHOTO ECHO_213 1 @R09_Z04 | Ein Foto für Sannes Abschied",
   "OBJ_TALK NPC_LABORLEITERIN_SANNE 1 @SET_C_PRISMARA | Sanne verabschieden"],
  "Kodex-Fragment „Missklang verheilt“; Hain-Dekor ITM_DECO_MISSLITLAMP", "Kodex Misslit: Nachhall-Verhalten je Ende", var="Time=Night", truth=9)
Q("SQ_185", "Glasbläser-Meisterwerk", "NPC_R09_QUILL|Glasbläserin Quill", "SET_C_PRISMARA", 4, 45,
  "Quill will ein Meisterwerk blasen: eine Glasharfe, auf der jedes Echo spielen kann. Dafür braucht sie Zutaten aus vier Regionen und einen Wärter, der Crafting-Stufe V beherrscht – oder bereit ist, es bei ihr zu lernen.",
  ["OBJ_TALK NPC_R09_QUILL 1 @SET_C_PRISMARA | Quills Entwurf",
   "OBJ_COLLECT ITM_MAT_SUNGLASS 3 @R04 | Sonnenglas aus Sahrun",
   "OBJ_COLLECT ITM_MAT_GLACIERQUARTZ 2 @R07 | Gletscherquarz aus Hvitfell",
   "OBJ_PUZZLE PZ_SQ185_HARP 1 @SET_C_PRISMARA | Die Glasharfe stimmen",
   "OBJ_OBSERVE ECHO_201 1 @SET_C_PRISMARA | Ein Klirrathan auf der Harfe spielen hören"],
  "Rezept RCP_075 (Crafting V); Hain-Dekor ITM_DECO_GLASSHARP", "Glasharfe im Kristallmarkt (spielbar)", truth=7)
Q("SQ_186", "Klirrathans Gesang", "NPC_FORSCHERIN_LIV|Meeresforscherin Liv", "SET_O_KRISTALLSEELAGER", 3, 30,
  "Liv, die Aquadrals am Riff erforschte (SQ_083), ist nach Prismtiefen gekommen: Klirrathans singen am Kristallsee in Intervallen wie Aquadrals leuchten. Gibt es eine Verbindung zwischen Meer und Kristall?",
  ["OBJ_TALK NPC_FORSCHERIN_LIV 1 @SET_O_KRISTALLSEELAGER | Liv am Kristallsee",
   "OBJ_OBSERVE ECHO_201 2 @R09_Z03 | Klirrathans nachts beobachten",
   "OBJ_INVESTIGATE - 2 @R09_Z03 | Intervalle mit Livs Riffdaten vergleichen",
   "OBJ_CHOICE DLG_SQ_186_01 1 @SET_O_KRISTALLSEELAGER | Livs These bewerten"],
  "ITM_KS_074; Kodex-Fragment „Mondzähler II“", "Kodex verknüpft Aquadral und Klirrathan (Mondzähler)", var="Time=Night", pre="Quest.SQ_083")
Q("SQ_187", "Das Rettungsseil", "NPC_STEIGER_BRANNOC|Steiger Brannoc d. Ä.", "SET_V_GLANZSCHACHT", 4, 40,
  "Im Nachhall gründet Brannoc d. Ä. eine Grubenwehr mit der Wildwacht. Die Übung: ein simulierter Einsturz in Glanzschacht, mit Mullhorns als Stützen und Ligravors, die Lasten schweben lassen.",
  ["OBJ_TALK NPC_STEIGER_BRANNOC 1 @SET_V_GLANZSCHACHT | Brannocs Übungsplan",
   "OBJ_OBSERVE ECHO_212 1 @R09_Z01 | Mullhorns beim Stützen beobachten",
   "OBJ_INVESTIGATE - 3 @R09_Z01 | „Verschüttete“ mit Resonanzsinn finden",
   "OBJ_ESCORT NPC_STEIGER_BRANNOC 1 @R09_Z01 | Die Übung abschließen"],
  "ITM_GEAR_TOOL_4; Wildwacht-Abzeichen „Grubenwehr“", "Grubenwehr Glanzschacht (Barks, schnellere Rettung bei Ereignissen)", truth=9)
Q("SQ_188", "Ilyx' Brechungsprobe", "NPC_ILYX|Ilyx Brannoc", "SET_C_PRISMARA", 6, 40,
  "Ilyx' Prismenhalle hat eine Brechungsregel: Fähigkeiten treffen gebrochen, ein Teil des Schadens geht auf das Nachbarziel. Die Probe besteht aus zwei Kämpfen und einem Rätsel, bei dem der Wärter Licht durch die Halle lenkt.",
  ["OBJ_BATTLE NPC_PRISMENPRUEFER_1 1 @SET_C_PRISMARA | Erste Brechung",
   "OBJ_PUZZLE PZ_SQ188_PRISM 1 @SET_C_PRISMARA | Das Licht durch die Halle lenken",
   "OBJ_BATTLE NPC_ILYX 1 @SET_C_PRISMARA | Ilyx",
   "OBJ_OBSERVE ECHO_249 1 @SET_C_PRISMARA | Prism'aion lauschen"],
  "ITM_HELD_TONE_CRYSTAL; ITM_KS_075", "Brechungstraining", pre="Akkorde>=9")
Q("SQ_189", "Verschüttete Stimmer", "NPC_STEIGER_BRANNOC|Steiger Brannoc d. Ä.", "SET_V_GLANZSCHACHT", 5, 45,
  "Ein Puls der Missklang-Adern hat einen Stollen in Glanzschacht einstürzen lassen; drei Stimmer der Gilde und ihre Facetins sind eingeschlossen. Diesmal ist es keine Übung.",
  ["OBJ_GOTO R09_Z01 1 @R09_Z01 | Zum eingestürzten Stollen",
   "OBJ_INVESTIGATE - 3 @R09_Z01 | Die Eingeschlossenen orten",
   "OBJ_TRAVERSE Mount.Dig 1 @R09_Z01 | Einen Rettungsgang graben",
   "OBJ_ESCORT NPC_STIMMER_JOREN 1 @SET_V_GLANZSCHACHT | Die Stimmer herausführen"],
  "ITM_GEAR_BOOTS_4; ITM_CON_HEAL_ALL ×2", "Stollen gesichert; Stimmer-Barks", truth=7)
Q("SQ_190", "Die Pause im Kristall", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_C_PRISMARA", 4, 40,
  "Die fünfte Station: In der Resonanzkammer, wo der zehnte Splitter lag, ist eine Lücke im Kristall – genau in der Form des Splitters. Wer hineinhorcht, hört die Pause am deutlichsten.",
  ["OBJ_GOTO POI_R09_9001 1 @R09_Z05 | In die Resonanzkammer",
   "OBJ_REST POI_R09_9001 1 @R09_Z05 | Stille an der Lücke",
   "OBJ_OBSERVE ECHO_202 1 @R09_Z05 | Ein Klirrnox, das die Lücke umkreist, beobachten",
   "OBJ_TALK NPC_SCHWESTER_IVRA 1 @SET_C_PRISMARA | Ivra berichten"],
  "Kodex-Fragment „Orte der Pause V“", "Lücke im Kristall als Ort der Pause", truth=9)

# ───────────────────────────── R10 Nimbara ─────────────────────────────
Q("SQ_191", "Orumas Sternkatalog", "NPC_STERNWAERTER_ELUN|Sternwärter Elun (Lumeya)", "SET_O_STERNWARTEORUMA", 3, 35,
  "Elun aus Lumeya führt die Sternwarte Oruma. Die Akademie will ihren Sternkatalog – Aerion hat 1.000 Jahre isoliert beobachtet. Elun ist bereit, wenn die Akademie im Gegenzug den Bodenkatalog teilt. Der Wärter überbringt und prüft.",
  ["OBJ_TALK NPC_STERNWAERTER_ELUN 1 @SET_O_STERNWARTEORUMA | Elun in der Sternwarte",
   "OBJ_OBSERVE ECHO_240 1 @R10_Z05 | Ein Astraviel bei Nacht beobachten",
   "OBJ_DELIVER ITM_KEY_STARCATALOG 1 @SET_C_AERION | Katalogabschrift ins Archiv der Baumeister bringen",
   "OBJ_CHOICE DLG_SQ_191_01 1 @SET_O_STERNWARTEORUMA | Tauschbedingungen festlegen"],
  "ITM_LURE_STARCHIME; Kodex-Fragment „Himmel über Aerion“", "Sternkatalog im Kodex (Himmelsereignisse vorhersagbar)", var="Time=Night", truth=7)
Q("SQ_192", "Lumaskiffs Heimweg", "NPC_WINDSEGLERIN_RIA|Windseglerin Ria", "SET_V_WOLKENRAST", 3, 30,
  "Ein junges Lumaskiff hat im Gewitter die Windbänder verlassen und landet erschöpft in Wolkenrast. Ria kennt die Bänder; der Wärter kennt Echos. Gemeinsam bringen sie es zurück zu seinem Schwarm.",
  ["OBJ_TALK NPC_WINDSEGLERIN_RIA 1 @SET_V_WOLKENRAST | Ria und das Lumaskiff",
   "OBJ_OBSERVE ECHO_239 1 @SET_V_WOLKENRAST | Das erschöpfte Lumaskiff beobachten",
   "OBJ_TRAVERSE Mount.Fly 1 @R10_Z01 | In die Windbänder fliegen",
   "OBJ_ESCORT NPC_WINDSEGLERIN_RIA 1 @R10_Z01 | Das Lumaskiff zum Schwarm führen"],
  "ITM_GEAR_GLIDER_4; Kodex-Beobachtung Lumaskiff", "Lumaskiff-Schwarm sichtbar über Wolkenrast", var="Weather=Thunderstorm")
Q("SQ_193", "Notizen von der Kronenwerft", "NPC_AEVRIN|Aevrin Thal", "SET_O_KRONENWERFTWACHT", 4, 40,
  "Im Nachhall sammelt Aevrin für die Akademie Venns Arbeitsnotizen von der Kronenwerft. Viele sind verweht. Der Wärter findet sie zwischen den Steinen – und eine, die Venn nach dem Finale geschrieben haben muss.",
  ["OBJ_GOTO R10_Z04 1 @R10_Z04 | Zur Kronenwerft",
   "OBJ_INVESTIGATE - 4 @R10_Z04 | Verwehte Notizen finden",
   "OBJ_OBSERVE ECHO_198 1 @R10_Z04 | Kronvaal, das zurückgekehrt ist, beobachten",
   "OBJ_TALK NPC_AEVRIN 1 @SET_C_AERION | Aevrin die Notizen per Klangbrief senden"],
  "Lore „Venns letzte Notiz“ (TruthLevel 9); ITM_GEAR_RESONATOR_5", "Notizen in der Akademie; Venn-Epilog erhält Rückbezug", truth=9)
Q("SQ_194", "Gewitterharfe", "NPC_R10_AELIA|Windhändlerin Aelia", "SET_C_AERION", 3, 30,
  "Bei Gewitter spielen Harfions auf den Spannseilen der Windanker – eine Harfe aus Sturm. Aelia sagt, früher hätten die Baumeister dazu getanzt, bis die Isolation das Fest vergessen ließ. Der Wärter bringt das Fest zurück.",
  ["OBJ_CONDITION Weather=Thunderstorm 1 @R10_Z01 | Gewitter über Nimbara",
   "OBJ_OBSERVE ECHO_230 2 @SET_O_WINDANKER | Harfions an den Seilen beobachten",
   "OBJ_PUZZLE PZ_SQ194_STRINGS 1 @SET_O_WINDANKER | Die Seile stimmen",
   "OBJ_REST SET_C_AERION 1 @SET_C_AERION | Das Gewitterfest"],
  "Hain-Dekor ITM_DECO_STORMHARP; ITM_LURE_WINDCHIME", "Gewitterharfe als Weltereignis (WE_STORM_HARP)", var="Weather=Thunderstorm")
Q("SQ_195", "Das Archiv der Baumeister", "NPC_R10_SIYEL_ARCHIVE|Archivar der Baumeister", "SET_C_AERION", 3, 35,
  "Das Archiv der Baumeister ist älter als die Akademie. Die Baumeister misstrauen der Akademie – sie kennen Maedryn. Der Archivar zeigt dem Wärter Pläne der Kronenwerft, damit „jemand vom Boden versteht, warum wir schweigen“.",
  ["OBJ_TALK NPC_R10_SIYEL_ARCHIVE 1 @SET_C_AERION | Der Archivar",
   "OBJ_INVESTIGATE - 3 @SET_C_AERION | Pläne der Kronenwerft studieren",
   "OBJ_OBSERVE ECHO_236 1 @R10_Z03 | Ein Levithar, das die Archivbücher schweben lässt, beobachten",
   "OBJ_CHOICE DLG_SQ_195_01 1 @SET_C_AERION | Was die Akademie erfahren darf"],
  "Lore „Kronenwerft-Pläne“ (TruthLevel 8); ITM_KS_077", "Archiv teilweise offen für die Akademie (Nachhall)", truth=8, pre="Quest.MQ_A3_02")
Q("SQ_196", "Aurelunes Sturmnacht", "NPC_STERNWAERTER_ELUN|Sternwärter Elun (Lumeya)", "SET_V_LUMEYA", 5, 45,
  "Im Nachhall sieht Elun in Resonanzsturm-Nächten ein Licht, das zugleich Leere ist, über Lumeya. Er glaubt an Aurelune. Der Wärter wartet mit ihm – ein Sturm muss kommen, natürlich oder mit der Sturmstimmgabel (CANON §63).",
  ["OBJ_CONDITION Weather=ResonanceStorm&Time=Night 1 @R10_Z02 | Resonanzsturm bei Nacht",
   "OBJ_OBSERVE ECHO_256 1 @R10_Z02 | Aurelunes Licht beobachten (Spur)",
   "OBJ_PHOTO ECHO_256 1 @R10_Z02 | Ein Foto der Erscheinung",
   "OBJ_TALK NPC_STERNWAERTER_ELUN 1 @SET_V_LUMEYA | Elun berichten"],
  "Kodex-Eintrag Aurelune (Spur); ITM_LURE_AURORAGLASS", "Spur „Aurelune“ im Kodex (K62)", var="Weather=ResonanceStorm & Time=Night", truth=9)
Q("SQ_197", "Wind gegen Fracht", "NPC_R10_AELIA|Windhändlerin Aelia", "SET_C_AERION", 3, 30,
  "Aelia handelt zwischen den Inseln mit Windkarten. Das Kontor will ihre Karten für die Luftfracht kaufen. Aelia will nicht verkaufen, sondern teilen – gegen einen Sitz im Frachtrat.",
  ["OBJ_TALK NPC_R10_AELIA 1 @SET_C_AERION | Aelias Bedingung",
   "OBJ_TALK NPC_KONTORAGENTIN_RIEKE 1 @SET_C_AERION | Rieke (Kontor) zuhören",
   "OBJ_OBSERVE ECHO_222 1 @R10_Z01 | Cirrels auf den Windkarten-Routen beobachten",
   "OBJ_CHOICE DLG_SQ_197_01 1 @SET_C_AERION | Vermitteln"],
  "ITM_GEAR_GLIDER_4; Windkarte (Lore)", "Frachtrat mit Aelia; Luftfracht-Routen (SQ_199)", truth=7)
Q("SQ_198", "Wendelins letzter Stein", "NPC_R10_SIYEL_ARCHIVE|Archivar der Baumeister", "SET_C_AERION", 4, 45,
  "In Aerion steht ein erloschener Resonanzstein, den Wendelin Aar 880 mit den Hütern setzte – die einzige Verbindung zum Boden. Der Archivar zeigt, wo er steht. Ihn zu reaktivieren verbindet Aerion mit Eichenhall (K12 §5) – und ist Wendelins letzte Seite.",
  ["OBJ_INVESTIGATE - 3 @SET_C_AERION | Den erloschenen Stein und Wendelins Zeichen finden",
   "OBJ_PUZZLE PZ_SQ198_STONE 1 @SET_C_AERION | Den Stein mit den Akkorden stimmen",
   "OBJ_OBSERVE ECHO_250 1 @SET_C_AERION | Aeth'rion antwortet dem Stein",
   "OBJ_GOTO SET_C_EICHENHALL 1 @SET_C_EICHENHALL | Erste Reise von Aerion nach Eichenhall"],
  "Wendelin-Tagebuch (letzte Seite); Schnellreise Aerion ↔ Eichenhall", "Resonanzstein aktiv; Wendelin-Sammlung vollständig (K39)", truth=8, pre="Quest.MQ_A3_06")
Q("SQ_199", "Die erste Luftfracht", "NPC_MARIEKE|Marieke Holm", "SET_O_WINDANKER", 4, 45,
  "Im Nachhall eröffnet Marieke die Luftfracht zwischen Boden und Nimbara. Der erste Flug trägt Saatgut, Bücher und einen Brief von Ysolde an die Baumeister. Ein Sturm, eine nervöse Mannschaft und Aelias Windkarten – der Wärter fliegt mit.",
  ["OBJ_TALK NPC_MARIEKE 1 @SET_O_WINDANKER | Marieke an den Windankern",
   "OBJ_TRAVERSE Mount.Fly 1 @R10_Z01 | Den Frachtsegler eskortieren",
   "OBJ_OBSERVE ECHO_221 1 @R10_Z01 | Nimbaroths, die den Segler stützen, beobachten",
   "OBJ_DELIVER ITM_KEY_YSOLDELETTER 1 @SET_C_AERION | Ysoldes Brief übergeben"],
  "Titel „Frachtpate“; ITM_GEAR_BAG_5", "Luftfracht-Route aktiv (Händlersortimente R10 +4)", var="Weather=Thunderstorm", truth=9)
Q("SQ_200", "Die Wand der Zehn", "NPC_R10_ORUMA_TUTOR|Hüterin Oruma", "SET_C_AERION", 4, 40,
  "Auf der Wand der Zehn ist nur Ilens Gesicht erhalten. Oruma will die anderen neun nicht erfinden – aber vielleicht erinnern sich die Stimmen. Mit jedem Akkord-Klang zeigt das Relief einen Schatten eines Gesichts.",
  ["OBJ_TALK NPC_R10_ORUMA_TUTOR 1 @SET_C_AERION | Oruma vor der Wand",
   "OBJ_PUZZLE PZ_SQ200_WALL 9 @SET_C_AERION | Neun Akkorde an der Wand anschlagen",
   "OBJ_INVESTIGATE - 1 @SET_C_AERION | Die Schatten der Gesichter deuten",
   "OBJ_CHOICE DLG_SQ_200_01 1 @SET_C_AERION | Ob die Gesichter nachgemeißelt werden"],
  "Kodex-Eintrag „Der Erstchor“; Hain-Dekor ITM_DECO_WALLOFTEN", "Wand der Zehn mit Schattenrelief (Data Layer)", truth=8, pre="Quest.MQ_A3_06")
Q("SQ_201", "Inselendemiten", "NPC_WILDWAECHTER_BOAZ|Wildwächter Boaz", "SET_V_LUMEYA", 3, 35,
  "Die Wildwacht hat zum ersten Mal Kontakt nach Nimbara. Boaz will wissen, welche Arten nur hier leben und ob sie Schutz brauchen. Elun aus Lumeya hilft; die Baumeister sind skeptisch, bis sie sehen, dass niemand etwas mitnehmen will.",
  ["OBJ_TALK NPC_WILDWAECHTER_BOAZ 1 @SET_V_LUMEYA | Boaz in Lumeya",
   "OBJ_OBSERVE ECHO_233 1 @R10_Z02 | Holmels auf ihren Inseln beobachten",
   "OBJ_OBSERVE ECHO_224 1 @R10_Z03 | Cirrhavens in den Gärten beobachten",
   "OBJ_PHOTO ECHO_227 1 @R10_Z02 | Ein Nubiluna fotografieren"],
  "ITM_GEAR_LENS_4; Wildwacht-Abzeichen „Himmelswacht“", "Schutzgebiete auf zwei Inseln (Kodex-Markierung)", var="Time=Day")
Q("SQ_202", "Letzte Bitten", "NPC_YSOLDE|Ysolde Varn", "SET_V_LUMEYA", 2, 30,
  "Vor dem Aufbruch zur Kronenwerft bittet Ysolde den Wärter um einen Spaziergang. Unterwegs: drei kleine Bitten von Menschen, die er unterwegs getroffen hat – ein Brief, ein Lied, ein Versprechen. Ein Atemzug vor dem Finale (DR-29).",
  ["OBJ_TALK NPC_YSOLDE 1 @SET_V_LUMEYA | Ysoldes Bitte",
   "OBJ_DELIVER ITM_KEY_LASTLETTER 1 @SET_V_WOLKENRAST | Einen Brief nach Wolkenrast bringen",
   "OBJ_OBSERVE ECHO_231 1 @R10_Z02 | Tintels in der Dämmerung singen hören",
   "OBJ_CHOICE DLG_SQ_202_01 1 @SET_V_LUMEYA | Ysolde ein Versprechen geben"],
  "Hain-Dekor ITM_DECO_LASTREQUEST; YSOLDE_BOND +1 (einfühlsam)", "Ysolde erwähnt das Versprechen im Brief (K46 §8.4)", var="Time=Dusk", truth=8,
  pre="Quest.MQ_A3_05")
Q("SQ_203", "Graupel im Garten", "NPC_GAERTNERIN_SOLA|Gärtnerin Sola (Aerion)", "SET_C_AERION", 3, 30,
  "In den Gärten von Aerion fällt Graupel bei Gewitter – und Graupix fressen die jungen Wolkenfrüchte. Sola will Netze spannen. Die Wildwacht schlägt etwas anderes vor: Graupix lieben Kälte, nicht Früchte.",
  ["OBJ_TALK NPC_GAERTNERIN_SOLA 1 @SET_C_AERION | Solas Gärten",
   "OBJ_OBSERVE ECHO_238 2 @R10_Z03 | Graupix bei Gewitter beobachten",
   "OBJ_INVESTIGATE - 2 @R10_Z03 | Herausfinden, was die Graupix wirklich anlockt",
   "OBJ_CHOICE DLG_SQ_203_01 1 @SET_C_AERION | Sola eine Lösung zeigen"],
  "ITM_FOOD_CLOUDFRUIT ×5; ITM_TRAP_WARM", "Kühlbecken für Graupix, Wolkenfrüchte geschützt", var="Weather=Thunderstorm")
Q("SQ_204", "Astraviels Sternbild", "NPC_STERNWAERTER_ELUN|Sternwärter Elun (Lumeya)", "SET_O_STERNWARTEORUMA", 3, 30,
  "Im Nachhall fliegen Astraviels in Formationen, die Sternbildern gleichen – aber einem, das es nicht gibt. Elun glaubt, sie zeichnen ein neues: die Stimmen, so wie sie jetzt sind.",
  ["OBJ_OBSERVE ECHO_240 3 @R10_Z05 | Astraviel-Formationen an drei Nächten",
   "OBJ_INVESTIGATE - 2 @SET_O_STERNWARTEORUMA | Mit dem Sternkatalog vergleichen",
   "OBJ_CHOICE DLG_SQ_204_01 1 @SET_O_STERNWARTEORUMA | Dem Sternbild einen Namen geben"],
  "Kodex-Fragment „Das neue Sternbild“; Hain-Dekor ITM_DECO_STARCHART", "Neues Sternbild am Nachthimmel (Name je Wahl)", var="Time=Night", truth=9)
Q("SQ_205", "Wächter der Windstufen", "NPC_WILDWAECHTER_BOAZ|Wildwächter Boaz", "SET_O_WINDANKER", 4, 40,
  "Im Nachhall richtet die Wildwacht an den Windstufen eine Wache ein. Nimbors nisten an den Ankerseilen; jede Wartung stört sie. Boaz will einen Wartungsplan, der Brutzeiten respektiert.",
  ["OBJ_OBSERVE ECHO_220 2 @R10_Z01 | Nimbor-Nester an den Ankern beobachten",
   "OBJ_INVESTIGATE - 2 @SET_O_WINDANKER | Wartungsbücher prüfen",
   "OBJ_TRAVERSE Mount.Fly 1 @R10_Z01 | Die Seile aus der Luft prüfen",
   "OBJ_CHOICE DLG_SQ_205_01 1 @SET_O_WINDANKER | Wartungsplan vorschlagen"],
  "ITM_GEAR_CLOAK_5; Titel „Windwacht“", "Wartungskalender (Nimbor-Population stabil)", truth=9)
Q("SQ_206", "Windstrom-Rennen", "NPC_WINDSEGLERIN_RIA|Windseglerin Ria", "SET_V_WOLKENRAST", 5, 35,
  "Ria veranstaltet das Windstrom-Rennen zwischen den Inseln. Teilnehmer fliegen auf Echos durch die Windbänder; wer zuerst die Sternwarte erreicht, gewinnt. Zwischendurch: zwei Wärterkämpfe auf schwebenden Plattformen.",
  ["OBJ_TALK NPC_WINDSEGLERIN_RIA 1 @SET_V_WOLKENRAST | Rias Rennen",
   "OBJ_TRAVERSE Mount.Fly 1 @R10_Z01 | Durch die Windbänder",
   "OBJ_BATTLE NPC_RENNFLIEGER_KESTREL 1 @R10_Z02 | Kampf auf der ersten Plattform",
   "OBJ_BATTLE NPC_WINDSEGLERIN_RIA 1 @R10_Z05 | Ria an der Sternwarte",
   "OBJ_OBSERVE ECHO_224 1 @R10_Z05 | Rias Cirrhaven nach dem Rennen beobachten"],
  "ITM_HELD_SWIFTFEATHER; Hain-Dekor ITM_DECO_RACEPENNANT", "Windstrom-Rennen als Weltereignis (WE_WIND_RACE)", var="Time=Day")
Q("SQ_207", "Bodenbewohner", "NPC_FS_ZELLE_AERION|Freie Stimmen (Windanker)", "SET_C_AERION", 4, 40,
  "Die Baumeister nennen Menschen vom Boden „Bodenbewohner“ – nicht freundlich. Ein Baumeisterkind hat Angst vor den Freien Stimmen an den Windankern. Die Freien Stimmen wollen kein Misstrauen säen. Der Wärter bringt beide Seiten an einen Tisch – und die Echos an denselben Brunnen.",
  ["OBJ_TALK NPC_FS_ZELLE_AERION 1 @SET_O_WINDANKER | Die Freien Stimmen an den Ankern",
   "OBJ_TALK NPC_BAUMEISTERIN_IRIS 1 @SET_C_AERION | Baumeisterin Iris zuhören",
   "OBJ_OBSERVE ECHO_225 2 @SET_C_AERION | Nubis und Boden-Echos am Brunnen beobachten",
   "OBJ_CHOICE DLG_SQ_207_01 1 @SET_C_AERION | Ein gemeinsames Mahl vorschlagen"],
  "ITM_FOOD_CLOUDFRUIT ×3; Hain-Dekor ITM_DECO_SKYTABLE", "Gemeinsames Mahl in Aerion (Barks ändern sich: „Bodenleute“ statt „Bodenbewohner“)", truth=8, pre="Quest.MQ_A3_05")
Q("SQ_208", "Orumas Sternfall", "NPC_ORUMA|Oruma Siyel", "SET_C_AERION", 6, 45,
  "Im Nachhall lädt Oruma zur Sternfallprobe in der Sternenarena: Jeder dritte Zug fällt ein Stern auf ein zufälliges, aber vorher angezeigtes Feld (DR-07). Drei Kämpfe; der letzte gegen Oruma mit Aeth'rion als Zuschauer.",
  ["OBJ_BATTLE NPC_STERNPRUEFER_1 1 @SET_C_AERION | Erster Sternfall",
   "OBJ_BATTLE NPC_STERNPRUEFER_2 1 @SET_C_AERION | Zweiter Sternfall",
   "OBJ_BATTLE NPC_ORUMA 1 @SET_C_AERION | Oruma",
   "OBJ_OBSERVE ECHO_250 1 @SET_C_AERION | Aeth'rion beobachten"],
  "ITM_HELD_TONE_SOUND; Titel „Sternfallgast“", "Oruma-Barks im Nachhall", truth=9)
Q("SQ_209", "Federn, die freiwillig fallen", "NPC_R10_BRISK|Federschneider Brisk", "SET_C_AERION", 3, 30,
  "Brisk schneidet Federkiele aus Cirrhawk-Federn. Die Freien Stimmen werfen ihm vor, Federn zu rupfen. Brisk schwört, er sammle nur gemauserte. Der Wärter beobachtet die Cirrhawks bei der Mauser – und Brisks Lieferanten.",
  ["OBJ_TALK NPC_R10_BRISK 1 @SET_C_AERION | Brisk in der Federschneiderei",
   "OBJ_OBSERVE ECHO_223 2 @R10_Z01 | Cirrhawks bei der Mauser beobachten",
   "OBJ_INVESTIGATE - 2 @R10_Z01 | Brisks Lieferanten folgen",
   "OBJ_CHOICE DLG_SQ_209_01 1 @SET_C_AERION | Ergebnis: Brisk, Lieferant, Freie Stimmen"],
  "ITM_HELD_SWIFTFEATHER; ITM_MAT_FERNFIBER ×3", "Federn mit Mausersiegel (Händler-Kennzeichnung)", var="Time=Day",
  solution="Brisk entlasten · Lieferanten melden · ein Mausersiegel einführen, das alle drei Seiten prüfen (dritte Lösung).")
Q("SQ_210", "Hüter der Pause", "NPC_SCHWESTER_IVRA|Schwester Ivra", "SET_O_KRONENWERFTWACHT", 6, 60,
  "Die sechste und letzte Station: die Kronenwerft, wo Velnox frei wurde und zurückkehrte. Ivra, Ulrek, Sereth (je nach Epilog), Ysolde und Bruder Odvar stehen im Kreis. Wer alle Orte der Pause gehört hat, wird zum Hüter – und hört zum ersten Mal Velnox selbst, wie er zwischen zwei Tönen atmet. Der Beginn von „Die Pause hören“ (K62).",
  ["OBJ_GOTO R10_Z04 1 @R10_Z04 | Zur Kronenwerft",
   "OBJ_REST R10_Z04 1 @R10_Z04 | Im Kreis schweigen",
   "OBJ_OBSERVE ECHO_251 1 @R10_Z04 | Velnox' Atem zwischen zwei Tönen hören",
   "OBJ_CHOICE DLG_SQ_210_01 1 @R10_Z04 | Das Gelöbnis der Hüter sprechen (oder nur zuhören)"],
  "Titel „Hüter der Pause“ (K47 F05 Rang 6 verstärkt); Hain-Dekor ITM_DECO_PAUSEBELL", "Questreihe „Die Pause hören“ (Velnox-Bindung, K62) beginnt", truth=9)


# ── Haken-Abgleich K11–K13 (Städte/Dörfer) → Nebenquests ──
HOOKS = [
    ("Eichenhall", "„Der Lindentisch“ (Bundesgeschichte)", "SQ_154 (Bundesrat, Zeugenrolle) und Weltereignis Lindenfest (CANON §52)"),
    ("Eichenhall", "„Wurzelpfade“ (Kletter-Sammlung)", "Sammelreihe der Kodex-Aufgaben R01 (K39), keine eigene SQ"),
    ("Eichenhall", "„Das Echo im Harzfass“", "SQ_005 „Das Echo der Außenstelle“ (Lumow-Sammler) – gleiche Prämisse, verlegt in die Außenstelle"),
    ("Eichenhall", "Fotowettbewerb der Akademie-Außenstelle", "SQ_003 (Foto-Schritt) und Foto-Aufträge CT_PHOTO"),
    ("Kharsholm", "„Die Schuld der Lastzüge“", "SQ_036"),
    ("Kharsholm", "„Drei Klans, ein Gipfel“ (Klan-Wettkampf)", "SQ_042 „Die Probe der Ahnen“ (Brückenprobe der Klans)"),
    ("Kharsholm", "„Verschüttet“ (Minenrettung)", "SQ_033"),
    ("Morvenfurt", "„Zwei Seiten des Kanals“ (Kontor vs. Freie Stimmen)", "SQ_055 / SQ_057 (Unterstadt) – Entscheidung ohne Ausschluss (K47 §7)"),
    ("Morvenfurt", "„Irrlichtjagd“", "SQ_049"),
    ("Morvenfurt", "„Der Fährmeister und das Turmgeheimnis“", "SQ_054 „Das Turmgeheimnis der Fährmeisterin“ (Ailsa Duvreth, CANON §52)"),
    ("Morvenfurt", "„Laternen für die Toten“", "SQ_048 (Laternensteg) und SQ_059 (Laternen, Irrlits)"),
    ("Qasr Sahrun", "„Das Gastrecht“ (Kette, 4 Teile)", "Kette FQ_F04_04 „Salz und Freiheit“ (Gastrecht der Oase als Motiv in SQ_109–111)"),
    ("Qasr Sahrun", "„Glas aus Licht“ (Glasbläser-Wettbewerb)", "SQ_101 (Glasbläserei Tavi) und SQ_185 (Meisterwerk)"),
    ("Qasr Sahrun", "„Harun und der Neumond“", "SQ_100"),
    ("Qasr Sahrun", "„Die verirrte Karawane“", "SQ_098"),
    ("Saltrand-Hafen", "„Die goldene Glocke schweigt“", "SQ_071 (Leuchtfelsen-Chor) und Weltereignis Glockenflut (CANON §52)"),
    ("Saltrand-Hafen", "„Schmugglerkeller“ (Ebbe)", "SQ_076 / SQ_089 (Lager im Kliffsund)"),
    ("Saltrand-Hafen", "„Bekes Wetten“", "SQ_085"),
    ("Saltrand-Hafen", "„Flaschenpost“ (Sammelreihe, Lore)", "Lore-Sammelreihe (K39, `LoreEntries.csv`), keine eigene SQ"),
    ("Schlackenwehr", "„Das Gelübde der Zunft“", "SQ_119"),
    ("Schlackenwehr", "„Sechs Glocken“ (Sammelquest)", "SQ_116 (Glockenguss) + Schmiedeglocken als Kodex-Aufgabe"),
    ("Schlackenwehr", "„Lavawächter in Not“", "SQ_120"),
    ("Schlackenwehr", "„Echos in den Minen“ (Freie Stimmen vs. Kontor)", "SQ_131 / SQ_129 (Zelle Schlackenwehr)"),
    ("Hvitmark", "„Namen auf dem Stein“", "SQ_135"),
    ("Hvitmark", "„Thing-Streit“", "SQ_141"),
    ("Hvitmark", "„Eiðvik-Neu baut auf“", "SQ_143"),
    ("Hvitmark", "„Aurora-Fotografie“", "SQ_147"),
    ("Dorunsruh", "„Glyphen-Übersetzung“ (10-teilige Rätselkette)", "SQ_157 (zehn Tafeln als Zählschritt)"),
    ("Dorunsruh", "„Der Hehler“", "SQ_161"),
    ("Dorunsruh", "„Kaels Forschungsarbeit“", "SQ_158 (vor und nach W6 spielbar)"),
    ("Dorunsruh", "„Die Bibliothek der Resonanz“", "SQ_167"),
    ("Dorunsruh", "„Studentenstreik“", "SQ_156"),
    ("Prismara", "„Licht für die Oberwelt“", "SQ_183"),
    ("Prismara", "„Verschüttete Stimmer“", "SQ_189"),
    ("Prismara", "„Brannocs Erbe“", "SQ_182"),
    ("Prismara", "„Glasbläser-Meisterwerk“", "SQ_185"),
    ("Aerion", "„Bodenbewohner“", "SQ_207"),
    ("Aerion", "„Inselendemiten“", "SQ_201"),
    ("Aerion", "„Windstrom-Rennen“", "SQ_206"),
    ("Aerion", "„Wendelins letzter Stein“", "SQ_198"),
    ("Aerion", "„Letzte Bitten“", "SQ_202"),
]


def hooks_table():
    lines = ["| Stadt | Haken (K11/K12) | Umsetzung |", "|---|---|---|"]
    for c, h, u in HOOKS:
        lines.append(f"| {c} | {h} | {u} |")
    return "\n".join(lines)


VILLAGES = [
    ("Lindwiesen", "Ysolde, Bäckerin Hedda, Müller Jost", "SQ_002, SQ_012, SQ_007 (Imkerin Hilde)"),
    ("Moosgrund", "Köhlerin Brida; Pilzringe", "SQ_022–024 (Kurierin Ennis), SQ_008"),
    ("Brakkfels", "Ulf Brakk; Lorenlauf/Minenunglück", "SQ_026, SQ_033 (Ulf Brakk), SQ_044"),
    ("Hrallsted", "Hirtin Svala; verlorene Herde", "SQ_029, SQ_045"),
    ("Fennhaven", "Lorcan; Reusen-Mysterium", "SQ_051, SQ_056, SQ_063 (Reusen)"),
    ("Duvreth", "Moorweise Ama Duvreth; Rückkehr nach Heilung", "SQ_047, SQ_058, SQ_060"),
    ("Harrâd / Mirsaan / Ashurim", "Nadira, Kesh, Imran", "SQ_092, SQ_093, SQ_101, SQ_108–112"),
    ("Vorthax / Kaldra", "Thessa (Ausbruchstag), Kurwirtin Malva", "SQ_114, SQ_120, SQ_126, SQ_127, SQ_130"),
    ("Tangwerft / Möwenhuk / Flottholm", "Marlene, Okko, Ebba", "SQ_069, SQ_074, SQ_075, SQ_081, SQ_090"),
    ("Fjallstad / Eiðvik-Neu", "Leif (Schwester im Kloster), Halla", "SQ_140, SQ_144 (Leif), SQ_143 (Halla)"),
    ("Thae'Luun / Säulenrast", "Dr. Imke Vael, Bruder Odvar", "SQ_153, SQ_155, SQ_163 (Odvar), SQ_165, SQ_167 (Imke Vael)"),
    ("Glanzschacht / Quarzgrund", "Steiger Brannoc d. Ä., Schleiferin Nyx", "SQ_174 (Nyx), SQ_180, SQ_187, SQ_189 (Brannoc d. Ä.)"),
    ("Lumeya / Wolkenrast", "Elun, Windseglerin Ria", "SQ_191, SQ_196, SQ_204 (Elun), SQ_192, SQ_206 (Ria)"),
]


def villages_table():
    lines = ["| Dorf | Schlüssel-NPC / Haken (CANON §57) | Nebenquests |", "|---|---|---|"]
    for v, n, q in VILLAGES:
        lines.append(f"| {v} | {n} | {q} |")
    return "\n".join(lines)


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


def stats_total():
    import sq_k49, sq_k50  # noqa: F401
    return _c.stats(sorted(_c.QUESTS))


def chains():
    return _c.chain_table(IDS)


def chains_all():
    import sq_k49, sq_k50  # noqa: F401
    return _c.chain_table(sorted(_c.QUESTS))


def givers():
    return _c.giver_table(IDS)


if __name__ == "__main__":
    import sq_k49, sq_k50  # noqa: F401
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    err = validate(IDS)
    r07 = [i for i in list(sq_k50.IDS) + IDS if _c.SKEL[i]["RegionId"] == "R07"]
    err += [e for e in validate(r07) if e.startswith("QS-15")]
    allids = sorted(_c.QUESTS)
    err += [e for e in validate(allids) if e.startswith("QS-14")]
    print("\n".join(err) if err else "", end="")
    print(f"K51: {len(IDS)} Nebenquests, {len(err)} Fehler. Gesamt beschrieben: {len(allids)}.")
    if cmd == "write" and not err:
        print("geschrieben:", write(IDS))
    sys.exit(1 if err else 0)
