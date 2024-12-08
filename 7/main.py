import itertools


data = [
[54753537, 2 ,35 ,2 ,5 ,5 ,9 ,1 ,17 ,367 ,73],
[4351178317, 51 ,646 ,47 ,281 ,6 ,91],
[452662455, 574 ,1 ,291 ,1 ,271 ,44],
[321264501, 3 ,45 ,97 ,69 ,501],
[137567, 319 ,6 ,1 ,561 ,3 ,6 ,2 ,328 ,7],
[945476, 2 ,9 ,968 ,79 ,3],
[44330019, 95 ,8 ,15 ,65 ,5 ,4 ,44 ,7 ,2 ,3 ,7],
[1387063, 1 ,5 ,55 ,3 ,301 ,9 ,2 ,9 ,4 ,6 ,5 ,8],
[10265528, 611 ,4 ,7 ,2 ,50 ,6 ,728],
[1909254886, 2 ,613 ,8 ,86 ,9 ,8 ,61 ,847],
[39744000, 66 ,3 ,180 ,640 ,5],
[850892742, 5 ,235 ,932 ,37 ,7 ,4 ,3 ,26 ,4],
[2069650924, 94 ,5 ,37 ,521 ,44],
[13065382, 6 ,6 ,8 ,8 ,6 ,3 ,8 ,377 ,4 ,3 ,4 ,22],
[532264632152, 69 ,3 ,8 ,4 ,4 ,7 ,3 ,6 ,9 ,8 ,144 ,8],
[2933920, 43 ,68 ,9 ,8 ,55 ,60 ,5],
[3608, 4 ,39 ,3 ,9 ,8],
[21667, 5 ,8 ,1 ,6 ,461],
[2770482, 4 ,3 ,8 ,3 ,8 ,1 ,52 ,43 ,3 ,7 ,8 ,49],
[25620, 696 ,64 ,87 ,7 ,5 ,6],
[120120, 725 ,45 ,52 ,3],
[399281807, 7 ,533 ,618 ,1 ,53],
[460024329, 5 ,1 ,6 ,69 ,3 ,3 ,1 ,428 ,4 ,332],
[43482258007, 80 ,592 ,2 ,467 ,983 ,87],
[719928, 13 ,325 ,7 ,54],
[19415161698, 6 ,2 ,206 ,6 ,7 ,5 ,36 ,277 ,6 ,6],
[356516192, 364 ,55 ,53 ,7 ,1 ,24 ,6 ,6 ,2 ,8],
[65345119842, 110 ,27 ,148 ,1 ,572 ,7 ,2],
[193326899, 67 ,412 ,14 ,7 ,899],
[184, 61 ,8 ,16 ,6 ,93],
[1877904, 9 ,9 ,84 ,6 ,46],
[796363074, 74 ,4 ,5 ,819 ,73 ,26 ,9],
[2703365481806, 44 ,8 ,768 ,54 ,817 ,26 ,80],
[1443, 369 ,5 ,348 ,716 ,5],
[629726, 62 ,442 ,523 ,2 ,8 ,1 ,47],
[1995000, 4 ,95 ,70 ,3 ,25],
[39210528000, 888 ,5 ,7 ,40 ,76 ,415],
[130761000, 3 ,835 ,87 ,3 ,5 ,40],
[656915580, 591 ,65 ,887 ,6 ,22 ,574 ,6],
[116418336, 5 ,94 ,2 ,4 ,10 ,449 ,809 ,96],
[796706, 8 ,277 ,39 ,40 ,423 ,9 ,706],
[2367, 3 ,30 ,26 ,25 ,2],
[94766755, 23 ,71 ,7 ,66 ,75 ,7],
[996, 24 ,35 ,7 ,143 ,6],
[65085180, 4 ,25 ,9 ,61 ,2 ,8 ,9 ,93 ,3 ,6 ,5 ,2],
[2478357, 69 ,867 ,51 ,81 ,31],
[65658600, 5 ,96 ,6 ,3 ,1 ,3 ,2 ,5 ,27 ,4 ,7 ,18],
[3310328358, 92 ,5 ,28 ,6 ,1 ,5 ,3 ,549 ,74],
[23286736563543, 5 ,1 ,7 ,5 ,72 ,682 ,9 ,815 ,4 ,3],
[322244, 1 ,304 ,106 ,4],
[6963228990, 748 ,7 ,34 ,30 ,93],
[16852589, 9 ,3 ,3 ,77 ,1 ,976 ,3 ,8 ,75 ,8 ,9],
[5142276457, 8 ,5 ,689 ,3 ,3 ,9 ,6 ,6 ,40 ,5 ,6],
[257579142, 2 ,8 ,539 ,3 ,65 ,2 ,802 ,3],
[3410836995, 2 ,7 ,643 ,7 ,9 ,3 ,251 ,983 ,3],
[132980407, 8 ,81 ,3 ,1 ,4 ,615 ,111 ,187],
[20582197, 288 ,9 ,7 ,99 ,94 ,3],
[392, 254 ,62 ,76],
[1609372858, 512 ,6 ,4 ,887 ,1 ,35 ,23],
[4128975, 9 ,7 ,91 ,7 ,3 ,9 ,3 ,4 ,2 ,424 ,71],
[2040918779, 5 ,44 ,1 ,7 ,374 ,779],
[139213718, 8 ,1 ,9 ,89 ,88 ,98 ,815 ,44 ,7],
[87195696371, 917 ,283 ,6 ,56 ,370],
[9706088, 802 ,36 ,10 ,2 ,2 ,8 ,6 ,1 ,1 ,7 ,4],
[1484253, 461 ,4 ,9 ,89 ,9],
[617638, 8 ,321 ,8 ,1 ,747 ,29 ,170],
[83249019, 4 ,430 ,5 ,86 ,7 ,2 ,5 ,6 ,7 ,63],
[46834, 17 ,5 ,27 ,7 ,9 ,39 ,73],
[19069722000, 3 ,989 ,7 ,852 ,84 ,6 ,70 ,5 ,5],
[477600, 4 ,24 ,41 ,1 ,758 ,9 ,60],
[880661, 150 ,3 ,575 ,91 ,1],
[1928660, 607 ,652 ,62 ,4 ,365],
[1281186, 7 ,5 ,1 ,5 ,8 ,6 ,1 ,2 ,65 ,654 ,3 ,1],
[4929201, 10 ,68 ,2 ,73 ,22 ,12 ,9 ,4 ,81],
[3850835, 818 ,47 ,57 ,5 ,26 ,9],
[767597973765, 8 ,2 ,3 ,6 ,1 ,5 ,7 ,732 ,75 ,9 ,3 ,5],
[1448163, 8 ,3 ,7 ,3 ,3 ,3 ,86 ,267],
[36588218862000, 2 ,936 ,15 ,945 ,8 ,520 ,75],
[150084752, 139 ,20 ,7 ,7 ,6 ,9 ,666 ,2 ,85],
[918138, 9 ,7 ,9 ,1 ,3 ,43 ,54 ,5 ,56 ,9 ,9],
[221, 9 ,8 ,21 ,97 ,5],
[64893075, 1 ,300 ,2 ,289 ,8 ,247 ,3],
[3649860742, 5 ,5 ,54 ,9 ,9 ,5 ,90 ,6 ,7 ,3 ,7 ,5],
[6212821112, 609 ,1 ,3 ,8 ,5 ,1 ,3 ,17 ,5 ,4 ,3],
[1259, 16 ,9 ,11 ,5 ,7 ,1 ,2 ,67 ,70],
[77842, 827 ,94 ,15 ,5 ,84],
[1863503, 62 ,3 ,346 ,4 ,3],
[8756909, 5 ,52 ,36 ,4 ,9 ,4 ,8 ,979 ,947],
[15306, 62 ,5 ,6 ,6 ,139 ,6],
[7729, 37 ,33 ,2 ,1 ,95 ,863 ,8 ,18 ,1],
[3818222931, 9 ,1 ,2 ,19 ,18 ,164 ,229 ,3 ,1],
[356166, 85 ,787 ,6 ,1 ,5 ,9 ,2 ,5 ,57 ,9],
[41491597288, 120 ,8 ,35 ,758 ,453],
[1168053, 679 ,2 ,7 ,6 ,43 ,7 ,4 ,5 ,8 ,6 ,7],
[741200, 6 ,6 ,2 ,8 ,4 ,2 ,455 ,2 ,3 ,3 ,436],
[2678756, 3 ,86 ,3 ,8 ,756],
[12168355, 277 ,24 ,206 ,8 ,3 ,347 ,8],
[17215297, 2 ,7 ,2 ,3 ,4 ,6 ,76 ,9 ,4 ,853 ,7],
[486305, 48 ,4 ,7 ,6 ,30 ,79 ,455],
[59514, 8 ,5 ,38 ,923 ,42],
[1081, 716 ,360 ,2 ,3 ,1],
[52644337, 8 ,14 ,4 ,8 ,391 ,3 ,3 ,4 ,44 ,40],
[191221, 3 ,6 ,79 ,34 ,510 ,19 ,8 ,43],
[188584887, 4 ,35 ,6 ,3 ,4 ,412 ,768 ,951],
[3515874, 6 ,52 ,2 ,3 ,903 ,57 ,6 ,5 ,110],
[187053830, 185 ,3 ,4 ,839 ,970],
[1258290, 4 ,8 ,2 ,33 ,3 ,140 ,558],
[29495340, 51 ,7 ,9 ,255 ,36],
[4424790, 442 ,4 ,78 ,2 ,8],
[21768474, 7 ,42 ,949 ,77 ,78],
[418815323, 618 ,517 ,369 ,3 ,23],
[335610768, 3 ,729 ,30 ,256 ,3],
[500108, 71 ,398 ,41 ,5 ,7],
[27697972, 3 ,257 ,10 ,341 ,5 ,52 ,34 ,2],
[2650285638, 422 ,73 ,4 ,5 ,819 ,3 ,1 ,858],
[7721858286, 982 ,9 ,193 ,3 ,5 ,6 ,19 ,8 ,57],
[116472, 844 ,46 ,3],
[6239044, 8 ,566 ,1 ,606 ,5 ,9 ,9 ,3 ,3 ,3 ,7],
[1866118192215, 7 ,66 ,3 ,5 ,84 ,962 ,9 ,9 ,16],
[1507, 86 ,3 ,61 ,4 ,3],
[109629690, 783 ,800 ,52 ,3 ,25 ,6 ,3 ,7 ,2],
[5306964937317, 752 ,3 ,952 ,741 ,48 ,83 ,7],
[63439552, 89 ,9 ,2 ,13 ,704],
[80598, 93 ,6 ,20 ,9 ,11 ,57 ,8 ,46 ,9 ,4],
[1729157144, 817 ,6 ,8 ,4 ,8 ,5 ,2 ,8 ,12 ,1 ,88],
[318526533, 60 ,72 ,9 ,12 ,70 ,9 ,13 ,9],
[75992592962, 9 ,478 ,12 ,870 ,846 ,2 ,2],
[36687434205, 3 ,4 ,9 ,47 ,5 ,2 ,743 ,5 ,743],
[2335413271, 2 ,7 ,207 ,8 ,9 ,5 ,4 ,1 ,327 ,1],
[157085, 77 ,3 ,680 ,5],
[7718989824, 84 ,4 ,944 ,39 ,78 ,8],
[86959770, 43 ,10 ,1 ,68 ,981 ,89 ,2 ,6],
[113448, 5 ,1 ,65 ,93 ,696],
[1183882321, 1 ,85 ,659 ,53 ,3 ,92 ,232 ,1],
[50527, 7 ,6 ,664 ,18 ,45],
[4909240, 95 ,7 ,905 ,5 ,1 ,1 ,7 ,89 ,5],
[5234297390, 6 ,905 ,89 ,85 ,574],
[31905152, 19 ,55 ,72 ,4 ,4 ,424],
[3850024234, 18 ,6 ,456 ,8 ,7 ,9 ,698 ,5 ,6 ,2],
[417726, 3 ,703 ,79 ,52 ,19 ,933 ,6],
[6167, 350 ,7 ,490 ,7 ,1 ,230 ,7],
[186, 44 ,59 ,7 ,47 ,29],
[306616797, 1 ,4 ,34 ,80 ,446 ,9 ,5 ,6 ,537],
[28792, 68 ,5 ,390 ,48 ,192 ,73 ,4 ,5],
[3378, 5 ,548 ,638],
[7446677, 8 ,4 ,7 ,985 ,8 ,9 ,5],
[29579340327, 23 ,7 ,1 ,80 ,3 ,980 ,27 ,5 ,7],
[1085192, 1 ,3 ,64 ,9 ,794 ,7 ,3 ,8 ,4 ,8 ,8 ,1],
[1429200, 1 ,5 ,85 ,16 ,195 ,89 ,9],
[20570, 61 ,8 ,33 ,7 ,9 ,14],
[9483, 3 ,90 ,1 ,83],
[13799096531, 3 ,904 ,55 ,98 ,7 ,944 ,3],
[30590388700, 5 ,6 ,58 ,2 ,6 ,4 ,7 ,731 ,8 ,700],
[4267872, 696 ,452 ,4 ,7 ,928],
[153573, 51 ,35 ,4 ,388 ,668 ,134 ,9],
[9720618307, 1 ,6 ,894 ,1 ,9 ,2 ,9 ,8 ,5 ,6 ,307],
[33397511, 3 ,330 ,1 ,9 ,747 ,4 ,1],
[873, 5 ,20 ,250 ,88 ,433 ,2],
[25005, 2 ,147 ,17 ,5 ,7 ,8],
[58786759769, 7 ,1 ,1 ,900 ,1 ,8 ,31 ,7 ,933 ,8],
[2387612493, 2 ,3 ,4 ,70 ,20 ,9 ,3 ,151 ,493],
[26852833, 630 ,8 ,33 ,3 ,6 ,6 ,8 ,7 ,6 ,7 ,7 ,7],
[809887, 71 ,50 ,948 ,78 ,9],
[151958, 492 ,913 ,2 ,2 ,1 ,6 ,9 ,2],
[56789, 4 ,71 ,95 ,29 ,66 ,94],
[463935731252, 471 ,985 ,486 ,245 ,2 ,52],
[42895, 32 ,8 ,4 ,384 ,95],
[85076145520, 35 ,973 ,473 ,5 ,514 ,5],
[843192, 6 ,6 ,937 ,7 ,98 ,9],
[19872, 6 ,5 ,517 ,46 ,18 ,22 ,3 ,4 ,8 ,4],
[5887869664, 8 ,8 ,3 ,6 ,596 ,7 ,16 ,701 ,7 ,8],
[1635898, 220 ,2 ,5 ,599 ,583],
[558360661, 5 ,629 ,9 ,2 ,3 ,35 ,177 ,1],
[115823720, 440 ,9 ,43 ,49 ,85 ,8],
[210515898969, 1 ,662 ,9 ,7 ,8 ,22 ,7 ,9 ,3 ,6 ,9 ,1],
[124440639859, 510 ,244 ,63 ,972 ,6 ,4 ,76],
[49816, 60 ,830 ,16],
[279572, 4 ,1 ,1 ,80 ,2 ,8 ,71 ,8 ,9 ,7 ,5 ,4],
[243618, 362 ,57 ,581 ,89 ,82 ,8],
[23616, 9 ,6 ,1 ,426 ,12 ,600],
[6411304, 8 ,5 ,9 ,2 ,9 ,5 ,6 ,8 ,5 ,5 ,2 ,212],
[311780, 4 ,4 ,175 ,4 ,8 ,2 ,7 ,5 ,6 ,70 ,2],
[134961625, 7 ,82 ,774 ,6 ,9 ,67 ,49 ,25],
[8762878, 76 ,8 ,9 ,99 ,18 ,10 ,1 ,78],
[5703, 96 ,4 ,5 ,920 ,3 ,2 ,2 ,2 ,5 ,4],
[1087818, 5 ,8 ,7 ,7 ,76 ,8 ,7 ,335 ,1 ,7 ,65],
[2912, 89 ,43 ,22 ,4 ,4],
[7136898766, 3 ,55 ,87 ,97 ,4 ,9 ,2 ,766],
[144594, 41 ,3 ,53 ,62 ,8 ,2],
[5718245, 57 ,879 ,3 ,9 ,5 ,3 ,2 ,2 ,4 ,5],
[12260616, 1 ,9 ,8 ,2 ,5 ,84 ,9 ,17 ,7 ,1 ,52 ,4],
[5040, 2 ,88 ,7 ,8],
[198, 3 ,6 ,4 ,9],
[10354266785, 1 ,88 ,903 ,9 ,9 ,609 ,1 ,64],
[18450, 923 ,707 ,416 ,4 ,9],
[23252292, 923 ,67 ,376 ,71 ,5],
[285885139, 84 ,58 ,2 ,7 ,4 ,215 ,5 ,4 ,839],
[5998, 5 ,2 ,13 ,659 ,8],
[8001936, 8 ,466 ,5 ,6 ,140 ,767 ,7 ,4 ,6],
[6528, 6 ,98 ,72 ,8 ,798 ,450],
[320068314, 265 ,87 ,8 ,1 ,6 ,771 ,3],
[4043970379, 67 ,741 ,794 ,5 ,379],
[4434, 6 ,433 ,9 ,5 ,77 ,9 ,939 ,3],
[87478812, 1 ,77 ,1 ,7 ,2 ,3 ,7 ,8 ,1 ,2 ,9 ,89],
[240189372, 2 ,921 ,590 ,77 ,49 ,4 ,1 ,3 ,3],
[6849841788, 6 ,7 ,811 ,5 ,2 ,8 ,7 ,8 ,2 ,88],
[6318400, 70 ,30 ,6 ,8 ,88 ,550],
[816598136, 9 ,791 ,834 ,9 ,33 ,245 ,36],
[801799, 2 ,134 ,6 ,3 ,979],
[179958, 7 ,3 ,3 ,200 ,5 ,74 ,73 ,8 ,67 ,8],
[16461229842, 7 ,66 ,364 ,4 ,26 ,89 ,8 ,6 ,4 ,2],
[1090, 28 ,24 ,1 ,8 ,67 ,136 ,206],
[153085142, 62 ,998 ,81 ,3 ,2],
[9614302984, 729 ,524 ,88 ,796 ,286],
[508606, 245 ,7 ,2 ,303 ,2],
[5567711552, 51 ,964 ,67 ,238 ,18 ,344],
[85376238, 8 ,7 ,4 ,6 ,3 ,929 ,9 ,5 ,6 ,9 ,3 ,8],
[206208012, 52 ,58 ,5 ,4 ,18 ,2 ,2 ,9 ,3 ,474],
[37794428, 8 ,47 ,9 ,3 ,99 ,2 ,389 ,39],
[20422831, 1 ,916 ,21 ,706 ,3 ,65 ,341],
[2633593816, 49 ,8 ,965 ,6 ,644 ,3 ,6 ,16],
[10108411292, 38 ,435 ,263 ,6 ,292],
[191874752, 5 ,7 ,24 ,83 ,82 ,8],
[22894, 41 ,54 ,5 ,681 ,68],
[14559, 9 ,66 ,194 ,2 ,7],
[38948878, 2 ,416 ,92 ,483 ,4 ,5 ,87 ,8],
[206, 9 ,9 ,188],
[560664616839, 92 ,7 ,4 ,8 ,1 ,246 ,2 ,564 ,39],
[805, 196 ,24 ,8 ,577],
[172349974, 9 ,2 ,9 ,67 ,4 ,8 ,441 ,7 ,9 ,7 ,48],
[9846287, 82 ,12 ,6 ,28 ,7],
[2632, 40 ,5 ,456 ,4 ,8],
[135680128, 6 ,9 ,4 ,19 ,8 ,8 ,9 ,7 ,9 ,782 ,8 ,8],
[17495482, 5 ,8 ,2 ,538 ,289 ,1],
[2399040, 229 ,9 ,8 ,140 ,9],
[118977, 9 ,1 ,6 ,4 ,79 ,9 ,2 ,3 ,25 ,127],
[4470355, 82 ,3 ,1 ,24 ,8 ,4 ,5 ,755],
[3185786752, 5 ,335 ,3 ,2 ,7 ,41 ,2 ,326],
[2009, 9 ,424 ,69 ,4 ,1],
[1276, 2 ,4 ,949 ,8 ,40 ,253 ,4 ,3 ,13],
[11520, 4 ,9 ,26 ,2 ,285 ,4 ,6 ,277 ,6 ,6],
[5075195721, 3 ,58 ,7 ,333 ,727 ,12 ,1],
[38241890, 7 ,648 ,23 ,5 ,8 ,732],
[560123, 9 ,28 ,18 ,2 ,3 ,3 ,93 ,959 ,48],
[1258, 7 ,7 ,27 ,474 ,1 ,405],
[200203180, 9 ,28 ,5 ,779 ,180],
[5384616, 255 ,18 ,2 ,85 ,9 ,58 ,6 ,2],
[10732, 8 ,88 ,15 ,4 ,168],
[595020, 39 ,4 ,42 ,30 ,9 ,20 ,3 ,8 ,3],
[14741030272, 1 ,6 ,888 ,7 ,76 ,6 ,8 ,487 ,8],
[50491569, 610 ,5 ,821 ,68 ,1],
[6690, 173 ,782 ,81 ,79 ,6],
[368089585, 40 ,939 ,40 ,6 ,49 ,7 ,5 ,80],
[2210725312, 319 ,1 ,866 ,6 ,4 ,8],
[735936, 5 ,8 ,6 ,3 ,888 ,6 ,13 ,659 ,1],
[367231069, 9 ,715 ,378 ,40 ,69],
[33491860, 1 ,22 ,2 ,27 ,5 ,6 ,8 ,63],
[52504, 8 ,7 ,936 ,4 ,76 ,8],
[51734895, 8 ,6 ,7 ,311 ,56 ,3 ,520 ,3 ,2 ,6],
[17919440, 58 ,13 ,5 ,70 ,44],
[683883, 261 ,181 ,241 ,8 ,83],
[60928, 601 ,7 ,4 ,8 ,8],
[75011628, 750 ,11 ,5 ,1 ,35 ,93],
[6846336, 6 ,1 ,120 ,51 ,8 ,5 ,9 ,3 ,6 ,48 ,4],
[432606725, 8 ,86 ,92 ,2 ,7 ,4 ,619 ,8 ,2 ,4 ,1],
[1738, 274 ,1 ,6 ,6 ,52],
[36811828, 601 ,625 ,3 ,1 ,7 ,4 ,7 ,65 ,2],
[2783203, 8 ,710 ,7 ,70 ,3],
[26705, 32 ,6 ,7 ,21 ,84],
[34008882432, 7 ,2 ,9 ,7 ,2 ,2 ,9 ,7 ,44 ,6 ,68 ,14],
[2065379968, 11 ,45 ,96 ,8 ,679 ,50 ,64],
[2089592975, 75 ,130 ,73 ,6 ,381],
[305519, 5 ,7 ,50 ,337 ,14 ,48 ,6 ,304],
[108951, 8 ,2 ,7 ,1 ,951],
[1113974643, 1 ,7 ,5 ,9 ,246 ,819 ,8 ,91],
[1560, 3 ,193 ,8 ,34 ,22 ,2 ,3],
[4434569, 4 ,42 ,997 ,452 ,2 ,77],
[740990253, 4 ,1 ,424 ,6 ,39 ,7 ,65 ,3 ,1 ,3],
[654983640, 799 ,9 ,5 ,81 ,92 ,6 ,640],
[147560, 5 ,35 ,5 ,6 ,306 ,96 ,33 ,3 ,5],
[9460841, 50 ,242 ,6 ,54 ,4 ,1 ,1],
[112336045, 1 ,29 ,58 ,93 ,395 ,415],
[264548660, 5 ,529 ,1 ,1 ,2 ,1 ,866 ,10],
[120206, 59 ,7 ,72 ,290 ,4 ,1 ,95 ,7 ,1],
[964442, 881 ,5 ,78 ,445],
[58489604, 9 ,48 ,88 ,12 ,2 ,672 ,7 ,68],
[6995, 4 ,3 ,6 ,8 ,9 ,164 ,2 ,598 ,7 ,9],
[1584, 955 ,4 ,3 ,223 ,354 ,18 ,27],
[6969, 1 ,8 ,83 ,1 ,69],
[825578, 7 ,9 ,8 ,6 ,8 ,1 ,42 ,8 ,7 ,2 ,9 ,8],
[1063552, 83 ,800 ,53 ,4 ,76 ,4],
[1264664016091, 91 ,77 ,870 ,3 ,3 ,88 ,2 ,91],
[231806, 231 ,69 ,8 ,4 ,2 ,30],
[28728158, 437 ,657 ,164 ,8 ,58],
[63329113, 79 ,9 ,4 ,77 ,71 ,307 ,924],
[1242, 44 ,131 ,943 ,49 ,75],
[7979912643, 544 ,1 ,9 ,7 ,1 ,1 ,5 ,366 ,8 ,5 ,3],
[84947, 7 ,121 ,84 ,163],
[32995, 9 ,2 ,1 ,5 ,7 ,85 ,8 ,262],
[2352835, 97 ,982 ,50 ,24 ,67],
[28447, 2 ,7 ,6 ,3 ,779 ,2 ,2 ,321 ,72 ,6],
[1222702380, 27 ,5 ,7 ,6 ,8 ,9 ,5 ,8 ,2 ,93 ,7 ,90],
[1762483649136, 336 ,562 ,98 ,61 ,876],
[146084158, 2 ,18 ,83 ,22 ,515 ,522 ,4 ,7],
[613893, 7 ,46 ,26 ,2 ,7 ,63 ,2 ,8 ,2 ,1],
[247198, 23 ,1 ,9 ,7 ,198],
[528428, 9 ,71 ,7 ,818],
[1359756, 911 ,91 ,40 ,4 ,326 ,988 ,1],
[915, 1 ,1 ,9 ,897 ,7],
[12, 3 ,3 ,5],
[1254753, 291 ,5 ,7 ,9 ,41 ,7 ,826 ,58 ,1],
[4275190, 702 ,35 ,87 ,2 ,5 ,5],
[54750, 696 ,34 ,75],
[490998931, 65 ,9 ,468 ,54 ,905 ,23 ,1],
[161948805, 482 ,4 ,8 ,5 ,26 ,8 ,20 ,6],
[20648862546, 82 ,4 ,6 ,572 ,22 ,9 ,6 ,530 ,6],
[3125600, 20 ,834 ,91 ,418 ,8 ,40],
[149520, 89 ,5 ,56 ,6],
[4602270405, 65 ,8 ,2 ,4 ,910 ,5 ,433 ,4 ,5],
[2328979191, 44 ,5 ,14 ,8 ,9 ,654 ,814 ,11],
[140130, 46 ,9 ,4 ,6 ,4 ,7 ,6 ,4 ,444 ,8 ,9],
[37543990, 1 ,9 ,3 ,80 ,92 ,6 ,3 ,1 ,37 ,170],
[37925201520, 11 ,3 ,4 ,3 ,3 ,477 ,1 ,7 ,20 ,6 ,6],
[8701, 26 ,2 ,1 ,35 ,8 ,560 ,2 ,39],
[77474, 1 ,719 ,6 ,743 ,4 ,40 ,7 ,51 ,5],
[789636, 540 ,487 ,3 ,370 ,326],
[16156392754413, 223 ,805 ,47 ,5 ,9 ,4 ,413],
[1554, 52 ,45 ,2 ,443 ,911 ,6],
[3171, 91 ,963 ,1 ,3 ,9],
[12014295, 3 ,87 ,8 ,927 ,3 ,2 ,4 ,3 ,6 ,53 ,3],
[28736, 1 ,7 ,191 ,425 ,46 ,78],
[739, 5 ,96 ,51 ,92 ,1],
[67092408236, 2 ,821 ,137 ,62 ,37 ,28],
[28040020908, 116 ,5 ,4 ,4 ,9 ,336 ,811 ,7 ,6],
[62339520, 64 ,25 ,847 ,5 ,46 ,90],
[73771505690, 922 ,143 ,1 ,8 ,2 ,4 ,2 ,2 ,7 ,10],
[29074322, 3 ,96 ,8 ,15 ,1 ,473 ,9 ,2 ,5 ,22],
[63009501, 11 ,95 ,5 ,6 ,938 ,7 ,113],
[70987224670, 1 ,4 ,9 ,1 ,2 ,644 ,8 ,1 ,6 ,1 ,469],
[817, 4 ,1 ,3 ,8 ,6 ,97],
[1666509161, 1 ,5 ,664 ,6 ,7 ,7 ,5 ,9 ,9 ,3 ,5 ,9],
[14179144144, 3 ,4 ,513 ,5 ,104 ,41 ,46],
[98291189, 59 ,79 ,4 ,8 ,659 ,21],
[11808436642, 417 ,495 ,26 ,2 ,572 ,2],
[49340170, 406 ,7 ,6 ,4 ,70 ,121],
[30650304, 4 ,5 ,354 ,346 ,18 ,244],
[30210212, 5 ,41 ,5 ,93 ,581 ,5 ,5 ,55 ,87],
[1206388, 19 ,73 ,9 ,2 ,6 ,3 ,8 ,9 ,20 ,8 ,1],
[189, 185 ,3 ,1],
[530030, 25 ,1 ,278 ,788 ,242],
[18288, 8 ,318 ,8 ,4 ,7 ,4],
[16712801285, 32 ,6 ,8 ,81 ,707 ,960 ,5],
[3377504, 46 ,1 ,17 ,4 ,706],
[283886218, 2 ,629 ,8 ,2 ,2 ,2 ,9 ,4 ,7 ,174 ,7],
[1736064, 12 ,75 ,468 ,267 ,704 ,3],
[64, 4 ,51 ,8 ,1],
[753040800, 518 ,9 ,3 ,3 ,6 ,233 ,4 ,5 ,9 ,5 ,9],
[553737781, 9 ,8 ,8 ,58 ,234 ,6 ,3 ,5 ,1 ,5 ,1],
[1367681, 96 ,2 ,2 ,156 ,62 ,597 ,61],
[106460, 5 ,91 ,6 ,98 ,63],
[1098372, 4 ,1 ,282 ,811 ,372],
[140890456, 5 ,9 ,909 ,945 ,40 ,6],
[8340, 55 ,78 ,8 ,7 ,892],
[193726460249, 5 ,439 ,49 ,353 ,60 ,2 ,49],
[141338352, 678 ,28 ,691 ,76 ,2],
[9856, 3 ,6 ,54 ,38 ,77],
[42123, 9 ,4 ,19 ,2 ,739],
[242468644, 647 ,936 ,579 ,61 ,4],
[230745066, 903 ,7 ,78 ,365 ,96],
[445943880, 23 ,95 ,2 ,3 ,18 ,6 ,1 ,648 ,9],
[1808893944, 7 ,2 ,7 ,6 ,4 ,7 ,9 ,1 ,81 ,78 ,964],
[2017445149, 61 ,33 ,3 ,573 ,872 ,14 ,2 ,7],
[435756771, 4 ,7 ,41 ,24 ,61 ,636 ,7 ,4 ,9],
[51689, 2 ,7 ,3 ,11 ,4 ,79 ,69 ,91],
[1752948, 6 ,8 ,7 ,7 ,219 ,62 ,54],
[121506, 45 ,48 ,8 ,7 ,546],
[15984364, 78 ,81 ,774 ,7 ,61 ,1 ,64],
[717180399, 6 ,9 ,1 ,11 ,4 ,4 ,2 ,222 ,8 ,7 ,9 ,3],
[231133474, 903 ,28 ,868 ,51 ,286],
[4601521, 262 ,56 ,4 ,8 ,7 ,166 ,4 ,3 ,1 ,1],
[10555808, 960 ,85 ,10 ,5 ,80 ,8],
[491087718, 7 ,7 ,10 ,868 ,7 ,60 ,158],
[152320, 12 ,56 ,5 ,7 ,64],
[411081, 47 ,1 ,2 ,1 ,2 ,7 ,5 ,4 ,8 ,1 ,1],
[79530, 24 ,174 ,5 ,1 ,4 ,1 ,117 ,1 ,8],
[405, 4 ,5 ,48 ,7 ,6],
[93674138, 3 ,89 ,73 ,3 ,4 ,936 ,7 ,4 ,3 ,8],
[3717392, 9 ,9 ,7 ,3 ,352 ,5 ,9 ,24 ,8 ,6 ,2],
[33776303, 94 ,294 ,230 ,87 ,293],
[23979563100, 393 ,956 ,555 ,5 ,23],
[292320, 74 ,9 ,61 ,29 ,70],
[983175600, 9 ,431 ,2 ,422 ,844 ,8 ,75],
[26865, 79 ,7 ,98 ,5 ,3],
[270720, 3 ,4 ,1 ,474 ,4 ,5 ,3 ,83 ,47 ,5 ,2],
[39508, 559 ,1 ,9 ,7 ,308],
[9480738, 61 ,42 ,46 ,29 ,69],
[16204, 65 ,247 ,2 ,82 ,65],
[251093080, 8 ,770 ,72 ,4 ,610 ,482 ,1],
[616869, 2 ,58 ,85 ,3 ,33 ,31],
[4239559, 8 ,4 ,776 ,50 ,759],
[167271, 70 ,3 ,72 ,590 ,4 ,4 ,883],
[219080, 975 ,7 ,4 ,8 ,8 ,1 ,1 ,8 ,1 ,3 ,532],
[120576020, 312 ,2 ,96 ,40 ,20],
[39262, 1 ,382 ,6 ,4 ,1 ,62],
[1750434, 374 ,2 ,2 ,76 ,31 ,3 ,9 ,587 ,6],
[1628938, 3 ,1 ,7 ,1 ,8 ,4 ,12 ,895 ,4 ,5 ,18],
[1608, 2 ,9 ,6 ,8 ,216],
[5466689812, 2 ,1 ,3 ,6 ,591 ,75 ,8 ,9 ,76 ,5 ,5],
[3368293974, 83 ,48 ,2 ,852 ,989 ,61 ,6],
[9246, 75 ,71 ,4 ,372 ,29 ,556 ,6],
[24758643213, 99 ,91 ,52 ,8 ,1 ,91 ,3 ,213],
[85379574, 90 ,296 ,10 ,717 ,938],
[7411924, 2 ,5 ,9 ,8 ,59 ,5 ,7 ,4 ,37 ,1 ,92 ,4],
[14439842712, 96 ,57 ,1 ,61 ,721 ,60 ,792],
[25942, 7 ,91 ,7 ,7 ,367 ,272 ,2 ,3 ,61],
[2009867742, 1 ,5 ,6 ,3 ,8 ,91 ,425 ,5 ,8 ,4 ,2 ,2],
[8100, 5 ,20 ,81],
[247376, 41 ,2 ,427 ,486 ,2],
[36664, 53 ,86 ,25 ,8],
[2203718597, 5 ,327 ,4 ,13 ,64 ,405 ,197],
[21061260, 66 ,46 ,29 ,43 ,14 ,1 ,3 ,484],
[11624536, 86 ,9 ,1 ,8 ,5 ,3 ,4 ,28 ,4 ,217 ,9],
[3331316592, 939 ,24 ,142 ,347 ,3],
[393313984, 1 ,1 ,746 ,4 ,6 ,7 ,82 ,9 ,7 ,8 ,7 ,8],
[12332, 960 ,53 ,23 ,5 ,2 ,6 ,975 ,2 ,6],
[368101809, 80 ,4 ,1 ,7 ,3 ,604 ,9 ,451 ,4 ,5],
[305907, 500 ,14 ,85 ,3 ,8 ,7],
[3173580, 32 ,9 ,5 ,11 ,80],
[22376, 707 ,31 ,3 ,26 ,416 ,9 ,5],
[267114879, 6 ,95 ,6 ,55 ,9 ,710 ,2 ,62 ,37],
[47977888197, 47 ,5 ,6 ,41 ,7 ,888 ,197],
[4058586, 74 ,3 ,320 ,1 ,408 ,1 ,3 ,81 ,2],
[9850439, 5 ,6 ,6 ,3 ,2 ,121 ,6 ,4 ,64 ,5 ,66],
[830200808, 676 ,731 ,11 ,7 ,30 ,31 ,8 ,1],
[65120079512, 130 ,2 ,5 ,5 ,74 ,8 ,9 ,9 ,8 ,3 ,1 ,2],
[1410, 25 ,1 ,53 ,3 ,24 ,5],
[164302236, 3 ,14 ,6 ,51 ,2 ,69 ,252 ,3],
[9695040, 78 ,981 ,3 ,4 ,7 ,8 ,9 ,76 ,20 ,5],
[31914715, 871 ,458 ,5 ,2 ,2 ,6 ,8 ,8 ,10 ,1],
[44007405, 5 ,8 ,2 ,492 ,59 ,326 ,1 ,4 ,6 ,7],
[28607442358, 61 ,9 ,62 ,7 ,907 ,6 ,359],
[14200, 4 ,8 ,1 ,4 ,9 ,54 ,2 ,7 ,163 ,5 ,7 ,8],
[29912, 47 ,93 ,8 ,87 ,6 ,2],
[1216, 415 ,699 ,90 ,3 ,4 ,3 ,2],
[61976625993, 79 ,705 ,6 ,6 ,1 ,877 ,77 ,9],
[62020, 84 ,732 ,7 ,50 ,475],
[9920575422, 35 ,83 ,683 ,1 ,5 ,42 ,2],
[28753659, 66 ,1 ,5 ,523 ,4 ,269 ,6 ,46],
[499210, 50 ,21 ,7 ,32 ,2 ,12],
[490392, 8 ,2 ,94 ,5 ,5 ,527 ,30 ,441],
[68883749136, 8 ,74 ,4 ,8 ,56 ,2 ,96 ,6 ,216],
[123493, 2 ,61 ,32 ,11 ,6 ,8 ,954 ,41],
[3374244, 156 ,6 ,6 ,398 ,9],
[122, 9 ,6 ,6 ,62],
[30831910, 179 ,4 ,648 ,260 ,70],
[6168597929, 7 ,3 ,7 ,3 ,28 ,2 ,3 ,4 ,7 ,481 ,4 ,5],
[2888, 4 ,9 ,6 ,6 ,277 ,4 ,2],
[45490, 5 ,8 ,315 ,7 ,84 ,9 ,2 ,38 ,6 ,3 ,7],
[2121768, 47 ,684 ,1 ,11 ,6],
[194810726, 3 ,23 ,8 ,17 ,82 ,48 ,43 ,97],
[7926469, 5 ,9 ,69 ,86 ,6 ,414 ,9 ,16],
[542725362, 168 ,5 ,646 ,85 ,25 ,2 ,110],
[12871320, 73 ,918 ,3 ,9 ,2 ,8 ,8 ,73 ,24],
[110766661, 2 ,5 ,6 ,4 ,7 ,584 ,80 ,9 ,4 ,8 ,5 ,1],
[8124928240, 20 ,312 ,3 ,206 ,40],
[1049, 8 ,2 ,99 ,170 ,770],
[824256407, 563 ,24 ,4 ,610 ,4],
[393358434, 726 ,105 ,91 ,859 ,6],
[38190276, 7 ,12 ,4 ,3 ,4 ,746 ,9 ,4 ,54 ,3 ,6],
[90162, 18 ,238 ,21 ,3 ,195],
[62622, 54 ,8 ,6 ,2 ,2],
[20647, 14 ,1 ,60 ,5 ,47],
[171, 1 ,69 ,7 ,64 ,30],
[1794, 749 ,1 ,419 ,248 ,330 ,48],
[914500, 3 ,60 ,3 ,4 ,5 ,261 ,10 ,992 ,8],
[792066628, 5 ,7 ,7 ,1 ,5 ,6 ,4 ,641 ,26 ,2 ,2 ,6],
[37407000, 648 ,3 ,89 ,674 ,75],
[10001377331, 2 ,33 ,6 ,902 ,7 ,4 ,2 ,1 ,6 ,5 ,3 ,1],
[11327400, 76 ,37 ,33 ,16 ,775],
[3199224, 82 ,87 ,676 ,14 ,28],
[434606464, 6 ,2 ,574 ,3 ,2 ,2 ,3 ,3 ,748 ,8 ,8],
[28503052248, 4 ,5 ,761 ,8 ,52 ,712 ,56 ,33],
[5441, 22 ,4 ,184 ,1 ,657],
[1924354, 83 ,644 ,9 ,4 ,82],
[650792283390, 325 ,395 ,87 ,27 ,16 ,95 ,2],
[172585, 423 ,1 ,44 ,692 ,5 ,106 ,2 ,2],
[816, 804 ,1 ,8 ,3],
[8617384, 37 ,6 ,8 ,11 ,3 ,9 ,7 ,9 ,6 ,78 ,40],
[5118957, 1 ,993 ,572 ,120 ,85 ,9],
[7211827560, 798 ,65 ,20 ,43 ,21],
[161839, 5 ,5 ,3 ,3 ,6 ,8 ,892 ,5 ,6 ,9 ,820],
[22326850, 4 ,66 ,79 ,8 ,9 ,5 ,811 ,2 ,1 ,20],
[3320238, 2 ,96 ,5 ,53 ,1 ,318],
[75810, 4 ,4 ,8 ,9 ,6 ,35],
[1303740489, 59 ,187 ,7 ,331 ,78 ,51],
[2071, 5 ,23 ,31 ,684 ,519],
[1409440, 7 ,4 ,4 ,32 ,1 ,155 ,285],
[525893, 3 ,867 ,5 ,3 ,8 ,4 ,5 ,7 ,716 ,8 ,2],
[235620, 238 ,51 ,1 ,2 ,94 ,612],
[136362275, 4 ,1 ,440 ,261 ,1 ,15 ,218 ,5],
[81194624, 633 ,6 ,509 ,9 ,6 ,9 ,3 ,74 ,7],
[38398954246, 857 ,448 ,53 ,5 ,424 ,8],
[4096, 2 ,3 ,9 ,8 ,8 ,41 ,6 ,24 ,5 ,76 ,5 ,2],
[73390, 7 ,282 ,8 ,37 ,56],
[7013, 35 ,105 ,5 ,6 ,4 ,3],
[2296, 711 ,863 ,9 ,8 ,705],
[22003119, 4 ,621 ,81 ,1 ,3 ,812 ,8 ,1 ,1 ,9],
[12156438, 30 ,391 ,4 ,2 ,1 ,6 ,2],
[195664, 4 ,4 ,35 ,127 ,76 ,8],
[85540, 1 ,3 ,56 ,443 ,140],
[2260779, 8 ,12 ,113 ,7 ,79],
[23747232312, 23 ,5 ,933 ,3 ,2 ,22 ,46 ,909],
[2678400, 372 ,3 ,800 ,3],
[121368, 223 ,8 ,65 ,16 ,389],
[1569526, 573 ,2 ,39 ,5 ,707 ,1 ,7 ,280],
[3484, 68 ,37 ,3 ,39 ,926],
[1000054560, 431 ,5 ,290 ,58 ,8],
[44435827, 86 ,358 ,358 ,26 ,1],
[5080, 527 ,4 ,3 ,99 ,752 ,60 ,36 ,2],
[1653900719, 5 ,881 ,65 ,370 ,712 ,7],
[105906, 499 ,80 ,2 ,4 ,387 ,76 ,38],
[149392679, 1 ,493 ,92 ,679],
[70, 1 ,27 ,4 ,21 ,17],
[376653066, 69 ,7 ,82 ,951 ,6],
[23455, 8 ,6 ,4 ,3 ,54 ,3 ,8 ,103],
[684, 47 ,427 ,6 ,111 ,93],
[538105211, 53 ,79 ,5 ,8 ,147 ,214],
[427, 2 ,39 ,4 ,227 ,36],
[46721700, 439 ,1 ,2 ,2 ,7 ,821 ,1 ,6 ,75],
[96998408, 4 ,103 ,5 ,1 ,3 ,9 ,64 ,10 ,5 ,8 ,8],
[929792, 7 ,22 ,51 ,48 ,8 ,908],
[182108262, 9 ,728 ,3 ,26 ,8 ,1 ,3 ,5 ,1 ,3 ,3 ,6],
[27013609896, 9 ,6 ,4 ,76 ,5 ,6 ,6 ,5 ,464 ,7 ,7 ,8],
[84960, 4 ,1 ,66 ,778 ,96],
[9789, 29 ,8 ,6 ,4 ,309 ,8 ,213],
[1254292600, 87 ,6 ,2 ,9 ,982 ,76 ,10 ,811],
[40395182, 95 ,2 ,823 ,958 ,6 ,7 ,1 ,6 ,5],
[137994809, 155 ,33 ,47 ,4 ,574 ,43],
[101860, 98 ,56 ,9 ,316 ,8 ,45],
[6394940, 223 ,416 ,454 ,40 ,10],
[299574, 32 ,19 ,3 ,142 ,951 ,9],
[40, 3 ,4 ,4],
[410609520, 19 ,8 ,342 ,8 ,23 ,968 ,15],
[115650, 535 ,12 ,5 ,6 ,3],
[2591820, 1 ,2 ,38 ,1 ,7 ,5 ,5 ,6 ,1 ,85 ,44 ,7],
[1544, 3 ,45 ,8 ,683 ,717 ,1],
[4919765291, 872 ,2 ,809 ,7 ,994 ,5 ,58],
[106160194, 41 ,99 ,250 ,48 ,3 ,47 ,7 ,71],
[10116145, 2 ,3 ,3 ,7 ,2 ,3 ,1 ,83 ,6 ,1 ,1 ,45],
[70200, 70 ,152 ,45 ,3],
[953666, 452 ,2 ,48 ,91 ,3 ,21 ,6 ,726],
[1989, 365 ,837 ,787],
[138170, 1 ,7 ,239 ,82 ,78 ,904 ,2],
[1596348, 97 ,37 ,627 ,19 ,6],
[14469223, 52 ,94 ,4 ,1 ,74 ,3],
[18819317430, 508 ,63 ,37 ,7 ,4 ,30],
[23779386, 977 ,57 ,7 ,3 ,61],
[130494339, 5 ,945 ,1 ,26 ,531 ,8 ,4 ,2 ,3],
[57240, 9 ,3 ,63 ,53 ,12],
[15430473, 937 ,6 ,3 ,8 ,1 ,4 ,6 ,2 ,9 ,301 ,9],
[26979225507, 106 ,70 ,1 ,91 ,67 ,25 ,507],
[947, 87 ,49 ,4 ,10 ,3 ,3 ,99 ,282 ,6],
[7861, 2 ,92 ,570 ,9 ,312],
[1902023, 889 ,73 ,36 ,654 ,29],
[217204008, 6 ,3 ,89 ,84 ,562 ,43],
[12280896, 9 ,336 ,272 ,9 ,414],
[8748, 8 ,2 ,55 ,3 ,7 ,5 ,7 ,4 ,1 ,74 ,5 ,8],
[3875, 77 ,44 ,4 ,31],
[98858631, 82 ,8 ,4 ,9 ,54 ,5 ,40 ,7 ,4 ,31 ,3],
[108659570, 5 ,133 ,449 ,865 ,214],
[21472929, 4 ,60 ,4 ,88 ,931],
[25548265, 76 ,386 ,4 ,929 ,2 ,4 ,216 ,1],
[33610664231, 7 ,8 ,25 ,530 ,48 ,408 ,459],
[9907455156, 30 ,330 ,2 ,4 ,1 ,4 ,550 ,8 ,7 ,9],
[44466396000, 785 ,98 ,5 ,170 ,975 ,116],
[261, 6 ,246 ,9],
[931780082, 3 ,367 ,63 ,8 ,5 ,79 ,7 ,3 ,76 ,9],
[890165367555, 5 ,257 ,904 ,82 ,97 ,91 ,79],
[517812, 11 ,3 ,7 ,74 ,301 ,2 ,90],
[19756008, 6 ,23 ,9 ,7 ,7 ,5 ,9 ,329 ,9 ,2 ,6 ,2],
[318, 8 ,6 ,2 ,2 ,36],
[13300, 3 ,1 ,2 ,46 ,9 ,1 ,2 ,9 ,36 ,4],
[9313, 72 ,5 ,55 ,2 ,843],
[6212221470, 660 ,87 ,42 ,94 ,398 ,3 ,7],
[11485480, 7 ,114 ,568 ,598 ,731 ,8 ,8],
[272945, 9 ,5 ,11 ,9 ,99 ,2 ,97 ,9 ,70 ,73],
[7338600, 832 ,6 ,7 ,5 ,855 ,7 ,8 ,243],
[2885, 32 ,9 ,4 ,8 ,3 ,196 ,9 ,2 ,4 ,1 ,2 ,5],
[64886, 27 ,8 ,3 ,88],
[53795280, 561 ,7 ,3 ,41 ,7 ,5 ,22],
[1071, 60 ,636 ,58 ,3 ,264 ,50],
[1614728, 3 ,887 ,5 ,5 ,5 ,619 ,3 ,7 ,6 ,8 ,4],
[5737474530, 3 ,106 ,4 ,2 ,6 ,9 ,9 ,6 ,45 ,2 ,9 ,1],
[471385127970, 506 ,857 ,8 ,729 ,930],
[29038135, 20 ,3 ,61 ,335 ,7],
[116693220, 9 ,845 ,7 ,35 ,545 ,7 ,4],
[2718, 23 ,6 ,90 ,1 ,107],
[1957951008, 9 ,581 ,57 ,78 ,8 ,6],
[872105643, 78 ,64 ,8 ,255 ,8 ,76 ,19 ,9],
[7050631, 5 ,5 ,8 ,7 ,1 ,4 ,88 ,2 ,9 ,985 ,6 ,1],
[540612630, 662 ,4 ,7 ,7 ,5 ,4 ,2 ,9 ,9 ,8 ,5 ,81],
[5664885508692, 71 ,9 ,5 ,5 ,7 ,4 ,2 ,9 ,9 ,22 ,486],
[981739455122, 34 ,4 ,86 ,87 ,792 ,1 ,68 ,9 ,2],
[2611086, 86 ,506 ,6 ,3 ,73 ,50],
[604443, 23 ,15 ,707 ,62 ,749],
[166424375, 41 ,50 ,9 ,5 ,5 ,4 ,4 ,5 ,5 ,13 ,5 ,5],
[142705, 6 ,1 ,81 ,859 ,97 ,8],
[96512, 372 ,5 ,4 ,8 ,8],
[10300682, 4 ,24 ,469 ,8 ,1 ,4 ,48 ,98],
[735876264, 817 ,53 ,7 ,4 ,9 ,202 ,6 ,8 ,48],
[63035035, 5 ,7 ,3 ,11 ,50 ,35],
[385290, 8 ,6 ,22 ,8 ,5 ,5 ,1 ,4 ,477 ,83 ,9],
[223068560, 93 ,842 ,8 ,31 ,962],
[28245564048, 939 ,6 ,25 ,5 ,2 ,166 ,9 ,4 ,8],
[62601, 6 ,97 ,2 ,94 ,1 ,49 ,905 ,5],
[5223705, 728 ,8 ,2 ,7 ,8 ,656 ,9 ,8 ,81],
[186592, 6 ,47 ,50 ,562 ,8],
[153887794, 191 ,209 ,3 ,5 ,257 ,49],
[45415065861, 8 ,7 ,653 ,769 ,3 ,786 ,26 ,9],
[4765325236, 5 ,63 ,7 ,526 ,6 ,39 ,6 ,7 ,3 ,6],
[9252704, 694 ,2 ,57 ,1 ,4 ,4 ,796 ,8],
[244739761, 4 ,5 ,21 ,742 ,4 ,2 ,796 ,9],
[3025066, 17 ,3 ,3 ,8 ,7 ,97 ,7 ,8 ,82],
[44785466, 68 ,9 ,65 ,377 ,89],
[1189, 25 ,978 ,80 ,97 ,9],
[37921905, 6 ,4 ,5 ,98 ,61 ,28 ,6 ,8 ,7 ,3 ,9 ,5],
[683378968, 9 ,4 ,360 ,328 ,938 ,9 ,5 ,7 ,4],
[746, 4 ,3 ,58 ,9 ,8 ,33],
[20300880, 8 ,4 ,75 ,8 ,4 ,67 ,72 ,6 ,7 ,1 ,6 ,8],
[4859680280, 50 ,2 ,563 ,2 ,456 ,4 ,8 ,91],
[101953865160, 129 ,755 ,3 ,2 ,7 ,372 ,67],
[739753, 791 ,7 ,927 ,2 ,7],
[21134, 1 ,21 ,134],
[16517, 1 ,99 ,83],
[80920, 80 ,2 ,9 ,5 ,56],
[33953, 92 ,1 ,9 ,41 ,5],
[197610127, 7 ,7 ,7 ,6 ,84 ,3 ,674 ,10 ,67],
[125399, 76 ,98 ,3 ,5 ,24],
[6914, 4 ,24 ,262 ,1 ,53],
[953, 81 ,9 ,66 ,1 ,152 ,5 ,1 ,3 ,2 ,7 ,2],
[1018, 7 ,33 ,5 ,818],
[729072, 6 ,55 ,32 ,4 ,249 ,8],
[241744595, 48 ,1 ,347 ,95 ,1 ,90 ,5 ,5 ,9 ,6],
[682083, 4 ,4 ,294 ,29 ,3],
[1806679601, 2 ,9 ,2 ,49 ,2 ,18 ,699 ,5 ,8 ,1],
[145013184, 6 ,7 ,69 ,842 ,3 ,192],
[58789610, 16 ,1 ,902 ,5 ,901 ,1 ,55],
[2160, 121 ,9 ,9 ,919 ,71],
[60835040199, 6 ,7 ,2 ,8 ,31 ,4 ,4 ,890 ,9 ,6 ,3 ,9],
[413542, 369 ,639 ,783 ,7 ,23 ,2],
[3963317850, 675 ,479 ,227 ,6 ,9],
[2222650400, 2 ,5 ,3 ,49 ,300 ,9 ,13 ,25 ,32],
[933, 499 ,424 ,10],
[459239372, 1 ,3 ,57 ,2 ,23 ,9 ,372],
[63771446, 702 ,85 ,3 ,90 ,7 ,9 ,9 ,2],
[2394004394, 7 ,600 ,57 ,4 ,340 ,54],
[7662017, 47 ,74 ,22 ,98 ,1 ,64 ,553],
[695505, 31 ,862 ,13 ,31 ,43 ,2 ,585],
[11014180797, 280 ,97 ,400 ,49 ,8],
[564216, 82 ,172 ,5 ,7 ,8],
[13588211, 2 ,9 ,356 ,7 ,2 ,97 ,7 ,298 ,7],
[1159803311118, 640 ,711 ,64 ,31 ,181 ,18],
[2280680821, 9 ,2 ,560 ,8 ,7 ,3 ,1 ,4 ,5 ,5 ,11 ,1],
[1632680, 50 ,50 ,5 ,1 ,3 ,7 ,1 ,227 ,85 ,7],
[1705, 7 ,9 ,12 ,3 ,55],
[157424832, 18 ,592 ,336 ,8 ,2 ,324 ,6 ,8],
[7861936445, 69 ,1 ,17 ,42 ,335 ,67],
[40608, 6 ,1 ,42 ,94 ,9],
[88857414912, 52 ,841 ,446 ,42 ,64 ,83],
[11418623, 943 ,295 ,263 ,55 ,41],
[756, 94 ,65 ,555 ,4 ,19 ,19],
[263007, 4 ,8 ,2 ,8 ,826 ,279 ,191],
[69918412, 8 ,4 ,8 ,721 ,86 ,412],
[10622, 6 ,219 ,11 ,8 ,22],
[40846854569, 85 ,3 ,292 ,841 ,16 ,9],
[1399560878, 6 ,5 ,972 ,3 ,1 ,2 ,727 ,9 ,92],
[1251967628, 40 ,834 ,8 ,56 ,4 ,67],
[1730, 373 ,586 ,18 ,688 ,65],
[5763837, 3 ,3 ,81 ,683 ,97],
[13534026, 4 ,9 ,727 ,6 ,517],
[501787440, 4 ,9 ,4 ,7 ,7 ,9 ,8 ,5 ,5 ,462 ,84 ,6],
[382060224, 4 ,96 ,3 ,7 ,52 ,6 ,37 ,84],
[90329420, 467 ,509 ,3 ,3 ,380],
[266046851022, 664 ,9 ,2 ,4 ,33 ,1 ,255 ,1 ,2 ,2],
[13907000870, 351 ,9 ,9 ,7 ,4 ,1 ,6 ,563 ,6 ,5 ,7],
[95025, 1 ,524 ,181],
[9694669442, 8 ,88 ,552 ,43 ,106 ,32 ,2],
[25012998, 3 ,9 ,4 ,1 ,7 ,9 ,472 ,1 ,3 ,256 ,6],
[2762479, 12 ,907 ,214 ,381],
[463098609028, 46 ,30 ,98 ,608 ,9 ,92 ,34],
[345847101, 11 ,3 ,1 ,79 ,4 ,529 ,9 ,9 ,9 ,8 ,3],
[6629013504, 2 ,2 ,790 ,5 ,4 ,4 ,8 ,6 ,362 ,8 ,3],
[151639320, 3 ,481 ,8 ,98 ,85 ,37],
[900851201, 95 ,8 ,1 ,35 ,2 ,94 ,6 ,5 ,310],
[3023181756, 839 ,9 ,3 ,3 ,635 ,6 ,5 ,7 ,7 ,6 ,3],
[78970, 594 ,502 ,9 ,8 ,56],
[243927620, 37 ,450 ,5 ,14 ,5 ,994 ,1 ,8 ,2],
[5002, 69 ,9 ,8 ,8 ,10],
[146846990, 4 ,5 ,8 ,8 ,80 ,9 ,764 ,8 ,10 ,4],
[8376971812, 957 ,90 ,8 ,97 ,18 ,12],
[25982, 484 ,33 ,8 ,1 ,5 ,86],
[87972, 116 ,3 ,738 ,73 ,2 ,75],
[30219, 855 ,7 ,5 ,7 ,7],
[40049, 804 ,3 ,4 ,3 ,4 ,9 ,543 ,893],
[4096449691, 532 ,5 ,385 ,12 ,4 ,4 ,8 ,5 ,5 ,1],
[1774079, 1 ,1 ,790 ,35 ,64],
[18138613, 1 ,813 ,85 ,6 ,5 ,3],
[7056, 6 ,8 ,9 ,47 ,3 ,660 ,2 ,6 ,9 ,3 ,3],
[5286779, 6 ,88 ,67 ,64 ,9 ,5],
[21548813239, 3 ,91 ,7 ,4 ,4 ,328 ,6 ,3 ,6 ,7 ,5 ,4],
[54193526, 609 ,98 ,2 ,5 ,454],
[3313, 31 ,98 ,1 ,8 ,267],
[1272773, 82 ,5 ,57 ,31 ,6],
[151927862, 9 ,4 ,794 ,712 ,2 ,78 ,1 ,4 ,4 ,8],
[11599243, 51 ,9 ,691 ,86 ,906 ,43],
[377568, 6 ,267 ,279 ,76 ,9],
[4759070, 4 ,757 ,93 ,5 ,8 ,5 ,46 ,962],
[475964300, 3 ,6 ,9 ,2 ,3 ,758 ,1 ,4 ,115 ,7 ,5],
[3902012400, 3 ,17 ,381 ,7 ,417 ,520 ,55],
[539408, 3 ,47 ,518 ,56 ,3],
[471833152952, 77 ,781 ,4 ,454 ,784 ,9 ,52],
[53928, 6 ,1 ,6 ,6 ,1 ,5 ,5 ,4 ,430 ,57 ,7 ,9],
[744595, 58 ,5 ,914 ,762 ,121],
[6604767, 7 ,55 ,3 ,83 ,8 ,1 ,9 ,3 ,758 ,9],
[30467264138, 74 ,5 ,107 ,48 ,2 ,91 ,42 ,38],
[7206, 5 ,6 ,2 ,67 ,6 ,6 ,4 ,7 ,678 ,9 ,6],
[3729982, 6 ,639 ,3 ,972 ,66 ,1 ,352],
[1400, 887 ,1 ,26 ,484 ,2],
[10618567232, 609 ,31 ,778 ,8 ,28],
[29344398, 2 ,7 ,9 ,2 ,190 ,1 ,653 ,1 ,398],
[3132084, 9 ,5 ,527 ,42 ,2 ,422],
[745442, 5 ,57 ,5 ,24 ,5 ,9 ,3 ,8 ,4],
[25389, 75 ,94 ,24 ,60 ,23 ,66],
[1064, 27 ,8 ,215 ,6 ,627],
[2202, 7 ,67 ,751 ,45 ,45 ,892],
[924, 4 ,7 ,84],
[131962, 8 ,5 ,8 ,781 ,4 ,5 ,1 ,2 ,6 ,734 ,4],
[15209, 1 ,440 ,8 ,9 ,5 ,2 ,7 ,1 ,32 ,64 ,9],
[13445076, 1 ,211 ,537 ,7 ,6 ,742 ,9 ,4],
[1662431, 999 ,441 ,33 ,47 ,4 ,6 ,887],
[30956672, 857 ,1 ,902 ,8 ,4],
[340965, 155 ,17 ,7 ,2 ,4 ,7 ,54 ,40 ,4 ,1],
[3530969806, 813 ,56 ,843 ,92 ,238],
[6677279225, 8 ,650 ,7 ,1 ,9 ,892 ,7 ,92 ,2 ,5],
[202833, 436 ,3 ,46 ,46 ,6 ,16],
[12852, 4 ,2 ,26 ,4 ,8 ,85 ,1 ,4 ,1 ,608],
[4329, 4 ,30 ,77 ,1 ,39],
[81602332, 1 ,1 ,9 ,46 ,90 ,657 ,975 ,3 ,7],
[2699179736, 7 ,543 ,5 ,1 ,1 ,5 ,1 ,6 ,71],
[344717100, 3 ,8 ,3 ,291 ,13 ,69 ,4 ,3 ,3 ,7 ,5],
[5328968, 2 ,24 ,5 ,1 ,2 ,1 ,1 ,2 ,2 ,780 ,7 ,8],
[883375333, 933 ,8 ,86 ,40 ,11 ,93],
[12854142, 50 ,2 ,72 ,3 ,318 ,2 ,709 ,7 ,6],
[1666239930991, 840 ,1 ,7 ,257 ,106 ,728],
[3577484468, 5 ,962 ,4 ,6 ,6 ,8 ,373 ,3 ,6 ,4 ,4],
[45942, 1 ,246 ,31 ,6],
[13400, 2 ,1 ,5 ,184 ,292 ,95 ,8],
[64941, 15 ,59 ,56 ,69 ,5 ,7],
[6366942354, 8 ,71 ,52 ,5 ,8 ,13 ,423 ,54],
[13377482272, 7 ,163 ,1 ,2 ,1 ,611 ,6 ,8 ,2 ,2 ,8],
[1939360587, 14 ,198 ,725 ,965 ,87],
[108931, 340 ,213 ,49 ,126 ,4 ,39],
[978436, 5 ,47 ,42 ,56 ,8 ,4],
[50217, 850 ,2 ,29 ,57],
[324576332842, 5 ,76 ,6 ,6 ,552 ,332 ,8 ,4 ,2],
[22302, 2 ,6 ,39 ,6 ,1 ,106 ,54],
[881555370, 9 ,4 ,5 ,8 ,4 ,8 ,5 ,84 ,1 ,9 ,15 ,62],
[123060175, 98 ,13 ,104 ,533 ,2 ,113 ,5],
[1884730165760, 5 ,1 ,1 ,1 ,2 ,981 ,66 ,9 ,80 ,52],
[1495440, 528 ,8 ,465 ,6],
[997086938313, 147 ,7 ,165 ,75 ,62 ,5 ,9 ,9 ,3],
[898129271, 55 ,3 ,4 ,543 ,2 ,5 ,46 ,93 ,77],
[49705, 835 ,6 ,4 ,396 ,8 ,13 ,5],
[776935098, 2 ,9 ,6 ,824 ,4 ,3 ,5 ,97 ,6 ,14 ,4],
[30572049, 95 ,2 ,2 ,8 ,8 ,1 ,95 ,7 ,358 ,4 ,9],
[18891, 9 ,2 ,6 ,21 ,4 ,74 ,5 ,5 ,726 ,3 ,7],
[6904400, 172 ,610 ,40],
[33890, 7 ,67 ,6 ,2 ,7 ,9 ,471 ,7 ,99],
[1349088, 2 ,6 ,4 ,5 ,8 ,4 ,6 ,7 ,155 ,2 ,47 ,8],
[3554816, 867 ,8 ,1 ,7 ,1 ,512],
[9997, 9 ,327 ,670],
[114417554850, 7 ,5 ,3 ,942 ,9 ,5 ,8 ,4 ,467 ,8 ,6],
[179, 5 ,3 ,2 ,9],
[33974281, 955 ,91 ,1 ,13 ,2 ,41 ,11 ,71],
[3934150675703, 673 ,7 ,8 ,8 ,81 ,16 ,8 ,5 ,9 ,5 ,3],
[5521774107, 6 ,741 ,39 ,21 ,895 ,107],
[85742668917, 4 ,67 ,34 ,271 ,9 ,7 ,2 ,6 ,5 ,6 ,7],
[25253, 77 ,326 ,55 ,96],
[1382589, 66 ,70 ,4 ,917 ,327 ,4 ,33],
[30290448160, 86 ,1 ,85 ,542 ,34 ,505 ,32],
[44311773, 6 ,2 ,323 ,711 ,117],
[3319100, 9 ,7 ,1 ,9 ,1 ,7 ,504 ,545 ,6 ,50],
[223237764792, 975 ,26 ,328 ,327 ,7],
[9361, 6 ,3 ,2 ,10 ,151],
[133084092525, 1 ,6 ,76 ,3 ,5 ,392 ,92 ,52 ,1 ,5],
[6014, 9 ,8 ,4 ,80 ,572 ,2],
[121315163, 51 ,85 ,892 ,3 ,166],
[39216456, 45 ,6 ,86 ,4 ,53],
[44331578775, 655 ,984 ,415 ,8 ,75 ,869],
[482258, 47 ,278 ,812 ,9 ,711 ,638],
[145159, 890 ,55 ,21 ,5 ,30 ,1 ,259],
[2529736075, 646 ,979 ,5 ,8 ,75],
[34250388482, 462 ,7 ,197 ,24 ,4 ,7 ,5 ,8 ,2 ,2],
[109320, 4 ,93 ,472 ,8 ,1 ,24 ,47 ,1],
[4074378, 4 ,3 ,4 ,5 ,7 ,2 ,87 ,94 ,8 ,7 ,7 ,6],
[3859615, 8 ,48 ,4 ,15 ,605 ,10],
[75656, 8 ,9 ,1 ,4 ,94 ,2 ,98],
[92471860, 4 ,866 ,94 ,190],
[584644384, 265 ,23 ,203 ,438 ,4],
[5701837232, 280 ,74 ,147 ,7 ,6 ,9 ,4 ,8 ,52],
[2262625, 87 ,9 ,78 ,151 ,35 ,86 ,51],
[527886, 525 ,2 ,8 ,8 ,8],
[44023034, 2 ,830 ,1 ,734 ,9 ,72 ,2],
[150440, 29 ,648 ,8 ,91 ,13],
[1076130, 74 ,34 ,1 ,6 ,990],
[114512499759, 63 ,6 ,1 ,2 ,9 ,7 ,1 ,1 ,9 ,759],
[40139167, 19 ,22 ,979 ,16 ,7],
[21414, 9 ,28 ,3 ,533 ,94],
[2510798344, 4 ,922 ,4 ,4 ,253 ,3 ,1 ,84 ,5 ,8],
[792, 5 ,52 ,6 ,20 ,4 ,51 ,5 ,9 ,3 ,87 ,3],
[504009644, 38 ,2 ,3 ,70 ,1 ,607 ,6],
[9509545, 2 ,2 ,943 ,19 ,376 ,45],
[1106472320, 273 ,1 ,81 ,9 ,6 ,6 ,8 ,457 ,7 ,5],
[438140, 2 ,320 ,9 ,5 ,76],
[2652799, 4 ,61 ,1 ,806 ,817],
[220, 6 ,3 ,83 ,74],
[59927247, 856 ,7 ,716 ,8 ,7],
[622284960, 454 ,9 ,840 ,8 ,1 ,160],
[5069046, 96 ,21 ,140 ,1 ,47 ,5 ,3 ,93],
[527, 7 ,5 ,513],
[983, 3 ,11 ,47 ,3 ,743],
[121980, 9 ,29 ,20 ,6 ,5 ,8 ,1 ,9 ,84 ,5 ,7 ,1],
[91650, 663 ,23 ,722 ,65 ,130],
[323870400, 135 ,5 ,126 ,952 ,4],
[64641600, 646 ,38 ,3 ,59 ,8],
[115420080, 96 ,183 ,40 ,6 ,2],
[321683040, 8 ,36 ,7 ,485 ,47 ,7],
[21700, 90 ,65 ,5 ,7 ,4],
[2651590, 84 ,17 ,4 ,4 ,7 ,17 ,50 ,53],
[432864, 19 ,8 ,501 ,1 ,32],
[439, 8 ,1 ,430],
[417145, 2 ,39 ,71 ,4 ,5],
[283940, 9 ,8 ,96 ,78 ,3 ,83 ,1 ,95 ,9 ,80],
[2511, 4 ,56 ,49 ,9 ,7 ,47],
[97360, 8 ,779 ,10 ,322 ,87 ,7],
[50259, 78 ,89 ,5 ,3 ,3],
[8011325, 58 ,573 ,96 ,2 ,3 ,98 ,5 ,24 ,5],
[741157, 288 ,6 ,9 ,70 ,4 ,38 ,3 ,9 ,4 ,61],
[77760221, 27 ,600 ,48 ,86 ,121 ,7 ,7],
[1003, 3 ,66 ,92 ,700 ,7 ,8 ,1]
]

# data = [
# [190, 10, 19],
# [3267, 81, 40, 27],
# [83,17, 5],
# [156, 15, 6],
# [7290, 6, 8, 6, 15],
# [161011, 16, 10, 13],
# [192, 17, 8, 14],
# [21037, 9, 7, 18, 13],
# [292, 11, 6, 16, 20],
# ]

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def calc_rec(row, i,val):
  if i == len(row):
    if not (val == 0 or val == row[len(row)-1]):
       return val
  else:
    return [calc_rec(row,i+1,val+row[i]),calc_rec(row,i+1,val*row[i]),calc_rec(row,i+1,int(str(val)+str(row[i])))]


def test_row(row):
  return flatten(calc_rec(row,1,0))

result = 0
for row in data:
  # print(test_row(row))
  if row[0] in  test_row(row):
    print(data.index(row),"/",len(data))
    result+=row[0]
    
print(result)