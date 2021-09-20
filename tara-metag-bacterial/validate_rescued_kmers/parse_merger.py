nb_sets = 241
nb_logs = 2543

"""
Arrange and analyse the number of non indexed kmers with respect to what is expected. 
Does several tasts: 
 0/ (preliminary) Assigns stations to technology when possible. 
 1/ Parse merger logs to grab the number of conserved kmers with or without rescue.
 2/ For each station: grab the total estimated number of kmers. 
 3/ Prints stats for each station associated to one technology. 
"""

"""
NON_SOLID: nombre de kmers distincts qui seraient perdus sans "rescue"
SAVE: nombre de kmers distincts sauvés par "rescue"

TOTAL WO/O: nombre total de kmers (avec redondance) des kmers conservés sans "rescue"
TOTAL W: nombre total de kmers (avec redondance) des kmers conservés par "rescue" uniquement
Donc : TOTAL W/O + TOTAL W c'est le nombre total de kmers indexés (avec redondance)
On n'a pas dans ces logs le nombre total de kmers distincts indexés.
"""

"""
Fichier type:
-------------
[INFO] - Fof:   /ccc/scratch/cont007/fg0001/peterlop/tara_metaG_bact_kmtricks/abundance1_logs/kmtricks0_0_1_metag_bact_tara_7f066239c8830b3d_ab1/storage/kmers_partitions/partition_0/partition0.fof
[INFO] - Mode:  bf_trp
[INFO] - A-min: 0
[INFO] - R-min: 1
[INFO] - Save-if: 1
[INFO] - ABS VEC: 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 3 3 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
[INFO] - NON_SOLID: 31 13582 42609 4372 504 1145 409 23218 246707 7618 17620 5289 45888 44314 26945 151 5608 2835 2319 504 5440 1112 3941 3616 12505 4514 8436 8004 10977 61081 90238 246 88723 13176 199835 39524 5841 898866 1756 1894 5551 4452 11237 6094 4918 299 138 353 1646 137291 60386 22119 547666 196158 6867 40885 5184 1517 21868 3325 93610 9039 1040 5151 2672 2740 9551 988763 406 16278 2493 263 351 2893 1268 3589 520 192 48791 30089 4136 673 16184 2655 6527 21032 9373 96675 251678 92119 4448 2583 1494 4688 1104 4640 90440 37367 19454 34165 7586 8778 5780 11546 94 1924 1370 4550 2918 2687 4886 226 5662 15497 20800 14252 20494 1230 16875 3702 7734 3129 1911 1478 2506 526 1218 1415 607 4176 760 7852 439959 436615 95352 32434 23914 24094 539 170976 7766 56774 899 263240 258398 149724 622472 194566 245796 423617 504663 9673 372964 626200 88001 159724 283375 434087 12763 325592 18426 162429 91219 116441 61561 129712 4809 75301 5633 336390 5985 126319 216244 13934 109001 8655 26351 544688 8465 2415 4909227 5522543 4469890 5085760 762748 13472 1703089 693137 1393910 588825 136362 120210 43600 26207 3246 10663 5725 1098 16377 2140 54790 1845 180129 4466 86888 1298 4902 1967 11997 315162 2208 3374 924 49113 35680 2045576 2047147 15077 16002 544094 1353431 3709 31655 48545 23100 953135 48184 66926 979273 1478546 17593 38155 32282 47105 1932671 1864041 37512 21395 26163 79930 460679 
[INFO] - SAVED: 31 13582 42609 4372 504 1145 409 23218 246707 7618 17620 5289 45888 44314 26945 151 5608 2835 2319 504 5440 1112 3941 3616 12505 4514 8436 8004 10977 61081 90238 246 88723 13176 199835 39524 5841 898866 1756 1894 5551 4452 11237 6094 4918 299 138 353 1646 137291 60386 22119 547666 196158 6867 40885 5184 1517 21868 3325 93610 9039 1040 5151 2672 2740 9551 988763 406 16278 2493 263 351 2893 1268 3589 520 192 48791 30089 4136 673 16184 2655 6527 21032 9373 96675 251678 92119 4448 2583 1494 4688 1104 4640 90440 37367 19454 34165 7586 8778 5780 11546 94 1924 1370 4550 2918 2687 4886 226 5662 15497 20800 14252 20494 1230 16875 3702 7734 3129 1911 1478 2506 526 1218 1415 607 4176 760 7852 439959 436615 95352 32434 23914 24094 539 170976 7766 56774 899 263240 258398 149724 622472 194566 245796 423617 504663 9673 372964 626200 88001 159724 283375 434087 12763 325592 18426 162429 91219 116441 61561 129712 4809 75301 5633 336390 5985 126319 216244 13934 109001 8655 26351 544688 8465 2415 4909227 5522543 4469890 5085760 762748 13472 1703089 693137 1393910 588825 136362 120210 43600 26207 3246 10663 5725 1098 16377 2140 54790 1845 180129 4466 86888 1298 4902 1967 11997 315162 2208 3374 924 49113 35680 2045576 2047147 15077 16002 544094 1353431 3709 31655 48545 23100 953135 48184 66926 979273 1478546 17593 38155 32282 47105 1932671 1864041 37512 21395 26163 79930 460679 
[INFO] - TOTAL W/O: 2393912557 788965208 528314561 972451468 1240274175 1017989170 1285240511 598157923 451248865 804169554 728490912 899024054 406143957 708343708 1007668856 743834780 862571217 1514135389 1267761136 1100821736 1489119581 1704437452 1599810523 1502091332 1479629765 1180492352 1187969484 1321139077 968900475 824843307 742431887 1134103621 813156975 1279242553 722894278 840266622 1221631879 579935159 1591451398 1396704425 1461875374 1315813367 1491024975 2033803237 1530266750 1432183719 1255494837 1095223289 740937546 759375684 1362726618 1200332404 1260966130 1141582627 805477363 955459915 899457133 988536134 1439988766 1165483793 870367537 1211226841 1578029345 1012464378 1287479561 1141685923 897383092 556729957 716817575 905282572 1162644763 1307123554 1041481491 1311387371 1289176467 992994711 1372910621 1321840656 580967215 925179715 941789899 914548252 771589566 1023021686 1207231747 1162157700 925943551 802961549 902832448 650945628 1088446829 1173632894 1035497806 1030162573 1191487023 1027275552 1145444735 1143232068 1849177289 1444810842 1284541157 977777668 930718916 1183845190 1400896746 903671751 1870389804 1103657176 911827618 1348850908 1201679473 1247702018 1205105341 1032121953 1015007178 1003288230 721565638 991419038 737885232 1062811379 693303146 1028720801 804997457 1052084521 903061837 1311884068 1174875658 1345390600 1107847524 1085679022 1273534864 805276121 421338063 420802164 1649794128 1284955187 1240411245 1110861587 1099917272 902494112 826170343 1360761436 1162841254 755162986 913950753 1125229942 1105984297 924731383 815805880 957685704 1166598500 890719069 852121669 755831404 1040060752 948378726 1194108975 817461965 837776016 1028116437 1008128401 895174406 1213262457 1247012821 1160200079 1022915466 960816874 1307294616 1099857404 1079836640 1229979137 1193415877 1247948745 1049250872 997394972 981237571 1127487234 371089764 1484243186 1389069542 91276852 76655849 120223511 76067905 430288657 1035856343 280557514 440513463 413868821 301482892 459846892 447710673 1139925611 1520888325 1193114295 709841829 943791404 1565221451 1097564435 1163337067 729970596 1600060015 754175457 1099114549 563966939 882802805 1185026165 1624423218 1009910400 432884058 1010948633 1372422084 1553907700 1042606690 1147943511 344968874 393741399 1201967912 894665483 449142485 480630333 989515456 1500756511 517100234 1023495219 275112587 727171897 591290320 429705260 371415611 1136869063 1171905372 638212364 982819689 416901329 404019976 1428587940 1409635113 1284406695 677589811 612287718 
[INFO] - TOTAL W: 53 23226 74160 7633 886 2034 712 40024 408546 13272 30194 9272 79805 76426 63032 281 9841 7000 5788 888 9304 1924 6775 6225 21266 7788 14566 13817 18548 103568 151585 438 147829 22434 328565 66449 10070 1442804 3066 3318 9581 7662 19181 10396 8502 522 250 628 2934 231194 100814 38194 877387 322172 12156 69511 9028 2705 36629 5757 156830 15459 1790 9126 4677 4768 16716 1570844 749 28150 4381 475 627 5043 2203 6374 934 349 84655 51014 7212 1223 28112 4621 11232 35656 16316 162463 413473 156647 7648 4512 2697 8279 1977 8187 148120 63632 32572 57884 13177 15102 10196 19871 169 3411 2399 7849 5212 4645 8455 406 9727 26662 35548 24509 35700 2160 29459 6436 13556 5461 3416 2608 4478 932 2156 2470 1074 7305 1369 13770 723244 717048 157091 54342 40690 41325 963 283519 13753 95229 1591 439269 427503 247148 985445 320124 403067 680031 801281 16993 606990 1016560 148412 264741 458113 703838 22284 527779 31824 272145 151115 192889 102940 219631 8456 126606 9910 547334 10394 211078 351214 24218 181677 15091 44751 891448 14730 4236 7062741 7816977 6492602 7316461 1236423 23466 2702123 1125972 2192389 980283 232662 205558 73236 44393 5669 18738 9969 1953 27945 3697 93806 3201 305468 7811 148087 2291 8430 3402 20656 529626 3879 5768 1596 82012 60311 3177821 3159632 25343 27254 897177 1353431 6441 52371 85667 39132 1537186 82793 113486 1563497 2362803 29643 63620 55299 79440 3012707 2911007 61934 35885 44234 133771 743112 
"""



