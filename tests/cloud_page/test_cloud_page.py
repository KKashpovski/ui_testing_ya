"""Test-suite for cloud page."""

import pytest
from common.constants import CloudConstants


@pytest.mark.cloud
class TestCloud:
    def test_copy_file_to_folder(self, app, auth):
        """
        Steps.

            1 Open main page
            2 Auth with valid data
            3 Open YA cloud
            4 Copy tile to folder
            5 Open folder
            6 Delete all files except the copied one
            7 Check file in folder
            8 Check file name
        """
        app.cloud_page.go_to_ya_cloud()
        app.cloud_page.copy_file()
        app.cloud_page.open_folder()
        app.cloud_page.del_files()
        assert app.cloud_page.my_file_in_folder(), "This file is not found in folder"
        assert CloudConstants.FILE_NAME == app.cloud_page.get_file_name(), "Name file is not valid!"
