#!/usr/bin/env python3

import pytest
from pywinauto import Application
import pywinauto.clipboard


@pytest.fixture
def notepad():
    notepad = Application().start('notepad.exe')

    yield notepad

    # Clear Notepad's contents to prevent any save prompts.
    notepad.UntitledNotepad.Edit.type_keys('^A{DEL}')
    notepad.kill()


def test_copy_to_clipboard(notepad):
    notepad.UntitledNotepad.Edit.type_keys('Hello')

    # Select All, Copy
    notepad.UntitledNotepad.Edit.type_keys('^A^C')

    assert pywinauto.clipboard.GetData() == 'Hello'


def test_copyright_notice(notepad):
    notepad.UntitledNotepad.menu_select('Help->About')
    copyright_notice = notepad.AboutNotepad.window(title_re='.*All rights reserved.*')

    assert copyright_notice.window_text() == '© 2017 Microsoft Corporation. All rights reserved.'

    notepad.AboutNotepad.OK.click()
