#test file for quizrun and old version
import unittest
from unittest.mock import patch
import os
import sys
import main

class TestMain(unittest.TestCase):
    def test_main(self):
        with patch.object(sys, 'argv', ['main.py']):
            with patch.object(os, 'chdir') as mock_chdir:
                with patch.dict('main.config', {"multicellversion": "Y"}):
                    with patch('main.multicellversion', autospec=True) as mock_multicellversion:
                        with patch('main.singlecellversion', autospec=True) as mock_singlecellversion:
                            configinputlist = ["Y", "N","y","n",""," ","genericstring"]
                            correct_uppers = ["Y","N"]
                            for i in configinputlist:
                                main.config["multicellversion"] = i
                                main.main()
                                if i.upper() in correct_uppers and i.upper() == "Y":
                                    mock_multicellversion.assert_called_once()
                                    mock_singlecellversion.assert_not_called()
                                    mock_chdir.assert_not_called()
                                    mock_multicellversion.reset_mock()
                                    mock_singlecellversion.reset_mock()
                                    mock_chdir.reset_mock()
                                elif i.upper() in correct_uppers and i.upper() == "N":
                                    mock_singlecellversion.assert_called_once()
                                    mock_multicellversion.assert_not_called()
                                    mock_chdir.assert_not_called()
                                    mock_multicellversion.reset_mock()
                                    mock_singlecellversion.reset_mock()
                                    mock_chdir.reset_mock()
                                elif i.upper() not in correct_uppers:
                                    mock_multicellversion.assert_not_called()
                                    mock_singlecellversion.assert_not_called()
                                    mock_chdir.assert_not_called()
                                    mock_multicellversion.reset_mock()
                                    mock_singlecellversion.reset_mock()
                                    mock_chdir.reset_mock()
                                
#run the tests
unittest.main(argv=[''], exit=False)