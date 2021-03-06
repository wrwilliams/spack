##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RAlpine(RPackage):
    """Fragment sequence bias modeling and correction for RNA-seq
    transcript abundance estimation."""

    homepage = "http://bioconductor.org/packages/alpine/"
    url      = "https://git.bioconductor.org/packages/alpine"

    version('1.2.0', git='https://git.bioconductor.org/packages/alpine', commit='896872e6071769e1ac2cf786974edb8b875c45eb')

    depends_on('r@3.4.0:3.4.9', when='@1.2.0')
    depends_on('r-biostrings', type=('build', 'run'))
    depends_on('r-iranges', type=('build', 'run'))
    depends_on('r-genomicranges', type=('build', 'run'))
    depends_on('r-genomicalignments', type=('build', 'run'))
    depends_on('r-rsamtools', type=('build', 'run'))
    depends_on('r-summarizedexperiment', type=('build', 'run'))
    depends_on('r-genomicfeatures', type=('build', 'run'))
    depends_on('r-speedglm', type=('build', 'run'))
    depends_on('r-graph', type=('build', 'run'))
    depends_on('r-rbgl', type=('build', 'run'))
    depends_on('r-stringr', type=('build', 'run'))
    depends_on('r-genomeinfodb', type=('build', 'run'))
    depends_on('r-s4vectors', type=('build', 'run'))