def expected_FP(nb_total_kmers: int, FP_rate: float, k: int):
    return int(nb_total_kmers * (1-(1-FP_rate)**k))

total_kmers = [0 for read_set_id in range(nb_sets)]
total_kmers_wo_rescued = [0 for read_set_id in range(nb_sets)]
total_kmers_with_rescued = [0 for read_set_id in range(nb_sets)]

# Parse merger logs to grab the number of conserved kmers with or without rescue.
# Need to combine results from all partitions. 
for partition_id in range(nb_logs):
    with open(f"logs/merger{partition_id}.log") as log_file:
        for _ in range(8):  # we dont care the first lines
            line = log_file.readline()
        WO_line = log_file.readline().strip().split(':')[1].split()
        assert(len(WO_line) == nb_sets)
        for read_set_id, nb_indexed_wo_rescue in enumerate(WO_line):
            total_kmers_wo_rescued[read_set_id] += int(nb_indexed_wo_rescue)
            total_kmers_with_rescued[read_set_id] += int(nb_indexed_wo_rescue)
        WI_line = log_file.readline().strip().split(':')[1].split()
        for read_set_id, nb_indexed_with_rescue in enumerate(WI_line):
            total_kmers_with_rescued[read_set_id] += int(nb_indexed_with_rescue)

