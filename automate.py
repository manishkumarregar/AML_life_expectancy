import os


redeuce_dim = [0,1]
apply_var = [0,1]
apply_nmf = [0,1]
variances = [1000,5000]
nmfs = [3,4,5]
cluster_algos = [4]
num_cluster = [3,4,5,6,9]


count = 0
for r in [0,1]:
    if r ==  1:
        for apply_v in apply_var:
            if apply_v == 1:
                for var in variances:
                    for apply_n in apply_nmf:
                        if apply_n == 1:
                            for nmf in nmfs:
                                for algo in cluster_algos:
                                    for c in num_cluster:
                                        fin = open('inputs/' + str(count) +  '.txt','w')
                                        count += 1
                                        fin.write(str(r) + '\n')
                                        if r == 1:
                                            fin.write(str(apply_v) + '\n')
                                            if apply_v == 1:
                                                fin.write(str(var) + '\n')
                                            fin.write(str(apply_n) + '\n')
                                            if apply_n == 1:
                                                fin.write(str(nmf) + '\n')

                                        fin.write(str(algo) + '\n')

                                        fin.write(str(c) + '\n')
                                        fin.close()
                        else:
                            for algo in cluster_algos:
                                for c in num_cluster:
                                    fin = open('inputs/' + str(count) +  '.txt','w')
                                    count += 1
                                    fin.write(str(r) + '\n')
                                    if r == 1:
                                        fin.write(str(apply_v) + '\n')
                                        if apply_v == 1:
                                            fin.write(str(var) + '\n')
                                        fin.write(str(apply_n) + '\n')
                                        # if apply_n == 1:
                                            # fin.write(str(nmf) + '\n')

                                    fin.write(str(algo) + '\n')

                                    fin.write(str(c) + '\n')
                                    fin.close()
            else:
                for apply_n in apply_nmf:
                    if apply_n == 1:
                        for nmf in nmfs:
                            for algo in cluster_algos:
                                for c in num_cluster:
                                    fin = open('inputs/' + str(count) +  '.txt','w')
                                    count += 1
                                    fin.write(str(r) + '\n')
                                    if r == 1:
                                        fin.write(str(apply_v) + '\n')
                                        # if apply_v == 1:
                                            # fin.write(str(var) + '\n')
                                        fin.write(str(apply_n) + '\n')
                                        if apply_n == 1:
                                            fin.write(str(nmf) + '\n')

                                    fin.write(str(algo) + '\n')

                                    fin.write(str(c) + '\n')
                                    fin.close()
                    else:
                        for algo in cluster_algos:
                            for c in num_cluster:
                                fin = open('inputs/' + str(count) +  '.txt','w')
                                count += 1
                                fin.write(str(r) + '\n')
                                if r == 1:
                                    fin.write(str(apply_v) + '\n')
                                    # if apply_v == 1:
                                        # fin.write(str(var) + '\n')
                                    fin.write(str(apply_n) + '\n')
                                    # if apply_n == 1:
                                        # fin.write(str(nmf) + '\n')

                                fin.write(str(algo) + '\n')

                                fin.write(str(c) + '\n')
                                fin.close()
    else:
        for algo in cluster_algos:
            for c in num_cluster:
                fin = open('inputs/' + str(count) +  '.txt','w')
                count += 1
                fin.write(str(r) + '\n')
                fin.write(str(algo) + '\n')

                fin.write(str(c) + '\n')
                fin.close()
# count = 0
# for r in [0,1]:
#     for apply_v in apply_var:
#         for var in variances:
#             for apply_n in apply_nmf:
#                 for nmf in nmfs:
#                     for algo in cluster_algos:
#                         for c in num_cluster:
#                             fin = open('inputs/' + str(count) +  '.txt','w')
#                             count += 1
#                             fin.write(str(r) + '\n')
#                             if r == 1:
#                                 fin.write(str(apply_v) + '\n')
#                                 if apply_v == 1:
#                                     fin.write(str(var) + '\n')
#                                 fin.write(str(apply_n) + '\n')
#                                 if apply_n == 1:
#                                     fin.write(str(nmf) + '\n')
#
#                             fin.write(str(algo) + '\n')
#
#                             fin.write(str(c) + '\n')
#                             fin.close()

print(count)
#
for c in range(count):
    os.system('python cluster_patient.py < inputs/' + str(c) + '.txt')
#
#
# for r in [0,1]:
#     if r == 0:
#         for algo in cluster_algos:
#             for c in num_cluster:
#                 fin = open('inputs.txt','w')
#                 fin.write(str(r) + '\n')
#                 fin.write(str(algo) + '\n')
#                 fin.write(str(c) + '\n')
#     else:
#         for apply_v in apply_var:
#             if apply_v == 1:
#                 for var in variances:
#                     for apply_n in apply_nmf:
#                         if apply_n == 1:
#                             for nmf in nmfs:
#                                 for algo in cluster_algos:
#                                     for c in num_cluster:
#                                         fin = open('inputs.txt','w')
#                                         fin.write(str(r) + '\n')
#                                         fin.write(str(algo) + '\n')
#                                         fin.write(str(c) + '\n')
