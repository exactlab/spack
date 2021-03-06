# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class H5part(AutotoolsPackage):
    """Portable High Performance Parallel Data Interface to HDF5"""

    homepage = "http://vis.lbl.gov/Research/H5Part/"
    url      = "https://codeforge.lbl.gov/frs/download.php/latestfile/18/H5Part-1.6.6.tar.gz"

    version('1.6.6', '327c63d198e38a12565b74cffdf1f9d7')
    patch('mpiio.patch')

    depends_on('mpi')
    depends_on('hdf5+mpi')

    def configure_args(self):
        args = ['--enable-parallel',
                '--with-hdf5=%s' % self.spec['hdf5'].prefix,
                'CC=mpicc',
                'CXX=mpicxx']
        return args