hs2000_set_names = set()
## deal with HS2000:
with open("stationsHS2000.txt") as mfile:
    for set_name in mfile:
        hs2000_set_names.add(set_name.split(" ")[0].strip())

hs2500_set_names = set()
## deal with HS2500:
with open("stationsHS2500.txt") as mfile:
    for set_name in mfile:
        hs2500_set_names.add(set_name.split(" ")[0].strip())

gaIIx_set_names = set()
## deal with GAIIx:
with open("stationsGAIIx.txt") as mfile:
    for set_name in mfile:
        gaIIx_set_names.add(set_name.split(" ")[0].strip())


k=20
ratios_with_rescue = []
ratios_kmers_seen_twice_or_more = []
print("ID station_name Total_kmers FP_wo_rescue FP_with_rescue\
      Techno Expected_FP \
      ratio_FP_wo \
      ratio_FP_with \
      NB_kmers_seen_once ratio_kmer_seen_once_Expected_FP \
      NB_kmers_seen_twice ratio_kmer_seen_twice_Expected_FP \
      ")
with open("bact_metaG_factorized.list") as mfile:
    sum_th_FP = 0
    sum_wo = 0
    sum_with = 0
    for read_set_id in range(nb_sets):
        set_name = mfile.readline().split(" ")[0]
        # define total_number_of_kmers:
        with open(f"estimated_kmer_counts_metaG_bact/{set_name}_count_k20_k20.hist") as est_file:
            total_number_of_kmers = int(int(est_file.readline().split()[-1]))#*2442/2443) # one log is empty, hence we decrease the total estimated number of kmers. Necessary?
            est_file.readline() # FO, we dont care
            kmer_seen_once = int(int(est_file.readline().split()[-1]))#*2442/2443)
            kmer_seen_twice = int(int(est_file.readline().split()[-1]))#*2442/2443)
        FP_wo_rescued = total_number_of_kmers-total_kmers_wo_rescued[read_set_id]
        FP_with_rescued = total_number_of_kmers-total_kmers_with_rescued[read_set_id]
        print(f"set{read_set_id} {set_name} {total_number_of_kmers} {kmer_seen_once} {FP_wo_rescued} {FP_with_rescued}", end="")

        threshold_2_kmers = kmer_seen_once
        threshold_3_kmers = kmer_seen_once + kmer_seen_twice
        techno = ""
        fp_rate = None
        if set_name in hs2000_set_names:
            techno = "hs2000"
            fp_rate = 0.00064086
        elif set_name in hs2500_set_names:
            techno = "hs2500"
            fp_rate = 0.004838
        elif set_name in gaIIx_set_names:
            techno = "gaIIx"
            fp_rate = 0.0017155

        if techno == "":
            print(" UNDEF")
        else:
            expected_FP_ = expected_FP(total_number_of_kmers, fp_rate,  k)
            sum_th_FP += expected_FP_
            sum_wo += FP_wo_rescued
            sum_with += FP_with_rescued
            ratio_wo = round(FP_wo_rescued/expected_FP_, 2)
            ratio_with = round(FP_with_rescued/expected_FP_, 2)
            ratio_seen_twice_or_more = round(threshold_2_kmers/expected_FP_, 2)
            print(f"\
                 {techno} {expected_FP_}\
                 {ratio_wo}\
                 {ratio_with}\
                 {threshold_2_kmers} {ratio_seen_twice_or_more}\
                 {threshold_3_kmers} {round(threshold_3_kmers/expected_FP_, 2)}")
            ratios_with_rescue.append(ratio_with)
            ratios_kmers_seen_twice_or_more.append(ratio_seen_twice_or_more)
        
    print(f" {sum_wo} have an abundance 1, {sum_with} are rescued by kmtrics, {sum_th_FP} are theoretically FP")

import matplotlib.pyplot as plt
import numpy as np

# Overlay 2 histograms to compare them
def overlaid_histogram(data1, data2, n_bins = 0, data1_name="", data1_color="#539caf", data2_name="", data2_color="#7663b0", x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 10
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins


    if n_bins == 0:
    	bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    else: 
    	bins = n_bins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(data2, bins = 20, color = data2_color, alpha = 0.75, label = data2_name)
    ax.hist(data1, bins = 80, color = data1_color, alpha = 0.75, label = data1_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')
    plt.show() 

overlaid_histogram(ratios_kmers_seen_twice_or_more, ratios_with_rescue, 10, "Hard abundance threshold ", "red", "Rescue strategie", "green", "ratio", "frequency", "Ratio filtered k-mers / expected erroneous k-mers")