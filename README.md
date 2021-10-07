
Second Quantization Algebra (SQA) package (Compatible with Python 3)

The working equations of the full-internally contracted multireference configuration interaction (FIC-MRCI) were derived with the slightly modified version of the SQA program by using the spin-free unitary group generators. In order to deal with the enormous numbers of tensor contractions, which are impossible to be coded manually, I wrote the code generator that works as a part of the SQA itself. Using this newly added feature, the FIC-MRCI was implemented as a pilot code at the earlier stage of the development of the DMRG-MRCI (M. Saitow et. al. J Chem Phys 139, 044118 (2013)). Even though the production level implementation of the DMRG-MRCI was achieved by using a new tensor generator, which was written from scratch by MS, the modified version of SQA package may still be useful tool for invention of the new idea on the electronic structure theory. So, I have decided to publicize the copy of it.

Distinctions from the original copy:

  * Use of spin-free unitary group generator is made fully functional
  * A simple code generator integrated inside SQA

If you use or modify this version of SQA package in your own work, you should cite the following publications: 

  * E. Neuscamman, T. Yanai, and G. K.-L. Chan, Quadratic canonical transformation theory and higher order density matrices, J. Chem. Phys. 130, 124102 (2009).
  * M. Saitow, Y. Kurashige, and T. Yanai, Multireference configuration interaction theory using cumulant reconstruction with internal contraction of density matrix renormalization group wave function, J. Chem. Phys. 139, 044118 (2013).


