from unittest import mock, TestCase

from twitter_cleaner import TwitterCleaner


class TestTwitterCleaner(TestCase):

    def setUp(self) -> None:
        self.client = mock.MagicMock()
        self.superclient = mock.MagicMock()

    def test_clean(self):
        with mock.patch("tweepy.Client") as tweepy_client:
            response = mock.MagicMock()
            response.meta["result_count"] = 1
            tc = TwitterCleaner()
            tc.clean("fakeuser")
            tweepy_client.assert_called()
            (tweepy_client.return_value
                .get_user.assert_called_with(id=None,
                                             username="fakeuser"))
