from ase.io import read, write
import numpy as np
import matplotlib.pyplot as plt
import sys
'''
traj_pu = read("PureFAPbBr3/longtrainstep/testMD/longtrain/traj.xyz", index="100:")
traj_Br = read("Brvacancy/longtrainstep/testMD/longtrain/traj.xyz", index="100:")
Br_lst_Br = [613, 567, 559, 648, 570, 680, 619, 532, 525, 512, 674, 686, 555, 605]
traj_FA = read("FAvacancy/longtrainstep/testMD/longtrain/traj.xyz", index="100:")
Br_lst_FA = [691, 677, 615, 668, 665, 533, 614, 662, 532, 511, 585, 661]

fig, ax = plt.subplots()

ax.set_title('Comparison of Br angles in FAPbBr3 with and without defects')
ax.set_ylabel('Angle [degree]')

labels = ["Pure", "Br vacancy", "FA vacancy"]

for tel, traj in enumerate([traj_pu, traj_Br, traj_FA]):
    All_br_angles = []
    for at in traj[0]:
        if at.symbol == "Br":
            Pb_bond= [at.index]
            for at2 in traj[0]:
                if at2.symbol == "Pb":
                    dist = traj[0].get_distance(at.index, at2.index, mic=True, vector=False)
                    if dist < 4.0:
                        Pb_bond.append(at2.index)
            assert len(Pb_bond) == 3 ,  "Found too litle of too many Pb neighbours for Br atom " + str(at.index)
            All_br_angles.append(Pb_bond)

    angle_np = np.zeros((len(traj), len(All_br_angles)))
    for i, atoms in enumerate(traj):
        for j, Pb_bond in enumerate(All_br_angles):
            angle_np[i, j] = atoms.get_angle(Pb_bond[1], Pb_bond[0], Pb_bond[2], mic = True)

    angles_Vac = np.array([])
    angles_all = np.array([])

    if tel == 1:
        Br_vac_lst = Br_lst_Br
    elif tel == 2:
        Br_vac_lst = Br_lst_FA
    else:
        Br_vac_lst = []

    for j, Pb_bond in enumerate(All_br_angles):
        if Pb_bond[0] in Br_vac_lst:
            angles_Vac = np.concatenate((angles_Vac, angle_np[:,j]))
        angles_all = np.concatenate((angles_all, angle_np[:,j]))

    ax.violinplot(angles_all, np.arange(tel, tel + 0.1), showmeans=True, showextrema=False, showmedians=False)
    if len(angles_Vac) > 0:
        ax.violinplot(angles_Vac, np.arange(tel+0.2, tel + 0.3), showmeans=True, showextrema=False, showmedians=False)


# set style for the axes
ax.get_xaxis().set_tick_params(direction='out')
ax.xaxis.set_ticks_position('bottom')
ax.set_xticks(np.arange(0, len(labels)))
ax.set_xticklabels(labels)
ax.set_xlim(-0.75, len(labels) - 0.25)

ax.set_xlabel("Material")
ax.set_ylabel('Angle [degree]')

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.savefig(sys.argv[0].strip(".py")+".pdf", format="pdf",bbox_inches='tight')
plt.close()

'''

fig, ax = plt.subplots()

ax.set_title('Comparison of Br angles in FAPbBr3 as a funtion of temperature')
ax.set_ylabel('Angle [degree]')

for tel in range(100,601,100):
    traj = read("run"+str(tel)+"/traj.xyz", index="1000:")
    All_br_angles = []
    for at in traj[0]:
        if at.symbol == "Br":
            Pb_bond= [at.index]
            for at2 in traj[0]:
                if at2.symbol == "Pb":
                    dist = traj[0].get_distance(at.index, at2.index, mic=True, vector=False)
                    if dist < 4.8:
                        Pb_bond.append(at2.index)
            assert len(Pb_bond) == 3 ,  "Found too litle of too many Pb neighbours for Br atom " + str(at.index) + " for vacancy " + str(tel)
            All_br_angles.append(Pb_bond)

    angle_np = np.zeros((len(traj), len(All_br_angles)))
    angles_all = np.array([])
    for i, atoms in enumerate(traj):
        for j, Pb_bond in enumerate(All_br_angles):
            angle_np[i, j] = atoms.get_angle(Pb_bond[1], Pb_bond[0], Pb_bond[2], mic = True)

    for j, Pb_bond in enumerate(All_br_angles):
        angles_all = np.concatenate((angles_all, angle_np[:,j]))

    ax.violinplot(angles_all, np.arange(tel, tel + 0.1), widths= 50, showmeans=True, showextrema=False, showmedians=False)
    print(tel, np.average(angles_all))

# set style for the axes
ax.get_xaxis().set_tick_params(direction='out')
ax.xaxis.set_ticks_position('bottom')
ax.set_xticks(np.arange(100,601,100))
ax.set_xlim(25, 675)

ax.set_xlabel("Temperature")
ax.set_ylabel('Angle [degree]')

plt.subplots_adjust(bottom=0.15, wspace=0.05)
plt.savefig(sys.argv[0].strip(".py")+".pdf", format="pdf",bbox_inches='tight')
plt.close()

