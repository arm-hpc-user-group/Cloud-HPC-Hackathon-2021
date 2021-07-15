# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install memxct-cpu
#
# You can edit this file again by typing:
#
#     spack edit memxct-cpu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

# Place this file at $SPACK_ROOT/var/spack/repos/builtin/packages/memxct-cpu

from spack import *


class MemxctCpu(Package):
    """MemXCT: Memory-Centric X-ray CT Reconstruction with Massive Parallelization
    Article link: http://impact.crhc.illinois.edu/Shared/Papers/MemXCT_SC19.pdf
    Also elected as SC20 SCC reproducibility challenge."""

    homepage = "https://merthidayetoglu.github.io/"
    git      = "https://github.com/merthidayetoglu/MemXCT-CPU.git"

    maintainers = ['merthidayetoglu', 'stephenlienharrell', 'msharmavikram']

    version('0.1', commit='7c3e342')

    #depends_on('mpich', type='build')
    #depends_on('mpich', type='run')
    depends_on('mpi')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make('-f', 'Makefile.arm')
        install('memxct', prefix.bin)
