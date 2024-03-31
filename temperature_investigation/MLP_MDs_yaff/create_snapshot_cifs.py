from ase.io import read,write
from ase import Atom, Atoms
import numpy as np
from pathlib import Path

for j in range(100,601,100):
    traj = read("run"+str(j)+"/traj.xyz", index="1000:-1:1000")

    for i, atoms in enumerate(traj):
        write("run"+str(j)+"/snap_"+str(i)+".cif",atoms)

    traj = read("run"+str(j)+"/traj.xyz", index="1000:")

    ave_pos  = np.zeros(traj[0].positions.shape)
    ave_cell = np.zeros((3,3))
    for atoms in traj:
        ave_pos += atoms.positions.copy()/len(traj)
        ave_cell += atoms.cell.copy()/len(traj)

    new_atoms = Atoms(symbols=atoms.symbols, positions=ave_pos, pbc=True, cell=ave_cell)
    write("run"+str(j)+"/snap_ave.cif", new_atoms)

    for i, atoms in enumerate(traj):
        if i != len(traj)-1:
            assert np.max(np.abs(atoms.get_positions()-traj[i+1].get_positions())) < 5.0,  "check if periodic image is changed at snapshot " + str(i)
            print(i, np.max(np.abs(atoms.get_positions()-traj[i+1].get_positions())))
        print(i, np.average(atoms.get_positions(), axis = 0))
        print(i, atoms.positions)
        atoms.positions -= np.average(atoms.get_positions(), axis = 0)
        print(i, atoms.positions)
        print(i, np.average(atoms.get_positions(), axis = 0))
        Path_folder = Path.cwd() / str("run"+str(j)) / "traj_folder_centered"
        Path_folder.mkdir(exist_ok=True)
        write("run"+str(j)+"/traj_folder_centered/snap_"+str(i)+".cif", atoms)
