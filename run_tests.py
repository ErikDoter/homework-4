#!/usr/bin/env python2

import sys
import unittest
from tests.signup.signup_success import SignupSuccessTests
from tests.signup.signup_wrong import SignupWrongTests
from tests.subscribe.subscribe_tests import SubscribeTests
from tests.subscribe.unsubscribe_tests import UnsubscribeTests
from tests.rating.rating_first_time_tests import RatingTestsFirst
from tests.rating.rerating_tests import ReratingTests
from tests.auth.auth_success import AuthTests
from tests.search.film_search_tests import FilmSearchTests
from tests.search.actors_search_tests import ActorsSearchTests
from tests.search.people_search_tests import PeopleSearchTests
from tests.search.all_search_tests import AllSearchTests
from tests.search.save_instanse_search_test import SaveInstanceSearchTests
from tests.comment.comments_tests import CommentsTests
from tests.setting.change_password_wrong import PasswordChangeWrongTests
from tests.setting.change_password_success import PasswordChangeSuccessTests
from tests.setting.change_username_success import UsernameChangeSuccessTests
from tests.setting.change_username_wrong import UsernameChangeWrongTests
from tests.playlist.playlist_create_success_tests import PlaylistCreateSuccessTests
from tests.playlist.playlist_create_wrong_tests import PlaylistCreateWrongTests
from tests.playlist.playlist_delete_tests import PlaylistDeleteTests
from tests.playlist.playlist_add_film_success_tests import AddFilmInPlaylistSuccessTests
from tests.playlist.playlist_add_film_wrong_tests import AddFilmInPlaylistWrongTests
from tests.playlist.playlist_delete_film_tests import DeleteFilmFromPlaylistTests

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SignupSuccessTests))
    suite.addTest(unittest.makeSuite(SignupWrongTests))
    suite.addTest(unittest.makeSuite(PasswordChangeWrongTests))
    suite.addTest(unittest.makeSuite(PasswordChangeSuccessTests))
    suite.addTest(unittest.makeSuite(UsernameChangeSuccessTests))
    suite.addTest(unittest.makeSuite(UsernameChangeWrongTests))
    suite.addTest(unittest.makeSuite(PlaylistCreateSuccessTests))
    suite.addTest(unittest.makeSuite(PlaylistCreateWrongTests))
    suite.addTest(unittest.makeSuite(PlaylistDeleteTests))
    suite.addTest(unittest.makeSuite(AuthTests))
    suite.addTest(unittest.makeSuite(SubscribeTests))
    suite.addTest(unittest.makeSuite(UnsubscribeTests))
    suite.addTest(unittest.makeSuite(RatingTestsFirst))
    suite.addTest(unittest.makeSuite(ReratingTests))
    suite.addTest(unittest.makeSuite(FilmSearchTests))
    suite.addTest(unittest.makeSuite(ActorsSearchTests))
    suite.addTest(unittest.makeSuite(PeopleSearchTests))
    suite.addTest(unittest.makeSuite(AllSearchTests))
    suite.addTest(unittest.makeSuite(SaveInstanceSearchTests))
    suite.addTest(unittest.makeSuite(CommentsTests))
    suite.addTest(unittest.makeSuite(AddFilmInPlaylistSuccessTests))
    suite.addTest(unittest.makeSuite(AddFilmInPlaylistWrongTests))
    suite.addTest(unittest.makeSuite(DeleteFilmFromPlaylistTests))
    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
