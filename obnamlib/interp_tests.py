# Copyright (C) 2009  Lars Wirzenius
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import unittest

import obnamlib


class InterpreterTests(unittest.TestCase):

    def callback(self, args):
        self.args = args

    def test_executes_registered_command(self):
        interp = obnamlib.Interpreter()
        interp.register('foo', self.callback)
        interp.execute('foo', ['bar', 'foobar'])
        self.assertEqual(self.args, ['bar', 'foobar'])
