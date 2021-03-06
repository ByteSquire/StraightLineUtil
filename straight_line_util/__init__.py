# -*- coding: utf-8 -*-
"""
/***************************************************************************
 StraightLineUtil
                                 A QGIS plugin
 Utilities for planning, creating and analysing straight lines
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-03-17
        copyright            : (C) 2022 by ByteSquire
        email                : to_be_determined
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load StraightLineUtil class from file StraightLineUtil.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .straight_line_util import StraightLineUtil
    return StraightLineUtil(iface)
