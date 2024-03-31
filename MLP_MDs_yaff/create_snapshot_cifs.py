from ase.io import read,write
from ase import Atom, Atoms
import numpy as np
from pathlib import Path

for defec in ["FABr"]: #, "PbBr2", "FAPbBr3"]:

    if defec == "FAPbBr3":
        ini_def = 0
    else:
        ini_def = 1

    for tel in range(9,13): #ini_def,9):
        #traj = read("vac_"+defec+"_"+str(tel)+"/traj.xyz", index="1000:-1:1000")

        #for i, atoms in enumerate(traj):
        #    write("vac_"+defec+"_"+str(tel)+"/snap_"+str(i)+".cif",atoms)

        traj = read("vac_"+defec+"_"+str(tel)+"/traj.xyz", index="1000:")
        
        ave_pos  = np.zeros(traj[0].positions.shape)
        ave_cell = np.zeros((3,3))
        for atoms in traj:
            ave_pos += atoms.positions.copy()/len(traj)
            ave_cell += atoms.cell.copy()/len(traj)

        new_atoms = Atoms(symbols=atoms.symbols, positions=ave_pos, pbc=True, cell=ave_cell)
        write("vac_"+defec+"_"+str(tel)+"/snap_ave.cif", new_atoms)
        

        '''
        for i, atoms in enumerate(traj):
            if i != len(traj)-1:
                assert np.max(np.abs(atoms.get_positions()-traj[i+1].get_positions())) < 5.0,  "check if periodic image is changed at snapshot " + str(i)
                print(i, np.max(np.abs(atoms.get_positions()-traj[i+1].get_positions())))
            print(i, np.average(atoms.get_positions(), axis = 0))
            print(i, atoms.positions)
            atoms.positions -= np.average(atoms.get_positions(), axis = 0)
            print(i, atoms.positions)
            print(i, np.average(atoms.get_positions(), axis = 0))
            Path_folder = Path.cwd() / str("vac_"+defec+"_"+str(tel)) / "traj_folder_centered"
            Path_folder.mkdir(exist_ok=True)
            write("vac_"+defec+"_"+str(tel)+"/traj_folder_centered/snap_"+str(i)+".cif", atoms)
        '''
