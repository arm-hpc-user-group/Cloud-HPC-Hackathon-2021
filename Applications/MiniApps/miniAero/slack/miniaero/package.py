# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Miniaero(MakefilePackage):
    """Proxy Application. MiniAero is a mini-application for the evaulation
       of programming models and hardware for next generation platforms.
    """

    homepage = "http://mantevo.org"
    git      = "https://github.com/ghe-asu/miniAero.git"

    tags = ['proxy-app']

    version('v1.0.1', commit='7744fa59cd93f6b0cc689f080314de8ff401d2a9')
    version('2016-11-11', commit='f46d135479a5be19ec5d146ccaf0e581aeff4596')

    variant(
        'mpi', default=False, description='Builds an MPI version'
    )

    depends_on('kokkos')
    depends_on('mpi', when='+mpi')

    @property
    def build_targets(self):

        if '+mpi' in self.spec:
            targets = [
                '--directory=kokkos',
                '--file=Makefile.mpi',
                'CXX=mpicxx',
                'KOKKOS_PATH={0}'.format(
                    self.spec['kokkos'].prefix),
                'KOKKOS_CPPFLAGS=-I{0}'.format(
                    self.spec['kokkos'].prefix.include
                ),
                'KOKKOS_LDFLAGS=-L{}'.format(
                    self.spec['kokkos'].prefix.lib64
                ),
                'KOKKOS_LIBS=-lkokkoscore'
            ]
        else:
            targets = [
                '--directory=kokkos',
                'CXX=c++',
                'KOKKOS_PATH={0}'.format(
                    self.spec['kokkos'].prefix),
                'KOKKOS_CPPFLAGS=-I{0}'.format(
                    self.spec['kokkos'].prefix.include
                ),
                'KOKKOS_LDFLAGS=-L{}'.format(
                    self.spec['kokkos'].prefix.lib64
                ),
                'KOKKOS_LIBS=-lkokkoscore'
            ]

        return targets

    def install(self, spec, prefix):
        # Manual Installation
        mkdirp(prefix.bin)
        mkdirp(prefix.doc)

        if '+mpi' in self.spec:
            install('kokkos/miniAero.mpi', prefix.bin)
        else:
            install('kokkos/miniAero.host', prefix.bin)
        install('kokkos/README', prefix.doc)
        install('kokkos/tests/3D_Sod_Serial/miniaero.inp', prefix.bin)
        install_tree('kokkos/tests', prefix.doc.tests)